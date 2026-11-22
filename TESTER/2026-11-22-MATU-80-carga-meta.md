# TESTER · 22-11: MATU-80, el #131 (`CARGA_META`) corrido en k6

**Revisor:** Martín Henríquez (modo Martín) · **Fecha:** 22-11-2026
**Resultado:**
- **El script funciona** (pruebas 2 y 3 PASS, y la prueba 1 muestra y evalúa bien la meta piloto).
- **La meta del piloto no se cumplió en esta máquina hoy:** confirmar y retorno quedan sobre 800 ms de mediana.
- **El #131 no se fusiona todavía.** La condición de Jorge era «piloto y CUMPLE».

## Dónde

- Copia local con la rama `matu-80-umbrales-k6` (c965151), que sale de `main` con el #130, y la pasarela falsa. Nunca contra Railway ni Transbank.
- ASUS VivoBook X515JA, i3-1005G1 de 2 núcleos, 8 GB de RAM y uvicorn con un solo proceso.
- Antes de cada corrida de la prueba 1 se repuso el stock con `preparar_carga.py --cuentas 50`. La base local **no se vació** entre corridas.

## Prueba 1 · piloto, sin `CARGA_META` y con 10 usuarios

El encabezado dice «meta piloto: 10 usuarios, 0 % de fallos y mediana < 800 ms en cada paso; el p95 se informa». ✅

| paso | 1.ª (11:47 a 11:57) med | p95 | 2.ª med | p95 | 21-11 (00:44) med |
|---|---|---|---|---|---|
| catalogo | 140 ✅ | 287 | 120 ✅ | 192 | 107 |
| pedido | 652 ✅ | 2286 | 541 ✅ | 1510 | 468 |
| confirmar | **987 ❌** | 2528 | **939 ❌** | 1983 | 724 |
| pagar | 598 ✅ | 1885 | 534 ✅ | 1631 | 436 |
| retorno | **1041 ❌** | 8134 | **908 ❌** | 5402 | 708 |
| iteraciones | 315 | | 370 | | 466 |

- En las dos corridas: `checks` 100 % y `http_req_failed` **0,00 %**. El 409 de un pedido sin pagar de otra corrida y el 401 del token vencido ya no cuentan como fallo (O1 del QA). ✅
- k6 marca error **solo** en `confirmar` y `retorno`, los pasos cuya mediana pasa de 800 ms. El script evalúa bien la meta piloto. ✅
- **La meta no se cumple:** confirmar y retorno quedan sobre 800 ms de mediana en las dos corridas. El 21-11, con el mismo código de la API, cumplía.

## Prueba 2 · `CARGA_META=produccion`

Parte con **50 max VUs**, y el encabezado dice «meta produccion: 50 usuarios, menos de 1 % de fallos y p95 < 800 ms en cada paso y en total». ✅ Se dejó correr entera: p95 de 9 a 39 s, `checks` 97,70 % y fallos 1,99 %. No cumple, como se esperaba en esta máquina con 50 usuarios.

## Prueba 3 · `CARGA_META=otra`

No parte: `Error: CARGA_META debe ser piloto o produccion: la carga no parte con una meta que no existe`. ✅

## Hallazgo

| ID | Severidad | Hallazgo |
|---|---|---|
| K6 | P2 | Con el mismo código de la API (#130), la mediana de confirmar y retorno pasó de 724 y 708 ms (21-11) a cerca de 950 ms (22-11), y las iteraciones bajaron de 466 a 315 y 370. **Hipótesis sin confirmar:** la base local acumula los pedidos y los pagos de cada corrida, porque `preparar_carga.py` repone el stock pero no los borra. Ya van cinco corridas. El #128 anotó que las consultas del pago se encarecen al crecer `transaccion_pasarela`. Si es así, en producción también pasaría con el tiempo. **Para confirmarlo:** una corrida con la base local vacía (`docker compose down -v`) |

## Para decidir (Jorge)

- **Fusionar el #131:** el script hace lo que dice, pero la prueba 1 no dio CUMPLE.
- **Qué hacer con K6:**
  - confirmar la hipótesis con la base vacía;
  - limpiar los datos de carga en `preparar_carga.py`;
  - o revisar el costo de confirmar y del retorno con más filas.

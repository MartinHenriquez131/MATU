# 2026-11-16 · Cola del sprint 5 · MATU-107, 106, 96, 105, 109 y 63, y el recorrido 6 de MATU-64

**PR revisados (MATU_PROYECTO):** #93 (MATU-107, política 0.18), #94 (MATU-106), #95 (MATU-96), #96 (MATU-105), #97 (MATU-109) y #98 (MATU-63, migración 0029, política 0.19).
**Documentos (MATU):** #91, #92, #93 y #94.
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor`, `disenador-revisor` y `revisor-documental` · **Fechas:** del 15 al 16/11/2026
**Revisión obligatoria:** sí (datos personales y dinero en MATU-107 y MATU-63)
**Veredicto general:** PASS, sin P1 de código

## Revisiones

| PR | QA | Analista | Diseñador | Lo principal |
|---|---|---|---|---|
| #93 MATU-107 | PASS | CUMPLE (CL-37 y CL-69 siguen abiertas) | — | C14 queda como control técnico: sin `PUSH_CUENTAS_PERMITIDAS` nadie activa los avisos push (409 `push-no-permitido`), y los UUID no aparecen en logs ni errores. Incluye la prueba de que `/v1/yo/datos` no entrega nada si falla la auditoría (54-H1) |
| #94 MATU-106 | PASS | — | — | Solo cambia el contrato: la presentación y el canje del relevo pasan a `openapi.json`, con una prueba de contrato nueva. La lógica no cambia |
| #95 MATU-96 | PASS | — | — | La prueba de carrera espera el bloqueo en `pg_locks` y ya no depende de un tiempo fijo |
| #96 MATU-105 | PASS | — | — | Prueba de que el pedido pagado queda intacto con la capa 3 apagada. `requiere_base` ahora falla en CI en vez de saltarse en silencio |
| #97 MATU-109 | PASS | — | APROBADA | «Me quedan» con envases cerrados y unidades sueltas. Corrige el P1 que había en `main`: «Cambiar» no abría el formulario (prueba con la app completa) |
| #98 MATU-63 | PASS | CUMPLE, con consulta legal pendiente | APROBADA | 0029 con FORCE RLS y reversible. El código de retiro se guarda como HMAC, permite 5 intentos, vence y no aparece en logs. Las devoluciones van solo a la misma tarjeta. Sin el secreto, falla cerrado |

**Documentos:** sin P1. Con la 0.18, la §6 de la política dice lo mismo que la §10 sobre lo que ve el cuidador, lo que cierra el pendiente de MATU-100. La 0.19 es coherente en la cabecera, la §12 y el registro, y las CL llegan sin saltos hasta la CL-73.

## Fusión y despliegue (hora de Chile)

**Orden de fusión:** el que pidió Jorge, con merge commit.
1. #93 y MATU#91.
2. #94, con un conflicto en `docs/api/README.md` resuelto: quedan las dos secciones.
3. #95.
4. #96 y MATU#92.
5. #97 y MATU#93, con un conflicto en `envasesMeQuedan.test.tsx` resuelto: queda la prueba rápida de MATU-107 con «Envases cerrados».
6. #98 y MATU#94.
   - En #98 había conflictos en `.env.example`, `config.py`, `textos_politica.py`, `test_politica.py` y README. Se resolvieron dejando las dos partes y la política en 0.19.
   - En MATU#94 había un conflicto en `lenguaje.md`: la §36 (comercio) quedó antes de la §37.

**Cada PR se puso al día con `main` y esperó su CI en verde antes de fusionarse.**

**Variables:** Martín las cargó directo en Railway, sin pasar por el chat.
- `CODIGO_RETIRO_SECRETO`, distinto en staging y en la demo.
- `PUSH_CUENTAS_PERMITIDAS` en `matu-api` y `matu-cron-avisos` de la demo. En staging queda sin definir, así que nadie activa los avisos.
- `POLITICA_VERSION=0.19` y `POLITICA_ACTUALIZADA_EN=2026-11-13`.

**Despliegue del 15-11, 23:35:**
- `Running upgrade 0028 -> 0029` sin errores en los dos entornos.
- Se creó `matu-cron-despacho` (`python -m app.tareas despacho`, cada 5 minutos, con las variables como referencias). Su primera corrida en la demo terminó con `resultado: ok`.
- Los cron de borrados, quiebres, conciliación y avisos estaban en commits viejos y se reconectaron a `main`.

**C14:** se contaron, en solo lectura y como operación, los `push_token` de cuentas que no están en la lista. El resultado fue `(0, 0)` en la demo y `(0, 0)` en staging.

## Prueba en el teléfono

Se hizo en la demo, con el Motorola Edge 50 y Edge (información de Martín).

**«Me quedan» y «Cambiar» (MATU-109), con Carmen, del 15-11 a las 23:41 al 15-11 a las 23:49:**

| # | Prueba | Resultado |
|---|---|---|
| M1 | «Envases cerrados» y «Unidades sueltas», con el total cambiando en vivo | OK |
| M2 | Guardar | OK |
| M3 | «Cambiar» abre el formulario (el P1) | OK |
| M4 | Bajo el total del pedido dice «Son los precios finales. El envío es uno solo, por todo el pedido.» | OK |

**Recorrido 6, el retiro con código (MATU-63 y MATU-64), del 15-11 a las 23:50 al 16-11 a las 00:07:**

| # | Prueba | Resultado |
|---|---|---|
| 1 | Carmen paga el pedido con la AMEX de prueba | OK |
| 2 | `comercio@example.com` ve el pedido QZMQMN solo con su referencia, sin persona ni dirección | OK |
| 3 | Empezar a preparar → «Lo tengo» → «Listo para retirar». Sin código, la pantalla dice «Todavía no hay un código para este pedido» | OK |
| 4 | Operación genera el código con `python -m app.tareas codigo-retiro <parte_id>` en una consola interactiva. El código sale solo en la consola, y la línea del log no lo trae | OK |
| R1 | Un código errado no se acepta y no muestra el bueno | OK |
| R2 | El código correcto deja el pedido en Retirado | OK |
| R3 | Carmen ve el pedido retirado | OK |

**Resultado:** PASS.

**Notas:**
- La cuenta del comercio no existía en la demo porque la semilla era anterior a MATU-63. Se volvió a correr la semilla sin `--restablecer`, lo que solo crea lo que falta.
- **El código de retiro se pegó una vez en el chat de trabajo.** Se regeneró con el mismo comando y el anterior dejó de servir. En R1 se usó ese código viejo como «código errado».
- **Logs de la demo desde el despliegue:** la búsqueda de código, `password`, `Bearer`, `pin`, `token` y `body` no dio resultados.

## Hallazgos

| ID | Severidad | Hallazgo | Estado |
|---|---|---|---|
| H1 | P2 | Un pedido sin versión de condiciones caía en la regla 0.3, que no devuelve el envío (analista) | MATU-112: Jorge lo pasa a la regla 0.2, que devuelve el envío siempre |
| H2 | P2 | Las rutas de operación no piden MFA | MATU-81, como requisito antes de manejar dinero real |
| H3 | P3 | **No se probó «No lo tengo» con un producto que falta**, ni la devolución parcial en el teléfono: el pedido tenía un solo producto. Lo cubren las pruebas automáticas | Repetirlo con un pedido de dos productos (MATU-64 o MATU-80) |
| H4 | P3 | Generar el código exige pegar `SCHEDULER_DATABASE_URL` en la consola de `matu-api`, porque los cron no tienen una consola abierta | Queda resuelto con la pantalla de MATU-81 |
| H5 | P3 | `compreMeQuedan` es intermitente en vitest bajo carga | Se anota |
| H6 | P3 | La exigencia de `PUSH_CUENTAS_PERMITIDAS` también rige en producción | Hay que quitarla antes de salir del piloto |

**Decisiones de Jorge del 15-11:**
- un comercio inactivo responde 403;
- el envío se devuelve solo si se devuelve todo (D-63-10 b);
- la línea bajo el total queda tal como está.

**A la consulta legal:** CL-71 (los días hábiles), CL-72 (el envío en el retracto), CL-73 (la calidad del comercio) y CL-55.

## Anexo · 16-11 · Pedido con dos productos y «No lo tengo» (cierra H3)

**Demo, dos teléfonos.** Carmen en el Motorola y `comercio@example.com` en el iPhone. De 11:45 a 12:18 (hora de Chile), según Martín.

| Paso | Qué se probó | Resultado |
|---|---|---|
| 1 | Carmen arma un pedido con dos productos de Almacén El Ejemplo y lo paga con la AMEX de prueba | OK |
| 2 | El pedido llega a «Pedidos de hoy» con la corrida siguiente de `matu-cron-despacho`. El comercio marca «Lo tengo» en uno y «No lo tengo» en el otro. Al marcar «No lo tengo», la pantalla dice: «No lo cambies por otra marca ni por otro producto. MATU se encarga del resto.» (ADR-027, sin sustitución) | OK |
| 3 | El comercio deja el pedido en «Listo» y el código se genera en la consola (`codigo-retiro`). El código no se escribió en el chat | OK |
| R1 | Un código errado se rechaza | OK |
| R2 | El código correcto deja el pedido retirado | OK |
| R3 | Carmen ve el pedido retirado y la devolución del producto que faltó, a la misma tarjeta | OK |

**Resultado:** PASS. **H3 queda cerrado.**

**Hallazgos nuevos:**

| ID | Severidad | Hallazgo | Propuesta |
|---|---|---|---|
| H7 | P2 | La semilla crea cuenta de comercio solo para Almacén El Ejemplo. Un pedido que cae en Bodega La Muestra (por ejemplo, con toallitas o crema, que solo tienen stock ahí) no lo puede preparar nadie en la demo. Los dos primeros pedidos de esta prueba quedaron ahí y no aparecieron en la consola | Jorge agrega a la semilla una cuenta para el segundo comercio (`comercio2@example.com`), o deja stock solo en el primero. Se nombra en el guion (MATU-77) |
| H8 | P3 | Entre el pago y la llegada al comercio pasan hasta 5 minutos (`matu-cron-despacho`, `*/5`). Ni la familia ni el comercio lo ven explicado | Un texto en la consola del comercio, o decirlo en voz alta en el guion de la demo |
| H9 | P3 | La carga de `SCHEDULER_DATABASE_URL` en la consola falló tres veces: se copió la referencia de Railway (29 caracteres), faltó el `export` y quedó `export ` pegado delante de la URL. El comando responde siempre «falta SCHEDULER_DATABASE_URL», sin distinguir si la variable no existe, no se lee como URL o es de otro usuario | Se suma a H4: lo resuelve la pantalla de MATU-81. Mientras tanto, el instructivo de MATU-64 trae el paso a paso con `railway variables -k` |

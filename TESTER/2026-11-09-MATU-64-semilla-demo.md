# 2026-11-09 · MATU-64 · Semilla de la demo (solo el código)

**Historia:** MATU-64 · Entorno de demostración operativo ([tarjeta](https://trello.com/c/37vOQT3q)). Esta revisión cubre solo la parte de Jorge, la semilla
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#68 (head f45c383 y, al día con `main`, fe9fd99)
**Revisó:** Martín Henríquez, con `qa-tester-revisor` · **Fecha:** 09/11/2026
**Veredicto general:** PASS en el código. No hay P1. **El entorno de la demo, la carga de la semilla y los recorridos quedan pendientes** y van en un informe aparte

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en f45c383 y en fe9fd99.
- **Entorno:** la demo todavía no existe en Railway. No se corrió la semilla en ningún entorno.

## Criterios de aceptación (la parte de la semilla)

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Solo datos sintéticos | PASS | Correos `@example.com` y `@example.org`; celulares `+56900000001` a `06`, como dice la tarjeta |
| 2 | La contraseña y el PIN se leen del entorno y no se imprimen | PASS, con una observación | `SEMILLA_CONTRASENA` y `SEMILLA_PIN` (`demo.py:869`, `:882`); solo se muestran con `--mostrar-credenciales`. Ver H1 |
| 3 | La ficha va cifrada con el puerto | PASS | `CifradorAesGcm` (`demo.py:608-625`); `test_la_ficha_queda_cifrada_y_descifra_con_su_clave` |
| 4 | Dos familias, insumos con alerta, relevo con PIN, catálogo y comercios | PASS | `test_crea_dos_familias_con_los_cuatro_roles`, `test_hay_una_alerta_abierta…`, `test_el_relevo_de_ejemplo_abre_la_ficha_con_su_pin` |
| 5 | Se puede repetir y restablecer | PASS | `test_es_idempotente`, `test_restablecer_deja_todo_como_recien_sembrado` |
| 6 | Restablecer toma menos de 10 minutos | PASS en local (unos 10 s, según el README); **falta medirlo en Railway** | |
| 7 | Se niega a correr en `produccion` y si no se conecta como `matu_app` | PASS | `demo.py:1008`, `:1017`; `test_no_corre_en_produccion`, `test_se_niega_si_no_esta_conectada_como_matu_app` |
| 8 | Las fechas se calculan con el `Reloj`, así el cron de borrados no las borra en la primera corrida | PASS | Sin fechas fijas (`grep` de `datetime(` y `date(`). Falta confirmarlo con el cron real en la demo |

**Fusión:** el 09-11 a las 10:54 (237a7f6).

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P2 | `infra/semillas/salida/relevo-demo.txt` guarda el PIN y el enlace del relevo (con permisos 0600 y en `.gitignore`), aunque el PIN venga de `SEMILLA_PIN` | `guardar_relevo`, aprox. `demo.py:918` | Para decidir (PO): si se acepta, o se guarda solo el enlace |

## Pendiente (Martín)

1. Crear el entorno de la demo en Railway, con secretos nuevos y propios, y sus tres cron.
2. Cargar la semilla desde el computador, con `railway run`, y medir cuánto toma restablecerla.
3. Probar los recorridos críticos 1 a 4 en el teléfono. El 5 y el 6 necesitan MATU-61 a MATU-63.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | | | |

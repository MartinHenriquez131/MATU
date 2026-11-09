# 2026-11-07 · MATU-73 · Prueba de conservación de sesiones estable

**Historia:** MATU-73 · Hacer estable la prueba de conservación de sesiones y dispositivos ([tarjeta](https://trello.com/c/PUOKVYH5))
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#61 (head a8b3ecc)
**Revisó:** Martín Henríquez, con `qa-tester-revisor` · **Fecha:** 07/11/2026
**Veredicto general:** PASS. No hay P1 ni P2

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en a8b3ecc. No se repitió el pipeline.
- **Revisión:** se leyó el diff. Solo cambia `backend/tests/modules/iam/test_refresh_api.py`, con 78 líneas agregadas y 6 quitadas, y no trae migración.
- **Teléfono:** no aplica, porque no hay pantalla.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | La causa queda escrita en el PR, con la forma de repetirla | PASS | La descripción del #61: un dispositivo de otra cuenta con último uso de hace 100 días y 12 h hace fallar la prueba vieja con `(0, 2) == (0, 1)` |
| 2 | La prueba ya no depende de otras filas de la base | PASS | `_sesiones_y_dispositivos(cuenta)` filtra por `usuario_id` (aprox. `:485-491`). Los conjuntos exactos se comparan antes y después de cada pasada (`:567`, `:576`, `:585`) |
| 3 | Sigue comprobando lo mismo, sin debilitarse | PASS | Las aserciones siguen exactas (`== esperado`), contra `_por_borrar()`, que usa los predicados de `iam_conservar` (`0008_sesion_dispositivos.py:82-130`). Se mantiene `_sesion_expirada` |
| 4 | Falla sin la corrección | PASS | El caso parametrizado `con_dispositivo_ajeno` |
| 5 | No toca código de producto | PASS | `git diff --stat`: un solo archivo de prueba |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1 y 2. Pruebas | PASS | `test_refresh_api.py` |
| 3. Contrato | No aplica | |
| 4. Accesibilidad | No aplica | |
| 5. Revisión de la otra persona | PASS | Aprobado y fusionado por Martín el 07-11 a las 20:07 (c40ab99) |
| 6. Prueba que falla sin la corrección | PASS | `con_dispositivo_ajeno` |

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P3 | `_por_borrar` copia la regla de la decisión 59. Si cambia la regla, hay que cambiar las dos | `test_refresh_api.py`, aprox. `:494-520` | Nada: el docstring ya apunta a la 0008 |
| H2 | P3 | Si se agrega ejecución en paralelo (xdist), puede haber una carrera entre `_por_borrar` y `conservar` | Hoy no hay xdist | Tenerlo presente |
| H3 | P3 | El PR deja anotadas tres pruebas de `test_aislamiento.py` que comparan totales globales | La descripción del #61 | Para decidir (PO) |

## Para decidir (PO)

- H3: si las tres pruebas de `test_aislamiento.py` van en una tarjeta propia.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | Se anota: el docstring apunta a la 0008 | — | |
| H2 | Se tiene presente si algún día se agrega xdist | — | |
| H3 | No va en una tarjeta propia: es un ítem de MATU-79 (Endurecimiento), para que esas tres pruebas cuenten solo sus filas (08-11) | Trello MATU-79 | |

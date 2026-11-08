# 2026-11-07 · MATU-70 · Prueba de una sola cabeza de Alembic

**Historia:** MATU-70 · Prueba de una sola cabeza de Alembic ([tarjeta](https://trello.com/c/ax7L8NDR))
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#59 (head 003b3c6 y, al día con `main`, 0cd01d0)
**Revisó:** Martín Henríquez, con `qa-tester-revisor` · **Fecha:** 07/11/2026
**Veredicto general:** PASS. No hay P1 ni P2

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en 003b3c6 y en 0cd01d0.
- **Prueba puntual:** se corrió sin base de datos con `uv run --no-project --with pytest --with alembic --with sqlalchemy pytest -q tests/test_cadena_migraciones.py`, en copias aparte de las ramas que después se borraron.
- **Protección de `main`:** «Require branches to be up to date» ya estaba activa (`strict_required_status_checks_policy: true` en la regla 24657517). `web` como check obligatorio: lo aprobó Jorge, y Martín lo agrega en Settings → Rules porque el proxy de la sesión no deja cambiar la regla (403).
- **Teléfono:** no aplica, porque no hay pantalla.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Falla con más de una cabeza, lista las cabezas y dice cómo corregir | PASS | Con una segunda `0015`: `AssertionError: Alembic tiene 2 cabezas: ['0015', '0016']. La migración nueva debe apuntar a la última.` |
| 2 | Detecta merges, ramas, una revisión repetida, un nombre que no empieza con su revisión, huecos y un `down_revision` que no es el anterior | PASS | Los 6 casos de `CHOQUES` y un control sano |
| 3 | Corre sin base de datos | PASS | Sin Postgres: `9 passed in 0.87s` |
| 4 | Pasa sobre `main` y sobre la fila abierta | PASS | Su rama: `9 passed`. Sobre la rama de MATU-44, hasta la 0016: `9 passed in 0.20s`. Sobre la de MATU-51, hasta la 0017: `9 passed in 0.71s` |
| 5 | Falla sin la corrección | PASS | Con `0015_dup.py`: `2 failed, 7 passed` |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1. Pruebas | PASS | `test_cadena_migraciones.py` |
| 2. Integración | No aplica | Es una prueba de arquitectura |
| 3. Contrato | No aplica | No cambia la API |
| 4. Accesibilidad | No aplica | No hay pantalla |
| 5. Revisión de la otra persona | PASS | Aprobado y fusionado por Martín el 07-11 a las 13:07 (1645029) |
| 6. Prueba que falla sin la corrección | PASS | Criterio 5 |

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P3 | Con dos 0015, `test_las_migraciones_del_repositorio_son_una_sola_cadena` se cae dentro de `walk_revisions()` («Dependency resolution failed») en vez de mostrar la lista de problemas. La otra prueba sí da el mensaje claro | Corrida con `0015_dup.py` | Opcional: capturar esa excepción y convertirla en un problema legible |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | Se anota y no se cambia: la otra prueba da el mensaje claro con dos cabezas | — | |

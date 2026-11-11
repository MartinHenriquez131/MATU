# 2026-11-10 · MATU-67 · Aviso de versión nueva de la app

**Historia:** MATU-67 ([tarjeta](https://trello.com/c/T7eTW8mA))
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#69 (al día con `main` en 916ec4c)
**Revisó:** Martín Henríquez, con `qa-tester-revisor` y `disenador-revisor` · **Fecha:** 10/11/2026
**Veredicto general:** PASS en el código y en el teléfono. No hay P1 ni P2

## Contexto

- **CI:** verde en `ci` y en `web`, en 916ec4c.
- **Aprobación:** el 10-11. **Fusión:** el 10-11 a las 00:32 (hora de Chile), fb202b1, después de la 0022 (MATU-74).
- **Despliegue:** staging y la demo desde fb202b1, los dos en SUCCESS a las 00:33. Sin migración.

## Criterios (Definición de Terminado)

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Una pestaña abierta muestra el aviso al volver a ella o a lo más en 15 minutos | PASS | Teléfono, paso a |
| 2 | Sin aviso si la versión no cambió o si falla la red | PASS (código) | Pruebas de Vitest de versión igual y de falla de red |
| 3 | «Recargar» carga la versión nueva, y si se ignora la app sigue funcionando | PASS | Teléfono, paso c |
| 4 | Nunca recarga sola | PASS | Teléfono, paso b |
| 5 | Región viva `polite`, foco visible, 48 px y revisión visual | PASS | El diseñador da APROBADA |
| 6 | Pruebas de Vitest y del backend, con el pipeline en verde | PASS | CI del #69 |

## Prueba en el teléfono

Staging, Motorola Edge 50 con Edge, el 10-11 de 00:29 a 00:37 (informado por Martín). La pestaña de Insumos se abrió a las 00:29, antes del despliegue del #69:
- **a.** Al volver a la pestaña aparece «Hay una versión nueva de MATU.» con su botón. **OK**
- **b.** La página no se recargó sola. **OK**
- **c.** El botón recarga la app y el aviso desaparece. **OK**

**Resultado:** PASS.

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P3 | La tarjeta pide `Cache-Control: no-cache` para `version.json`, y el PR usa `no-store` (decisión 172) | `backend/app/core/cabeceras.py:46` | Alinear el texto de la tarjeta con la decisión 172 |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | La descripción de la tarjeta dice `no-store` (decisión 172). El código no cambia | descripción de MATU-67 en Trello (10-11) | |

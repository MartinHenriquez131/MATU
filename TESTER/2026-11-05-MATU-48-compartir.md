# 2026-11-05 · MATU-48 · Compartir la ficha y cortar el acceso

**Historia:** MATU-48 · App de familia: compartir la ficha con un relevo y cortar el acceso
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#45 (fusionado), junto con MartinHenriquez131/MATU#27
**Entorno:** staging, desplegado desde `main` en `0b18786` (merge del #45)
**Revisó:** Martín Henríquez · **Fecha:** 05/11/2026 · **Teléfono y navegador:** Motorola Edge 50 con Microsoft Edge. El relevo se abrió en el navegador del computador
**Veredicto general:** PASS

## Revisión del código (#45)

| # | Criterio | Veredicto |
|---|---|---|
| 1 | El PIN vive solo en la memoria de la pantalla: no va en `document.title`, en la URL ni en el almacenamiento del navegador | PASS |
| 2 | «Enviar» y «Copiar» llevan solo la URL, nunca el PIN, y no usan `wa.me` ni otros terceros | PASS |
| 3 | «Cortar» no es optimista: la pantalla cambia con el 204 | PASS |
| 4 | Estado «En pausa» según la decisión 33 | PASS (por lectura del código) |
| 5 | CI en verde en `ci` y `web`, y la rama al día con `main`. QA dio PASS en 11 criterios y el diseñador aprobó las cuatro pantallas | PASS |

## Prueba en el teléfono

| # | Paso | Veredicto |
|---|---|---|
| 1 | Compartir con «Rosa», `+56 9 5555 0137` (inventado), una sección marcada y «Sus remedios» sin marcar, con la casilla «Le avisé a Rosa…» | PASS |
| 2 | El PIN se muestra una sola vez. Al recargar aparece «El PIN ya no se puede ver» | PASS |
| 3 | El enlace copiado no trae el PIN | PASS |
| 4 | El relevo abre `/r` con el PIN en otro navegador y ve solo lo que se compartió | PASS |
| 5 | Al cortar en «Enlaces», el relevo recarga y ve «Este enlace se cortó» | PASS |

## Hallazgos

Ninguno.

## Respuestas del día anterior

- El P3 de caché de `2026-11-05-MATU-50-telefono.md` lo respondió Jorge: el `index.html` se sirve con `no-cache`, pero una pestaña que ya está abierta no se recarga sola. Se deja para el sprint 4, como un aviso de que hay una versión nueva.

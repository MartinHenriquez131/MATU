# 2026-11-05 · MATU-50 · Prueba en el teléfono de la ficha ampliada

**Historia:** MATU-50 · Ficha ampliada (backend #41 y pantalla #42)
**Entorno:** staging, desplegado desde `main` en el commit `e7da531` (merge del #42), con la migración 0013 aplicada
**Revisó:** Martín Henríquez · **Fecha:** 05/11/2026 · **Teléfono y navegador:** Motorola Edge 50, Microsoft Edge
**Veredicto general:** PASS. Hay un P3

## Resultado

| # | Recorrido | Veredicto |
|---|---|---|
| 1 | En «Más sobre Elena», agregar dos secciones (Quién es y Cómo hablarle) con textos inventados | PASS |
| 2 | Editar una de las dos | PASS |
| 3 | Agregar «Sus remedios»: no aparece el botón de dictar y sí el aviso de remedios | PASS |
| 4 | Quitar una sección | PASS |
| 5 | Salir y volver a entrar: todo queda como se dejó, con la línea «Agregaste N secciones.» | PASS |

Con esto se cierra la prueba en el teléfono que quedó pendiente en `2026-11-05-MATU-50-ficha-ampliada-backend.md`.

## Hallazgos

| ID | Sev. | Hallazgo | Respuesta de Jorge | Verificado |
|---|---|---|---|---|
| P3-1 | P3 | **Después del despliegue, el teléfono siguió mostrando la versión anterior de la app** (sin «Más sobre…», y con la bajada «puedes compartir solo algunos», que ya no está en `main`) hasta que se cerró la pestaña y se volvió a abrir. Hay que revisar la caché del `index.html` de la app (MATU-58 usa `Cache-Control: no-cache`) y del navegador. Sin eso, quien prueba puede creer que una historia no está desplegada | El `index.html` ya va con `Cache-Control: no-cache`. El problema es la pestaña que sigue abierta, porque no lo vuelve a pedir. Se resuelve en la tarjeta del sprint 4 «Aviso de versión nueva de la app». Mientras tanto, después de cada despliegue, hay que cerrar la pestaña y volver a abrirla antes de probar | |

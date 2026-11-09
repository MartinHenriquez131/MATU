# 2026-11-07 · MATU-60 · Lista de insumos: imprimir y compartir como texto

**Historia:** MATU-60 · Lista de reposición: exportar, imprimir y compartir ([tarjeta](https://trello.com/c/I6aMB3nz))
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#57 (head e6e75d7, y después 639d06c) y MartinHenriquez131/MATU#45
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `disenador-revisor` y `revisor-documental` · **Fecha:** 07/11/2026
**Veredicto general:** PASS. No hay P1. El único P2 se corrigió antes de fusionar (639d06c)

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en e6e75d7, en 639d06c y en el merge 53bfdda. No se repitió el pipeline.
- **Entorno:** staging, desplegado desde `main` en 02a707e el 07-11 a las 13:01 (hora de Chile). En el log, `Running upgrade 0014 -> 0015` corre antes de que arranque Uvicorn (`entorno=staging`), y `/v1/salud` responde 200.
- **Teléfono:** Motorola Edge 50 con Microsoft Edge. Ctrl+P en la ficha se probó en el computador.
- **Qué no se revisó y por qué:**
  - el analista revisor no corrió: el CUMPLE del analista de Jorge está en `docs/legal/revision-matu-60.md`, y el prompt del sprint no pedía repetirlo;
  - el contraste del tema oscuro se revisó a la vista, sin medirlo con números.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | La lista trae los insumos de «Se acaban pronto» (decisión 117), ordenados por fecha, con los días que quedan y la cantidad sugerida en enteros (decisiones 119 y 120) | PASS | `consumption/domain/lista.py`: `entra()` con `avisa_hoy`, `max(1, techo(30*tu/td) - stock_estimado_hoy)` con `techo_division`, `clave_orden`; `test_lista_dominio.py`; `test_lista_api.py::test_la_lista_trae_lo_que_avisa_con_la_cantidad_y_en_orden` |
| 2 | Con `unidades_por_envase` la cantidad va en envases enteros, y si no, en la unidad del insumo. El envase sale solo del perfil (decisión 121). Migración 0015 reversible | PASS | `0015_perfil_unidades_por_envase.py`; `test_migraciones.py::test_0015_…`; `test_el_nombre_es_el_del_producto_y_el_envase_nunca_sale_del_catalogo`; `textoLista.ts` (`sufijoCantidad`); teléfono, paso 1 |
| 3 | Se imprime o se guarda como PDF, y se comparte como texto o se copia, sin un enlace nuevo (RF-15, RF-09, ADR-029 y ADR-031) | PASS | `ListaInsumos.tsx:228` (`navigator.share({ text })`), `:240` (`clipboard.writeText`), `:256` (`window.print()`); teléfono, pasos 3 y 4 |
| 4 | No lleva el nombre de la persona cuidada, datos de la ficha, precios ni comercios | PASS | `LineaListaInsumos`; `test_la_respuesta_trae_exactamente_los_campos_del_esquema`; teléfono, paso 3 |
| 5 | El texto no lleva los días, y el observador ve la lista sin botones | PASS | `textoDeLista`; `ListaInsumos.tsx:92` (`puede = rol !== 'observador'`); teléfono, paso 5 |
| 6 | Sin insumos por acabarse, la pantalla lo dice y deja armar la lista a mano | PASS | `test_la_lista_vacia`; `listaInsumos.test.tsx` |
| 7 | Funciona sin la capa 3 y sin la autorización de pedidos | PASS | 639d06c: la ruta va en `RUTAS_CAPAS_1_Y_2` y en `PETICIONES`, y el camino feliz en `FLUJOS` de `test_capa3_desacoplable.py` |
| 8 | Otro grupo da 404, la respuesta lleva `no-store` y nada de la lista queda en el navegador | PASS | `test_lista_api.py:292-309`; `no-store` en 200, 401 y 404 (`:94`, `:173`, `:247`); grep sin `localStorage` ni `sessionStorage` en `ListaInsumos.tsx` |
| 9 | La regla de impresión oculta toda la app, y Ctrl+P en la ficha imprime solo «Esta pantalla no se imprime.» | PASS | `web/src/index.css` (`body > :not([data-impresion])` y `:modal`); `web/pruebas/reglaImpresion.test.ts`; computador, paso 6 |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1. Pruebas de dominio | PASS | `test_lista_dominio.py` |
| 2. Integración: camino feliz y de error | PASS | `test_lista_api.py`, `test_envase_router.py`, `test_aislamiento.py` |
| 3. Contrato OpenAPI | PASS | `test_lista_contrato.py`; `familia.openapi.ts` regenerado |
| 4. Accesibilidad | PASS | Revisión visual de Martín (abajo) y la del diseñador de Jorge |
| 5. Revisión de la otra persona | PASS | Este informe; aprobado y fusionado por Martín el 07-11 a las 12:51 (53bfdda) |
| 6. Prueba que falla sin la corrección | PASS | `reglaImpresion.test.ts` falla si se quita la regla |

## Revisión visual (disenador-revisor)

Vista funcionando con Vite y los dobles, a 360 y 1280 px en claro y oscuro, y a 320 px con el texto al 200 %:
- sin desplazamiento horizontal;
- áreas táctiles de 48 px o más;
- sin valores escritos a mano.

**Veredictos:**
- Insumos: APROBADA.
- Lista de insumos: APROBADA.
- Campo del envase: APROBADA.

## Prueba en el teléfono

Staging, después de cerrar y volver a abrir la pestaña, con cuentas sintéticas:
1. **Envase de 20 unidades en un insumo:** se guarda y sigue ahí al volver a entrar.
2. **Lista de insumos:** trae los de «Se acaban pronto», con los días y la cantidad en envases.
3. **Compartir por WhatsApp:** sale solo texto, con el título y la fecha, sin los días, sin enlace y sin el nombre de la persona.
4. **Imprimir y guardar como PDF:** la hoja lleva solo el título, las líneas y el pie.
5. **Como observador:** ve la lista sin los botones de imprimir, compartir ni copiar.
6. **En el computador, Ctrl+P en la ficha:** sale solo «Esta pantalla no se imprime.».

**Resultado:** PASS en los seis pasos (informado por Martín el 07-11).

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P2 | Ninguna prueba corría la lista con la capa 3 quitada | `test_capa3_desacoplable.py`, `FLUJOS` | Agregar el flujo de la lista. **Corregido en 639d06c** |
| H2 | P3 | Los colores de `@media print` están repetidos a mano en `index.css` y ninguna prueba los compara con `@theme` | `web/src/index.css` | Para decidir (PO) |

## Para decidir (PO)

- H2: aceptar la duplicación de los colores de impresión o pedir una prueba que los compare.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | Agregó la lista a `FLUJOS` (07-11) | 639d06c | sí |
| H2 | No se acepta la repetición: se resuelve. `web/pruebas/coloresRepetidos.test.ts` falla si la impresión se separa de `@theme` o si los dos bloques del tema oscuro difieren. Ningún color cambia (08-11) | MATU_PROYECTO #62 | |

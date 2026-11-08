# 2026-11-07 · MATU-51 · «Compré» y «Me quedan»

**Historia:** MATU-51 · Registrar que se repuso un insumo ([tarjeta](https://trello.com/c/VVMURV9g))
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#60 (head 1d33851 y, al día con `main`, bda9219) y MartinHenriquez131/MATU#47
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor` y `disenador-revisor` · **Fecha:** 07/11/2026
**Veredicto general:** PASS. No hay P1

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en 1d33851 y en bda9219. No se repitió el pipeline.
- **Prueba puntual:** `test_cadena_migraciones.py` dio `9 passed` hasta la 0017.
- **Entorno:** staging, desplegado desde `main` en 3f7495a el 07-11 a las 20:21 (hora de Chile). En el log:
  - `Running upgrade 0016 -> 0017` corre antes de Uvicorn;
  - el arranque muestra `entorno=staging` y `diagnostico_proxy=apagado`;
  - `/v1/salud` responde 200.
- **Revisión obligatoria:** sí, por los datos de consumo.
- **Teléfono:** Motorola Edge 50 con Microsoft Edge.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | «Compré» y «Me quedan N», en un toque, recalculan en el acto el stock y la fecha. ETag nuevo, If-Match obligatorio y sin interfaz optimista | PASS | `router_reposicion.py` (`_responder`, 428 y 412); `test_compre_sin_if_match_es_428` (`test_reposicion_api.py:315`); `test_me_quedan_cobertura_maxima_412_y_428` (`:580`); teléfono, pasos 1 y 2 |
| 2 | La alerta se cierra con la regla de MATU-37, sin duplicarla | PASS | `reposiciones.py` reutiliza `reponer()`, `declarar_reposicion` y `dejan_de_corresponder`; `test_compre_con_la_alerta_de_la_fecha_ya_cerrada_funciona_sin_409` (`:169`) |
| 3 | Funciona sin la capa 3 (decisión C) | PASS | `test_capa3_desacoplable.py:64-65` y `:96-97`; solo importa de `consumption`, `core` y `shared` |
| 4 | Topes: envases de 1 a 99, unidad de 1 a 10.000, «Me quedan» de 0 a 100.000, y el stock no pasa de 100.000 ni de 10 años | PASS | `router_reposicion.py:95-100` y `:163-166`, con 422 por campo |
| 5 | Solo admin y cuidador. Pagador y observador reciben 404, un insumo sin seguir da 409 y otro grupo da 404 | PASS | `test_pagador_y_observador_404` (`:427`); `test_otro_grupo_y_perfil_ajeno_404` (`:442`); `test_compre_y_me_quedan_en_un_insumo_sin_seguir_es_409` (`:346`) |
| 6 | «Me quedan» no se guarda como compra, la fecha la pone el servidor, no hay historial, las compras se borran a los 90 días y la auditoría no lleva cantidades | PASS | `recontar`; `0017_conservar_compras.py:54` y `:103`; `test_tras_90_dias_del_retiro_consumo_conservar_borra_las_compras` (`:690`); `test_logs_errores_y_auditoria_sin_cantidad_stock_ni_nombre` (`:598`) |
| 7 | `FOR SHARE`: una compra al mismo tiempo que un retiro termina en 403 | PASS | `test_compre_simultaneo_a_un_retiro_espera_y_termina_en_403` (`:629`) |
| 8 | La 0017 se puede bajar y cuelga de la 0016 | PASS | `down_revision = "0016"`; las políticas son solo para `matu_owner` con `operacion` |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1. Pruebas de dominio | PASS | `test_reposicion_dominio.py` |
| 2. Integración: camino feliz y de error | PASS | `test_reposicion_api.py`, `test_aislamiento.py` |
| 3. Contrato OpenAPI | PASS | `test_reposicion_contrato.py`; decisiones 136 a 148 |
| 4. Accesibilidad | PASS | Revisión visual de Martín (abajo) |
| 5. Revisión de la otra persona | PASS | Este informe y la prueba en el teléfono; aprobado y fusionado por Martín el 07-11 a las 20:15 (3f7495a) |
| 6. Prueba que falla sin la corrección | No aplica | |

## Revisión normativa (analista-revisor)

- **CUMPLE** en minimización, finalidad, la conservación de 90 días (que coincide en la política, el registro, la migración y `conservacion.py`), quién lo ve y quién lo borra, la auditoría, la información al usuario, `POLITICA_VERSION` 0.10 y la capa 3.
- **REQUIERE CONSULTA LEGAL:** el derecho de acceso. Las compras anotadas no se ven en la app (H1).

## Revisión visual (disenador-revisor)

Probé a 360 px en claro y oscuro, y a 320 px con el texto al 200 %:
- **Panel «Compré»:** el foco cae en el campo con un anillo de 3 px.
- **Confirmación:** se lee la fecha completa, con ícono además del color.
- **Error de tope:** lleva ícono y texto.
- **«Guardando…»:** cabe entero.
- **En todos los anchos:** sin desplazamiento horizontal y sin valores escritos a mano.

**Veredicto:** Insumos queda APROBADA.

## Prueba en el teléfono

Staging, después de cerrar y volver a abrir la pestaña:
1. **«Compré», 1 envase, en un insumo de «Se acaban pronto»:** el insumo sale del bloque y la fecha cambia en el acto.
2. **«Me quedan 0» en otro insumo:** el insumo entra al bloque.

**Resultado:** PASS (informado por Martín el 07-11).

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P2 | Las compras anotadas se guardan 90 días, pero la titular no las puede ver en la app (derecho de acceso) | `registro-tratamientos.md:222` | Cubrirlo en MATU-54, y antes de usar datos reales confirmarlo con la consulta legal |
| H2 | P3 | A 320 px con el texto al 200 %, «Ya lo resolví» queda casi pegado a los bordes del botón (`angosto:px-0.5!`) | `m51-resolvi-320-light-200.png` | Opcional: el botón a todo el ancho en `angosto` |
| H3 | P3 | El `input` de la casilla «Seguir» mide 21 px. No se confirmó que la etiqueta dé los 48 px. Viene de antes | Medición del diseñador | Revisarlo en MATU-68, punto 1 |
| H4 | P3 | El 412 lleva en `detalle` el nombre de quien guardó el perfil, igual que el PATCH | `router_reposicion.py` (`_responder`) | Solo se anota |

## Para decidir (PO)

- Confirmar que MATU-54 cubre el acceso a las compras anotadas (H1).

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | Sí: MATU-54 «Mis datos» descarga las compras anotadas de los últimos 90 días (está en su descripción y en su «Definición de Terminado») | Trello MATU-54 | |
| H2 | Se corrige en MATU-68: «Ya lo resolví» a todo el ancho en `angosto` (ítem agregado el 08-11) | Trello MATU-68 | |
| H3 | Se corrige en MATU-68, punto 1 (el diseñador decide el tamaño de las casillas) | Trello MATU-68 | |
| H4 | Se anota. El 412 dice quién guardó, igual que el PATCH, a propósito (decisiones de la ficha) | — | |

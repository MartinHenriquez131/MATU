# 2026-11-07 · MATU-44 · Retirar la autorización y cortar los accesos de relevo

**Historia:** MATU-44 · Revocar el consentimiento y cortar los accesos de relevo ([tarjeta](https://trello.com/c/zAyxF6J0))
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#58 (head 312267e, después 15d5cec y, al día con `main`, 2353b2f) y MartinHenriquez131/MATU#46
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor`, `disenador-revisor` y `revisor-documental` · **Fecha:** 07/11/2026
**Veredicto general:** PASS en el código, el contrato y lo normativo. No hay P1. **Falta la prueba en el teléfono**, que va en un informe aparte

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en 312267e, 15d5cec y 2353b2f. No se repitió el pipeline.
- **Entorno:** staging, desplegado desde `main` en 02a707e el 07-11 a las 13:01 (hora de Chile). En el log:
  - `Running upgrade 0015 -> 0016` corre antes de Uvicorn;
  - el arranque muestra `entorno=staging` y `diagnostico_proxy=apagado`;
  - `/v1/salud` responde 200.
- **Revisión obligatoria:** sí, porque toca el consentimiento.
- **Qué no se revisó y por qué:**
  - el diálogo de retiro abierto no se capturó en la revisión visual de Martín. Lo aprobó el diseñador de Jorge en tres rondas, y se ve en la prueba en el teléfono;
  - la tarea de 90 días no se corrió sobre un retiro real de 90 días, porque staging no tiene ninguno.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | El retiro marca `revocado_en` con `revocacion_motivo = retiro` en la misma fila y corta, en la misma transacción, todos los accesos vigentes (también los bloqueados y los en pausa), con auditoría y un solo instante. Si falla un corte, todo vuelve atrás | PASS | `repositorio_retiros.py` (`FOR UPDATE`); `repositorio_accesos.py` (`ORDER BY a.id FOR UPDATE OF a`); `test_retiro_corta_vigentes_bloqueados_y_en_pausa_y_no_toca_vencidos_ni_cortados`; `test_si_falla_el_corte_de_un_acceso_todo_vuelve_atras` (`test_retiro_autorizacion_api.py:328`) |
| 2 | El relevo deja de ver la ficha en el acto (410 `relevo-revocado`, para siempre); escribir la ficha sin autorización da 403; otro grupo da 404 | PASS | `test_el_relevo_queda_cortado_para_siempre`; `test_la_ficha_tras_el_retiro_403…`; `test_otro_grupo_finalidad_y_persona_invalidas_404` |
| 3 | Retirar los insumos detiene el cálculo y los avisos y descarta las alertas abiertas (D5) | PASS | `consumption/infrastructure/efecto_retiro.py`; `test_retiro_consumo_api.py`; `test_avisos_integracion.py` |
| 4 | D1, D2, D4, D7 y D8, la barrera por rol en RLS, P2 y P6 | PASS | `app_retira_autorizacion()` en la 0016; los `CHECK` de `revocacion_motivo`; 409 `ya-retirada`; `test_se_retira_con_la_revision_anual_vencida`. D8 está en `GET …/consentimientos` (decisión 127), con `revocado_en` |
| 5 | D3 y P8: la ficha se borra a los 90 días y no a los 89, con `Reloj` y el rol de operación. Después del día 90 vuelve en blanco y con una clave nueva | PASS | `tarea_destruccion.py`; `plan_destruir_claves` (SECURITY DEFINER); `test_a_los_89_dias_no_y_a_los_90_si_y_es_idempotente`; `test_autorizar_despues_del_dia_90_destruye_aunque_la_tarea_no_haya_corrido` |
| 6 | «Retirar la autorización» en Grupo familiar, con su confirmación y los textos de `lenguaje.md` 22 | PASS (código) | `Grupo.tsx` (`<dialog>` con `showModal()`), `textosGrupo.ts`, `Compartir.tsx`; `grupoFamiliar.test.tsx` |
| 7 | La 0016 se puede bajar y cuelga de la 0015 | PASS | `test_0016_retiro_con_motivo_y_baja_al_esquema_de_0015`; `test_cadena_migraciones.py` (9 passed hasta la 0016) |
| 8 | Carrera entre el retiro y la creación de un acceso (agregada por Jorge después de la revisión) | PASS | 15d5cec: `test_crear_un_acceso_simultaneo_a_un_retiro_espera_y_termina_en_403` y `test_crear_un_acceso_primero_el_retiro_espera_y_lo_corta` |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1. Pruebas de dominio | PASS | `test_retiro_dominio.py` |
| 2. Integración: camino feliz y de error | PASS | `test_retiro_autorizacion_api.py`, `test_destruccion_ficha_api.py`, `test_retiro_consumo_api.py`, 184 líneas en `test_aislamiento.py` |
| 3. Contrato OpenAPI | PASS | `test_retiro_contrato.py`; `POST …/consentimientos/{finalidad}/retiro` con 404, 409 y RFC 7807 |
| 4. Accesibilidad | PASS | Revisión visual de Martín (abajo) y tres rondas del diseñador de Jorge |
| 5. Revisión de la otra persona | PASS en la revisión; **pendiente en el teléfono** | Aprobado y fusionado por Martín el 07-11 a las 12:58 (02a707e) |
| 6. Prueba que falla sin la corrección | No aplica | No se corrige un defecto |

## Revisión normativa (analista-revisor)

| Punto | Veredicto |
|---|---|
| Quién retira y qué ven el pagador y el observador | CUMPLE |
| El corte es inmediato, definitivo y queda auditado | CUMPLE |
| El plazo de 90 días es el mismo en la pantalla, la política y el registro | CUMPLE |
| Volver a autorizar dentro y después de los 90 días | CUMPLE |
| Retirar los insumos frena los avisos y avisa que la lista ya compartida no se borra | CUMPLE |
| Coherencia entre documentos y código (`POLITICA_VERSION` 0.10) | CUMPLE |
| CL-1 a CL-6 | REQUIERE CONSULTA LEGAL (ya están en su tarjeta) |

## Revisión visual (disenador-revisor)

- **Grupo familiar:** APROBADA. El estado se marca con ícono, texto y borde: sólido si está vigente, discontinuo si se retiró. Las fechas van en DD/MM/AAAA.
- **Enlaces después del retiro:** APROBADA.
- **El diálogo de retiro abierto:** sin captura (ver «Qué no se revisó»).

## Prueba en el teléfono

**Pendiente.** Va en `TESTER/2026-11-07-MATU-44-telefono.md` cuando Martín la haga:
- enlace de relevo en otro dispositivo;
- retirar la autorización;
- el enlace se corta en el acto;
- volver a autorizar;
- la tarea de 90 días a mano.

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P3 | No había una prueba de la carrera entre el retiro y la creación de un acceso | Comentario de `repositorio_retiros.py` | **Corregido en 15d5cec**, en los dos órdenes |
| H2 | P3 | La tarjeta decía `retirada_en` (D8), y el contrato entrega `revocado_en` en `GET …/consentimientos` | `docs/api/README.md`, decisión 127 | **Corregido:** la tarjeta ahora dice `revocado_en` |
| H3 | P2 | La tarea de 90 días se corre a mano, y el plazo de las copias de respaldo no está definido (CL-6) | `politica-privacidad.md:254`; `revision-matu-44.md:58` | Antes de usar datos reales (Jorge lo dejó en la lista de pendientes) |
| H4 | P3 | La política decía «90 días después de que termine» | `politica-privacidad.md:254` | **Corregido en MATU #46:** «que se retire o termine» |

## Para decidir (PO)

- **Decidido el 07-11:** una solicitud de borrado deja la ficha ilegible en el acto, sin esperar los 90 días. Lo implementa MATU-72, que también tiene que quitar la marca «[PENDIENTE: …]» de la línea 254 de la política.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | Agregó la prueba en los dos órdenes | 15d5cec | sí |
| H2 | Ajustó la tarjeta | Trello | sí |
| H3 | Queda para antes de usar datos reales | — | — |
| H4 | Corrigió la política | MATU #46 | sí |

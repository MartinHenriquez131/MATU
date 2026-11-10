# 2026-11-09 · MATU-47 y MATU-66 · Permisos acotados y RLS por operación y rol

**Historias:**
- MATU-47 · Acotar los permisos de matu_app sobre indice_token ([tarjeta](https://trello.com/c/xCVtDXeG));
- MATU-66 · Acotar por rol en RLS la escritura de acceso_relevo y clave_datos ([tarjeta](https://trello.com/c/tWrWXOuR)).

**PR revisados:** MartinHenriquez131/MATU_PROYECTO#70 (head 5dbd903 y, al día con `main`, 0fcd775) y MartinHenriquez131/MATU#58
**Revisó:** Martín Henríquez, con `qa-tester-revisor` y `analista-revisor` · **Fecha:** 09/11/2026
**Veredicto general:** PASS. No hay P1 ni P2

## Contexto

- **CI:** verde en `ci` y en `web`, en 5dbd903 y en 0fcd775. No se repitió el pipeline.
- **Prueba puntual:** `test_cadena_migraciones.py` dio 9 passed hasta la 0021.
- **Fusión:** #70 el 09-11 a las 16:57 (hora de Chile, ac3c78b). MATU #58 a las 16:53.
- **Despliegue:** staging a las 17:08 y la demo a las 17:09, con `0019 -> 0020` antes de Uvicorn y los dos en SUCCESS.
- **Teléfono:** no aplica, porque no hay pantalla. Los recorridos de la demo y de staging siguieron funcionando después de la 0020.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | `matu_app` en `indice_token`: SELECT e INSERT, UPDATE solo de `revocado_en` y sin DELETE | PASS | 0020: `REVOKE UPDATE, DELETE` y `GRANT UPDATE (revocado_en)`; `test_la_api_no_borra_un_token` |
| 2 | Un corte no se reabre y un vencimiento no se alarga | PASS | Trigger `token_vida_fija()` en `indice_token` y `acceso_relevo`; `test_la_api_no_reabre_una_revocacion_de_indice_token`, `test_nadie_alarga_el_vencimiento_de_indice_token`, `test_un_acceso_cortado_no_se_reabre_y_ninguno_se_alarga` |
| 3 | `acceso_relevo`: RLS separada por operación; crean y cortan solo admin y cuidador | PASS | `acceso_familia_leer`, `_crear` y `_cortar`, sin política de DELETE; `test_el_pagador_con_permiso_lee_los_accesos_pero_no_los_crea_ni_los_corta`, `test_nadie_borra_un_acceso_de_relevo` |
| 4 | `clave_datos`: RLS separada y escritura solo de admin y cuidador | PASS | `clave_familia_leer`, `_crear` y `_destruir`; `test_el_pagador_con_permiso_lee_la_clave_pero_no_la_crea_ni_la_destruye` |
| 5 | Nadie lee contraseñas | PASS | SELECT por columna, sin `password_hash` ni `mfa_secreto_cifrado`, y la función `iam_credencial()`; `test_nadie_lee_password_hash_con_sql_directo` |
| 6 | Una cuenta no se hace «operacion» | PASS | `usuario_propio_crear` con `NOT es_operacion`; `test_una_cuenta_no_se_hace_operacion_ni_cambia_su_estado_ni_se_borra` |
| 7 | La 0020 se puede bajar y cuelga de la 0019 | PASS | El `DOWNGRADE` restaura las políticas, los permisos, el trigger y la función; `test_migraciones.py` (+69) |
| 8 | El registro de tratamientos describe las medidas (MATU #58) | PASS | El analista da CUMPLE: `registro-tratamientos.md:34`, `:122`, `:189` y `:282` |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1 y 2. Pruebas | PASS | `test_aislamiento.py` y `test_conexion_app.py` |
| 3. Contrato | No aplica | No cambia la API |
| 4. Accesibilidad | No aplica | No hay pantalla |
| 5. Revisión de la otra persona | PASS | Aprobado y fusionado por Martín |
| 6. Prueba que falla sin la corrección | PASS | Cada prueba verifica un permiso o una política que no existe en la 0019 |

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P3 | La 0020 también restringe la creación del consentimiento a admin y cuidador, y eso no estaba en los criterios | `test_pagador_y_observador_no_dan_una_autorizacion` | Para decidir (PO): confirmar que entra en MATU-66 |
| H2 | P3 | Quedan políticas `FOR ALL` en la capa 3, en `care_circle` y en notificaciones | Docstring de la 0020 | Ya están asignadas a MATU-61 a 63, MATU-42 y MATU-79 |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | | | |
| H2 | | | |

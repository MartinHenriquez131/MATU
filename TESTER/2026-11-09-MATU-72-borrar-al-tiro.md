# 2026-11-09 · MATU-72 (y MATU-71) · Borrar los datos de la persona al tiro

**Historia:** MATU-72 · Borrar los datos de la persona al tiro, cuando se pide ([tarjeta](https://trello.com/c/FFmpTC8k)). Absorbe MATU-71: cerrar la carrera entre las escrituras de insumos y el retiro
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#66 (head 64bc2db y, al día con `main`, 0d26ec0). Documentos: MartinHenriquez131/MATU#53 (**sin fusionar**, en conflicto después de MATU #52)
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor` y `disenador-revisor` · **Fecha:** 09/11/2026
**Veredicto general:** PASS en el código, la normativa y el teléfono. No hay P1. **Queda pendiente fusionar MATU #53**, que lo resuelve Jorge

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en 64bc2db y en 0d26ec0. No se repitió el pipeline.
- **Prueba puntual:** `test_cadena_migraciones.py` dio 9 passed.
- **Entorno:** staging, desplegado desde `main` en 237a7f6 el 09-11 a las 10:57 (hora de Chile). En el log, `Running upgrade 0017 -> 0018` corre antes de Uvicorn y `/v1/salud` responde 200.
- **Revisión obligatoria:** sí, porque toca datos personales.
- **Teléfono:** Motorola Edge 50 con Microsoft Edge, más el PC para el relevo, de 11:20 a 11:40.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | La ficha queda ilegible en el acto: se destruye la clave, sin esperar los 90 días | PASS | `care_plan/infrastructure/efecto_retiro.py` (`borrar`, `_destruir`); `test_borrado_persona_api.py:139` y `:561` |
| 2 | Una sola transacción, con un solo instante: retira las autorizaciones con motivo `borrado`, corta los enlaces, destruye la clave, borra las secciones y los perfiles de consumo (las alertas y las compras caen en cascada). Si algo falla, no queda nada | PASS | `care_circle/application/borrado.py`; `:246`, `:366` (rollback) y `:431` (un instante) |
| 3 | Solo admin y cuidador. Pagador, observador y otro grupo reciben 404 | PASS | `router_borrado.py`; RLS de la 0018 con `app_retira_autorizacion()`; `:309`, `:320`, `:326`; `test_aislamiento.py` (+99 líneas) |
| 4 | Idempotente: pedirlo dos veces da 409 `ya-borrada`, y dos borrados a la vez también | PASS | `:231` y `:504` |
| 5 | Auditoría solo con identificadores | PASS | `repositorio_borrado.py` (`anonimizar`, `PERSONA_BORRAR`); `:588` |
| 6 | Se conservan las autorizaciones (con motivo `borrado`), los accesos sin el nombre de pila y la fila de la persona sin datos. La dirección se borra si nadie más la usa | PASS | `_ACCESOS_SIN_NOMBRE`; `:264`, `:294` y `:534`; la 0018 bloquea la fila (CHECK y trigger `persona_borrada_fija`) |
| 7 | Confirmación en la pantalla, con la casilla y el foco en «No borrar» | PASS | `Grupo.tsx`, `textosGrupo.ts`; `borrarPersona.test.tsx`; diseñador APROBADA; teléfono, paso C4 |
| 8 | MATU-71: las 13 escrituras de la ficha y de los insumos bloquean con `FOR SHARE`, y cruzadas con el retiro o el borrado terminan en 403 | PASS | `care_plan/api/dependencias.py` y `consumption/api/dependencias.py`; `test_escrituras_bloquean_api.py:143-145` |
| 9 | La 0018 se puede bajar y cuelga de la 0017 | PASS | `down_revision = "0017"`; el downgrade se detiene si ya hay personas borradas; `test_migraciones.py` (+47) |
| 10 | Política, registro y `lenguaje.md` 24 | PASS en contenido, **sin fusionar** | MATU #53: el analista lo da CUMPLE. Está en conflicto con `main` y lo resuelve Jorge |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1 y 2. Pruebas | PASS | `test_borrado_persona_api.py`, `test_escrituras_bloquean_api.py`, `test_aislamiento.py` |
| 3. Contrato | PASS | `POST /v1/personas-cuidadas/{persona_id}/borrado` con 200, 401, 404, 409 y 422 en `openapi.json`. El 404 cubre al rol sin permiso y al otro grupo |
| 4. Accesibilidad | PASS | Diseñador de Martín: la casilla mide 48 px, y «Borrar todo» queda inhabilitado y marcado así para el lector de pantalla |
| 5. Revisión de la otra persona | PASS | Fusionado por Martín el 09-11 a las 10:37 (16cd3dc) y probado en el teléfono |
| 6. Prueba que falla sin la corrección | PASS | Las pruebas de carrera de MATU-71 |

## Revisión normativa (analista-revisor)

- **CUMPLE** en la supresión en el acto, la transacción única, lo que se conserva y por qué, quién puede pedirlo, la información al usuario (`lenguaje.md` 24 y la política §10) y la auditoría.
- **REQUIERE CONSULTA LEGAL:** CL-6 ampliada (las copias de respaldo), CL-7 (quién pide el borrado por correo y cómo se verifica su identidad) y CL-8 (el plazo de lo que se conserva).

## Prueba en el teléfono

Staging, con una persona de prueba:
1. **C1:** crear un enlace de relevo para la persona.
2. **C2:** abrirlo en el PC con el PIN y dejar la ficha abierta.
3. **C3:** en Grupo familiar, tocar «Borrar los datos de…».
4. **C4:** «Borrar todo» queda apagado hasta marcar la casilla. Se marca y se confirma.
5. **C5:** al recargar en el PC, el enlace sale cortado.
6. **C6:** la persona ya no aparece.

**Resultado:** PASS (informado por Martín el 09-11, de 11:20 a 11:40). No se hicieron capturas con el enlace ni el PIN.

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P2 | MATU #53 quedó en conflicto con `main` después de fusionar MATU #52 | GitHub: `mergeable_state=dirty` | Resolver el conflicto (Jorge) y que lo fusione Martín |
| H2 | P2 | El registro de MATU #53 dice dos veces «[PENDIENTE: plazo, CL-8]», que en la numeración nueva es CL-27 | Revisor documental del #54 | Cambiarlo al resolver el conflicto |
| H3 | P3 | La tarjeta dice «compras», y el código las llama reposiciones | `consumption/infrastructure/efecto_retiro.py` | Solo se anota, para el vocabulario |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | | | |
| H2 | | | |
| H3 | | | |

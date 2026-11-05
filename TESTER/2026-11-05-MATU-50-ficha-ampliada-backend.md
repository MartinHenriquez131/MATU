# 2026-11-05 · MATU-50 · Ficha ampliada (backend)

**Historia:** MATU-50 · Ficha ampliada: seis secciones complementarias, cifradas y compartibles con el relevo (ADR-028, RF-03)
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#41 (commit de24c77), junto con MartinHenriquez131/MATU#25 (commit fa55fd0)
**Revisó:** Martín Henríquez, con `qa-tester-revisor` y `analista-revisor` · **Fecha:** 05/11/2026
**Veredicto general:** PASS. No hay P1 ni P2

## Contexto de la revisión

- **CI del PR:** verde. El check `ci` dio *success* sobre `de24c77` el 04/11 a las 23:19 (hora de Chile), así que no se repitió el pipeline completo.
- **Prueba puntual** en una base desechable con `alembic upgrade head`: `test_secciones_{api,relevo_api,contrato,dominio}.py`, `test_cifrador_secciones.py`, `test_aislamiento.py` y `test_migraciones.py`. Resultado: **347 passed**.
- **Entorno:** revisión del código y de los documentos. Sin teléfono: el PR es solo backend.
- **Qué no se revisó:**
  - la comparación línea a línea del contrato contra `propuestos/ficha-ampliada.openapi.yaml` (lo cubre `test_secciones_contrato.py`);
  - el recorrido en pantalla, que va en el PR #42.

## Criterios (ADR-028, líneas 91-97, y decisiones 91 a 103 de `docs/api/README.md`)

MATU-50 no tiene entrada en `docs/backlog-sprints-1-3.md` (P3-1).

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Seis secciones opcionales; largo máximo 500, y 800 en «Sus remedios» | PASS | `test_secciones_api.py:148`, `:351`; CHECK de tipos en `0013_ficha_ampliada.py` (a) y (b) |
| 2 | AES-256-GCM con la clave de la persona y AAD `plan_id ‖ tipo` | PASS | `domain/cifrado.py:150`; `infrastructure/cifrador_aes_gcm.py:57`, `:64`, `:76`, `:127`; sin texto en claro en `contenido_cifrado` (`test_secciones_api.py:115`, `:165`) |
| 3 | Nunca texto en claro en logs, errores ni auditoría | PASS | `router_secciones.py:238`; 422 sin el valor (`test_secciones_api.py:337`, `:347`); logs (`:469`); auditoría (`:443`, `:465`); CHECK `auditoria_detalle_acotado` (0013 e) |
| 4 | 404 fuera de las seis secciones y para otro grupo, nunca 403 | PASS | `test_secciones_api.py:364`, `:373`, `:397`. El único 403 es el de falta de consentimiento (`:413`), como en la ficha |
| 5 | ETag, 412 con `actual`, 428 y 422 de precondición | PASS | `test_secciones_api.py:201`, `:221`, `:230`, `:244`, `:283`, `:292`, `:300`, `:312`; `router_secciones.py:194-213` |
| 6 | Leer quien ve el plan; escribir solo admin y cuidador, también en RLS (decisión 102) | PASS | `test_secciones_api.py:183`, `:397`; políticas `seccion_leer/crear/editar/borrar` (0013 f); SQL directo en `test_aislamiento.py:387` |
| 7 | El relevo ve solo las secciones compartidas que existían al crear el acceso | PASS | política `seccion_relevo` (0013 d); `repositorio_relevo.py:49-51`; trigger `plan_seccion_creado_fijo`; `test_secciones_relevo_api.py:82`, `:101`, `:191`, `:202`, `:231` |
| 8 | Migración 0013 reversible, con `down_revision = "0012"` | PASS | `test_migraciones.py:551`, `:597`. El downgrade no borra datos: aborta si quedan secciones nuevas |
| 9 | Decisión 103: `matu_app` sin DELETE en `plan_cuidado` | PASS | 0013 (g); `test_aislamiento.py:427`, `:446` |
| 10 | `openapi.json` coherente con la API; `campos` queda deprecado | PASS | `test_secciones_contrato.py:40`, `:48`, `:54`, `:72` |

## Revisión normativa (analista-revisor)

| Punto | Veredicto |
|---|---|
| «Sus remedios» como dato sensible: cifrado, tope y sin interpretación | CUMPLE |
| «Sus remedios» no se comparte por defecto | CUMPLE |
| Sin diagnóstico ni términos prohibidos | CUMPLE |
| Quién ve cada sección (roles y relevo), igual a la política §208 | CUMPLE |
| Conservación y borrado («se borra en ese momento») | CUMPLE |
| Auditoría sin texto | CUMPLE |
| ADR-029: sin imprimir ni exportar | CUMPLE |
| La política y el registro describen lo implementado (MATU#25) | CUMPLE, con P3-4 |
| Dictado por voz en «Sus remedios» y la sección sin consulta previa | REQUIERE CONSULTA LEGAL (ya está en la tarjeta; el dictado sigue apagado) |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1. Pruebas de dominio | PASS | `test_secciones_dominio.py`, `test_cifrador_secciones.py` |
| 2. Integración: camino feliz y de error | PASS | `test_secciones_api.py`, `test_secciones_relevo_api.py` |
| 3. Contrato OpenAPI | PASS | `test_secciones_contrato.py` |
| 4. Accesibilidad | No aplica | Solo backend; las pantallas van en el #42 |
| 5. Revisión de la otra persona | PASS | Este informe |
| 6. Prueba que falla sin la corrección | PASS | Decisiones 102 y 103 con prueba (`test_aislamiento.py:387`, `:427`) |

## Prueba en el teléfono

No aplica a este PR. El recorrido de MATU-50 en el teléfono se hace con la pantalla (#42), en staging, cuando MATU-58 publique la app de familia.

## Hallazgos

| ID | Sev. | Hallazgo | Respuesta de Jorge | Verificado |
|---|---|---|---|---|
| P3-1 | P3 · Para decidir (PO) | MATU-50 no está en `docs/backlog-sprints-1-3.md`. La revisión se hizo contra ADR-028 y las decisiones 91 a 103. ¿Se agrega con sus criterios, como MATU-57 y MATU-41 en la v1.4? | | |
| P3-2 | P3 · Para decidir (PO) | `seccion_relevo` usa `creado_en <= a.creado_en`: una sección creada en el mismo instante que el acceso sí se ve. ADR-028 dice «agregadas después». ¿Se confirma ese borde? | | |
| P3-3 | P3 | Los tipos `horarios` y `actividades` siguen en el CHECK de la base aunque la API ya no los escribe. Está documentado en la 0013 (a); queda como deuda | | |
| P3-4 | P3 · Para decidir (PO) | Si se edita una sección que ya se compartió, un acceso vigente ve el texto nuevo, también en «Sus remedios» (`domain/secciones.py:16-18`). Tiene sentido, porque el relevo necesita la dosis vigente, pero `politica-privacidad.md:208` solo habla de secciones agregadas después. Propuesta: «Si editas una sección que compartiste, el relevo ve el texto nuevo». No es un uso nuevo | | |
| P3-5 | P3 | Un 412 descifra y devuelve la sección vigente, pero se audita como `plan.leer` sin el tipo de sección (`application/secciones.py:98`). No se filtra nada, pero el registro de acceso de la titular queda menos preciso | | |

## Para decidir (PO)

- P3-1, P3-2 y P3-4.

# 2026-11-11 · MATU-85 y MATU-83 · Correcciones de los informes y teléfonos en el relevo

**PR revisados:**
- MartinHenriquez131/MATU_PROYECTO#79 (MATU-85): botones, número enmascarado, pruebas y la cita de la 0021;
- MartinHenriquez131/MATU_PROYECTO#80 (MATU-83): el teléfono del relevo no se parte, y la pregunta de «A quién llamar» le habla a quien reemplaza;
- MartinHenriquez131/MATU#67 (`lenguaje.md` 5.3);
- MartinHenriquez131/MATU#68 (respuestas de Jorge).

**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `disenador-revisor` y `revisor-documental` · **Fecha:** 10 y 11/11/2026
**Veredicto general:** PASS, también en el teléfono. No hay P1

## Fusiones y despliegue (hora de Chile)

| PR | Commit |
|---|---|
| MATU #67 | 8084eb5 |
| MATU_PROYECTO #79 | 3d3590b, al día con `main` y vuelto a aprobar |
| MATU #68 | 3d306e2 |
| MATU_PROYECTO #80 | ea0d06d, al día con `main` y vuelto a aprobar |

Staging y la demo se desplegaron desde ea0d06d, los dos en SUCCESS, a las 23:44 del 10-11. No hay migración ni variables nuevas.

## Revisiones

| PR | QA | Diseñador | Documentos |
|---|---|---|---|
| #79 | PASS: 10 de 13 pruebas fallan sin la corrección; la 0021 solo cambia el docstring; no rompe ninguno de los 21 usos de `Boton` | APROBADA: «Confirma tu celular» y «Tu cuenta» a 320 px con texto al 200 % | — |
| #80 y MATU #67 | PASS: el texto queda intacto, no hay inyección, 8 de 53 pruebas fallan sin el cambio y no toca la API | APROBADA: 8 teléfonos, con espacios, con guiones y sin separadores | Sin P1. P2: falta la línea en la cabecera de `lenguaje.md` y la cita de la tarjeta |
| MATU #68 | — | — | Solo cambia las tablas de respuesta. Va después del #79 |

## Prueba en el teléfono

Staging, Motorola Edge 50 con Edge y la letra del teléfono al máximo, el 10-11 (informado por Martín):
1. **A1 · «Tu cuenta»:** el número se corta solo entre «+56 9» y «•••• ••37». **OK**
2. **A2 · «Confirma tu celular»** con el código enviado: «Enviar» no se parte. **OK**
3. **A3 · Lo mismo en tema oscuro**, que el diseñador no alcanzó a ver. **OK**
4. **B1 · El editor de la familia** sigue con «¿A quién llamar si algo pasa y no te ubican?». **OK**
5. **B2 · El relevo**, con teléfonos inventados escritos con espacios, con guiones y sin separadores: dice «¿A quién llamar si algo pasa?» y ningún número se corta entre sus dígitos. **OK**
6. **B3 · El acceso de relevo de prueba** se cortó al terminar. **OK**

**Resultado:** PASS.

## Hallazgos

| ID | Severidad | Hallazgo | Qué pido |
|---|---|---|---|
| H1 | P2 | `lenguaje.md` no anota en su cabecera el cambio de 5.3, y la decisión no cita MATU-83 | Agregarlo en la próxima corrección de documentos |
| H2 | P3 | Para decidir (PO): la pregunta 5.1 («Puedes contar…») también le habla a quien escribe la ficha | Decidir si cambia en el relevo |

La ficha de la familia todavía parte los teléfonos. Ya tiene su tarjeta: MATU-86.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | Corregido (MATU-88). La cabecera de `lenguaje.md` anota MATU-83 (la 5.3 del relevo), MATU-84 (la sección 30) y MATU-88, y la decisión de la 5.3 cita MATU-83 | MATU `afe69c3` y `6932650` (rama `docs/matu-88-correcciones`) || sí, 11-11: teléfono (MATU-88, D1 a D4) |
| H2 | Corregido (MATU-88), según la decisión de Jorge del 11-11. En el relevo, «Su día» pregunta «¿Cómo es un día normal para {nombre}?», sin «Puedes contar un día bueno o uno difícil.». El editor de la familia sigue igual. `lenguaje.md` 5.1 suma la variante del relevo. Con una prueba que falla sin el cambio | MATU_PROYECTO `a2a42f4` (rama `matu-88-correcciones-tester`) y MATU `afe69c3` || sí, 11-11: teléfono (MATU-88, D1 a D4) |

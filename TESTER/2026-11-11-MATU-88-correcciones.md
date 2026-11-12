# 2026-11-11 · MATU-88 · «Su día» del relevo y el envase en sobres

**Origen:** los hallazgos de Martín en `TESTER/2026-11-11-MATU-85-83-correcciones-y-relevo.md` (H1 y H2) y en `TESTER/2026-11-11-MATU-84-envases.md` (H1, H2 y H3).
**PR revisados:** MartinHenriquez131/MATU_PROYECTO#82 (head a2a42f4) y MartinHenriquez131/MATU#73
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `disenador-revisor` y `revisor-documental` · **Fecha:** 11/11/2026
**Veredicto general:** PASS, también en el teléfono. No hay P1 ni P2

## Fusión y despliegue (hora de Chile)

MATU #73 (2a98485) y #82 (c304812). Staging y la demo desplegados desde c304812, los dos en SUCCESS a las 17:47. No hay migración ni variables.

## Revisiones

| PR | Veredicto | Evidencia |
|---|---|---|
| #82 · QA | PASS | 6 pruebas fallan sin el cambio; el editor de la familia y las unidades no cambian; sin backend |
| #82 · Diseñador | APROBADA | «Su día» del relevo y «sobres» en el envase, de 320 px con texto al 200 % a 1920 px, en tema claro y oscuro |
| MATU #73 · Documentos | Sin P1 ni P2 | Cabecera de `lenguaje.md` con MATU-83, 84 y 88; 5.3 cita MATU-83; 5.1 con la variante del relevo |

## Prueba en el teléfono

Staging, Motorola Edge 50 con Edge y la letra al máximo, el 11-11 de 17:48 a 17:54 (informado por Martín):
1. **D1 · El relevo:** «Su día» muestra solo «¿Cómo es un día normal para …?». El acceso de prueba se cortó al terminar. **OK**
2. **D2 · El editor de la familia** sigue con «Puedes contar un día bueno o uno difícil». **OK**
3. **D3 · Un insumo en sobres:** la pregunta y el error dicen «sobres». **OK**
4. **D4 · El H3 de MATU-84:** tocar la palabra «Seguir» marca la casilla, así que la etiqueta da el área táctil. **OK**

**Resultado:** PASS. Los hallazgos de origen quedan corregidos y verificados.

## Hallazgos

| ID | Severidad | Hallazgo | Qué pido |
|---|---|---|---|
| H1 | P3 | En los informes de TESTER, las dos filas H1 de la misma corrección citan commits distintos | Citar los mismos |
| H2 | P3 | En `lenguaje.md` 5.1, la variante del relevo pone primero la razón y después el texto | Poner primero el texto, como en la 5.3 |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | | | |
| H2 | | | |

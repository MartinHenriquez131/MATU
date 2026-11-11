# 2026-11-11 · MATU-84 · «Me quedan» y el alta del insumo, también en envases

**Origen:** el hallazgo U3 (P2) de la usabilidad ronda 1 (MATU-34): quien controla el stock «a la vista» no puede declarar lo que le queda sin contar unidades.
**PR revisados:** MartinHenriquez131/MATU_PROYECTO#81 (head 8ce62e8) y MartinHenriquez131/MATU#70 (`lenguaje.md` sección 30)
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `disenador-revisor` y `revisor-documental` · **Fecha:** 11/11/2026
**Veredicto general:** PASS, también en el teléfono. No hay P1 ni P2 de código

## Fusión y despliegue (hora de Chile)

- MATU #70: fusionado (59403a8).
- #81: fusionado al día con `main` (594eded).
- Staging y la demo: desplegados desde 594eded, los dos en SUCCESS a las 12:23. No hay migración ni variables.

## Revisiones

| PR | Veredicto | Evidencia |
|---|---|---|
| #81 · QA | PASS | Ver el detalle debajo |
| #81 · Diseñador | APROBADA | Ver el detalle debajo |
| MATU #70 · Documentos | Sin P1 | Los 11 textos coinciden con el código y la especificación. No hay términos prohibidos y la numeración no tiene saltos |

**QA del #81:**
- La conversión de envases a unidades usa solo enteros, y está probada en los casos límite (campos vacíos, envase faltante, de 0 o de 1, y un total sobre 100.000).
- A la API se sigue mandando `stock_unidades` entero. No se tocan el backend, el contrato ni las migraciones.
- 41 pruebas fallan sin el cambio, y `compreMeQuedan` pasó 5 de 5 veces.

**Diseñador del #81:**
- Revisó 6 estados a 320 px con texto al 200 %, a 360 px, a 1280 px y a 1920 px, en tema claro y oscuro.
- No hay desplazamiento horizontal ni palabras partidas.
- Las áreas táctiles miden 48 px o más.
- El error no se marca solo por el color.

## Prueba en el teléfono

Staging, Motorola Edge 50 con Edge y la letra al máximo, el 11-11 de 12:23 a 12:32 (despliegue en SUCCESS a las 12:23 y resultado informado a las 12:32):
1. **C1 · «Me quedan» en envases**, con 3 envases de 20 y 5 sueltos: muestra y guarda 65. **OK**
2. **C2 · Un insumo sin envase:** pide las unidades por envase, y si se deja vacío aparece el error. **OK**
3. **C3 · Volver a «Contar sueltos»:** funciona como antes. **OK**
4. **C4 · Alta de un insumo en envases:** la vista previa usa el total correcto. **OK**
5. **C5 · «Compré»:** sin cambios. **OK**

**Resultado:** PASS.

## Hallazgos

| ID | Severidad | Hallazgo | Qué pido |
|---|---|---|---|
| H1 | P2 | La cabecera de `lenguaje.md` no registra MATU-84 | Agregarlo en MATU-88, junto con el de MATU-83 |
| H2 | P3 | El error «Escribe cuántas unidades trae cada envase.» dice «unidades» también en los insumos en sobres | Para decidir (PO): si se agrega una variante para sobres |
| H3 | P3 | Las casillas «Seguir» miden 26×26 px. Su `label` da el área táctil, y este PR no las cambia | Se anota |

**Quedó sin revisar a fondo:** el foco con lector de pantalla, los errores del servidor (412, 500 y 422) en el envase, y los insumos en ml o en sobres.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | | | |
| H2 | | | |
| H3 | | | |

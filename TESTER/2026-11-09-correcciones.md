# 2026-11-09 · Correcciones de la revisión del 09-11 (MATU-68, MATU-57, MATU-72, MATU-59, MATU-82 y MATU-64)

**Qué cubre:** las correcciones de Jorge a los hallazgos de los informes del 09-11, en un solo informe (sugerencia de Jorge).
**PR revisados:**
- MartinHenriquez131/MATU#60 · documentos: MATU-68 H3 y H4, MATU-59 H1, MATU-72 H3, MATU-82 H3 a H6, y la decisión D2 del relevo;
- MartinHenriquez131/MATU_PROYECTO#72 · frontend: MATU-57, MATU-68 H1 y H2, y palabras partidas con la letra al 200 %;
- MartinHenriquez131/MATU_PROYECTO#73 · el relevo sin el ejemplo (H3 de MATU-64);
- MartinHenriquez131/MATU_PROYECTO#75 · backend: MATU-64 H1, MATU-59 H1 y MATU-72 H3.

**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor`, `disenador-revisor` y `revisor-documental` · **Fecha:** 09/11/2026
**Veredicto general:** PASS, también en el teléfono. No hay P1. Queda un P2 de diseño (H1) para un PR aparte

## Fusiones y despliegue (hora de Chile)

| PR | Fusión | Commit |
|---|---|---|
| MATU #60 | 09-11, 16:54 | b2551d2 |
| MATU_PROYECTO #75 | 09-11, 20:01 | 5823527 |
| MATU_PROYECTO #73 | 09-11, 20:11 | 960e7b2 |
| MATU_PROYECTO #72 | 09-11, 20:21 | 47e2e0d |

Staging y la demo se desplegaron desde 47e2e0d a las 20:52, los dos en SUCCESS. Ningún PR trae migración.

## Hallazgos de origen y su corrección

| Informe | Hallazgo | Corregido | Evidencia |
|---|---|---|---|
| MATU-68 | H1 · `px-0!` quitado sin pedirlo | Sí | No queda ningún `px-0!` en `web/src`; regla en `Demo/DISENO.md` §6 (#72) |
| MATU-68 | H2 · `[PROPUESTO]` en `datos.ts:59` | Sí | Quitado (#72) |
| MATU-68 | H3 · «diagnóstico» en la ayuda de la ficha frente a `lenguaje.md:61` | Sí | `lenguaje.md:65`: excepción escrita para la ayuda de la ficha (MATU #60) |
| MATU-68 | H4 · dueño de la sección 25 | Sí | `lenguaje.md:835-837`: es de MATU-68 (MATU #60) |
| MATU-59 | H1 · la bolsa colectora | Sí | «Higiene y cuidado personal», decisión D3 (`lenguaje.md:956`, `catalogo_demo.py:106`); `test_semilla_catalogo.py` (MATU #60 y #75) |
| MATU-72 | H3 · «compras» o «reposición» | Sí | «Compras anotadas» en lo que ve el usuario (`router.py:284`, `:477`, `router_alertas.py:99`); en el contrato cambian solo descripciones (#75); `lenguaje.md:785` (MATU #60) |
| MATU-82 | H3 a H6 · equivalencias CL, «26 comentarios», CL-13 y CL-37 | Sí | `consulta-legal.md:11`, `:15`, `:172-174`, `:452`, y la tabla de `:628` (MATU #60) |
| MATU-64 | H1 (de Jorge) · el PIN de `SEMILLA_PIN` en el archivo y la consola | Sí | `guardar_relevo(..., pin_de_entorno=True)`; `test_con_semilla_pin_el_archivo_guarda_solo_el_enlace`, `test_el_pin_de_semilla_pin_no_se_escribe_ni_se_imprime` (#75). El analista da CUMPLE |
| MATU-64 | H3 · el ejemplo con un teléfono bajo «A quién llamar» en la hoja del relevo | Sí | `MOSTRAR_EJEMPLO = false` (`relevo/textos.ts:94`); `relevoSinEjemplo.test.tsx`; decisión de Jorge que cambia la D2 (`lenguaje.md`, MATU #60). El diseñador da APROBADA |
| MATU-57 | Palabras partidas en «Tu cuenta» y «Confirma tu celular» | Sí, con un pendiente | `Cuenta.tsx:66`, `:71`, `:145`, `:155`, `:325`, `:350`; `cuentaAngosto.test.tsx`. El diseñador da APROBADA a «Tu cuenta» y a «Confirma tu celular» antes del código. Ver H1 |

## Revisión visual (disenador-revisor)

| Pantalla | Veredicto |
|---|---|
| «Tu cuenta» | APROBADA |
| «Confirma tu celular» antes de enviar el código | APROBADA |
| «Confirma tu celular» con el código enviado | CAMBIOS REQUERIDOS (H1) |
| Pantalla de permiso con «María lo autoriza y yo lo registro» | PASS en el teléfono (D1 y D2) |
| Hoja del relevo sin el ejemplo | APROBADA |

## Prueba en el teléfono

Motorola Edge 50 con Edge, **con la letra del teléfono al máximo**, el 09-11 (informado por Martín):
1. **B2 · «Tu cuenta»** (staging): ninguna palabra partida y nada se sale de la pantalla. **OK**
2. **C1 · «Confirma tu celular»** (staging), antes de enviar el código: sin palabras partidas, «WhatsApp» entero. **OK**. El «En-viar» del botón de reenvío es el H1 conocido.
3. **D1 · Pantalla de permiso** con «María lo autoriza y yo lo registro» (staging): el texto de la opción queda bajo el indicador, sin palabras partidas. **OK**
4. **D2 · Nota «Lo que declaras»:** «representante» no se parte. **OK**
5. **F1 · Hoja del relevo de Rosa** (demo): solo la pregunta guía y el contenido, sin ningún «Por ejemplo» ni el número 5555 0102. **OK**

**Resultado:** PASS.

## Hallazgos nuevos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P2 | Con el código enviado y a 320 px con el texto al 200 %, «¿No te llegó? Enviar otro código» parte «En-/viar». La causa es `hyphens-auto` en la base de `Boton` (`web/src/compartido/ui/Boton.tsx:72`), así que puede pasar en otros botones | `s4d-p72-codigo-320z.png` | PR aparte. Para decidir (PO): quitar el guionado de todos los botones o solo de los de texto |
| H2 | P3 | `ConfirmarCelular` no tiene una prueba propia en angosto | `cuentaAngosto.test.tsx` solo renderiza `TuCuenta` | Opcional |
| H3 | P3 | El número «+56 9 •••• ••37» se reparte en dos líneas a 320 px con el texto al 200 % | `s4d-p72-codigo-320z.png` | Espacio duro o `whitespace-nowrap` en el número |
| H4 | P3 | `lenguaje.md:460` todavía dice «Lista de reposición, pedido y boleta», y la regla es «lista de insumos» | MATU #60 | Cambiarla en la próxima corrección de documentos |
| H5 | P3 | El `web` del #73 falló una vez después de ponerlo al día, con `ReferenceError: document is not defined` originado en `pruebas/compreMeQuedan.test.tsx`, con todas las pruebas en verde. Al volver a correrlo pasó | Corrida 42716973231, 09-11 | Hacer estable esa prueba de MATU-51 (cerrar los temporizadores o esperar lo pendiente antes de terminar) |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | Opción A, en todos los botones: cortan por palabras (`max-w-full break-words`), sin guionado. Los títulos no se tocan. Diseñador APROBADA | MATU_PROYECTO #79 (5702dd5) || sí, 11-11: QA PASS, diseñador APROBADA y teléfono (A2 y A3) |
| H2 | «Confirma tu celular» tiene su prueba en angosto | MATU_PROYECTO #79 (58ffd82) || sí, 11-11: la prueba falla sin la corrección |
| H3 | Opción B: «+56 9» y «•••• ••37» van juntos, con espacios duros, y solo se corta entre los dos bloques. Solo en pantalla | MATU_PROYECTO #79 (25eee24) || sí, 11-11: teléfono (A1) |
| H4 | `lenguaje.md` dice «Lista de insumos, pedido y boleta» | MATU #66 || sí, 11-11: MATU #66 fusionado (f383dea) |
| H5 | La causa eran los temporizadores de foco de Insumos, que seguían vivos después del `cleanup`. `preparacion.ts` los espera después de cada prueba, con un tope de 2 s. Pasó 12 veces seguidas | MATU_PROYECTO #79 (0ad2c04) || sí, 11-11: CI en verde dos veces seguidas (#79 y #80) |

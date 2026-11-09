# 2026-11-09 · MATU-68 · Ajustes menores de la app de familia

**Historia:** MATU-68 · Ajustes menores de la app de familia ([tarjeta](https://trello.com/c/Z7O6rMKV))
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#64 (head da86fd5 y, al día con `main`, e8c75d7) y MartinHenriquez131/MATU#51
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `disenador-revisor`, `revisor-documental` y `analista-revisor` (política §5) · **Fecha:** 09/11/2026
**Veredicto general:** PASS. No hay P1 ni P2

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en da86fd5 y en e8c75d7. No se repitió el pipeline.
- **Pruebas puntuales:** se corrieron en una copia de la rama:
  - `focoTras422`, `casillasYBotones` y `altaSinDireccion`: 10 de 10;
  - mutación de `flushSync`: si se quita, `focoTras422.test.tsx` falla (3 de 5 sin el de Recuperar y 2 de 5 sin el de Cuenta).
- **Entorno:** staging, desplegado desde `main` en 237a7f6 el 09-11 a las 10:57 (hora de Chile).
- **Teléfono:** Motorola Edge 50 con Microsoft Edge, de 11:20 a 11:40.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Casillas de Insumos con la medida del diseñador y 48 px de área táctil | PASS | `Insumos.tsx:813`: `size-6` dentro de una etiqueta `min-h-12`; `Demo/DISENO.md`, fila «Casilla (checkbox nativa)»; diseñador: 48 px medidos; teléfono, paso A1 |
| 2 | «Ya lo resolví» en angosto (H2 de MATU-51) | PASS | `Insumos.tsx:2063-2067`, con `angosto:flex-col` y `angosto:w-full`; se quitó `angosto:px-0.5!`; teléfono, paso A2 |
| 3 | Foco tras un 422 en Recuperar y en Confirma tu celular | PASS | `Recuperar.tsx:47` y `:148-157`; `Cuenta.tsx:206-213`; la mutación de arriba; teléfono, paso A3 |
| 4 | El comentario de `SeccionesCompartir.tsx` queda al día | PASS | Líneas 1-19 |
| 5 | Sin textos `[PROPUESTO]` ni `[demo]` fuera de `lenguaje.md`, y sin funciones sin uso | PASS | `git grep` de `listarAlertas` y `descartarAlerta` vacío |
| 6 | Alta sin dirección | PASS | `Alta.tsx`; en `openapi.json`, `direccion` es opcional y anulable en `SolicitudPersona`; `altaSinDireccion.test.tsx` |
| 7 | Textos en `lenguaje.md` 25, 26 y 6.6, y política §5 (MATU #51) | PASS | Numeración sin choques (6.5 → 6.6 → 7 y 23 → 27); analista: CUMPLE en §5, y `POLITICA_VERSION` sigue en 0.10 |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1 y 2. Pruebas | PASS | `focoTras422.test.tsx`, `casillasYBotones.test.tsx`, `altaSinDireccion.test.tsx` |
| 3. Contrato | PASS | No cambia ninguna ruta |
| 4. Accesibilidad | PASS | Diseñador de Martín: Insumos y «Se acaban pronto» APROBADAS a 360 px en claro y oscuro, y a 320 px con el texto al 200 % |
| 5. Revisión de la otra persona | PASS | Fusionado por Martín el 09-11 a las 10:28 (01e6acc) y MATU #51 a las 10:06 |
| 6. Prueba que falla sin la corrección | PASS | La mutación de `flushSync` |

## Prueba en el teléfono

Staging, después de cerrar y volver a abrir la pestaña:
1. **A1 · Casillas de Insumos:** se ven más grandes y se tocan fácil.
2. **A2 · «Ya lo resolví» con el texto al máximo:** los botones no se cortan.
3. **A3 · Recuperar el acceso con un código malo:** el cursor queda en el campo del código.

**Resultado:** PASS (informado por Martín el 09-11, de 11:20 a 11:40).

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P3 | Se quitó `px-0!` en «Enviar otro código» y «¿No llegó?», que la tarjeta no pedía | `Recuperar.tsx:233`, `Cuenta.tsx:297` | Que el diseñador lo confirme (Para decidir) |
| H2 | P3 | Queda un `[PROPUESTO]` en un comentario de rutas | `datos.ts:59` | Opcional: quitarlo |
| H3 | P3 | `lenguaje.md:61` dice que «diagnóstico» va solo en textos legales, pero `:533` y `:568` lo usan en la ayuda de la ficha | MATU #51 | Para decidir (PO) |
| H4 | P3 | No se sabe qué historia es dueña de la sección 25 (el alta): `lenguaje.md:831` dice MATU-39 | MATU #51 | Confirmarlo |

## Para decidir (PO)

- H1: si se acepta quitar `px-0!` de los botones de texto.
- H3: si «diagnóstico» se queda en la ayuda de la ficha (y se corrige la línea 61) o se reescribe la ayuda.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | | | |
| H2 | | | |
| H3 | | | |
| H4 | | | |

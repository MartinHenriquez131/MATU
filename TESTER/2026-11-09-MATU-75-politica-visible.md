# 2026-11-09 · MATU-75 · La política de privacidad en la app, la versión aceptada y el correo de contacto

**Historia:** MATU-75 ([tarjeta](https://trello.com/c/LG4qPX65))
**PR revisados:** MartinHenriquez131/MATU_PROYECTO#71 (head 92b5568 y, al día con `main`, 36fddaf) y MartinHenriquez131/MATU#59
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor` y `disenador-revisor` · **Fecha:** 09/11/2026
**Veredicto general:** PASS en el código, en el teléfono y CUMPLE en lo normativo. No hay P1

## Contexto

- **CI:** verde en `ci` y en `web`, en 92b5568 y en 36fddaf.
- **Prueba puntual:** `test_cadena_migraciones.py` dio 9 passed hasta la 0021.
- **Fusión:** #71 el 09-11 a las 17:07 (hora de Chile, 1b73c55). MATU #59 (política 0.11) a las 16:54.
- **Despliegue:** staging a las 17:08 y la demo a las 17:09, con `0020 -> 0021` antes de Uvicorn.
- **Variables:** a las 17:33 se cargaron en las dos API `POLITICA_VERSION=0.11`, `POLITICA_ACTUALIZADA_EN=2026-11-09` y `CORREO_PRIVACIDAD=cuidaconmatu@gmail.com`, y se redesplegaron (los dos en SUCCESS a las 17:34). **Entre las 17:08 y las 17:34 staging y la demo corrieron sin esas variables** (H1).

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | `/privacidad` muestra la política vigente (0.11) y su versión, legible a 320 px con el texto al 200 % | PASS (código y diseñador) | `PaginaPrivacidad.tsx`, `politica-0.11.md`, `router_politica.py`; `paginaPrivacidad.test.tsx`. El diseñador: sin desplazamiento horizontal a 360 px y a 320 px con el texto al 200 % (`s4c-priv-*.png`) |
| 2 | Enlace desde las tres autorizaciones, crear cuenta, Tu cuenta y el relevo | PASS | `Alta.tsx:151` y `:704`, `Insumos.tsx:1169`, `Cuenta.tsx:113`, `relevo/PantallaPin.tsx:150`; `politicaEnLaApp.test.tsx`; teléfono, pasos A1, B1, D3 y E1 |
| 3 | Se guardan la versión, la fecha y la huella aceptadas al crear la cuenta, con migración reversible | PASS | 0021: tabla `aceptacion_politica`, de solo agregar, con FORCE RLS; `test_aceptar_estampa_la_version_y_la_huella_vigentes`, `test_aceptar_con_otra_huella_falla` |
| 4 | El buzón `cuidaconmatu@gmail.com` en la política, en `lenguaje.md` y en el relevo | PASS | MATU #59: política §2, §10 y §13; `lenguaje.md:305`, `:990` y `:1003`; `relevo/textos.ts` |
| 5 | `POLITICA_VERSION` y la huella coinciden con el texto | PASS | `test_cada_version_publicada_tiene_su_archivo_con_su_huella`, `test_un_texto_que_cambia_sin_cambiar_su_huella_no_se_sirve` |
| 6 | Corregir datos y eliminar la cuenta se piden al buzón | PASS | `politica-privacidad.md:385`; el analista da CUMPLE |

## Revisión normativa (analista-revisor)

- **CUMPLE:** la evidencia de cada aceptación (versión, huella y fecha, sin IP ni navegador), el buzón como tratamiento propio, y el cambio 0.10 → 0.11 justificado por un dato nuevo y un destinatario nuevo.
- **REQUIERE CONSULTA LEGAL (ya en la tarjeta):** CL-49 (cuánto se guarda la aceptación), CL-50 (si «acepto» es consentimiento o acuse) y CL-51 (Gmail en EE. UU.).

## Prueba en el teléfono

Staging, Motorola Edge 50 con Edge, **con la letra del teléfono al máximo**, el 09-11 (informado por Martín):
1. **A1 · Crear cuenta:** el enlace a la política está junto a la casilla. **OK**
2. **A2:** la política dice «Versión 0.11» y se lee hasta el final sin desplazamiento horizontal. **OK**
3. **B1 · Tu cuenta:** el enlace a la política está. **OK**
4. **D3 · Pantalla de permiso** («María lo autoriza y yo lo registro»): el enlace a la política está. **OK**
5. **E1 · Pantalla del PIN del relevo** (abierta en el PC): el enlace a la política y `cuidaconmatu@gmail.com`. **OK**. El enlace de prueba se cortó al terminar.

**Resultado:** PASS.

**Segunda parte, 09-11 de 23:40 a 23:51** (informado por Martín):
6. **G1 · Autorización de la ficha** (retirar y volver a autorizar): el enlace abre `/privacidad` con la versión 0.11. **OK**
7. **G2 · Autorización de insumos:** el enlace abre la política 0.11. **OK**
8. **G3 · Autorización de pedidos:** el enlace a la política está. **OK**
9. **H1 · El correo `cuidaconmatu@gmail.com`** abre la aplicación de correo con esa dirección. **OK**
10. **H2 · Correo de prueba** «Prueba MATU-75», sin datos personales, enviado sin error. **OK**

**Resultado de las dos partes:** PASS.

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P2 (resuelto) | El #71 necesitaba tres variables nuevas en Railway que no estaban en la descripción del PR (solo en el contrato y en `.env.example`). Staging y la demo corrieron 26 minutos sin ellas | Railway: despliegue a las 17:08 y variables a las 17:33 | Resuelto. Desde el 09-11, cada PR trae la sección «Para desplegar» (acuerdo con Jorge) |
| H2 | P3 | La 0021 cita «CL-75-2», que ahora es CL-49 | `0021_aceptacion_politica.py:14` y `:18` | Cambiar la referencia |
| H3 | P3 | Operación puede leer todas las aceptaciones | La política `aceptacion_operacion_leer` | Para decidir (PO) |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | «Para desplegar» en cada PR, desde el 09-11 | — | sí |
| H2 | La 0021, su prueba y la decisión 178 citan CL-49 | MATU_PROYECTO #79 (c1512a9) | |
| H3 | Decisión de Jorge del 10-11: se decide en MATU-81, cuando exista la consola de operación. Hoy ninguna ruta ni tarea usa ese permiso | ítem y comentario en MATU-81 | |

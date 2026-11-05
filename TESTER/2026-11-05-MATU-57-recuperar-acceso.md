# 2026-11-05 · MATU-57 · Recuperar el acceso y confirmar el celular

**Historia:** MATU-57 · Recuperar el acceso con un código y confirmar el celular
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#39 (commit 1f18dc3), junto con MartinHenriquez131/MATU#24 (commit 0111141)
**Revisó:** Martín Henríquez, con `qa-tester-revisor` y `analista-revisor` · **Fecha:** 05/11/2026
**Veredicto general:** PASS, con la prueba en el teléfono pendiente (P2-1)

## Contexto de la revisión

- **CI del PR:** verde. El check `ci` dio *success* sobre `1f18dc3` el 03/11 a las 19:46 (hora de Chile), así que no se repitió el pipeline.
- **Entorno:** revisión del código y de los documentos, sin staging ni teléfono.
- **Qué no se revisó:**
  - la comparación uno por uno de `web/src/familia/textos.ts` contra `lenguaje.md` 19 (P3-1);
  - la medición de tiempos en vivo de la respuesta 202.

## Criterios (decisiones 81 a 90, `docs/api/README.md:387-396`)

MATU-57 no tiene entrada en `docs/backlog-sprints-1-3.md`. Se revisó contra las decisiones y la especificación (`docs/diseno/matu-57-recuperar-acceso.md`).

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Código de 6 dígitos, 10 min, un solo uso, 5 intentos y comparación en tiempo constante (81) | PASS | `domain/recuperacion.py:6`, `:106-113`; Lua atómico en `recuperacion_redis.py:28-31`, `:88-94` |
| 2 | Envío simulado que no arranca en `produccion` (82) | PASS | `core/config.py:247-250`; prueba en `tests/core/test_configuracion.py` |
| 3 | Solo la huella HMAC en Redis con TTL; pedir otro código borra el anterior; trigger que borra la confirmación si cambia el número (83) | PASS | `recuperacion_redis.py:57-73`, `:96-100`; `0012_celular_verificado.py:28` (`down_revision = "0011"`), `:52-63`, downgrade `:66-81` |
| 4 | 202 igual exista o no la cuenta, sin enumeración (84) | PASS | `router_recuperacion.py:161-205` (BackgroundTasks y `no-store`); `application/recuperacion.py:153-168` |
| 5 | Límites por IP, correo y celular; 429 con `Retry-After` (84, 85, 87) | PASS | `application/recuperacion.py:146-177`, `:340-346`; `router_recuperacion.py:131, 145, 223, 303, 356` |
| 6 | Un solo 422 `codigo-invalido` (85) | PASS | `router_recuperacion.py:216-217`; `application/recuperacion.py:254-282` |
| 7 | El cambio de contraseña revoca todas las sesiones, sin emitir tokens (86) | PASS | `application/recuperacion.py:288`, `:297`; 204 en `router:264` |
| 8 | Auditoría y logs sin código, celular, correo, huellas ni IP | PASS | auditoría en `application/recuperacion.py:190, 263, 294, 362, 398, 426`; logs en `:119`, `:157` |
| 9 | Textos de los mensajes según `lenguaje.md` 19 (88) | PASS | `domain/recuperacion.py:46`, `:71` = `lenguaje.md:559` (MATU#24) |
| 10 | «Tu cuenta» con el celular enmascarado (89, 90) | PASS | `api/esquemas.py:209-218`; `lenguaje.md:557` |
| 11 | Nada sensible en el almacenamiento del navegador ni en la URL | PASS | `grep localStorage\|sessionStorage\|location\|history\|URLSearch` en `web/src/familia/*.tsx` no da resultados |

## Revisión normativa (analista-revisor)

| Punto | Veredicto |
|---|---|
| Minimización del celular y del canal | CUMPLE |
| La política y el registro describen lo implementado | CUMPLE, con P2-2 |
| No revela si una cuenta existe | CUMPLE |
| Logs y auditoría sin datos personales | CUMPLE |
| Derecho de acceso (celular enmascarado) | CUMPLE |
| `lenguaje.md` 19 y términos prohibidos | CUMPLE |
| Declaraciones de consumo con «avisarme» (MATU#24) | CUMPLE |
| Plazo de conservación del celular tras eliminar la cuenta (`registro-tratamientos.md:253`) | REQUIERE CONSULTA LEGAL |
| Base de licitud del celular obligatorio y de los contadores con huella | REQUIERE CONSULTA LEGAL |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1. Pruebas de dominio | PASS | `tests/.../test_recuperacion_dominio.py` |
| 2. Integración: camino feliz y de error | PASS | `test_recuperacion_api.py` (358 líneas) y las de aplicación y Redis |
| 3. Contrato OpenAPI | PASS | `docs/api/openapi.json` (+422), cliente regenerado y `test_recuperacion_contrato.py` |
| 4. Accesibilidad | Pendiente | Sin prueba en el teléfono (P2-1) |
| 5. Revisión de la otra persona | PASS | Este informe |
| 6. Prueba que falla sin la corrección | No aplica | |

## Prueba en el teléfono

- **No realizada.** Necesita staging, que depende de fusionar el #39 y el #46 (MATU-25).
- **Recorrido a hacer:**
  1. pedir el código;
  2. leerlo en el registro del envío simulado;
  3. cambiar la contraseña y ver que la sesión se cierra;
  4. confirmar el celular en «Tu cuenta».

  Se anotan el modelo del teléfono y el navegador.

## Hallazgos

| ID | Sev. | Hallazgo | Respuesta de Jorge | Verificado |
|---|---|---|---|---|
| P2-1 | P2 | Falta la prueba en el teléfono y el recorrido de punta a punta. Se hace en staging apenas esté arriba | De acuerdo. La haces tú en staging cuando MATU-25 esté arriba. El código se lee en el registro del envío simulado. Ver P3-2 | |
| P2-2 | P2 · Para decidir (PO) | `politica-privacidad.md:59` dice «te enviamos un código» y ofrece SMS o WhatsApp, pero no dice que en el semestre el envío es simulado. El registro sí lo dice (`:250`). Con usuarios reales nadie recibiría el código. ¿Se informa en la política, o la recuperación no se usa con usuarios reales mientras el envío sea simulado? | Se informa en la política: «En el piloto, el código se prueba sin enviarse». MATU#30, commit f1e3d35 | |
| P2-3 | P2 · Consulta legal | El plazo de conservación del celular tras eliminar la cuenta sigue en [PENDIENTE] (`registro-tratamientos.md:253`). Va a la tarjeta de consulta legal, junto con la base de licitud del celular obligatorio | A la tarjeta de consulta legal (comentario del 05-11), con la base de licitud del celular obligatorio. No bloquea el semestre | |
| P2-4 | P2 · Para decidir (PO) | `politica-privacidad.md:7`: la versión 0.10 sigue con «[PENDIENTE: aprobación de Jorge en este PR]». Viene del PR MATU#23, que ya está en `main`, no de este PR. Hay que cerrarlo antes de tratar datos reales | La 0.10 queda aprobada por Jorge el 05-11 como borrador del piloto, con datos sintéticos. La consulta legal sigue siendo obligatoria antes de datos reales. MATU#30, f1e3d35 | |
| P3-1 | P3 | Falta comparar uno por uno los textos de `textos.ts` contra `lenguaje.md` 19 | Hecho por el QA el 05-11: PASS, los 62 textos coinciden y no hay términos prohibidos. §19 ahora dice que «1 minuto» va en singular. MATU#30, cecefbf | |
| P3-2 | P3 | Con `REGISTRO_ENVIOS` definido, el envío simulado escribe el destino y el código en claro en un JSONL (`enviador_simulado.py:44-51`), solo fuera de producción y con datos sintéticos. Conviene una línea en el registro de tratamientos que diga que es un registro de desarrollo. En staging hay que revisar que ese archivo no quede accesible | El registro de tratamientos dice que es un registro de desarrollo con el código en claro, que se admite en staging (decisión 105) y que ahí no debe quedar accesible desde fuera. MATU#30, f1e3d35 | |
| P3-3 | P3 | `enviador_simulado.py` usa `datetime.now(UTC)` en `infrastructure/`. Está permitido, pero no usa el puerto `Reloj` | No se cambia: `infrastructure/` puede usar el reloj del sistema, y el adaptador simulado no tiene reglas de dominio | |

## Para decidir (PO)

- P2-2 y P2-4.
- MATU-57 no tiene entrada en `docs/backlog-sprints-1-3.md`. ¿Se agrega con sus criterios?
- Decisión 86: después del cambio de contraseña, un access token ya emitido sigue vivo hasta 15 minutos. ¿Se confirma?

**Respuestas de Jorge (05-11):**
- P2-2 y P2-4: ver la tabla.
- Backlog: sí. MATU-57 y MATU-41 quedan en `backlog-sprints-1-3.md` v1.4, con sus criterios (MATU#30, ff538a6).
- Decisión 86: se confirma para el semestre. Las sesiones de todos los teléfonos se cierran, y la ventana de hasta 15 minutos queda como riesgo conocido. Se revisa antes de operar con datos reales.

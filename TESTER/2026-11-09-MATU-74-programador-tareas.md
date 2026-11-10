# 2026-11-09 · MATU-74 · Programador de tareas

**Historia:** MATU-74 · Programador de tareas: que las tareas de MATU corran solas ([tarjeta](https://trello.com/c/X5j5Nw1i))
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#65 (head 81ab995 y, al día con `main`, c9bd0ba) y MartinHenriquez131/MATU#52
**Revisó:** Martín Henríquez, con `qa-tester-revisor` y `analista-revisor` · **Fecha:** 09/11/2026
**Veredicto general:** PASS. No hay P1. **Los cron de la demo quedan pendientes**, porque la demo todavía no existe

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en 81ab995 y en c9bd0ba.
- **Cron en staging**, creados por Martín el 09-11 a las 11:01 (hora de Chile):
  - `matu-cron-borrados`, con `python -m app.tareas borrados` y `10 6,7 * * *`;
  - `matu-cron-quiebres`, con `python -m app.tareas quiebres` y `30 7 * * *`;
  - `matu-cron-avisos`, con `python -m app.tareas avisos` y `*/15 * * * *`.
- **Configuración de los cron:**
  - la misma imagen (`infra/railway/Dockerfile`), con `restartPolicyType=NEVER` y sin healthcheck ni pre-deploy;
  - `DATABASE_URL`, `POLITICA_VERSION` y `ORIGEN_WEB` van como referencia `${{matu-api.…}}`, sin copiar valores;
  - `ENTORNO=staging`, y en el de avisos `ENVIADOR_AVISOS=simulado` y `REGISTRO_AVISOS=/tmp/matu-avisos.jsonl`.
- **Corridas:**
  - `matu-cron-avisos` corrió solo el 09-11 a las 11:17: `tarea=avisos`, `resultado=ok`, `duracion_ms=134.4`, con los contadores en 0 y sin datos personales;
  - Martín corrió `python -m app.tareas borrados` a mano en staging, con `railway ssh`, y dio `ok`.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Reutiliza el `ejecutar` de cada módulo, sin duplicar reglas | PASS | `app/tareas.py` |
| 2 | Cada tarea corre en su `try`: una falla no detiene a las demás | PASS | `correr_una`; `test_una_tarea_que_falla_no_detiene_a_las_demas` |
| 3 | Sale con 1 si alguna falla y con 2 si el nombre es desconocido | PASS | `SALIDA_FALLO`, `SALIDA_USO`; `test_quiebres_con_un_grupo_fallido` |
| 4 | Log JSON sin `str(e)`, traceback ni `grupo_id` | PASS | `tipo_error`; la corrida real de avisos |
| 5 | `matu_app` con `app.rol`, nunca el dueño, y un tope de 10 s solo en las tareas | PASS | `fabrica_tareas`; `test_el_engine_de_las_tareas_lleva_un_tope` |
| 6 | El grupo `borrados` cubre los plazos de 90 días | PASS | `BORRADOS_DIARIOS`; la conservación de alertas y compras va en `quiebres` |
| 7 | Los borrados corren antes que los quiebres, en verano y en invierno | PASS | 07:10 UTC frente a 07:30 UTC |
| 8 | Correr dos veces el mismo día no repite nada | PASS | `test_todas_diarias_corre_cada_tarea_y_una_segunda_corrida_no_repite_nada` |
| 9 | Los cron están configurados en staging y en la demo | PASS en staging; **pendiente en la demo** | Ver el contexto |
| 10 | La política §8 y §13 y el registro dicen que los borrados corren solos (MATU #52) | PASS | Analista: CUMPLE. Se fusionó con los cron activos, como pidió el analista (09-11, 11:30, 2881eb9) |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1 y 2. Pruebas | PASS | `tests/test_tareas.py` (14) y `test_tarea_quiebres_fallo.py` |
| 3. Contrato | No aplica | No hay rutas HTTP |
| 4. Accesibilidad | No aplica | No hay pantalla |
| 5. Revisión de la otra persona | PASS | Fusionado por Martín el 09-11 a las 10:21 (0a66b58) |
| 6. Prueba que falla sin la corrección | PASS | La prueba del grupo fallido de quiebres |

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P2 | Faltan los cron en la demo | MATU-64 | Crearlos con la demo, después de revisar las fechas de la semilla |
| H2 | P3 | Se queda con `matu_app` y `app.rol`, y no usa los roles `matu_scheduler` ni `matu_publisher` que proponía la tarjeta | README del backend | Para decidir (PO) |
| H3 | P3 | Los avisos corren cada 15 minutos y no cada minuto, porque Railway no admite menos de 5 | README del backend | Para decidir (PO) |
| H4 | P3 | Con el envío simulado, `REGISTRO_AVISOS` se pierde en cada contenedor del cron | README del backend | Se anota |
| H5 | P3 | Si los borrados de las 07:10 UTC tardaran más de 20 minutos, se cruzarían con los quiebres | Horarios | Se anota |
| H6 | P3 | La política habla de «sus avisos», y el registro de avisos (sin texto ni destino) también se guarda 90 días | `politica-privacidad.md:265,331` | Para decidir (PO) |

## Para decidir (PO)

- H2, H3 y H6.

## Segunda revisión: la 0022 y los cron con sus roles (10-11)

**PR:** MartinHenriquez131/MATU_PROYECTO#76 (H2 a H5) y MartinHenriquez131/MATU#62 (registro de tratamientos y CL-27). QA PASS en los 6 puntos y el analista da CUMPLE. No hay P1.

**Despliegue, el 10-11 en hora de Chile:**
1. **23:58 a 00:03 del 09-11:** Martín carga `MATU_SCHEDULER_PASSWORD` (cron de borrados y de quiebres) y `MATU_PUBLISHER_PASSWORD` (cron de avisos). Las genera en su computador, nuevas y distintas por entorno, sin que pasen por el chat.
2. **00:11:** se fusionan MATU #62 (ef20968) y, con su CI al día, el #76 (aa91f4e).
3. **00:14:** Martín corre `preparar_base.sh` en staging y en la demo, con el TCP Proxy abierto solo para ese paso: «los roles ya existían», «BASE PREPARADA». Después se cierra el TCP Proxy.
4. **00:16:**
   - `SCHEDULER_DATABASE_URL` y `PUBLISHER_DATABASE_URL` se cargan como referencias;
   - los horarios quedan en `0 6 * * *`, `0 8 * * *` y `*/5 * * * *`;
   - la API y los tres cron se despliegan en los dos entornos, todos en SUCCESS;
   - la API aplica `0021 -> 0022` antes de Uvicorn.

**Primeras corridas (logs de Railway, hora de Chile):**

| Cron | Staging | Demo |
|---|---|---|
| Avisos (00:20) | `ok` | `ok` |
| Borrados (03:00) | `ok`: `destruccion_fichas`, `conservacion_consumo` y `conservacion_sesiones` | `ok` en las tres |
| Quiebres (05:00) | `ok`: 7 grupos, 0 fallidos, 2 alertas creadas | `ok`: 3 grupos, 0 alertas |

- Ningún `FaltaConexion` ni error de autenticación.
- Los logs solo llevan contadores, sin URL ni contraseñas.

**Un aviso de quiebre llega al enviador simulado:**
- las 2 alertas de staging de las 05:00 quedaron pospuestas en la corrida de las 05:05;
- a las 09:00 salieron (`outbox: 2 publicados, 0 fallidos`).

**Resultado:** PASS. H2, H3, H4 y H5 quedan corregidos y verificados en Railway.

**Pendiente menor:** `REGISTRO_AVISOS` sigue cargada en los cron de avisos, porque la herramienta no borra variables. El código nuevo ya no la usa. Se quita desde el panel de Railway.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | Cron creados en la demo (09-11) | MATU-64 | sí, 10-11 |
| H2 | Roles propios `matu_scheduler` y `matu_publisher` (0022) | #76 | sí, 10-11 |
| H3 | Avisos cada 5 minutos | #76 | sí, 10-11 |
| H4 | El registro es la tabla `notificacion` | #76 | sí, 10-11 |
| H5 | Borrados 06:00 UTC y quiebres 08:00 UTC | #76 | sí, 10-11 |
| H6 | La política 0.11 dice 90 días para el registro de avisos | MATU #59 | sí |

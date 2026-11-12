# Revisión previa del analista normativo · MATU-55 · «Dónde entraste», con los teléfonos y los últimos ingresos

**10 de noviembre de 2026, noche** · Agente analista normativo, a pedido de Jorge · Estado: **decisiones D1 a D8 pendientes de Jorge**

Esto no es asesoría legal: sirve para que Jorge decida. La fuente de verdad es `docs/`. Del código solo se revisó lo que ya existe.

**Nota del orquestador:**
- **CL-52.** Esta revisión y la de MATU-61 (`revision-previa-matu-61.md`) proponen las dos una «CL-52» nueva, con preguntas distintas. Se numeran al guardarlas en `consulta-legal.md`: la de MATU-61, sobre la dirección en los pedidos de una persona borrada, queda como **CL-52**, y la de esta revisión, sobre el plazo del registro de la cuenta, como **CL-53**.
- **Política 0.12.** Las dos historias proponen publicarla. Se publica una versión por fusión, en el orden de la fila de migraciones.

## 0. Resumen para la planificación

**Sí hace falta una migración: la 0024, que va después de la 0023 de MATU-61.**

**Por qué:** hoy nadie puede leer las filas de auditoría de la cuenta, que son las que tienen `grupo_id` NULL.
- La política `auditoria_familia` (0005) exige `grupo_id = app_grupo()`, y con NULL esa condición nunca se cumple.
- `auditoria_aperturas_relevo` (0010) solo cubre las aperturas del relevo.
- La 0005 borró `auditoria_operacion`.

El resultado es que las filas `sesion.*`, `dispositivo.*` y `cuenta.*` que se escriben desde MATU-38 y MATU-57 no las lee nadie: ni la titular ni operación.

**Lo que no necesita migración:**
- `dispositivo_propio` (`02_rls.sql`) ya deja leer los dispositivos propios, incluso los que se sacaron.
- `auditoria.accion` y `auditoria.entidad` son texto sin `CHECK`. Agregar `avisos.preferencia` es un cambio de código en `backend/app/shared/auditoria.py`.
- El `CHECK auditoria_detalle_acotado` no cambia, porque la preferencia se audita sin sus valores.

**Borrador de la 0024** (para quien implemente):

```sql
-- upgrade
CREATE POLICY auditoria_cuenta_propia ON auditoria FOR SELECT USING (
    grupo_id IS NULL AND (
        actor_ref = app_usuario()
        -- solo si Jorge elige D1-c: la recuperación pedida, que va con actor sistema
        OR (actor_tipo = 'sistema' AND entidad = 'usuario' AND entidad_id = app_usuario())));
CREATE INDEX auditoria_cuenta_ix ON auditoria (actor_ref, ocurrido_en DESC) WHERE grupo_id IS NULL;
-- solo si Jorge aprueba D7:
ALTER TABLE auditoria DROP COLUMN ip;

-- downgrade (en orden inverso)
ALTER TABLE auditoria ADD COLUMN ip inet;   -- si se aplicó D7; la columna nunca tuvo datos
DROP INDEX auditoria_cuenta_ix;
DROP POLICY auditoria_cuenta_propia ON auditoria;
```

**Pruebas en `test_aislamiento.py`:**
- A lee sus propias filas de cuenta y no las de B.
- Con un grupo en el contexto, A sigue sin ver las filas de cuenta de otro miembro.
- El relevo, el sistema y operación no ven ninguna.
- `sesion.inicio_fallido`, que va sin actor ni entidad, no la ve nadie.
- Las aperturas del relevo y la auditoría de la ficha siguen como estaban.
- El ciclo `upgrade` / `downgrade` / `upgrade` funciona.

## 1. Veredicto por punto

| # | Punto | Veredicto | Condiciones |
|---|---|---|---|
| P1 | **Derecho de acceso a la auditoría de la cuenta** | Hoy **NO CUMPLE** en la app. Con MATU-55, la 0024 y la política 0.12: **CUMPLE** con condiciones | La política (§10) promete «Ver qué datos tenemos», y la Ley 19.628 lo reconoce en su art. 12. La Ley 21.719 mantiene el derecho, sin artículo citado. Lo que no salga en pantalla se sigue pidiendo por correo (§10). **C1:** se lee con `sesion_de_usuario`, solo `app.usuario_id`, y filtra RLS, no un `WHERE`. **C2:** sin parámetro de usuario |
| P2 | **Minimización: dispositivo, ingreso y nada de IP** | **CUMPLE** con condiciones | Hoy `RegistroAuditoriaSql` nunca escribe `ip`, y `DispositivoVista` no trae `push_token`, hashes, IP ni agente. **C3:** la respuesta lleva solo el tipo, el instante, el nombre del dispositivo y si es el actual. Nunca `ip`, `request_id`, `actor_ref`, `entidad_id`, `detalle` ni `familia_id`, con `extra="forbid"` y una prueba que falle si aparecen. **C4:** columnas nombradas, sin `SELECT *`. **C5:** sin ubicación, y la bajada lo aclara. **C6:** `Cache-Control: no-store` y nada en el almacenamiento del navegador |
| P3 | **Conservación de los ingresos** | **REQUIERE CONSULTA LEGAL** (CL-53). En transparencia hoy **NO CUMPLE** | La política no declara el registro de la cuenta ni su plazo: §8 solo trae «quién abrió la ficha: 3 años», y la arquitectura 11.8 dice «Auditoría de acceso: 3 años». No existe la tarea que la borre. Mientras tanto: D2 y D3 |
| P4 | **Auditoría de la preferencia de avisos** | **CUMPLE** con condiciones | **C7:** `avisos.preferencia`, con `grupo_id` NULL y sin detalle ni valores. **C8:** en la misma transacción, y solo si hubo cambios. **C9:** `notifications` usa el puerto `RegistroAuditoria` de `shared`, verificado por `test_arquitectura.py`. **C10:** las lecturas no se auditan |
| P5 | **Cerrar en otro teléfono** | **CUMPLE**. Faltan los textos | `DELETE /v1/dispositivos/{id}` ya existe (MATU-38): 404 si es ajeno, idempotente, revoca las sesiones, borra el `push_token` y audita. **C11:** la confirmación dice lo de los 15 minutos (política §4). **C12:** en este teléfono se ofrece «Salir». **C13:** sin pedir la contraseña |
| P6 | **Textos** | **NO CUMPLE** hasta que Jorge los apruebe (sección 5) | (a) «En este teléfono» para la preferencia global engaña, porque vale para todos los teléfonos y grupos (decisión 111): ver D5. (b) En el piloto los avisos no se envían, y la pantalla no puede dar a entender que llegan. (c) Qué se dice en un computador en vez de «Este teléfono»: lo decide el diseñador |
| P7 | **Accesibilidad** | **CUMPLE** con condiciones | Lista semántica con fechas legibles. Interruptores con su estado en texto y 48 px. Un diálogo que atrapa el foco y lo devuelve. 17 px en rem, sin desplazamiento a 320 px con el texto al 200 %. `aria-live` en los resultados |
| P8 | **Inscribir el navegador en su servicio de push durante el piloto** | **REQUIERE CONSULTA LEGAL** (amplía CL-37). Hallazgo nuevo | `PushManager.subscribe()` contacta de verdad el servicio del fabricante (Google, Mozilla o Apple), aunque MATU no envíe nada. **Faltante técnico:** no hay una clave VAPID, y sin ella el interruptor no funciona. Ver D6 |
| P9 | **El registro de tratamientos, entrada 8, dice algo falso** | **NO CUMPLE** en el documento | Dice que «Operación ve solo eventos de auditoría», pero desde la 0005 no los ve nadie. Ver la sección 4 |

## 2. ¿Migración?

**Sí: la 0024 (`down_revision = "0023"`).**
- **Siempre:** la política `auditoria_cuenta_propia` y el índice `auditoria_cuenta_ix`.
- **Según lo que decida Jorge:** la segunda condición de la política (D1-c) y `DROP COLUMN ip` (D7).

No lleva columnas nuevas ni toca los `CHECK`.

## 3. Decisiones para Jorge (con la recomendación del analista)

- **D1 · Qué muestra «Últimos ingresos».**
  - (a) Solo `sesion.iniciar`.
  - (b) Además, los eventos de seguridad propios: `sesion.cerrar`, `dispositivo.sacar`, `sesion.reutilizacion_detectada`, `cuenta.contrasena_cambiar`, `cuenta.celular_verificar`, `dispositivo.push_*` y `avisos.preferencia`.
  - (c) Lo de b, más «Se pidió un código para recuperar tu cuenta». Necesita la segunda condición de la política.
  - **Se recomienda c.** Así la titular se entera de un intento de quitarle la cuenta. Los inicios fallidos nunca se muestran.
- **D2 · Cuánto se muestra.** (a) 90 días y hasta 20 líneas, (b) 20 líneas sin fecha o (c) todo con paginación. **Se recomienda a**, porque coincide con la vida de un dispositivo.
- **D3 · El plazo en la política.** (a) 3 años, igual que la auditoría, con CL-53, (b) 1 año o (c) 90 días. **Se recomienda a por ahora**, y declarar en §13 que el borrado automático todavía no existe.
- **D4 · La política.** (a) Publicar la 0.12 o (b) no tocarla. **Se recomienda a**, sin pedir de nuevo la aceptación, porque no agrega usos ni destinatarios. Hay que coordinarla con MATU-61. Actualiza `POLITICA_VERSION` y la copia del texto.
- **D5 · El canal de push global.** (a) Dejar «En este teléfono», (b) «En tus teléfonos», con la ayuda «Vale para todos tus grupos.», o (c) una sola casilla. **Se recomienda b.**
- **D6 · La inscripción real en push durante el piloto.**
  - (a) Real, con una clave VAPID como secreto, solo al tocar el botón y con la frase en §6.
  - (b) Ocultar el interruptor hasta que haya un proveedor.
  - (c) Solo en local.
  - **Se recomienda a**, con datos sintéticos en los teléfonos del equipo. Si Jorge prefiere no tener un flujo real hacia terceros antes de la consulta legal, b.
- **D7 · Borrar la columna `auditoria.ip` en la 0024.** (a) Sí o (b) no. **Se recomienda a**: nunca tuvo datos. Está fuera del alcance de la tarjeta y necesita la aprobación de Jorge.
- **D8 · Cerrar en otro teléfono.** (a) Con un diálogo y sin contraseña, (b) pidiendo la contraseña o (c) sin confirmación. **Se recomienda a.**

## 4. Documentos que hay que actualizar (borradores)

- **`registro-tratamientos.md`, entrada 6:**
  - **Datos:** la auditoría de la cuenta (`sesion.*`, `dispositivo.*`, `cuenta.*` y `avisos.preferencia`), sin grupo, sin IP, sin la huella del email y sin los valores.
  - **Quién accede:** la titular, en «Dónde entraste», con la RLS `auditoria_cuenta_propia` (0024): los últimos 90 días, con fecha, hora y nombre del dispositivo. Lo anterior se pide por correo. Nadie más lo ve.
  - **Conservación:** 3 años [PENDIENTE: CL-53 y la tarea que lo borre].
  - **Comunicaciones a terceros:** la inscripción del navegador en push [PENDIENTE: CL-37 ampliada].
- **`registro-tratamientos.md`, entrada 8, «Quién accede»:** «Nadie ve el código. Los eventos de recuperación van sin contacto, código ni IP. Operación no los lee (0005). La titular ve en "Dónde entraste" el pedido de código y el cambio de contraseña (MATU-55)». La última parte depende de D1.
- **`registro-tratamientos.md`, entrada 5, «Medidas»:** «el cambio de la preferencia se audita como `avisos.preferencia`, sin grupo y sin valores».
- **`politica-privacidad.md` 0.12** (si D4-a):
  - **Encabezado:** «No agrega usos ni destinatarios».
  - **§4, «Tus dispositivos»:** el registro de la cuenta, con fecha, hora y dispositivo, nunca la IP ni la ubicación.
  - **§6, «Dónde entraste»:** qué se ve, que solo lo ve la titular y que lo anterior se pide por correo.
  - **§6, avisos:** «Por correo» y «En tus teléfonos», y la inscripción del navegador.
  - **§8:** el registro de la cuenta, 3 años `<!-- PENDIENTE: CL-53 -->`.
  - **§13:** quitar la elección de avisos y la vista de dónde entraste, que ya existen, y agregar el borrado a los 3 años.
- **`consulta-legal.md`:**
  - **CL-53 (nueva):** ¿es proporcional conservar 3 años la fecha, la hora y el dispositivo de cada ingreso y evento de seguridad? ¿Basta mostrar 90 días y entregar el resto a pedido? Bloquea los datos reales.
  - **CL-37 (ampliada):** la inscripción del navegador en push sin envíos.
- **Fuera de `docs/legal/`:**
  - `docs/modelo-datos.md`: la fila de `auditoria`, los índices y, con D7, la IP.
  - `docs/api/README.md`: una decisión nueva con la ruta y la 0024.

## 5. Textos que faltan en `lenguaje.md` (propuestos)

Sin la palabra «sesión» (sección 19).

**Pantalla «Dónde entraste»:**
- Bajada: «Los teléfonos y computadores donde entraste a MATU. No guardamos tu ubicación ni tu dirección IP.»
- Bloque: «Últimos ingresos» · «Los de los últimos 90 días.»
- Línea: «{Hoy | Ayer | El DD/MM/AAAA} a las {HH:MM} · {nombre del dispositivo}», con «(este teléfono)» si corresponde.
- Vacío: «No hay ingresos en los últimos 90 días.»
- Error: «No pudimos traer dónde entraste. Revisa tu conexión e inténtalo de nuevo.»
- Si no reconoce un ingreso: «¿No reconoces un ingreso? Cierra MATU en ese teléfono y cambia tu contraseña.»

**Eventos de la lista (según D1):**
- «Entraste» · «Saliste» · «Cerraste MATU en {nombre}»
- «Te sacamos de MATU en {nombre} porque notamos un uso extraño. Vuelve a entrar.»
- «Cambiaste tu contraseña» · «Confirmaste tu celular» · «Se pidió un código para recuperar tu cuenta» · «Cambiaste tus avisos»
- «Activaste los avisos en {nombre}» · «Desactivaste los avisos en {nombre}»

**Cerrar en otro teléfono:**
- Pregunta: «¿Cerrar MATU en {nombre}?»
- Texto: «Quien lo use tendrá que volver a entrar con tu correo y tu contraseña. Puede seguir abierto hasta 15 minutos.»
- Botones: «Cerrar en ese teléfono» · «Dejarlo abierto»
- Hecho: «Cerramos MATU en {nombre}.»
- Si ya no estaba (404): «Ese teléfono ya no estaba en tu lista.»
- En el teléfono actual: «Salir»

**Recibir avisos en este teléfono:**
- Ayuda: «Te avisamos cuando un insumo se esté acabando. El aviso no dice cuál ni de quién.»
- En el piloto: «En el piloto los avisos se prueban sin enviarse: no te llegará nada.»
- Permiso negado: «Tu navegador no deja que MATU te avise. Puedes cambiarlo en los ajustes del navegador.»
- Sin soporte: «Este navegador no puede recibir avisos.»

**Preferencias en «Tu cuenta»** (ajusta la sección 20, según D5):
- «Avisos cuando un insumo se está acabando» · «Por correo» · «En tus teléfonos» · «Vale para todos tus grupos.»
- Guardado: «Guardamos tus avisos.»
- Error: «No pudimos guardar. Revisa tu conexión y vuelve a intentarlo.»

**Para el diseñador:** qué reemplaza a «Este teléfono» cuando se entra desde un computador.

## 6. Consulta legal

- **CL-53 (nueva):** la proporcionalidad de los 3 años del registro de la cuenta.
- **CL-37 (ampliada):** la inscripción del navegador en push durante el piloto.

Ninguna bloquea el semestre, que usa datos sintéticos. Las dos bloquean el paso a datos reales.

## Archivos revisados

- **En MATU:** la política, el registro, `consulta-legal.md`, `revision-matu-72.md`, la arquitectura (11.6 y 11.8), el modelo de datos y `lenguaje.md` (13.3 y 20).
- **En MATU_PROYECTO:**
  - el esquema: `01_esquema.sql` y `02_rls.sql`;
  - las migraciones 0005, 0008, 0010, 0013, 0014, 0020, 0021 y 0022;
  - la auditoría: `shared/auditoria.py` y `auditoria_sql.py`;
  - el código: `iam/application/sesiones.py`, `recuperacion.py` y `notifications/application/preferencias.py`;
  - el contrato: `openapi.json` (`DispositivoVista`) y `README.md`, decisiones 108 a 113.

## Decisiones de Jorge (12 de noviembre de 2026)

Jorge decidió las primeras cinco de MATU-55 una por una y delegó el resto con «todas de acuerdo a tus recomendaciones». Se aplican las recomendaciones actualizadas del analista, que tienen en cuenta MATU-61, 62 y 94. Versión de la política según la D11, una por fusión. Fila de migraciones: 0024 MATU-62, 0025 MATU-55, 0026 MATU-42, 0027 MATU-46 y 0028 MATU-54. La próxima CL libre es la CL-68.

| Id | Decisión |
|---|---|
| D1 | **c)** ingresos, eventos de seguridad y el código pedido para recuperar la cuenta. Los ingresos fallidos no se muestran nunca |
| D2 | **a)** 90 días y hasta 20 líneas |
| D3 | **a)** 3 años, con la CL-53. El borrado lo construye MATU-89 |
| D4 | Ya no hace falta: la resolvió la D11 (la versión que toque al fusionar, sin volver a aceptar) |
| D5 | **b)** «En tus teléfonos» |
| D6 | **a)** suscripción real del navegador (service worker, `manifest` y clave VAPID), con el envío simulado, como decidió Jorge el 08-11 (M9). **Corregida por Jorge el 12-11:** la recomendación inicial (ocultar el push) chocaba con los ítems 5.5 y 5.6 y la DdT 3 y 3.5 de la tarjeta. La política que trae MATU-55 (0.14) suma una línea: al activar «Recibir avisos», el navegador registra una dirección de avisos en el servicio de su fabricante; MATU no le envía ningún texto en el piloto. Sigue abierta la CL-37 |
| D7 | **a)** se borra la columna `auditoria.ip` en la **0025** (`down_revision = "0024"`). Antes se verifica que MATU-62 no la escribe |
| D8 | **a)** cerrar en otro teléfono con un diálogo, sin pedir la contraseña |

**Ajustes:** la migración es la 0025, no la 0024; la «0.12» de las secciones 3 y 4 pasa a «la versión que toque al fusionar».

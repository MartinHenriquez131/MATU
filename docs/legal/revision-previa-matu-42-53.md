# Revisión previa del analista normativo · MATU-42 (invitar y gestionar roles) y MATU-53 (su pantalla)

**11 de noviembre de 2026, madrugada** · Agente analista normativo, a pedido de Jorge · Estado: **decisiones D-42-1 a D-42-14 pendientes de Jorge**

No es asesoría legal. Lo que queda en REQUIERE CONSULTA LEGAL va a `consulta-legal.md`, desde la CL-57.

**Notas del orquestador:**
- **La sección de `lenguaje.md`:** el analista la propuso como «sección 30», pero la 30 ya es de MATU-84. Los números se asignan al fusionar, en el orden de la fila: MATU-61 la 31, MATU-62 la 32 y MATU-42/53 la 33.
- **La versión de la política:** esta revisión pregunta qué significa «una versión por fusión» (§4). Hay que confirmarlo con Jorge: una 0.12 que junte MATU-61, 55, 62 y 42, o una versión por cada fusión.

**Qué se leyó:**
- **En MATU:**
  - el backlog, sección 8 (RF-38);
  - la arquitectura, 7.7, 11.1, 11.2, 11.5, 11.6 y 11.8;
  - el modelo de datos: `membresia`, `invitacion`, `indice_token` y la decisión abierta de que la invitación vale 7 días;
  - la política 0.11, el registro, `consulta-legal.md` y `lenguaje.md` (3, 22 y 25).
- **En MATU_PROYECTO:**
  - el esquema: `01_esquema.sql` (líneas 109 a 163) y `02_rls.sql` (líneas 50 a 83);
  - las migraciones 0013, 0016, 0020 (líneas 52 a 57) y 0022;
  - el código: `care_circle` (`infrastructure/membresia.py`) y `shared/auditoria.py`;
  - el contrato: `docs/api/README.md`, línea 166, donde dice «No hay invitaciones ni cambio de roles».
- **Las revisiones de esta noche:** la de MATU-61, la de MATU-55 y la de MATU-62. Esta no las contradice.

## Siete hallazgos del código que cambian el plan

1. **La 0020 dejó para MATU-42 la división de varias políticas `FOR ALL`:** `membresia_familia`, `membresia_operacion`, `invitacion_familia`, `grupo_familia`, `direccion_familia` y `direccion_operacion`. Hoy, **por SQL directo, cualquier miembro, incluso un observador, puede:**
   - insertar membresías en su grupo;
   - subirse a admin;
   - cambiar el rol de otros;
   - crear o anular invitaciones;
   - cambiar el nombre del grupo o archivarlo.

   La API no lo permite, pero falta la segunda barrera en la base.
2. **Nada garantiza que el grupo tenga siempre un admin.**
3. **`membresia_uq UNIQUE (grupo_id, usuario_id)`:** a quien sacan no se le puede volver a invitar si su fila queda como `retirada`.
4. **`usuario_comiembro` no filtra `m.estado = 'activa'`.** Los miembros pueden leer la fila completa de `usuario` de cualquier miembro, incluso de quien ya salió: el email, el celular y si está verificado. La política (§6) promete «ven tu nombre» solo porque la API no muestra lo demás.
5. **El esquema obliga a guardar el contacto de quien se invita:** `CHECK invitacion_destino` exige el email o el teléfono.
6. **`EntidadAuditoria` y `AccionAuditoria`** no tienen nada de membresía ni de invitación.
7. **El registro ya revela si un correo tiene cuenta:** lo dicen `lenguaje.md` 25.1 («Ese correo ya tiene una cuenta») y la política §13. Las invitaciones no deben sumar otra forma de averiguarlo.

## 1. Veredicto por punto

| # | Punto | Veredicto | Condiciones |
|---|---|---|---|
| 1 | **Base de licitud del correo o celular de quien se invita** | Con D-42-1 (a), **CUMPLE**, porque MATU no recibe ese dato. Con (b) o (c), **REQUIERE CONSULTA LEGAL** (CL-33 ampliada) | Con (b) o (c), quien invita entrega el dato de un tercero que todavía no conoce MATU. Es el mismo caso que el relevo y «A quién llamar». Mientras tanto, «interés legítimo informado», como en la entrada 4 del registro |
| 2 | **Lo que ve la persona invitada antes de aceptar** | **NO CUMPLE** todavía, porque no existe. Con las condiciones, **CUMPLE** | **C1:** antes del código, solo el nombre de pila de quien invita, el rol y el vencimiento. **C2:** después del código y antes de «Unirme», el nombre del grupo, los nombres de pila de las personas cuidadas, qué permite el rol, que el grupo verá su nombre, el aviso de confidencialidad y la política. **C3:** sin cuenta, la crea y acepta la política vigente (MATU-75). Con cuenta, no se le pide otra aceptación |
| 3 | **¿La persona cuidada debe saber o autorizar que entra alguien nuevo?** | **REQUIERE CONSULTA LEGAL** (CL-57, ligada a CL-05 y CL-01) | Las declaraciones de §5 autorizan a guardar la ficha y compartirla con «el relevo que elija el grupo». Que el grupo vea la ficha según el rol está en §6, pero ninguna declaración lo nombra. Mientras tanto: **C4:** no se cambian las declaraciones, porque eso obligaría a autorizar de nuevo. **C5:** la pantalla de invitar le recuerda a quien administra que se lo cuente a la persona cuidada si puede comprenderlo. **C6:** todo el grupo ve la lista de miembros |
| 4 | **Cruce con MATU-07 y las autorizaciones por finalidad** | **CUMPLE** en el diseño. Hay un caso en **REQUIERE CONSULTA LEGAL** (CL-58) | La membresía no crea, no copia ni cambia autorizaciones, que son por persona y por finalidad (`consentimiento_vigente_uq`). El nuevo accede según su rol y solo con la autorización VIGENTE. **C7:** aceptar una invitación nunca registra una autorización. **Caso abierto:** quien autorizó como cuidador de hecho sale o pierde el rol (D-42-9). Aplica también a `despacho` (D1 de MATU-61) |
| 5 | **Minimización de la invitación** | **NO CUMPLE** en el esquema | El `CHECK invitacion_destino` obliga a guardar un contacto, y no hay conservación. Ver D-42-1 y D-42-6. **C8:** la invitación lleva solo el rol, nunca `puede_ver_plan`. El permiso del pagador lo da quien administra, en un paso aparte |
| 6 | **Qué ve cada rol en la lista de miembros** | **NO CUMPLE** en RLS (hallazgo 4). En la API, **CUMPLE** con condiciones | **C9:** solo el id de la membresía, el nombre, el rol, si puede ver la ficha (solo para el pagador), `unido_en` y `eres_tu`. Nunca el email, el celular ni `usuario_id`, con `extra="forbid"` y una prueba que falle si aparecen. **C10:** las invitaciones pendientes las ve solo quien administra. Ver D-42-10 |
| 7 | **Roles: quién gestiona** (11.2) | **NO CUMPLE** en RLS (hallazgo 1) | Se corrige en la 0026. En la API, el rol que no alcanza recibe 404 (decisión 4 del contrato) |
| 8 | **El grupo nunca queda sin admin** | **NO CUMPLE** | **C11:** un trigger con `FOR UPDATE` sobre `grupo_familiar`. **C12:** 409 al quitar, bajar de rol o hacer salir al último admin, con una prueba de concurrencia |
| 9 | **Sacar a alguien del grupo** | **CUMPLE** con condiciones | Deja de ver el grupo al instante, porque `membresia_activa` se consulta en cada petición. **C13:** sus enlaces de relevo se cortan en la misma transacción (D-42-7); si no, **sigue leyendo la ficha con el enlace y el PIN que creó**. **C14:** la fila queda `retirada`, con `retirado_en`, y no se borra mientras la nombre la auditoría (CL-59). **C15:** sus avisos se cortan solos. **C16:** lo que escribió en la ficha queda, y el autor se muestra según D-42-10. **C17:** volver a invitarlo tiene que funcionar (hallazgo 3) |
| 10 | **Cambio de rol** | **CUMPLE** con condiciones | **C18:** al dejar de ser pagador, `puede_ver_plan` vuelve a false en la misma sentencia. **C19:** si el cambio le quita la ficha, se cortan sus enlaces de relevo. **C20:** el cambio no anula un pago en curso (MATU-62), y el rol vale desde la petición siguiente |
| 11 | **Enlace de un solo uso, que vence, en el fragmento y fuera de los logs** | **CUMPLE** en el diseño, con condiciones | Ya existen `indice_token` (`tipo = 'invitacion'`), `token_vida_fija` (0020) y `CHECK invitacion_vigencia` (7 días como máximo). **C21:** 256 bits, solo SHA-256, `/invitacion#<token>`, canje por POST y `history.replaceState`. **C22:** en una transacción se fijan `aceptada_en`, `aceptada_por` e `indice_token.revocado_en`, y si hay dos aceptaciones a la vez gana una, con prueba. **C23:** `no-store`, `no-referrer` y `noindex`. **C24:** nunca el token ni el código en logs, errores, auditoría ni eventos. **C25:** el token **no** va en `sessionStorage` ni en `localStorage` mientras se crea la cuenta: queda en memoria, y si se recarga se vuelve a abrir el enlace |
| 12 | **Enumeración** | **CUMPLE** con condiciones | **C26:** crear una invitación responde siempre igual, y nunca se busca el contacto entre las cuentas. **C27:** el 409 «ya eres parte» solo lo recibe quien acepta. **C28:** un token inexistente y uno anulado dan el mismo 410 genérico |
| 13 | **Límite de intentos** | **NO CUMPLE** todavía | **C29:** MATU-25: un contador por huella HMAC de la IP en Redis, 1 hora (por ejemplo, 30 presentaciones y 10 canjes). **C30:** con D-42-2 (a), 5 códigos malos bloquean (423). **C31:** un tope de creación por admin y grupo (por ejemplo, 20 al día) |
| 14 | **Otro grupo recibe 404** | **CUMPLE** en el diseño | **C32:** pruebas en `test_aislamiento.py` para `membresia`, `invitacion` y `grupo_familiar` |
| 15 | **Auditoría** | **NO CUMPLE** todavía (hallazgo 6) | Ver D-42-8. Sin contacto, token, código, nombre ni IP |
| 16 | **Cómo llega la invitación** | Con D-42-1 (a), **CUMPLE**. Con correo o SMS reales, **REQUIERE CONSULTA LEGAL** (CL-36) | Con (a), quien invita la manda desde su teléfono, como el relevo. **C33:** el mensaje no lleva el nombre de la persona cuidada, el del grupo, datos de salud ni el código |
| 17 | **Política y registro** | **NO CUMPLE** hasta que se publique la versión con estos cambios | §4 dice «Invitaciones: *Todavía no disponible*», §6 tiene el PENDIENTE del email entre miembros, y §13 las lista como pendientes |
| 18 | **Accesibilidad** | **CUMPLE** con condiciones | Ver la sección 6 |

## 2. ¿Migración?

**Sí: la 0026, con `down_revision = "0025"`.** Va después de la 0023 de MATU-61, la 0024 de MATU-55 y la 0025 de MATU-62.

**Dependencias:**
- **Con la 0023 hay una dependencia real:** si la 0023 divide `direccion_familia` y `direccion_operacion` (D4 de MATU-61), la 0026 no las toca. Si no las divide, las divide la 0026. Se revisa en la rama de MATU-61.
- **Con la 0024 y la 0025 no hay dependencia técnica.**
- **Si MATU-42 está lista antes que MATU-62,** se intercambian los números (D-42-14).

**Contenido propuesto:**
1. **`app_es_admin()`**, `STABLE`.
2. **`membresia`:**
   - sale `membresia_familia`;
   - entra `membresia_familia_leer` (SELECT del grupo, y solo filas activas según D-42-10);
   - entra `membresia_admin_editar` (UPDATE con `app_es_admin()`);
   - `GRANT UPDATE` solo de `rol`, `puede_ver_plan`, `estado` y `retirado_en`;
   - `REVOKE DELETE`;
   - `membresia_operacion` pasa a solo SELECT;
   - `membresia_fundador` no cambia.
3. **El trigger «nunca sin admin»:** `BEFORE UPDATE`, con `FOR UPDATE` sobre `grupo_familiar`.
4. **Volver a invitar (D-42-11):** un índice único parcial `(grupo_id, usuario_id) WHERE estado <> 'retirada'`.
5. **`invitacion`:** sale `invitacion_familia`, y quedan SELECT, INSERT y UPDATE solo con `app_es_admin()`. `GRANT UPDATE` solo de `revocada_en`, sin DELETE. `invitacion_operacion` queda en SELECT.
6. **Aceptar (D-42-12):**
   - `invitacion_aceptar(p_token_hash, p_codigo, p_ahora)`, `SECURITY DEFINER`, con dueño `matu_owner`, `search_path` fijo y `EXECUTE` solo para `matu_app`. Hace todo en una transacción: exige `app.usuario_id`, toma la invitación con `FOR UPDATE`, valida, cuenta los intentos, inserta la membresía y fija `aceptada_*` e `indice_token.revocado_en`. Devuelve solo `grupo_id` y el estado.
   - Además, `invitacion_presentar(p_token_hash, p_ahora)`: el nombre de pila de quien invita, el rol, `expira_en` y el estado.
7. **Con D-42-1 (a):** se quitan `invitacion_destino`, `destino_email` y `destino_telefono`, o se agrega un `CHECK` que las deje siempre nulas. En el downgrade vuelven como columnas que admiten nulos, con el `CHECK NOT VALID`, como hizo la 0013.
8. **Con D-42-2 (a):** `codigo_hash bytea` (HMAC con pepper, como el PIN), `codigo_intentos_fallidos smallint` y `bloqueada_en timestamptz`.
9. **`grupo_familiar`:** sale `grupo_familia`. Queda la lectura para el grupo, y el UPDATE solo del `nombre` con `app_es_admin()`, sin DELETE.
10. **D-42-10:** `usuario_comiembro` exige `m.estado = 'activa'`.
11. **D-42-8 (b):** `auditoria_detalle_acotado` acepta `rol`, con la lista cerrada.
12. **D-42-6:** `invitacion_conservar(limite, ahora)`, `SECURITY DEFINER`, que solo puede llamar `matu_scheduler`. Borra las invitaciones cerradas hace 30 días y su `indice_token`.
13. **Pruebas:**
    - en `test_aislamiento.py`, todo lo de arriba: nadie que no sea admin cambia membresías ni invitaciones, B no ve a A, nadie borra, el último admin con concurrencia, la aceptación de un solo uso con concurrencia, el código, que quien salió no vea a sus excompañeros y que se pueda volver a invitar;
    - en `test_migraciones.py`, el ciclo completo.

**Sin migración:** cortar los enlaces de relevo al sacar a alguien, con el UPDATE de `revocado_en` (0020 c) y un `relevo.revocar` por acceso.

## 3. Decisiones para Jorge (con la recomendación del analista)

- **D-42-1 · Cómo llega la invitación y qué se guarda.** Hay tres opciones:
  - (a) quien administra la manda desde su teléfono, como el relevo, y MATU no guarda el contacto;
  - (b) se guarda el contacto y MATU envía, simulado en el piloto;
  - (c) además, queda atada a ese contacto.

  **Se recomienda (a):** es mínima, no suma proveedores ni la CL-36, no expone a la enumeración y es coherente con el relevo.
- **D-42-2 · Qué protege un enlace reenviado.**
  - (a) un código de 4 dígitos que se muestra una vez y se dicta aparte, con 5 intentos;
  - (b) que quien administra lo confirme después;
  - (c) solo el enlace.

  **Se recomienda (a):** un admin o un cuidador lee la ficha, y un enlace reenviado en un chat dejaría entrar a un desconocido.
- **D-42-3 · Vigencia.** (a) 7 días o (b) 48 horas. **Se recomienda (a) con el código, y (b) si no hay código.** Esto cierra la decisión abierta del modelo de datos.
- **D-42-4 · Qué se ve antes del código.** (a) Solo el nombre de pila de quien invita y el rol, o (b) además, el de la persona cuidada. **Se recomienda (a).**
- **D-42-5 · Roles que se pueden dar al invitar:** los cuatro, incluido admin, con una advertencia. El permiso del pagador para ver la ficha va aparte (C8). **Faltante:** hoy no hay ninguna ruta que dé `puede_ver_plan`, y debería entrar en «gestionar roles».
- **D-42-6 · Conservación:** las invitaciones cerradas se borran a los 30 días, con su `indice_token`, por MATU-74, y la auditoría queda 3 años. La membresía retirada queda mientras la auditoría la nombre (CL-59).
- **D-42-7 · Al sacar a alguien o quitarle la ficha:**
  - (a) se cortan sus enlaces de relevo (`otorgado_por`) en la misma transacción;
  - (b) quien administra elige;
  - (c) no se tocan.

  **Se recomienda (a),** y que la confirmación diga cuántos se cortan.
- **D-42-8 · Auditoría.**
  - Las acciones: `invitacion.crear`, `.anular`, `.aceptar`, `.codigo_incorrecto`, `.bloqueo` y `.cerrar`, y `membresia.cambiar_rol`, `.permiso_ficha`, `.sacar` y `.salir`.
  - Las entidades: `invitacion` y `membresia`, con `grupo_id`.
  - (a) Sin detalle, o (b) con `rol` de la lista cerrada. **Se recomienda (b).**
  - No se auditan las lecturas.
- **D-42-9 · La autorización de quien sale o pierde el rol** (CL-58).
  - (a) Sigue vigente, con un aviso a quienes administran o cuidan;
  - (b) la de un cuidador de hecho queda por renovar;
  - (c) se retira.

  **Se recomienda (a) en el semestre.**
- **D-42-10 · Qué se ve de los miembros y de quien salió.** (a) Solo el nombre y el rol de los activos: `usuario_comiembro` exige que la membresía esté activa, y el autor que salió aparece como «Alguien que ya no está en el grupo». (b) Como hoy. **Se recomienda (a):** cierra el PENDIENTE de §6.
- **D-42-11 · Volver a invitar.** (a) Un índice parcial, con una fila nueva cada vez, o (b) reactivar la fila. **Se recomienda (a).**
- **D-42-12 · La aceptación.** (a) Funciones `SECURITY DEFINER`, o (b) `indice_token` con `sistema` y políticas. **Se recomienda (a).**
- **D-42-13 · Salir del grupo por cuenta propia:** hoy no existe. **Se recomienda incluirlo en MATU-42**, con 409 si es el último admin, o crear una tarjeta. **Es un faltante.**
- **D-42-14 · Número de la migración.** (a) La 0026, después de MATU-62, o (b) intercambiar. **Se recomienda (a),** con la regla de la fila.

## 4. Documentos de `docs/legal/` que hay que actualizar (borradores)

**La política** (en la versión que se publique al fusionar, ver la nota del orquestador): no agrega usos, porque §3.2 ya cubre formar el grupo y los permisos, y no cambia las declaraciones de §5 (C4).
- **Encabezado:** «MATU-42 y MATU-53: se ajustan las secciones 4, 6, 8, 10 y 13 con las invitaciones, los roles y la lista de miembros. No agregan usos ni cambian las declaraciones.»
- **§4, «De ti»:** «**Los grupos a los que perteneces**, tu rol en cada uno, quién te invitó, cuándo te uniste y, si sales o te sacan, la fecha.»
- **§4, «Tu sesión»:** «Si alguien te saca de un grupo, dejas de verlo en ese mismo momento, y se cortan los enlaces de relevo que creaste en ese grupo. Lo que escribiste en la ficha queda, porque es parte del cuidado de la persona.»
- **§4, «Invitaciones a tu grupo»** (D-42-1 a y D-42-2 a): «No guardamos el correo ni el teléfono de la persona que invitas. Tú le mandas el enlace desde tu teléfono, con la aplicación que elijas, y le dictas el código aparte. MATU no le envía mensajes. Guardamos el rol que le das, quién la invitó, hasta cuándo vale y si la aceptó. La invitación sirve una sola vez y vence en 7 días. Antes de unirse, ve tu nombre de pila, el nombre del grupo, a quién cuidan y qué le permite su rol.»
- **§6, «Tu cuenta»:** «Las personas de tus grupos ven tu nombre y tu rol. Nunca ven tu email ni tu celular.»
- **§6, un bloque nuevo, «Quién forma el grupo»:** «Todas las personas del grupo ven quiénes lo forman y con qué rol. Solo quien administra el grupo invita, cambia los roles, da al pagador el permiso de ver la ficha y saca a alguien, y es quien ve las invitaciones pendientes. El grupo siempre tiene al menos una persona que lo administra. Cada vez que alguien invita, se une, cambia un rol o sale, MATU registra quién y cuándo, sin datos de contacto. Lo ve quien administra el grupo.»
- **§8:**
  - «**Invitaciones:** 30 días desde que se aceptan, vencen o se anulan. El registro de quién invitó y quién se unió sigue el plazo de 3 años.»
  - «**Tu paso por un grupo**, si sales o te sacan: tu rol y las fechas, mientras existan los registros que te nombran. Todavía no definimos ese plazo. Lo publicaremos antes de usar MATU con datos reales.» `<!-- PENDIENTE: CL-59 -->`
- **§10, «Salir de un grupo»** (con D-42-13): «Puedes salir de un grupo cuando quieras, en «Grupo familiar». Si eres la única persona que lo administra, primero da ese rol a otra persona. Al salir, dejas de verlo en ese momento y se cortan los enlaces de relevo que creaste. Los registros de lo que hiciste en el grupo ya no los ves en la aplicación: si los necesitas, pídelos por el correo de esta sección.»
- **§13:** «Invitaciones, pedidos y pagos.» pasa a «Pedidos y pagos.», si todavía no están (según MATU-61 y MATU-62).

**`registro-tratamientos.md`, una entrada 12 nueva, «Grupo familiar: invitaciones, membresías y roles (MATU-42, MATU-53)»:**
- **Finalidad:** formar el grupo, dar a cada persona su rol y saber quién tiene acceso a los datos de la persona cuidada.
- **Titulares:** las personas que invitan, se unen, cambian de rol o salen; la invitada antes de aceptar, sin datos de contacto; la persona cuidada, cuyo círculo de acceso cambia.
- **Datos:**
  - **invitación:** grupo, rol, quién invita, creación, vencimiento (7 días como máximo), aceptación, anulación, la huella SHA-256 del token y la HMAC del código, los intentos y el bloqueo, sin contacto;
  - **membresía:** grupo, usuario, rol, `puede_ver_plan`, estado, quién invitó, unión y retiro;
  - **auditoría:** las acciones de D-42-8, con el rol como único detalle;
  - **la IP:** solo como huella HMAC en Redis, durante 1 hora.
- **Base de licitud:** la ejecución del servicio que pide la persona. Que una persona nueva acceda a los datos de la persona cuidada se apoya en la autorización de MATU-07, sin cambios [PENDIENTE: CL-57]. Cuando quien autorizó sale del grupo [PENDIENTE: CL-58].
- **Quién accede:**
  - los miembros activos ven el nombre y el rol de los activos, nunca el email ni el celular (`usuario_comiembro` con la membresía activa, 0026);
  - solo el admin gestiona invitaciones, roles, el permiso de la ficha y la salida de miembros, y los demás reciben 404 (RLS por operación, 0026);
  - la persona invitada ve lo que dicen C1 y C2;
  - operación lee para dar soporte, sin cambiar nada.
- **Conservación:**
  - invitaciones cerradas: 30 días (`invitacion_conservar`, MATU-74);
  - membresías retiradas: mientras la auditoría las nombre [PENDIENTE: CL-59];
  - auditoría: 3 años.
- **Medidas:**
  - el token en el fragmento, canje por POST y `history.replaceState`, nunca en el almacenamiento del navegador;
  - el código de 4 dígitos dictado aparte, con 5 intentos y 423;
  - un solo uso con `FOR UPDATE`, `revocado_en` y `token_vida_fija`;
  - la misma respuesta exista o no la cuenta;
  - los contadores de MATU-25 y el tope de creación;
  - el grupo nunca queda sin admin;
  - se cortan los enlaces de relevo al sacar a alguien o quitarle la ficha;
  - `no-store`, `no-referrer` y `noindex`;
  - nunca el token ni el código en logs, errores, auditoría ni eventos.
- **Comunicaciones a terceros:** ninguna desde MATU.
- **Transferencia internacional:** [PENDIENTE: CL-35].
- **Decisiones automatizadas:** ninguna. El bloqueo es un control de seguridad.

**Otras entradas:**
- **Entrada 1:** «Quién tiene cada rol lo decide quien administra el grupo (entrada 12).»
- **Entrada 4:** «Al sacar a quien creó un acceso, o quitarle la ficha, el acceso se corta (MATU-42).»

**`consulta-legal.md`:** las CL-57 a CL-59, «la próxima es CL-60» y la fila de MATU-42.

**Fuera de `docs/legal/`:**
- el modelo de datos: `invitacion` sin contacto y con código, el índice parcial y los 7 días;
- la arquitectura: en 11.2, una columna «Grupo», y en 11.8, las invitaciones;
- `docs/api/README.md`: quitar «No hay invitaciones ni cambio de roles».

## 5. Textos propuestos para `lenguaje.md` («Grupo e invitaciones»)

Sin «revocar», «rechazar», «token», «usuario» ni «observador» en pantalla, y sin pronombres para la persona cuidada.

**Roles:**
- **Administra el grupo:** Ve y cambia todo, comparte la ficha, invita y cambia los permisos.
- **Cuida:** Ve y cambia la ficha y los insumos, y comparte la ficha con quien te reemplaza.
- **Paga:** Ve los insumos y paga los pedidos. Ve la ficha solo si quien administra le da permiso.
- **Se informa:** Ve el nombre de `{nombre_pila}` y sus insumos. No ve la ficha.

Lo de los pedidos se muestra solo cuando MATU-61 y MATU-62 estén en `main`.

**Lista de miembros:**
- «Quiénes forman el grupo» · `{nombre}` · `{rol}`, con «(tú)».
- Para el pagador: «Puede ver la ficha» / «No ve la ficha».
- Autor que salió: «Alguien que ya no está en el grupo».
- Botón: «Invitar a alguien».

**Invitar:**
- «Invitar a alguien al grupo» · «¿Qué podrá hacer?»
- Para admin: «Podrá invitar, cambiar permisos y sacar a otras personas, también a ti.»
- Recordatorio: «Si `{nombre_pila}` puede comprenderlo, cuéntale que invitaste a otra persona.»
- Botón: «Crear la invitación».
- Hecho: «Invitación lista. Vale una sola vez, hasta el `{fecha}` a las `{hora}`.»
- Código: «Código: `{codigo}`. Díselo por teléfono, no lo escribas en el mensaje. No lo volverás a ver.»
- Botones: «Enviar el enlace» · «Copiar el enlace».
- Mensaje: «Te invito a mi grupo de cuidado en MATU. Abre este enlace para unirte. El código te lo digo por teléfono. `{enlace}`»

**Pendientes:**
- «Invitaciones sin usar» · «`{rol}` · vence el `{fecha}`».
- Botón: «Anular la invitación».
- Confirmación: «¿Anular esta invitación? El enlace dejará de servir.» · «Anular» · «No anular».
- Hecho: «Invitación anulada.»

**Página de la persona invitada (`/invitacion`):**
- Antes del código: «`{nombre_pila_invita}` te invita a su grupo de cuidado en MATU, para `{rol}`.» · «Escribe el código que te dijo.» · «Seguir».
- Código incorrecto: «Ese código no es. Te quedan `{n}` intentos.»
- Bloqueada: «Esta invitación se bloqueó por seguridad. Pídele a `{nombre_pila_invita}` una nueva.»
- Sin cuenta: «Para unirte, crea tu cuenta o entra con la que tienes.»
- Después del código:
  - «Te unes a `{grupo}`. Cuidan a `{nombres_pila}`.»
  - «Con tu rol podrás: `{descripción}`.»
  - «Las personas del grupo verán tu nombre. No verán tu correo ni tu celular.»
  - «Lo que veas sobre `{nombre_pila}` es para su cuidado. No lo compartas fuera del grupo.»
  - «Política de privacidad».
- Botones: «Unirme al grupo» · «No quiero unirme».
- Hecho: «Ya eres parte de `{grupo}`.»
- Ya era parte (409): «Ya eres parte de este grupo.»
- 410: «Esta invitación ya no sirve. Pídele una nueva a quien te invitó.»
- Si recarga: «Vuelve a abrir el enlace que te enviaron.»

**Cambiar el rol:**
- «Cambiar lo que puede hacer `{nombre}`» · «Guardar el cambio».
- Hecho: «Ahora `{nombre}` `{rol en minúscula}`.»
- Si pierde la ficha: «`{nombre}` dejará de ver la ficha. Se cortan `{n}` enlaces de relevo que compartió.»
- Permiso del pagador: «Dejar que vea la ficha» · «Quitarle la ficha».
- Último admin (409): «El grupo necesita alguien que lo administre. Primero da ese rol a otra persona.»

**Sacar:**
- «¿Sacar a `{nombre}` del grupo?» · «Dejará de verlo ahora. Se cortan `{n}` enlaces de relevo que compartió. Lo que escribió en la ficha queda.»
- Botones: «Sacar del grupo» · «No sacar».
- Hecho: «`{nombre}` ya no está en el grupo.»
- 404: «Esa persona ya no estaba en el grupo.»

**Salir (D-42-13):**
- «Salir del grupo» · «¿Salir de `{grupo}`?» · «Dejarás de verlo ahora y se cortan los enlaces de relevo que compartiste.»
- Botones: «Salir del grupo» · «Quedarme».

**D-42-9:** «La autorización la dio `{nombre}`, que ya no está en el grupo. Si ahora cuidas tú a `{nombre_pila}`, renuévala.»

**Errores:** «No pudimos traer quiénes forman el grupo. Revisa tu conexión e inténtalo de nuevo.» · «No pudimos guardar el cambio. Todo sigue como estaba.»

**Para el diseñador:** dónde vive el enlace mientras la persona crea su cuenta (C25), y la página sin sesión.

## 6. Accesibilidad (MATU-53)

- Lista semántica, con el rol en texto y nunca solo con color.
- Los roles en un `fieldset` con `legend` y botones de radio, cada uno con `aria-describedby`.
- El código en un solo campo `inputmode="numeric"` que admite pegar (WCAG 3.3.8), con su etiqueta y los errores en `role="alert"`.
- Diálogos que atrapan el foco y lo devuelven, y los resultados en `aria-live`.
- 48 px, foco visible y 17 px en rem, sin desplazamiento a 320 px con el texto al 200 %.
- El código grande, con contraste y un botón para leerlo de nuevo.
- El vencimiento escrito: «hasta el 18/11/2026 a las 21:30».

## 7. Consulta legal (desde la CL-57)

- **CL-57 · Nuevas personas con acceso a los datos de la persona cuidada.**
  - **Pregunta:** ¿basta la autorización registrada, o la persona cuidada (o quien la representa) debe ser informada o autorizar a cada persona nueva? ¿Puede un cuidador de hecho extender ese acceso?
  - **Se relaciona con:** CL-01 y CL-05.
  - **Mientras tanto:** C4 a C6.
  - **Bloquea:** los datos reales.
- **CL-58 · La autorización cuando quien la dio sale del grupo.**
  - **Pregunta:** ¿sigue valiendo la declaración «cuido a esta persona»? ¿Corresponde una autorización nueva?
  - **Se relaciona con:** CL-01, CL-06 y la autorización de pedidos de MATU-61.
  - **Mientras tanto:** D-42-9 (a).
  - **Bloquea:** los datos reales.
- **CL-59 · Cuánto se guarda la membresía de quien salió.**
  - **Pregunta:** ¿cuánto se pueden guardar el rol y las fechas, si sirven para interpretar la auditoría de 3 años? ¿Puede la persona pedir que se supriman?
  - **Se relaciona con:** CL-26, CL-34 y CL-53.
  - **Bloquea:** los datos reales.
- **CL-33 (ampliar), solo si D-42-1 no es (a):** la base de licitud del contacto de una persona invitada.
- **Siguen abiertas:** CL-01, CL-05, CL-09 (si se invita a una cuidadora con contrato) y CL-36 (si MATU envía la invitación).

Ninguna bloquea el semestre, que usa datos sintéticos.

## Certeza de las citas

- **WCAG:** 1.4.4, 1.4.10 y 3.3.8 son seguras.
- **Ley 19.628:** el art. 12 (acceso), como en la revisión de MATU-55.
- **Ley 21.719:** sin artículos.
- **Ley 20.422:** como marco.

## Decisiones de Jorge (12 de noviembre de 2026)

Jorge decidió las primeras cinco de MATU-55 una por una y delegó el resto con «todas de acuerdo a tus recomendaciones». Se aplican las recomendaciones actualizadas del analista, que tienen en cuenta MATU-61, 62 y 94. Versión de la política según la D11, una por fusión. Fila de migraciones: 0024 MATU-62, 0025 MATU-55, 0026 MATU-42, 0027 MATU-46 y 0028 MATU-54. La próxima CL libre es la CL-68.

| Id | Decisión |
|---|---|
| D-42-1 | **a)** la invitación la manda quien administra, sin que MATU guarde el contacto |
| D-42-2 | **a)** un código de 4 dígitos que se dicta aparte |
| D-42-3 | 7 días con código, 48 horas sin código |
| D-42-4 | **a)** antes del código se ve quién invita y el rol |
| D-42-5 | Se pueden dar los cuatro roles, con advertencia para admin, incluido el permiso del pagador para ver la ficha |
| D-42-6 | Las invitaciones cerradas se borran a los 30 días con la tarea de MATU-74, que corre siempre |
| D-42-7 | **a)** al sacar a alguien, sus enlaces de relevo se cortan al tiro |
| D-42-8 | **b)** la auditoría lleva el rol, sin otros datos. Antes se verifica que la 0024 no cambió `auditoria_detalle_acotado` |
| D-42-9 | **a)** si quien autorizó sale del grupo, la autorización sigue, con aviso (CL-58). El aviso cubre también la autorización de pedidos |
| D-42-10 | **a)** solo los miembros activos; quien salió se ve como «Alguien que ya no está», también en los pedidos que armó, confirmó o pagó |
| D-42-11 | **a)** volver a invitar crea una fila nueva, con un índice parcial |
| D-42-12 | **a)** aceptar la invitación con funciones `SECURITY DEFINER` |
| D-42-13 | Salir del grupo por cuenta propia se incluye en esta historia |
| D-42-C20 | Un cambio de rol con un pago en curso vale desde la petición siguiente, y el pago no se anula |
| D-42-14 | Ya no hace falta: la migración es la **0026** |

**Ajustes:** si la 0024 no divide `direccion_familia` y `direccion_operacion`, las divide la 0026; el texto sobre pedidos del rol «Paga» se muestra solo con la capa 3 encendida; se borra «la próxima es CL-60».

## Revisión de cierre (12-11)

El analista revisó el código de MATU-42 y MATU-53 contra esta revisión previa y las decisiones de Jorge.

- **El código CUMPLE en todos los puntos**, incluidas `membresia_retirar` (decisión 327) y la decisión 322.
- **La política 0.15 se aplica en este PR**, junto con el registro de tratamientos (entrada 12 nueva y ajustes en las entradas 1 y 4), la consulta legal, el modelo de datos y la arquitectura (secciones 11.2 y 11.8).
- **Observaciones:**
  - **O1** (la cota de `p_ahora` hacia el pasado) y **O2** (la prueba del marcador `app.funcion`) se corrigen en el PR de código.
  - **O3** (el email y el celular de un miembro todavía se pueden leer en SQL desde otro miembro activo) pasa a la tarjeta MATU-102, y se resuelve antes de datos reales.
  - **O4** (avisar que se anulan las invitaciones sin usar de quien deja de administrar) va con un texto en las pantallas, que llega a `lenguaje.md` en un commit posterior.
- **D-46-7** queda anotada en el registro de tratamientos, entrada 4: la copia del nombre de pila de quien comparte se anonimiza al eliminar la cuenta y en la purga de MATU-89.
- **Quedan abiertas** la CL-57, la CL-58, la CL-59 y la CL-66 ampliada.

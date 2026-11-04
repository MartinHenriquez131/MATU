# Registro de tratamientos de MATU

**Estado:** borrador para el piloto académico, a la par de la política de privacidad v0.10. Lo redacta el analista normativo y lo aprueba Jorge Espinoza. Este documento no es asesoría legal.

Cada historia que empieza a tratar datos personales agrega aquí su entrada.

## 1. Alta de la persona cuidada y registro de su autorización (MATU-07)

- **Finalidad:** organizar su cuidado y la ficha de relevo (`plan_cuidado`).
- **Titulares:** la persona cuidada, y el usuario que da la autorización.
- **Datos:**
  - nombre y nombre de pila
  - nivel de apoyo, que es un **dato sensible**
  - dirección de entrega, opcional
  - la autorización: calidad, versión de la política, evidencia mínima y la referencia al documento si es representante legal
- **Base de licitud:** consentimiento del titular o de su representante legal. Cuidadora o cuidador de hecho: [PENDIENTE: consulta legal].
- **Quién accede:**
  - administrador y cuidador ven todo
  - el pagador ve el nombre y la dirección
  - el observador ve el nombre
  - operación: [PENDIENTE: acotar a nombre y dirección en la historia de backoffice]
- **Conservación:** [PENDIENTE: plazo del registro de autorizaciones, en consulta legal].
- **Medidas:**
  - separación por familia con RLS forzado
  - la aplicación se conecta sin privilegios de dueño
  - registros técnicos sin datos de la persona
  - auditoría de solo inserción
  - consentimiento de solo inserción: [PENDIENTE: tarjeta "S2 · Consentimiento inalterable"]
- **Comunicaciones a terceros:** ninguna.
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna.

## 2. Pedidos y pagos de insumos (ADR-027)

> Aprobado por Jorge el 27-10 como diseño. Las frases sobre lo que el comercio ve o no ve se publican solo cuando la migración del sprint 4 (requisitos R7 a R9, arquitectura 18.1) las haga ciertas.

> ADR-027 (27-10), aprobado por Jorge.

**Todavía no se trata.** Durante el semestre los pedidos y los pagos se hacen solo con datos sintéticos, precios de ejemplo y el ambiente de integración de Transbank (`figura-legal-piloto.md`, sección 5).

- **Finalidad:** pedir insumos a comercios en convenio, a precio exacto, y cobrar una sola vez el total confirmado. MATU vende y emite una sola boleta por el total, con el envío incluido.
- **Titulares:** el usuario que pide y paga, y la persona cuidada a quien va el pedido.
- **Datos:**
  - productos, cantidades, precios, envío y total. El historial de pedidos y de consumo de la persona cuidada se trata como **dato sensible**, porque junto con un dato que identifica puede revelar salud o dependencia (`investigacion-normativa-adr-027.md`, sección 3) [PENDIENTE: consulta legal sobre si los productos de un pedido son un dato relativo a la salud]
  - dirección de entrega
  - teléfono de contacto para la entrega
  - la elección por producto si falta (RF-21), y la versión de las condiciones del pedido aceptadas, con su fecha
  - el pago: monto cobrado, monto devuelto, código de autorización, tipo de tarjeta y últimos 4 dígitos. MATU nunca recibe ni guarda los datos de la tarjeta
- **Base de licitud:** consentimiento expreso y **separado** del de la ficha, solo para los pedidos, que se revoca por un medio igual de fácil que el usado para darlo. La titular es la persona cuidada, y quién consiente sigue la calidad de MATU-07.
  - [PENDIENTE: consulta legal sobre si el art. 16 bis, inciso 1, limita el tratamiento aunque haya consentimiento, y si sirve como base su letra e)]
  - quién consiente por la persona mayor dependiente (arts. 12 y 16 c) se resuelve con MATU-07: calidad del otorgante y revisión a los 12 meses. Lo que quede abierto se une a la consulta del cuidador de hecho (decisión de Jorge, 27-10)
  - la evaluación de impacto del art. 15 ter se hace antes de operar con datos reales, sea obligatoria o no (decisión de Jorge, 27-10)
- **Quién accede:**
  - en el grupo, todos los roles ven los pedidos, incluido el observador, que nunca ve la ficha; administrador y cuidador los crean, y administrador y pagador pagan (arquitectura, sección 11.2)
  - el comercio que prepara ve solo sus productos, la referencia del pedido y el código de retiro. **Ningún nombre**, ni la ficha ni la dirección. El comercio que reemplaza a otro ve lo mismo, solo con lo que le toca
  - operación ve pedidos y pagos para dar soporte, y devuelve por anulación. Nunca la ficha ni el consumo de insumos
- **La consulta de stock no trata datos personales:** lleva solo productos, cantidades y una referencia opaca para apartar, **aleatoria por pedido y nunca por familia**. No lleva datos de la familia, de la persona cuidada ni de la dirección, y una prueba sobre el objeto de la consulta lo verifica.
- **Conservación:** pedidos y comprobantes de entrega, 2 años. Pagos y boletas, 6 años, por obligación tributaria (arquitectura, sección 11.8).
- **Medidas:**
  - separación por familia con RLS forzado
  - el comercio ve un pedido solo cuando está pagado y enviado, y nunca la dirección, que vive en una tabla aparte
  - el precio pagado queda fijo en la base desde el pago, y lo devuelto nunca supera lo cobrado
  - registro de transacciones de pasarela que nunca se borra
  - la proyección del comercio excluye todo identificador de la familia y de la persona, con una prueba de contrato. [PENDIENTE: hoy la base deja al comercio leer `destinatario_nombre_pila`, `grupo_id`, `persona_cuidada_id`, `creado_por` y las transiciones de los pedidos que ve, y escribir la elección de RF-21 y `monto_devuelto`. Se corrige con una migración nueva antes de construir la vista del comercio]
- **Comunicaciones a terceros:**
  - comercios en convenio, con lo que dice "Quién accede". **La dirección nunca llega al comercio.** MATU trata al comercio como si fuera encargado, sea o no un dato personal para él la referencia del pedido, y el convenio lleva siempre las cláusulas del art. 15 bis (decisión de Jorge, 27-10)
  - quien despacha, que ve la dirección, el teléfono de contacto y el paquete: **encargado** de MATU, con contrato según el art. 15 bis (instrucciones, confidencialidad, seguridad, reporte de vulneraciones y supresión al terminar)
  - Transbank, que procesa el pago en su propia página. La devolución vuelve a la misma tarjeta, por anulación de Webpay Plus, sin pedir datos nuevos
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna.

## 3. Ficha de relevo (MATU-09, MATU-11 a MATU-14, MATU-50)

> Aprobado por Jorge el 27-10 como diseño. Que retirar la autorización corte los accesos de relevo vigentes depende de la historia del sprint 3 "Revocar el consentimiento y cortar los accesos de relevo vigentes". Esa historia es requisito para operar con datos reales, igual que los requisitos R7 a R9 del ADR-027.

**Todavía no se trata con datos reales.** Durante el semestre la ficha se escribe solo con datos sintéticos (`figura-legal-piloto.md`).

- **Finalidad:** guardar la ficha de relevo, con sus tres campos ("Su día", "Si se altera" y "A quién llamar") y hasta seis secciones adicionales opcionales (ADR-028), para que quien reemplaza a quien cuida sepa qué hacer y conozca a la persona.
- **Titulares:**
  - la persona cuidada
  - los miembros del grupo que escriben la ficha
  - las personas anotadas en "A quién llamar"
- **Datos:**
  - el texto de cada uno de los tres campos, hasta 500 caracteres por campo. Es **dato sensible**, porque habla de la salud y de la dependencia de la persona. MATU no pide diagnósticos
  - quién escribió cada campo y cada sección, cuándo y su versión, y cuándo se agregó cada sección (`plan_seccion.creado_en`, que no cambia al editar)
  - la auditoría, sin el texto: `plan.leer` de cada lectura, incluida la del 412; `plan.editar` de cada escritura, con el tipo de la sección en `detalle.seccion` si es adicional; y `plan.quitar_seccion`, con el tipo de la sección quitada. El `CHECK auditoria_detalle_acotado` admite solo los seis tipos (migración 0013)
  - el texto de las secciones adicionales `quien_es`, `preferencias`, `alimentacion`, `movilidad`, `comunicacion` y `remedios`, hasta 500 caracteres cada una y 800 en `remedios`. Es **dato sensible**. `remedios` es un dato relativo a la salud, en texto libre escrito por la familia, sin catálogo, dosis estructuradas ni recordatorios (decisión de Jorge del 03-11, sin consulta legal previa, por la seguridad del cuidado). Quitar una sección (`DELETE` con `If-Match`) borra su fila y su texto cifrado en el acto; volver a agregarla crea otra fila. El servidor no interpreta ni clasifica el texto
- **Base de licitud:** la autorización registrada en MATU-07, con el texto ampliado a las secciones adicionales desde la versión 0.10. Las versiones anteriores a la 0.10 solo se usaron con datos sintéticos y ninguna persona real las aceptó, así que no hay autorizaciones previas que renovar (decisión de Jorge del 03-11). Sin autorización vigente la API responde 403.
  - cuidadora o cuidador de hecho: [PENDIENTE: consulta legal]
  - personas anotadas en "A quién llamar": [PENDIENTE: consulta legal sobre su base de licitud]
- **Quién accede:**
  - administrador y cuidador leen, escriben y quitan secciones
  - el pagador lee los campos y las secciones solo si tiene el permiso de ver la ficha. No escribe ni quita: la API le responde 404, y la política RLS de `plan_seccion` solo permite escribir a administrador y cuidador (decisión 102, migración 0013)
  - el observador nunca. La API le responde 404
  - el relevo, mientras su acceso esté vigente, lee los campos base habilitados y las secciones adicionales que se le marcaron y que ya existían al crear su acceso (`plan_seccion.creado_en <= acceso_relevo.creado_en`, en la política RLS `seccion_relevo`, de solo lectura, y en la consulta)
  - operación nunca
- **Conservación:**
  - mientras la autorización esté vigente y hasta 90 días después
  - el borrado se cumple destruyendo la clave de la persona. [PENDIENTE: confirmar que una solicitud de borrado no espera los 90 días]
  - copias de respaldo: [PENDIENTE]
  - una sección adicional quitada: se borra en el acto. Queda en las copias de respaldo hasta que venzan
  - auditoría: 3 años, también la que guarda el tipo de una sección quitada
- **Medidas:**
  - cifrado AES-256-GCM con una clave por persona, envuelta por una clave maestra (MATU-11). Durante el semestre, con datos sintéticos, la clave maestra está en una variable de entorno del mismo servidor: quien accede al servidor accede a todo. La API no arranca así en producción (decisión de Jorge del 28-10, MATU-12). [PENDIENTE: servicio de custodia de claves antes de operar con datos reales (ADR-016)]
  - nonce de 12 bytes, nuevo en cada escritura
  - cada sección adicional se cifra por separado, con AAD `plan_id ‖ tipo`, lo que permite compartirlas una por una
  - `remedios` nunca se incluye en un acceso de relevo si quien comparte no la marca
  - el texto cifrado queda atado a su plan y a su campo
  - separación por familia con RLS forzado
  - auditoría de solo inserción (MATU-14)
  - `ETag` y 412 cuando dos personas editan el mismo campo (MATU-13)
  - el texto nunca aparece en logs, errores, URLs ni en el almacenamiento del navegador
  - el detalle de la auditoría solo admite tipos de sección, nunca texto (`CHECK` de la migración 0013)
  - la ficha y sus secciones no se imprimen ni se exportan: no hay ruta ni vista de impresión (ADR-029)
- **Comunicaciones a terceros:**
  - solo al relevo, con lo que dice la entrada 4
  - dictado: si quien escribe usa el micrófono, el reconocimiento de voz lo hace el servicio del navegador (en Chrome, Google), que recibe el audio. MATU no lo recibe ni lo guarda. En Sus remedios el dictado está desactivado hasta la respuesta legal (decisión de Jorge del 03-11). [PENDIENTE: consulta legal sobre el envío de audio de un dato sensible, nombrar los servicios y sus países]
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna.

## 4. Acceso de relevo (MATU-09, MATU-18 a MATU-20, MATU-23, MATU-25)

> Aprobado por Jorge el 27-10 como diseño. Que retirar la autorización corte los accesos de relevo vigentes depende de la historia del sprint 3 "Revocar el consentimiento y cortar los accesos de relevo vigentes". Esa historia es requisito para operar con datos reales, igual que los requisitos R7 a R9 del ADR-027.

**Todavía no se trata con datos reales.** Durante el semestre los accesos se crean solo con datos sintéticos (`figura-legal-piloto.md`).

- **Finalidad:**
  - dar un acceso temporal, de solo lectura, a los tres campos de la ficha y a las secciones adicionales que marque quien comparte (`remedios` viene sin marcar), y que se puede cortar en cualquier momento. Registra qué secciones se mostraron en cada apertura, sin su contenido
  - el teléfono del relevo sirve para que quien comparte le envíe el enlace desde su propio teléfono, por WhatsApp o SMS, y para que la familia pueda contactarlo. MATU no envía mensajes
  - el registro sirve para saber a quién se entregó la ficha y para detectar un enlace reenviado
- **Titulares:**
  - el relevo: su nombre, su teléfono, cada vez que abre el enlace o la ficha, sus PIN incorrectos y su dirección IP
  - la persona cuidada: su nombre de pila, y los campos y secciones adicionales compartidos
  - quien otorga el acceso. También por su nombre de pila, que el relevo ve (decisión de Jorge del 27-10)
- **Datos:**
  - nombre y teléfono del relevo, obligatorios
  - el nombre de pila de la persona cuidada, copiado al crear el acceso. Se anonimiza si se borra a la persona
  - el nombre de pila de quien comparte
  - los campos base y las secciones adicionales habilitadas (`secciones_permitidas`). Los accesos nuevos llevan siempre los tres campos base y las secciones adicionales marcadas; `remedios` solo si quien comparte la marca y confirma. Los anteriores a MATU-50 conservan los que se eligieron
  - el motivo, elegido de una lista cerrada (`salgo_unas_horas`, `fin_de_semana_fuera`, `turno_de_noche`, `otro`), sin texto libre
  - las fechas de creación, vencimiento y corte, y quién otorgó el acceso
  - el hash del token y el PIN transformado con HMAC-SHA-256 y *pepper*. Nunca en claro
  - los intentos fallidos, los usos y el último uso
  - la auditoría, sin IP, de cada vez que el relevo abre el enlace aunque no escriba el PIN (`relevo.presentar`), y de las aperturas de la ficha, los PIN incorrectos y los bloqueos. `relevo.abrir` guarda en `detalle.secciones` la lista de tipos de las secciones adicionales mostradas (puede ser vacía), sin su texto. La familia la ve en "Quién la vio"
  - la dirección IP, solo en los contadores temporales de 1 hora en Redis, uno para abrir el enlace y otro para el canje, con una huella HMAC como clave. No se guarda en la base, en la auditoría ni en los logs
- **Base de licitud:**
  - para lo que se muestra de la persona cuidada: la autorización de MATU-07, que permite "compartirla con el relevo que elija el grupo"
  - para los datos del relevo: interés legítimo de la familia, informado. Quien comparte declara que avisó al relevo (`relevo_informado`, con la fecha en `acceso_relevo.relevo_informado_en`, decisión 34 del contrato), y el relevo ve el aviso de `lenguaje.md`, sección 7.5, antes del PIN. [PENDIENTE: consulta legal]
  - para la dirección IP: [PENDIENTE: consulta legal]
- **Quién accede:**
  - administrador y cuidador crean accesos, los ven, los cortan y ven las aperturas en "Quién la vio" (MATU-45; el observador no las ve), incluidas las veces que se abrió el enlace ("abrió el enlace"). Son los únicos que ven el teléfono del relevo en la lista de accesos, y después de los 30 días aparece vacío (contrato de MATU-09, decisión 31)
  - el pagador con permiso de ver la ficha lista los accesos y las aperturas, sin crear ni cortar (contrato de MATU-09). No ve el teléfono del relevo
  - el observador nunca
  - el relevo ve el nombre de pila de la persona cuidada y el de quien comparte, también antes de escribir el PIN (decisión de Jorge del 27-10). Los campos y las secciones los ve solo después del PIN
  - operación nunca
- **Conservación:**
  - nombre del relevo, motivo y fechas: 3 años desde que el acceso vence o se corta, igual que la auditoría (arquitectura, sección 11.8)
  - teléfono del relevo: se borra 30 días después de que el acceso vence o se corta
  - sesión del relevo: 12 horas como máximo, y nunca más allá del vencimiento del acceso
  - contadores por IP: 1 hora
- **Medidas:**
  - token de 256 bits en el fragmento del enlace (`/r#<token>`). Se canjea por POST junto con el PIN, y la página lo limpia con `history.replaceState`
  - con solo el token, la presentación (`POST /v1/relevo/presentacion`) devuelve únicamente los dos nombres de pila. No crea sesión ni cuenta como intento de PIN. Queda en la auditoría como `relevo.presentar`, sin IP, y la familia la ve en "Quién la vio" como "abrió el enlace", para detectar un enlace reenviado (decisión 30)
  - PIN de 4 dígitos, que se muestra una sola vez y quien comparte dicta por otro canal
  - cookie `HttpOnly`, `Secure` y `SameSite=Strict`, con la sesión en Redis
  - 5 PIN incorrectos bloquean el acceso (423)
  - desde una misma IP, 30 presentaciones por hora y 10 canjes por hora, cada límite con su propio contador por huella HMAC, que dura 1 hora (decisión 29)
  - un acceso vencido o cortado responde 410, aunque la cookie siga vigente
  - la sesión del relevo no fija el grupo
  - vigencia de 24 horas por omisión y de 30 días como máximo
  - cabeceras `no-store`, `no-referrer` y `noindex`
  - nunca token, PIN ni texto de la ficha en los logs
  - la app de la familia guarda el PIN y el enlace solo en la memoria de la pantalla, los muestra una vez y nunca copia el PIN al portapapeles ni lo pone en el mensaje. El enlace se envía con la hoja de compartir del teléfono o copiándolo, nunca con el token en la dirección de un servicio de terceros (MATU-48)
  - nombre y teléfono del relevo sin autocompletado del navegador
  - sin impresión ni exportación de la ficha (ADR-029)
- **Comunicaciones a terceros:** ninguna desde MATU. Si un día MATU envía el PIN por SMS, se agrega aquí.
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna con efectos sobre las personas. El bloqueo por PIN incorrecto es un control de seguridad.

## 5. Consumo de insumos y fecha estimada (MATU-36, MATU-37)

**Todavía no se trata con datos reales.** Solo con datos sintéticos (`figura-legal-piloto.md`).

- **Finalidad:** calcular cuándo se acaba cada insumo de la persona cuidada y mostrar cuáles se acaban pronto.
- **Titulares:** la persona cuidada, y quien anota.
- **Datos:**
  - producto del catálogo o `nombre_libre` (1 a 60 caracteres, en una línea);
  - unidad (la app ofrece unidad y sobre);
  - tasa (`tasa_unidades`/`tasa_dias`);
  - stock y fecha del stock (la fija el servidor);
  - días de aviso y fecha estimada;
  - si se sigue o no, y la versión.

  Se trata como **dato sensible**. [PENDIENTE: consulta legal sobre si es dato relativo a la salud y si basta RLS sin cifrado (decisión 63)]
- **Base de licitud:** consentimiento separado, `finalidad = consumo`, en la misma calidad de MATU-07, con la declaración `declaracion_consumo_<calidad>` (aprobadas por Jorge el 03-11) y la revisión de 12 meses. Sin él, 403. Cuidador de hecho: [PENDIENTE: consulta legal].
- **Quién accede:**
  - admin y cuidador leen y escriben (en la API y en una política RLS de escritura);
  - pagador y observador solo leen (decisión de Jorge del 03-11);
  - operación nunca.
- **Conservación:**
  - mientras la autorización esté vigente y hasta 90 días después, también los insumos que no se siguen;
  - eliminar un insumo lo borra en el acto;
  - el consumo se **borra**, porque no hay clave que destruir (decisiones de Jorge del 03-11);
  - copias de respaldo: [PENDIENTE].
- **Medidas:**
  - RLS forzado por grupo y escritura por rol en RLS;
  - `ETag`/`If-Match` (412/428);
  - `nombre_libre` nunca en logs, errores, auditoría ni eventos;
  - auditoría de solo inserción de `consumo.crear`, `consumo.editar`, `consumo.desactivar`, `consumo.activar`, `consumo.eliminar` y `consentimiento.otorgar`, sin nombre, cantidades ni IP;
  - los eventos llevan solo identificadores;
  - nada en el almacenamiento del navegador ni en la URL;
  - RLS separada de `alerta_quiebre` y `reposicion` (MATU-37): leen los cuatro roles; solo el rol sistema crea alertas; solo admin y cuidador las cierran o declaran una compra; nadie las borra a mano;
  - auditoría de `alerta.materializar`, `alerta.resolver`, `alerta.descartar` y `reposicion.declarar`, sin nombre, cantidades ni IP;
  - el aviso por push o correo es un texto fijo sin nombres de personas ni de insumos, y su enlace no lleva identificadores.
- **Alertas y compras declaradas (MATU-37):**
  - alertas: insumo (por su identificador), fecha estimada, estado y cuándo se avisó y se cerró. Sin nombre del insumo ni cantidades;
  - compras declaradas con «Ya lo resolví»: cantidad, fecha y quién la anotó; se suman a lo que quedaba;
  - el trabajo diario (rol sistema) crea las alertas solo para personas con la autorización de insumos vigente;
  - para recorrer los grupos, el trabajo diario usa en el semestre el rol operación, que lee solo el identificador de cada grupo activo; después trabaja grupo por grupo con el rol sistema. [PENDIENTE: usuario propio de tareas programadas, con permiso solo para leer los identificadores, antes de datos reales];
  - conservación: alertas cerradas 90 días desde que se cierran, eventos publicados 30 días, avisos enviados 90 días, compras mientras exista el insumo (decisiones de Jorge del 03-11).
- **Comunicaciones a terceros:** el servicio de push del navegador y el proveedor de correo reciben un aviso de texto fijo, «MATU: un insumo se está acabando. Abre la app para ver cuál», y el destino (token push o email). Por defecto avisan a admin y cuidador. Son encargados de MATU. [PENDIENTE: nombrarlos, su país y el contrato de encargo]. **Transferencia internacional:** [PENDIENTE]. **Decisiones automatizadas:** ninguna. La fecha es una estimación informativa y la alerta nunca genera un pedido.

## 6. Cuenta, sesión y dispositivos (MATU-38)

- **Finalidad:** mantener la sesión, permitir sacar un dispositivo, detectar el robo de una sesión, limitar los intentos de entrada y enviar avisos.
- **Titulares:** las personas usuarias, y quien intenta entrar con un email (que puede no ser usuaria).
- **Datos:**
  - sesión: SHA-256 del refresh, emisión, vencimiento, revocación y motivo;
  - dispositivo: nombre general sin agente de usuario, creación, último uso y `push_token` opcional;
  - huella HMAC de la IP y del email en Redis, por 1 hora;
  - auditoría `sesion.*` y `dispositivo.*`, sin huella del email (decisión 64), con `sesiones_revocadas` como único detalle.
- **Base de licitud:** ejecución del servicio que pide la persona. Para los contadores por huella de IP y de email: [PENDIENTE: consulta legal].
- **Quién accede:**
  - cada persona a sus dispositivos;
  - operación no ve ninguna fila, y la conservación corre con `iam_conservar`;
  - la auditoría de la cuenta la podrá leer su titular en "Dónde entraste" (MATU-55, sprint 4).
- **Conservación:**
  - ventana deslizante de 30 días sin tope absoluto (decisión de Jorge del 31-10);
  - las sesiones se borran 30 días después de vencer o de cerrarse;
  - los dispositivos, 90 días después del último uso;
  - el `push_token`, al cerrar o sacar el dispositivo;
  - los contadores, en 1 hora.
- **Medidas:**
  - cookie `HttpOnly`, `Secure`, `SameSite=Strict` y `Path=/v1/sesiones`;
  - access token en memoria, por 15 minutos;
  - rotación con detección de reutilización;
  - `no-store`;
  - push con texto fijo y sin datos de personas ni de insumos, y con una lista cerrada de hosts.
- **Comunicaciones a terceros:** el servicio de push del navegador recibe un aviso de texto fijo, sin datos de personas ni de insumos. [PENDIENTE: nombrarlos y su país]. **Decisiones automatizadas:** ninguna. La espera después de varios intentos es un control de seguridad.

## 7. Celular de la cuenta (MATU-39, MATU-57)

- **Finalidad:** enviar un código por SMS o WhatsApp para recuperar la contraseña o confirmar la identidad (MATU-57). El celular se confirma con un código antes de usarlo para recuperar (decisión de Jorge del 03-11).
- **Titulares:** las personas usuarias.
- **Datos:** celular en formato E.164 (`+569XXXXXXXX`), obligatorio al crear la cuenta (decisión de Jorge del 03-11).
- **Base de licitud:** ejecución del servicio que pide la persona.
- **Quién accede:** la propia persona y operación para soporte. No lo ven las otras personas del grupo.
- **Conservación:** mientras exista la cuenta. [PENDIENTE: plazo tras eliminar la cuenta]
- **Medidas:** nunca en logs, errores, auditoría ni eventos.
- **Comunicaciones a terceros:** ver la entrada 8.

## 8. Recuperación del acceso (MATU-57) · todavía no implementada

- **Finalidad:** comprobar que quien pide recuperar la cuenta es su titular, y permitirle cambiar la contraseña.
- **Titulares:** las personas usuarias.
- **Datos:**
  - el email que escribe la persona (nunca se pide el celular para recuperar);
  - la huella HMAC del código (pepper propio);
  - el canal (celular confirmado o email);
  - la creación, la expiración, los intentos y el uso;
  - las huellas HMAC de la IP, del email y del celular en los contadores de límite.
- **Base de licitud:** ejecución del servicio que pide la persona.
- **Quién accede:** nadie ve el código. Operación ve solo eventos de auditoría sin datos de contacto.
- **Conservación:** el código, hasta usarse o 10 minutos. Los contadores, 24 horas como máximo. La auditoría, según la entrada de auditoría.
- **Medidas:**
  - código de 6 dígitos, de un solo uso y con 5 intentos como máximo; pedir uno nuevo invalida el anterior;
  - límite de 3 envíos por hora y 10 al día por IP, email y celular;
  - la misma respuesta exista o no la cuenta;
  - el celular se usa solo si está confirmado; si no, el email;
  - cierre de todas las sesiones al cambiar la contraseña y aviso por el otro canal;
  - nunca el código, el celular ni el email en logs, errores, auditoría ni eventos.
- **Comunicaciones a terceros:** los proveedores de SMS, WhatsApp y correo, como encargados con contrato. Reciben solo el destino y el texto del mensaje. En el semestre el envío es simulado, sin proveedor real (decisión de Jorge del 03-11). [PENDIENTE: nombrarlos y su país]
- **Transferencia internacional:** [PENDIENTE: proveedor, país y garantía]. Requiere consulta legal.
- **Decisiones automatizadas:** ninguna. La espera después de varios intentos es un control de seguridad.

## Nota sobre la ficha ampliada (ADR-028)

La sección "Sus remedios" se mantiene por decisión de Jorge del 03-11, sin consulta legal previa: quien releva y no conoce los remedios pone en riesgo a la persona cuidada. Se trata como dato sensible, cifrado como la ficha, y al compartir viene sin marcar. Su tratamiento queda descrito en las entradas 3 y 4 (revisión previa de MATU-49 y de cierre de MATU-50, 03-11). La confirmación al compartir Sus remedios se revisa cuando MATU-48 integre el paso de compartir.

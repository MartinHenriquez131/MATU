# Registro de tratamientos de MATU

**Estado:** borrador para el piloto académico, a la par de la política de privacidad v0.9. Lo redacta el analista normativo y lo aprueba Jorge Espinoza. Este documento no es asesoría legal.

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

## 3. Ficha de relevo (MATU-09, MATU-11 a MATU-14)

> Aprobado por Jorge el 27-10 como diseño. Que retirar la autorización corte los accesos de relevo vigentes depende de la historia del sprint 3 "Revocar el consentimiento y cortar los accesos de relevo vigentes". Esa historia es requisito para operar con datos reales, igual que los requisitos R7 a R9 del ADR-027.

**Todavía no se trata con datos reales.** Durante el semestre la ficha se escribe solo con datos sintéticos (`figura-legal-piloto.md`).

- **Finalidad:** guardar la ficha de relevo, con sus tres campos "Su día", "Si se altera" y "A quién llamar", para que quien reemplaza a la cuidadora sepa qué hacer.
- **Titulares:**
  - la persona cuidada
  - los miembros del grupo que escriben la ficha
  - las personas anotadas en "A quién llamar"
- **Datos:**
  - el texto de cada campo, hasta 500 caracteres por campo. Es **dato sensible**, porque habla de la salud y de la dependencia de la persona. MATU no pide diagnósticos
  - quién escribió cada campo, cuándo y su versión
  - la auditoría de cada lectura y escritura, sin el texto
- **Base de licitud:** la autorización registrada en MATU-07. Sin autorización vigente la API responde 403.
  - cuidadora o cuidador de hecho: [PENDIENTE: consulta legal]
  - personas anotadas en "A quién llamar": [PENDIENTE: consulta legal sobre su base de licitud]
- **Quién accede:**
  - administrador y cuidador leen y escriben
  - el pagador lee solo si tiene el permiso de ver la ficha
  - el observador nunca. La API le responde 404
  - el relevo lee solo los campos habilitados, mientras su acceso esté vigente
  - operación nunca
- **Conservación:**
  - mientras la autorización esté vigente y hasta 90 días después
  - el borrado se cumple destruyendo la clave de la persona. [PENDIENTE: confirmar que una solicitud de borrado no espera los 90 días]
  - copias de respaldo: [PENDIENTE]
  - auditoría: 3 años
- **Medidas:**
  - cifrado AES-256-GCM con una clave por persona, envuelta por una clave maestra (MATU-11). Durante el semestre, con datos sintéticos, la clave maestra está en una variable de entorno del mismo servidor: quien accede al servidor accede a todo. La API no arranca así en producción (decisión de Jorge del 28-10, MATU-12). [PENDIENTE: servicio de custodia de claves antes de operar con datos reales (ADR-016)]
  - nonce de 12 bytes, nuevo en cada escritura
  - el texto cifrado queda atado a su plan y a su campo
  - separación por familia con RLS forzado
  - auditoría de solo inserción (MATU-14)
  - `ETag` y 412 cuando dos personas editan el mismo campo (MATU-13)
  - el texto nunca aparece en logs, errores, URLs ni en el almacenamiento del navegador
- **Comunicaciones a terceros:** solo al relevo, con lo que dice la entrada 4.
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna.

## 4. Acceso de relevo (MATU-09, MATU-18 a MATU-20, MATU-23, MATU-25)

> Aprobado por Jorge el 27-10 como diseño. Que retirar la autorización corte los accesos de relevo vigentes depende de la historia del sprint 3 "Revocar el consentimiento y cortar los accesos de relevo vigentes". Esa historia es requisito para operar con datos reales, igual que los requisitos R7 a R9 del ADR-027.

**Todavía no se trata con datos reales.** Durante el semestre los accesos se crean solo con datos sintéticos (`figura-legal-piloto.md`).

- **Finalidad:**
  - dar un acceso temporal, de solo lectura, a los campos de la ficha que elige quien comparte, y que se puede cortar en cualquier momento
  - el teléfono del relevo sirve para que quien comparte le envíe el enlace desde su propio teléfono, por WhatsApp o SMS, y para que la familia pueda contactarlo. MATU no envía mensajes
  - el registro sirve para saber a quién se entregó la ficha y para detectar un enlace reenviado
- **Titulares:**
  - el relevo: su nombre, su teléfono, cada vez que abre el enlace o la ficha, sus PIN incorrectos y su dirección IP
  - la persona cuidada: su nombre de pila y los campos compartidos
  - quien otorga el acceso. También por su nombre de pila, que el relevo ve (decisión de Jorge del 27-10)
- **Datos:**
  - nombre y teléfono del relevo, obligatorios
  - el nombre de pila de la persona cuidada, copiado al crear el acceso. Se anonimiza si se borra a la persona
  - el nombre de pila de quien comparte
  - los campos habilitados
  - el motivo, elegido de una lista cerrada (`salgo_unas_horas`, `fin_de_semana_fuera`, `turno_de_noche`, `otro`), sin texto libre
  - las fechas de creación, vencimiento y corte, y quién otorgó el acceso
  - el hash del token y el PIN transformado con HMAC-SHA-256 y *pepper*. Nunca en claro
  - los intentos fallidos, los usos y el último uso
  - la auditoría, sin IP, de cada vez que el relevo abre el enlace aunque no escriba el PIN (`relevo.presentar`), y de las aperturas de la ficha, los PIN incorrectos y los bloqueos
  - la dirección IP, solo en los contadores temporales de 1 hora en Redis, uno para abrir el enlace y otro para el canje, con una huella HMAC como clave. No se guarda en la base, en la auditoría ni en los logs
- **Base de licitud:**
  - para lo que se muestra de la persona cuidada: la autorización de MATU-07, que permite "compartirla con el relevo que elija el grupo"
  - para los datos del relevo: [PENDIENTE: consulta legal]. MATU los recibe de quien comparte y se lo informa al relevo con el aviso de `lenguaje.md`, sección 7.5
  - para la dirección IP: [PENDIENTE: consulta legal]
- **Quién accede:**
  - administrador y cuidador crean accesos, los ven, los cortan y ven las aperturas, incluidas las veces que se abrió el enlace ("abrió el enlace"). Son los únicos que ven el teléfono del relevo en la lista de accesos, y después de los 30 días aparece vacío (contrato de MATU-09, decisión 31)
  - el pagador con permiso de ver la ficha lista los accesos y las aperturas, sin crear ni cortar (contrato de MATU-09). No ve el teléfono del relevo
  - el observador nunca
  - el relevo ve el nombre de pila de la persona cuidada y el de quien comparte, también antes de escribir el PIN (decisión de Jorge del 27-10). Los campos los ve solo después del PIN
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
- **Comunicaciones a terceros:** ninguna desde MATU. Si un día MATU envía el PIN por SMS, se agrega aquí.
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna con efectos sobre las personas. El bloqueo por PIN incorrecto es un control de seguridad.

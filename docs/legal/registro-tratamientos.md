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
  - cifrado AES-256-GCM con una clave por persona, envuelta por una clave maestra en custodia externa (MATU-11). [PENDIENTE: servicio de custodia de claves]
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
  - el registro sirve para saber a quién se entregó la ficha
- **Titulares:**
  - el relevo: su nombre, su teléfono, sus aperturas, sus PIN incorrectos y su dirección IP
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
  - la auditoría de aperturas, PIN incorrectos y bloqueos
  - la dirección IP, solo como contador temporal de 1 hora en Redis, con una huella HMAC como clave. No se guarda en la base ni en los logs
- **Base de licitud:**
  - para lo que se muestra de la persona cuidada: la autorización de MATU-07, que permite "compartirla con el relevo que elija el grupo"
  - para los datos del relevo: [PENDIENTE: consulta legal]. MATU los recibe de quien comparte y se lo informa al relevo con el aviso de `lenguaje.md`, sección 7.5
  - para la dirección IP: [PENDIENTE: consulta legal]
- **Quién accede:**
  - administrador y cuidador crean accesos, los ven, los cortan y ven las aperturas
  - el pagador con permiso de ver la ficha lista los accesos y las aperturas, sin crear ni cortar (contrato de MATU-09). Ninguna respuesta de la API devuelve el teléfono del relevo
  - el observador nunca
  - el relevo ve el nombre de pila de la persona cuidada y el de quien comparte, también antes de escribir el PIN (decisión de Jorge del 27-10). Los campos los ve solo después del PIN
  - operación nunca
- **Conservación:**
  - nombre del relevo, motivo y fechas: 3 años desde que el acceso vence o se corta, igual que la auditoría (arquitectura, sección 11.8)
  - teléfono del relevo: se borra 30 días después de que el acceso vence o se corta
  - sesión del relevo: 12 horas como máximo, y nunca más allá del vencimiento del acceso
  - contador por IP: 1 hora
- **Medidas:**
  - token de 256 bits en el fragmento del enlace (`/r#<token>`). Se canjea por POST junto con el PIN, y la página lo limpia con `history.replaceState`
  - con solo el token, la presentación (`POST /v1/relevo/presentacion`) devuelve únicamente los dos nombres de pila. No crea sesión, no cuenta como intento de PIN ni como apertura
  - PIN de 4 dígitos, que se muestra una sola vez y quien comparte dicta por otro canal
  - cookie `HttpOnly`, `Secure` y `SameSite=Strict`, con la sesión en Redis
  - 5 PIN incorrectos bloquean el acceso (423)
  - 10 presentaciones y canjes por hora desde una misma IP, contados con su huella
  - un acceso vencido o cortado responde 410, aunque la cookie siga vigente
  - la sesión del relevo no fija el grupo
  - vigencia de 24 horas por omisión y de 30 días como máximo
  - cabeceras `no-store`, `no-referrer` y `noindex`
  - nunca token, PIN ni texto de la ficha en los logs
- **Comunicaciones a terceros:** ninguna desde MATU. Si un día MATU envía el PIN por SMS, se agrega aquí.
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna con efectos sobre las personas. El bloqueo por PIN incorrecto es un control de seguridad.

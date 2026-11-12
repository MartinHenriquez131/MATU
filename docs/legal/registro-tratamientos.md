# Registro de tratamientos de MATU

**Estado:** borrador para el piloto académico, a la par de la política de privacidad v0.12 (MATU-61), aprobada por Jorge el 11-11 (MATU-94, 74-1). Lo redacta el analista normativo y lo aprueba Jorge Espinoza. Este documento no es asesoría legal.

Cada historia que empieza a tratar datos personales agrega aquí su entrada.

## 1. Alta de la persona cuidada y registro de su autorización (MATU-07)

- **Finalidad:** organizar su cuidado y la ficha de relevo (`plan_cuidado`).
- **Titulares:** la persona cuidada, y el usuario que da la autorización.
- **Datos:**
  - nombre y nombre de pila
  - nivel de apoyo, que es un **dato sensible**
  - dirección de entrega, opcional (MATU-61, D4): en `direccion`, unida por `persona_cuidada.direccion_entrega_id`. No se pide en el alta: se pide con el primer pedido y se guarda para los próximos. Calle, número, depto, comuna, región, etiqueta y referencia (hasta 200 caracteres, con una ayuda contra los datos de salud, C9), y `direccion.version` para el `ETag`. **Sin ubicación:** `lat` y `lng` siempre nulas, con un `CHECK` (C8). Al confirmar un pedido se copia a `pedido_entrega` (entrada 2)
  - la autorización: calidad, versión de la política, evidencia mínima y la referencia al documento si es representante legal
  - el retiro (MATU-44): `revocado_en` con `revocacion_motivo = retiro`, y en la auditoría `consentimiento.revocar`, quién y cuándo, sin nombre ni IP
  - el borrado (MATU-72): `revocado_en` con `revocacion_motivo = borrado` en las autorizaciones vigentes, `persona_cuidada.datos_borrados_en` y `eliminado_en`, y en la auditoría `persona.borrar`, quién y cuándo, sin nombre ni IP. El nombre, el nombre de pila, el nivel de apoyo y la dirección se borran en la misma transacción
- **Base de licitud:** consentimiento del titular o de su representante legal. Cuidadora o cuidador de hecho: [PENDIENTE: consulta legal].
- **Quién accede:**
  - administrador y cuidador ven todo
  - el pagador ve el nombre y la dirección
  - el observador ve el nombre
  - el estado de cada autorización (vigente, por renovar, retirada o borrada) y sus fechas los ven los cuatro roles. La calidad del otorgante, solo administrador y cuidador (MATU-44, decisión de Jorge del 06-11)
  - administrador y cuidador retiran cualquier autorización de la persona, sin importar quién la dio, y vuelven a darla. Pagador y observador reciben 404, y una política RLS por rol limita quién fija `revocado_en` (MATU-44, migración 0016)
  - administrador y cuidador borran los datos de la persona. Pagador, observador y otro grupo reciben 404. Una política RLS por rol lo limita (`app_retira_autorizacion()`) (MATU-72)
  - la dirección de entrega (MATU-61): administrador y cuidador la agregan, la cambian (`PUT …/personas-cuidadas/{persona_id}/direccion`, con `If-None-Match` o `If-Match`) y la vacían (`DELETE`, con `If-Match`). El pagador la ve en la persona y no la cambia (404). El observador no la recibe. Otro grupo, 404. No pide la autorización de pedidos, vigente, vencida, retirada o nunca dada (CJ8 de Jorge). Cada cambio y cada vaciado se audita como `direccion.cambiar`, sin el contenido (D12)
  - operación: [PENDIENTE: acotar a nombre y dirección en la historia de backoffice]
- **Conservación:** [PENDIENTE: plazo del registro de autorizaciones, también de las retiradas, en consulta legal]. Hoy no se borra (trigger `consentimiento_sin_borrado`). Después de un borrado, la autorización se conserva con su motivo. [PENDIENTE: plazo, CL-27] La fila de una persona borrada queda solo con su id, el grupo, las fechas y el valor fijo `borrada`, sin nivel de apoyo ni dirección, mientras existan los registros que la referencian. [PENDIENTE: plazo, CL-27] La dirección de entrega se guarda mientras la persona esté registrada, hasta que se vacía o se borra a la persona. Retirar la autorización de pedidos no la borra (CJ6 de Jorge). Vaciarla deja `persona_cuidada.direccion_entrega_id` en `null` y borra la fila de `direccion` si nadie más del grupo la usa.
- **Medidas:**
  - separación por familia con RLS forzado
  - la aplicación se conecta sin privilegios de dueño
  - registros técnicos sin datos de la persona
  - auditoría de solo inserción
  - consentimiento inalterable (migración 0006, ajustada en la 0016): solo se fijan `revocado_en` y `revocacion_motivo`, juntos y una vez, y nunca se borra
  - dar una autorización y retirarla queda limitado en la base a administrador y cuidador: una política RLS por rol rechaza que el pagador o el observador la registren (MATU-66, migración 0020) o la retiren (MATU-44, migración 0016)
- **Comunicaciones a terceros:** ninguna.
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna.

## 2. Pedidos y pagos de insumos (ADR-027, MATU-61, MATU-62)

> Aprobado por Jorge el 27-10 como diseño. Las frases sobre lo que el comercio ve o no ve se publican solo cuando la migración del sprint 4 (requisitos R7 a R9, arquitectura 18.1) las haga ciertas.

> ADR-027 (27-10), aprobado por Jorge.

> **Dos series «C» (MATU-94, 74-4):** desde el 11-11, las decisiones de Jorge sobre el contrato de MATU-61 se escriben **CJ1 a CJ10** (en `docs/api/README.md` del repositorio MATU_PROYECTO siguen como C1 a C10), y las condiciones del analista de la revisión previa de MATU-61 siguen como **C1 a C23**. Una «C» sin «J» es siempre del analista.

> MATU-61 (11-11): decisiones D1 a D12 de Jorge (`revision-previa-matu-61.md`, sección 7) y CJ1 a CJ10 del contrato (`docs/api/README.md` del repositorio MATU_PROYECTO, decisiones 188 a 222). MATU-61 llega hasta el total confirmado. El pago y el cargo son de MATU-62, y la preparación, la entrega y la vista del comercio, de MATU-63.

> MATU-62 (11-11): decisiones D-62-1 a D-62-17 y P-62-1 a P-62-9 del orquestador por delegación de Jorge (`revision-previa-matu-62-segunda.md`, sección 7) y decisiones 223 a 248 del contrato. Migración 0024. Se cobra en Webpay Plus, en el ambiente de integración de Transbank.

**Se trata solo con datos sintéticos.** Desde MATU-61 se arma el pedido y se confirma el total, con precios de ejemplo, comercios ficticios (`comercio.ficticio`, D9) y una consulta de stock simulada. Los pagos se harán solo en el ambiente de integración de Transbank (`figura-legal-piloto.md`, sección 5).

- **Finalidad:** pedir insumos a comercios en convenio, a precio exacto con IVA incluido, y cobrar una sola vez el total confirmado. MATU vende. En el piloto no se emite boleta (condiciones del pedido v0.2, D8).
- **Titulares:** el usuario que pide, quien paga (administrador o pagador, desde MATU-62), la persona cuidada a quien va el pedido, y la persona cuyo teléfono se anota como contacto si no es quien pide.
- **Datos:**
  - productos, cantidades, precios, envío y total. Cada línea guarda el precio y la oferta del carrito (`precio_carrito`, `oferta_carrito_id`), para marcar contra ellos un cambio de precio o de comercio al confirmar (C15), y una copia de `producto.retracto_pierde_al_abrir` (C3). Todos los precios llevan el IVA incluido. El historial de pedidos y de consumo de la persona cuidada se trata como **dato sensible**, porque junto con un dato que identifica puede revelar salud o dependencia (`investigacion-normativa-adr-027.md`, sección 3) [PENDIENTE: consulta legal sobre si los productos de un pedido son un dato relativo a la salud, CL-11 y CL-12]
  - **sin el nombre de la persona cuidada:** `pedido.destinatario_nombre_pila` sale en la migración de MATU-61 (R7, C16). El pedido se une a la persona por `persona_cuidada_id`
  - dirección de entrega y teléfono de contacto en `pedido_entrega`, copiados al confirmar el total desde la dirección de la persona (entrada 1) y desde el teléfono que se elige (D4). Sin `lat` ni `lng`, con un `CHECK` (C8). El teléfono es por omisión el celular verificado de quien confirma, editable, y si es el de otra persona la pantalla pide avisarle (CL-33)
  - la elección por producto si falta (RF-21): `otro_comercio` o `quitar`, nunca otra marca
  - la parte de cada comercio (`pedido_comercio`, D7): el comercio, su referencia opaca y sus líneas
  - la línea de tiempo (`pedido_transicion`), con un motivo de una lista cerrada (C19): `total_vencio`, `familia_cancela`, `familia_cambia_carrito`, `autorizacion_retirada` y `persona_borrada`
  - las condiciones del pedido aceptadas (`condiciones_version`, `condiciones_aceptadas_en` y `condiciones_huella`, SHA-256, D6). Las columnas se crean en MATU-61 y se escriben al pagar, en MATU-62. Un `CHECK` impide `pagado_en` sin `condiciones_aceptadas_en`
  - la autorización de pedidos (`consentimiento.finalidad = despacho`, D1), con la calidad, la versión de la política, la declaración `declaracion_pedidos_<calidad>` y su huella, y la revisión de 12 meses
  - el pago, desde MATU-62 (`cargo`, `participacion` y `transaccion_pasarela`): monto cobrado, monto devuelto por línea, código de autorización, tipo de tarjeta (crédito, débito o prepago), cuotas, últimos 4 dígitos, el token y la orden de la venta, su `session_id`, el motivo de cierre y la referencia corta del pedido (4 a 6 cifras). La venta queda atada al total y a su `total_confirmado_en`. `payload_respuesta` queda siempre vacío, con un `CHECK`. MATU nunca recibe ni guarda los datos de la tarjeta
  - quién aceptó las condiciones (`condiciones_aceptadas_por`, D-62-16), dentro del `CHECK` de las condiciones completas. No se guarda un correo para el comprobante: en el piloto no se envía (P-62-5)
  - `idempotencia` de `POST …/pedidos`, `…/confirmar`, `…/cambiar` y `…/cancelar` (con `Idempotency-Key`, arquitectura 9.4): solo el estado HTTP y el id del pedido, nunca el cuerpo (D5)
- **Base de licitud del pago (MATU-62):** ejecución de la compra que pide quien paga, que acepta las condiciones del pedido con su versión y su huella. [PENDIENTE: el artículo, en la consulta legal; ampliación de la CL-66]
- **Base de licitud:** consentimiento expreso y **separado** del de la ficha y del de consumo, solo para los pedidos: la finalidad `despacho` (D1). Se pide la primera vez que se toca «Pedir», lo dan el admin y el cuidador en la calidad de MATU-07, con `declaracion_pedidos_<calidad>` y su huella, y se revisa a los 12 meses. Sin la autorización `VIGENTE` según el `Reloj`, crear, ajustar, elegir la regla, confirmar, cambiar el teléfono y «Cambiar el pedido» responden 403 (C21). Leer, cancelar y la dirección no la piden. Se retira en Grupo familiar, por un medio igual de fácil que el usado para darla. La titular es la persona cuidada, y quién consiente sigue la calidad de MATU-07.
  - [PENDIENTE: consulta legal sobre si el art. 16 bis, inciso 1, limita el tratamiento aunque haya consentimiento, y si sirve como base su letra e), CL-11]
  - quién consiente por la persona mayor dependiente (arts. 12 y 16 c) se resuelve con MATU-07: calidad del otorgante y revisión a los 12 meses. Lo que quede abierto se une a la consulta del cuidador de hecho (decisión de Jorge, 27-10)
  - el teléfono de contacto de alguien que no es usuario: [PENDIENTE: consulta legal, CL-33 ampliada]
  - la evaluación de impacto del art. 15 ter se hace antes de operar con datos reales, sea obligatoria o no (decisión de Jorge, 27-10)
- **Quién accede:**
  - en el grupo (arquitectura, sección 11.2, con CJ3 de Jorge): administrador y cuidador arman, ajustan, eligen la regla, confirman, cambian el teléfono, usan «Cambiar el pedido» y cancelan sin pagar. El pagador ve el pedido, la entrega y el resumen, no confirma y no cancela, y paga desde MATU-62. **Pagan** el administrador y el pagador (D-62-8). El pago y el comprobante los leen el administrador, el cuidador y el pagador, el detalle de la tarjeta solo quien pagó, y el observador ve solo «Pagado» (D-62-2). Con un pago en curso nadie cambia el pedido (409 `pago-en-curso`, D-62-4 regla 1). Después de pagar, cancela solo el administrador. El observador ve el carrito sin la entrega ni el resumen (`PedidoVistaObservador`), y nunca la ficha. Otro grupo, 404
  - un solo pedido sin pagar por persona (C4)
  - el comercio, desde MATU-63, ve solo su parte (`pedido_comercio`): sus productos, su referencia del pedido y el código de retiro. **Ningún nombre**, ni la ficha, la dirección, el teléfono, las líneas de otro comercio ni el total de la familia (R8, D7). El comercio que reemplaza a otro ve lo mismo, solo con lo que le toca
  - operación ve pedidos y pagos para dar soporte (lee todos los pedidos, de todos los grupos, con su rol propio), y devuelve por anulación. Sus lecturas no se auditan, igual que las de la familia (decisión 52); sus escrituras sí. [PENDIENTE: CL-67, si las lecturas de operación de pedidos de otros grupos se deben registrar; se recomienda auditarlas en la historia del backoffice] Nunca la ficha ni el consumo de insumos
  - `sistema` (la vuelta de Transbank, sin grupo ni cuenta) y `matu_scheduler` (la conciliación) resuelven las ventas por funciones `SECURITY DEFINER` que devuelven solo ids
- **La consulta de stock no trata datos personales:** se hace al confirmar, **una por comercio**, y lleva solo productos, cantidades y una referencia opaca para apartar, **aleatoria por pedido y por comercio, nunca por familia** (C22). No lleva datos de la familia, de la persona cuidada ni de la dirección, y una prueba sobre el objeto de la consulta lo verifica.
- **Conservación:**
  - **lo que no se pagó** (`borrador`, total vencido y `cancelado` sin pago): se borra a los 30 días desde la última vez que cambió, desde que venció o desde que se canceló (C10), con una tarea del programador de MATU-74 que corre aunque los pedidos estén apagados, y con su línea de tiempo en cascada (D5). La copia de la entrega (`pedido_entrega`) se borra al cancelar. `idempotencia` se borra al vencer, a las 24 horas (D5). [PENDIENTE: CL-28 ampliada]
  - **lo que se intentó pagar y no se cobró** (D-62-13 c): el cargo y sus transacciones se borran con el pedido a los 30 días. **Un cobro anulado completo** se conserva 6 años, con el pedido sin entrega, el cargo y sus transacciones, y se borran las líneas, las reglas, la línea de tiempo y las partes por comercio. [PENDIENTE: CL-64]
  - pedidos pagados y comprobantes de entrega, 2 años. Pagos y boletas, 6 años, por obligación tributaria (arquitectura, sección 11.8). [PENDIENTE: CL-28]
  - **retiro de la autorización de pedidos** (D1): en la misma transacción, los pedidos sin pagar de la persona pasan a `cancelado` con motivo `autorizacion_retirada`, se borra su `pedido_entrega` y se registra un `pedido.cancelar` por pedido. Si cancelar falla, se deshace también el retiro. Los pagados siguen su plazo [PENDIENTE: CL-44]. Desde MATU-62, un pago en curso que se aprueba después del retiro se anula completo el mismo día (D-62-4, regla 3). La dirección de la persona se conserva (CJ6 de Jorge)
  - **borrado de la persona** (MATU-72, D2): retira también la autorización `despacho` y, en la misma transacción, cancela los pedidos sin pagar con motivo `persona_borrada` y borra su `pedido_entrega`. Desde MATU-62 y MATU-63: los pedidos cerrados quedan solo con la comuna, y los pagados en curso conservan la dirección hasta cerrarse. Productos y montos siguen su plazo, sin verse después del retracto. En MATU-61 aplica solo la regla de los sin pagar. [PENDIENTE: CL-52 y CL-44]
  - con la capa 3 apagada, el retiro y el borrado cancelan igual los pedidos sin pagar y borran su `pedido_entrega`, en la misma transacción (MATU-94, decisión 250, que corrige CJ2). Solo con la capa 3 quitada (sin el paquete `ordering`, ADR-002) no los tocan, y la capa se quita solo en una base sin pedidos (arquitectura, ADR-002)
- **Medidas:**
  - separación por familia con RLS forzado, también en `pedido_comercio`
  - el comercio ve un pedido solo cuando está pagado y enviado, y nunca la dirección, que vive en una tabla aparte. Las políticas de `pedido_comercio` y `pedido_linea` por `pedido_comercio.comercio_id` van en la migración de MATU-61, con sus pruebas en `test_aislamiento.py` (D7)
  - el precio pagado queda fijo en la base desde el pago, y lo devuelto nunca supera lo cobrado
  - la regla si falta un producto queda fija al pagar, con un trigger, y solo el admin y el cuidador la escriben, con políticas por operación (C12 y C13)
  - registro de transacciones de pasarela que nunca se borra mientras tenga dinero (D-62-13). Solo `sistema` u `operacion` marcan un pedido `pagado`, con una venta aprobada y no anulada del mismo total. Una sola venta aprobada por cargo, el token es único y una línea se devuelve una sola vez. `matu_app` no puede borrar `cargo` ni `participacion`
  - el token, la orden de la venta, el `session_id`, la respuesta de Transbank y el correo nunca en logs: la vuelta registra solo el caso (decisiones 235 y 247)
  - la política de contenido de la aplicación solo deja enviar el formulario a las dos direcciones de Webpay. El token de la vuelta se limpia de la URL con `history.replaceState` y vive solo en memoria
  - la proyección del comercio excluye `grupo_id`, `persona_cuidada_id`, `creado_por`, las transiciones y todo identificador de la familia y de la persona, con una prueba de contrato (C16). El nombre de pila sale del pedido en la migración de MATU-61. [PENDIENTE: la vista del comercio y su prueba de contrato se construyen en MATU-63. Hasta entonces, revisar que el comercio no pueda leer `grupo_id`, `persona_cuidada_id`, `creado_por`, el `total`, el `costo_envio` ni las transiciones, ni escribir `monto_devuelto`. Hoy `pedido_comercio_ver` le deja leer la fila completa de `pedido` una vez enviado: se acota por columnas en MATU-63 (cierre del analista de MATU-61)]
  - productos, cantidades, precios, dirección, referencia y teléfono nunca en logs, errores, eventos, auditoría ni URL, con `Cache-Control: no-store` en todas las respuestas del pedido y de la dirección (C17)
  - el carrito vive en el servidor como borrador, nunca en `localStorage`, `sessionStorage` ni la URL (C18)
  - el servidor no lee `perfil_consumo` para crear el pedido, y el pedido no suma al consumo (C20, CL-17 no se activa)
  - auditoría de solo inserción, sin contenido (D12): `consentimiento.otorgar` y `consentimiento.revocar` de `despacho`, `direccion.cambiar`, `pedido.crear`, `pedido.confirmar`, `pedido.cancelar` y `pedido.regla_faltante`, y desde MATU-62 `pago.iniciar` (quien paga), `pago.aprobar` y `pago.anular` (el sistema), con la entidad `cargo`, sin montos ni datos de la pasarela (decisión 244). Las lecturas no se auditan (decisión 52): la línea de tiempo la da `pedido_transicion`
  - el total confirmado vale 15 minutos según el `Reloj`, y la pantalla avisa 2 minutos antes y ofrece volver a confirmar sin perder el carrito (C23)
- **Comunicaciones a terceros:**
  - comercios en convenio, con lo que dice "Quién accede". **La dirección nunca llega al comercio.** MATU trata al comercio como si fuera encargado, sea o no un dato personal para él la referencia del pedido, y el convenio lleva siempre las cláusulas del art. 15 bis (decisión de Jorge, 27-10). El primer convenio real debe autorizar a publicar el nombre de fantasía, los precios y el stock (D9)
  - quien despacha, que ve la dirección, el teléfono de contacto y el paquete: **encargado** de MATU, con contrato según el art. 15 bis (instrucciones, confidencialidad, seguridad, reporte de vulneraciones y supresión al terminar)
  - Transbank, que procesa el pago en su propia página. Recibe de MATU solo el monto, una orden que no identifica a nadie y un `session_id` aleatorio. La devolución vuelve a la misma tarjeta, por anulación de Webpay Plus, sin pedir datos nuevos. Débito y anulación parcial verificados el 10-11 en integración (MATU_PROYECTO #77). [PENDIENTE: su rol, CL-56]
  - el proveedor de correo, cuando el comprobante se envíe (después de MATU-91). [PENDIENTE]
  - los reclamos de un pedido llegan al buzón (entrada 11, D8)
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** la anulación automática de un pago aprobado cuando el pedido ya cambió, se canceló o se retiró la autorización (D-62-4, regla 3). Siempre devuelve el total completo a la misma tarjeta, el mismo día, y se le muestra a quien pagó. [PENDIENTE: CL-65] Al confirmar, MATU mueve un producto que falta al comercio de menor precio solo si la familia eligió buscarlo en otro comercio (CJ5 de Jorge), y lo muestra antes de pagar.

## 3. Ficha de relevo (MATU-09, MATU-11 a MATU-14, MATU-50)

> Aprobado por Jorge el 27-10 como diseño. Desde MATU-44, retirar la autorización de la ficha corta en la misma transacción los accesos de relevo que todavía abrían.

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
  - mientras la autorización esté vigente y hasta 90 días después de que se retire o termine. En ese plazo nadie la lee: la API responde 403 a todos los roles y el relevo, 410
  - el borrado se cumple destruyendo la clave de la persona (borrado criptográfico de MATU-11). Lo hace la tarea `tarea_destruccion` (función `plan_destruir_claves`, migración 0016) con las fichas cuya autorización se retiró hace 90 días o más: destruye la clave y, en la misma transacción, borra el texto cifrado y las filas de las secciones de esa persona, con `clave.destruir` en la auditoría. La corre el programador de tareas cada madrugada, en hora de Chile (MATU-74), conectado como `matu_scheduler`, el único rol que puede llamar a `plan_destruir_claves` desde la migración 0022. Si una corrida falla, la siguiente destruye lo pendiente. Desde el día 90 nadie puede leer ni recuperar la ficha, aunque la tarea no haya corrido, porque una autorización nueva destruye primero la clave y borra lo cifrado con ella. La ficha empieza en blanco y la primera escritura crea una clave nueva, que solo puede existir después de esa autorización (índice `clave_datos_vigente_uq` y trigger `clave_datos_nueva_tras_autorizacion`).
  - una solicitud de borrado no espera los 90 días (decisión de Jorge del 07-11, MATU-72): en la misma transacción de la petición se destruye la clave, se borran las filas de `plan_seccion` y el plan queda en 0 de 3, con `clave.destruir` y `persona.borrar` en la auditoría
  - copias de respaldo: [PENDIENTE: plazo, CL-29]. La auditoría `persona.borrar` sirve de lista para volver a borrar antes de usar una copia restaurada
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
  - desde la aplicación, la clave de la persona solo admite las dos escrituras del cifrado, y solo de administrador y cuidador: crearla y destruirla. La aplicación no la borra ni cambia la clave maestra que la protege. Ese cambio, cuando se pase al servicio de custodia, irá por una función propia de la base (MATU-66, migración 0020)
- **Comunicaciones a terceros:**
  - solo al relevo, con lo que dice la entrada 4
  - dictado: si quien escribe usa el micrófono, el reconocimiento de voz lo hace el servicio del navegador (en Chrome, Google), que recibe el audio. MATU no lo recibe ni lo guarda. En Sus remedios el dictado está desactivado hasta la respuesta legal (decisión de Jorge del 03-11). [PENDIENTE: consulta legal sobre el envío de audio de un dato sensible, nombrar los servicios y sus países]
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna.

## 4. Acceso de relevo (MATU-09, MATU-18 a MATU-20, MATU-23, MATU-25)

> Aprobado por Jorge el 27-10 como diseño. Desde MATU-44, retirar la autorización de la ficha corta en la misma transacción los accesos de relevo que todavía abrían.

**Todavía no se trata con datos reales.** Durante el semestre los accesos se crean solo con datos sintéticos (`figura-legal-piloto.md`).

- **Finalidad:**
  - dar un acceso temporal, de solo lectura, a los tres campos de la ficha y a las secciones adicionales que marque quien comparte (`remedios` viene sin marcar), y que se puede cortar en cualquier momento. Registra qué secciones se mostraron en cada apertura, sin su contenido
  - el teléfono del relevo sirve para que quien comparte le envíe el enlace desde su propio teléfono, con la aplicación de mensajes que elija, y para que la familia pueda contactarlo. MATU no envía mensajes
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
  - la auditoría de quien crea (`relevo.compartir`) y de quien corta (`relevo.revocar`) cada acceso: la fecha, el usuario, el identificador del acceso y, al crear, el motivo de la lista cerrada. Sin el nombre ni el teléfono del relevo, sin IP, sin el token y sin el PIN
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
  - si la autorización de la persona está en pausa porque venció la revisión anual, la presentación, el canje y la ficha responden 410 `relevo-pausado` sin decir el motivo, y el canje no cuenta como intento (decisión 33). Vuelve a abrir al renovarse, si el acceso no venció
  - si la autorización se retira (MATU-44), en la misma transacción se cortan todos los accesos que no vencieron ni se cortaron, incluidos los bloqueados y los en pausa (`acceso_relevo.revocado_en` e `indice_token.revocado_en`), con un `relevo.revocar` por acceso y el mismo `request_id`. Responden 410 `relevo-revocado` y no vuelven a abrir, aunque se autorice de nuevo. Los plazos de 3 años y de 30 días corren desde el corte
  - al borrar los datos de la persona (MATU-72) se cortan los accesos como en el retiro, con un `relevo.revocar` por acceso, y se anonimiza `nombre_pila_persona`. Los plazos de 3 años y 30 días corren desde el corte
  - cortar un acceso no exige autorización vigente (204 idempotente)
  - la sesión del relevo no fija el grupo
  - vigencia de 24 horas por omisión y de 30 días como máximo
  - cabeceras `no-store`, `no-referrer` y `noindex`
  - nunca token, PIN ni texto de la ficha en los logs
  - la app de la familia guarda el PIN y el enlace solo en la memoria de la pantalla, los muestra una vez y nunca copia el PIN al portapapeles ni lo pone en el mensaje. El enlace se envía con la hoja de compartir del teléfono o copiándolo, nunca con el token en la dirección de un servicio de terceros (MATU-48)
  - nombre y teléfono del relevo sin autocompletado del navegador
  - sin impresión ni exportación de la ficha (ADR-029)
  - la base limita por rol quién escribe los accesos (MATU-66, migración 0020): administrador y cuidador los crean, los cortan y anonimizan el nombre de pila de la persona; el pagador con permiso solo los lee; el relevo solo actualiza los contadores de su acceso vigente. La aplicación no puede cambiar el teléfono, el PIN, los campos habilitados ni el vencimiento de un acceso, ni borrar un acceso o su token. Un acceso o un token cortado no se reabre ni cambia la fecha de su corte, y ningún vencimiento se alarga: un trigger lo rechaza para todos los roles de la base, también el dueño (MATU-47, migración 0020)
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
  - unidades por envase (`unidades_por_envase`, opcional, de 1 a 10.000; describe el envase, no a la persona; MATU-60);
  - stock y fecha del stock (la fija el servidor);
  - días de aviso y fecha estimada;
  - preferencias de aviso por persona: tipo de aviso, canal y si está activo (`preferencia_notificacion`);
  - registro de avisos (`notificacion`): persona, grupo, evento, canal, plantilla, estado, fechas y un código de error de una lista cerrada. **Sin destino ni contenido**;
  - si se sigue o no, y la versión.

  Se trata como **dato sensible**. [PENDIENTE: consulta legal sobre si es dato relativo a la salud y si basta RLS sin cifrado (decisión 63)]
- **Base de licitud:** consentimiento separado, `finalidad = consumo`, en la misma calidad de MATU-07, con la declaración `declaracion_consumo_<calidad>` (aprobadas por Jorge el 03-11) y la revisión de 12 meses. Sin él, 403. Cuidador de hecho: [PENDIENTE: consulta legal]. Se retira en la aplicación (MATU-44): en ese momento deja de calcular, de crear alertas y de avisar, y las alertas abiertas se descartan con `alerta.descartar`. El consumo queda sin lectura y se borra a los 90 días con `consumo_conservar`, que corre cada madrugada con el programador de tareas (MATU-74). Si se vuelve a autorizar antes del día 90, lo anotado vuelve. Desde el día 90, una autorización nueva borra primero los perfiles de la persona, aunque la tarea no haya corrido (decisión 128). El borrado a pedido (MATU-72) borra en el acto los perfiles, y con ellos las alertas y las compras, por `ON DELETE CASCADE`, sin esperar `consumo_conservar` ni `quiebre_conservar`.
- **Quién accede:**
  - admin y cuidador leen y escriben (en la API y en una política RLS de escritura);
  - pagador y observador solo leen (decisión de Jorge del 03-11);
  - operación nunca, tampoco el registro de avisos (`notificacion`): la migración 0022 quitó la política que se lo permitía.
- **Conservación:**
  - mientras la autorización esté vigente y hasta 90 días después, también los insumos que no se siguen;
  - eliminar un insumo lo borra en el acto;
  - el consumo se **borra**, porque no hay clave que destruir (decisiones de Jorge del 03-11);
  - borrado a pedido (MATU-72): en el acto, los perfiles y con ellos las alertas y las compras (`ON DELETE CASCADE`). El registro de avisos (`notificacion`) sigue su plazo de 90 días, sin destino ni contenido;
  - copias de respaldo: [PENDIENTE: plazo, CL-29].
- **Medidas:**
  - RLS forzado por grupo y escritura por rol en RLS;
  - `ETag`/`If-Match` (412/428);
  - `nombre_libre` nunca en logs, errores, auditoría ni eventos;
  - auditoría de solo inserción de `consumo.crear`, `consumo.editar`, `consumo.desactivar`, `consumo.activar`, `consumo.eliminar`, `consentimiento.otorgar` y `consentimiento.revocar`, sin nombre, cantidades ni IP;
  - los eventos llevan solo identificadores;
  - nada en el almacenamiento del navegador ni en la URL;
  - RLS separada de `alerta_quiebre` y `reposicion` (MATU-37): leen los cuatro roles; solo el rol sistema crea alertas; solo admin y cuidador las cierran o declaran una compra; nadie las borra a mano; la API no expone las compras (sin ruta de lectura, MATU-51) y la conservación las borra con `quiebre_conservar`, solo como `matu_owner` con `app.rol = 'operacion'` (migración 0017);
  - auditoría de `alerta.materializar`, `alerta.resolver`, `alerta.descartar` y `reposicion.declarar`, sin nombre, cantidades ni IP;
  - el aviso por push o correo es un texto fijo sin nombres de personas ni de insumos, y su enlace no lleva identificadores. El correo va sin seguimiento de aperturas ni de clics. El push va sin contenido (RFC 8030 con VAPID, decisión 50 del contrato): el servicio de push solo recibe la dirección de avisos y el teléfono muestra el texto fijo
  - antes de cada envío, en cada intento y en cada canal, se revisa que la autorización de `consumo` esté `VIGENTE` según el `Reloj` (no retirada y con la revisión de 12 meses al día), que la alerta siga abierta con su perfil, que la membresía y el usuario sigan activos, y que el canal esté activo y tenga destino. Si algo falla, el aviso queda `omitida` con su código (MATU-41, decisión 107)
  - el correo es el canal garantizado y el push va además, cada uno solo si la persona no lo apagó, desde las 9:00 hora de Chile. La preferencia es de la persona, por canal, y vale para todos sus grupos (`GET/PUT /v1/yo/avisos`, decisión 111). Un canal que la persona no eligió usa el valor por omisión de su rol en cada grupo: avisa a admin y cuidador, y al pagador y al observador solo si lo activan. El `PUT` guarda solo el canal que la persona cambia (decisión de Jorge del 04-11)
  - los logs nunca llevan el email, el `push_token` ni el texto. En todo entorno, el registro de cada aviso, también del envío simulado, es su fila de `notificacion` (estado, `enviada_en`, canal y plantilla), con su plazo de 90 días (MATU-74, hallazgo H4). El envío simulado (`ENVIADOR_AVISOS=simulado`) solo carga con `ENTORNO` `local`, `pruebas` o `staging`, con datos sintéticos, y nunca en producción. Solo en `local` y en `pruebas` escribe además un archivo de desarrollo (`REGISTRO_AVISOS`, por omisión `.dev/avisos.jsonl`) con la hora, `notificacion_id`, `usuario_id`, el canal y la plantilla, sin destino ni texto, que se conserva como máximo 90 días desde que se escribe (política, sección 8; decisión de Jorge del 05-11). En staging y en la demostración no se escribe ningún archivo (decisión D3-b de Jorge del 09-11)
- **Lista de insumos (MATU-60):**
  - Finalidad: armar, con los insumos que hoy se acaban pronto (los que aparecen en «Se acaban pronto», calculados al momento), una lista para que la familia compre donde quiera, sin depender de la capa 3 (RF-09, RF-14 y RF-15; ADR-002; ADR-027, punto 2; ADR-031).
  - Datos: nombre del producto o `nombre_libre`, días hasta la fecha estimada (solo en pantalla) y cantidad sugerida (lo que falta para cubrir 30 días, descontando lo que MATU estima que queda hoy y como mínimo 1, redondeado hacia arriba a envases enteros si se conocen las unidades por envase, o en la unidad del insumo si no), calculados en cada petición. Sin el nombre de la persona cuidada, la ficha, el nivel de apoyo, la dirección, el grupo, la tasa, el stock, precios ni comercios. El texto que se imprime o se comparte no lleva los días.
  - No se guarda nada nuevo en el servidor. Los ítems agregados a mano y las cantidades cambiadas viven solo en la memoria de la página y nunca llegan al servidor.
  - Base de licitud: la misma autorización de `consumo`, `VIGENTE` según el `Reloj` (no retirada y con la revisión de 12 meses al día). Sin ella, 403. [PENDIENTE: consulta legal sobre si la declaración de consumo debe nombrar la lista y su salida antes de la versión 1.0]
  - Quién accede: los cuatro roles leen la lista. Administrador, cuidador y pagador la imprimen o la comparten desde la interfaz, y el observador solo la ve (decisión de Jorge del 06-11). Operación nunca. Otro grupo recibe 404.
  - Comunicaciones a terceros: ninguna por parte de MATU. La impresión, el PDF, la hoja de compartir del teléfono (`navigator.share`, solo con texto) y el portapapeles los usa la persona desde su dispositivo, con el destinatario que ella elige. MATU no lo conoce.
  - Medidas: `Cache-Control: no-store`. Nada de la lista en el almacenamiento del navegador, la URL, `history.state` ni `document.title` (al imprimir, el título es solo «Lista de insumos»). La impresión oculta todo salvo la lista y el distintivo del piloto. Ninguna otra pantalla de la app se imprime, tampoco la ficha ni la página del relevo: sale solo «Esta pantalla no se imprime.» (ADR-029). Aviso en pantalla antes de compartir. `nombre_libre` nunca en logs, errores ni eventos. Usa las políticas RLS que ya existen para `perfil_consumo` y `alerta_quiebre`, sin cambios.
  - Auditoría: no se registra que se imprimió o se compartió, porque el navegador no lo confirma y un registro de intención no prueba nada. Las lecturas del consumo tampoco se auditan (decisión 52).
  - Conservación: no aplica en el servidor. Las copias que salen del teléfono no las alcanzan ni el borrado del insumo ni el retiro de la autorización, y la política lo informa.
  - Decisiones automatizadas: ninguna. La cantidad es una sugerencia que la familia cambia.
  - «Pedir estos productos» (MATU-61, D10): un botón al final de la lista, visible solo con la autorización de pedidos (`despacho`) vigente, para el admin y el cuidador. Pasa al pedido solo las líneas con producto del catálogo, con la cantidad que se ve en pantalla convertida a envases del catálogo, y nombra las demás. Para eso cada línea de la lista suma `producto_id`, o `null` si se anotó con `nombre_libre`: es una lectura del consumo de quien ya ve la lista. La pantalla arma el pedido con los `oferta_id` del catálogo, y **el servidor no lee `perfil_consumo` para crear el pedido** (C20), así no se mezclan las finalidades y la CL-17 no se activa. Sin la autorización, la lista se imprime y se comparte como antes, y el botón lleva a pedirla. La lista y el aviso nunca hacen un pedido solos (entrada 2).
- **Alertas y compras declaradas (MATU-37, MATU-51):**
  - alertas: insumo (por su identificador), fecha estimada, estado y cuándo se avisó y se cerró. Sin nombre del insumo ni cantidades;
  - compras declaradas con «Ya lo resolví» o con «Compré» (MATU-51), haya alerta o no: cantidad, fecha (la fija el servidor) y quién la anotó; se suman a lo que quedaba. «Me quedan N» corrige el stock como la edición del insumo y no crea una compra. Anotan solo admin y cuidador; pagador, observador y otro grupo reciben 404. Auditoría: `reposicion.declarar`, `consumo.editar`, `alerta.resolver` y `alerta.descartar`, sin cantidades. Un pedido entregado por MATU no suma el stock todavía: queda para MATU-62 y MATU-63, con versión nueva de la política (decisión C de Jorge del 07-11). MATU-61 no lo hace: el pedido no lee ni escribe el consumo (C20);
  - el trabajo diario (rol sistema) crea las alertas solo para personas con la autorización de insumos vigente;
  - las tareas programadas se conectan con roles de base propios desde la migración 0022 (MATU-74), sin privilegios de dueño ni BYPASSRLS. `matu_scheduler` recorre los grupos (lee solo el identificador y el estado de cada grupo activo) y es el único que puede llamar a las funciones de borrado por plazo. `matu_publisher` es el único que puede tomar y cerrar los eventos de la cola de avisos. La API (`matu_app`) ya no puede llamar a ninguna de esas funciones. El trabajo grupo por grupo sigue con `matu_app` y el rol sistema, dentro del aislamiento por fila;
  - conservación: alertas cerradas 90 días desde que se cierran, eventos publicados 30 días, registro de avisos (`notificacion`, enviados, omitidos y fallidos) 90 días desde `creada_en`, compras declaradas 90 días desde que se anotan (decisión A de Jorge del 07-11, MATU-51, migración 0017; antes, mientras existiera el insumo). Eventos que no se pudieron procesar: 30 días desde `fallido_en` (decisión de Jorge del 04-11, MATU-41).
- **Comunicaciones a terceros:** **en el semestre el envío es simulado y no sale de la máquina (MATU-41, decisión 112).** Cuando entre un proveedor real, el proveedor de correo recibirá el email del destinatario y el texto fijo del correo (remitente, asunto, cuerpo, enlace a la raíz de la aplicación y pie), sin identificadores internos y sin seguimiento de aperturas ni clics. El servicio de push, que elige el navegador y no MATU, recibirá solo el `push_token` y un push sin contenido (decisión 50). El proveedor de correo será encargado de MATU, con contrato de encargo. [PENDIENTE: nombrarlo, su país y el contrato]. [PENDIENTE: consulta legal sobre la calidad del servicio de push del navegador y la transferencia internacional]. Antes de activarlo: versión nueva de la política, MATU-55 en `main`, verificación del email y la preferencia resuelta. **Decisiones automatizadas:** ninguna. La fecha es una estimación informativa y la alerta nunca genera un pedido.

## 6. Cuenta, sesión y dispositivos (MATU-38)

- **Finalidad:** mantener la sesión, permitir sacar un dispositivo, detectar el robo de una sesión, limitar los intentos de entrada y la creación de cuentas desde una misma IP (MATU-25), y enviar avisos.
- **Titulares:** las personas usuarias, y quien intenta entrar o crear una cuenta (que puede no ser usuaria).
- **Datos:**
  - sesión: SHA-256 del refresh, emisión, vencimiento, revocación y motivo;
  - dispositivo: nombre general sin agente de usuario, creación, último uso y `push_token` opcional;
  - huella HMAC de la IP y del email en Redis, por 1 hora;
  - huella HMAC de la IP en el contador de creación de cuentas (`usuarios-ip`, 5 por hora, ventana fija de 1 hora; MATU-25, decisión 114). La IP no llega a Redis, a los logs, a la auditoría ni a la respuesta 429;
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
  - el `push_token`, al cerrar o sacar el dispositivo, al desactivar los avisos en él, o cuando el servicio de push dice que la suscripción ya no existe (MATU-41);
  - los contadores, en 1 hora.
- **Medidas:**
  - cookie `HttpOnly`, `Secure`, `SameSite=Strict` y `Path=/v1/sesiones`;
  - access token en memoria, por 15 minutos;
  - rotación con detección de reutilización;
  - `no-store`;
  - push sin contenido (el texto fijo lo pone el service worker), sin datos de personas ni de insumos, y con una lista cerrada de hosts.
  - la aplicación no puede leer la contraseña transformada ni el secreto del doble factor de ninguna cuenta. Al entrar, obtiene solo la contraseña transformada de la cuenta que está entrando, con una función de la base que nunca la entrega a operación ni a otra persona del grupo. Operación lee las cuentas solo para dar soporte (email y celular, entrada 7), y no las crea, no las cambia ni las borra. Una cuenta tampoco puede darse permisos de operación, cambiar su estado ni borrarse desde la aplicación (MATU-66, migración 0020)
- **Comunicaciones a terceros:** el servicio de push del navegador recibirá solo el `push_token` y un push sin contenido (decisión 50). El texto fijo lo muestra el service worker de la aplicación. En el semestre el envío es simulado (MATU-41). [PENDIENTE: nombrarlos y su país]. **Decisiones automatizadas:** ninguna. La espera después de varios intentos es un control de seguridad.

## 7. Celular de la cuenta (MATU-39, MATU-57)

- **Finalidad:** enviar un código para recuperar la contraseña o confirmar el celular (MATU-57). El celular se confirma con un código antes de usarlo para recuperar (decisión de Jorge del 03-11).
- **Titulares:** las personas usuarias.
- **Datos:**
  - celular en formato E.164 (`+569XXXXXXXX`), obligatorio al crear la cuenta (decisión de Jorge del 03-11);
  - `celular_verificado_en`: cuándo se confirmó con un código. Vuelve a vacío si cambia el número, para que un número nuevo nunca herede la confirmación;
  - `celular_canal`: la preferencia de canal (`sms` o `whatsapp`, por omisión `sms`), que se elige al confirmar. En el semestre el envío es simulado y siempre como SMS; la preferencia se guarda para cuando haya un proveedor.
- **Base de licitud:** ejecución del servicio que pide la persona.
- **Quién accede:** la propia persona, que ve el número enmascarado (`+56 9 •••• ••37`) y si está confirmado, y operación para soporte. No lo ven las otras personas del grupo.
- **Conservación:** mientras exista la cuenta. [PENDIENTE: plazo tras eliminar la cuenta]
- **Medidas:** nunca en logs, errores, auditoría ni eventos. La auditoría registra `cuenta.celular_solicitar`, `cuenta.celular_verificar` y `cuenta.celular_verificar_fallido`, sin el número ni el canal.
- **Comunicaciones a terceros:** ver la entrada 8.

## 8. Recuperación del acceso y confirmación del celular (MATU-57)

- **Finalidad:** comprobar que quien pide recuperar la cuenta es su titular y permitirle cambiar la contraseña, y confirmar que el celular de la cuenta es de su titular.
- **Titulares:** las personas usuarias, y quien pide un código con un email (que puede no ser usuaria).
- **Datos:**
  - el email que escribe la persona (nunca se pide el celular para recuperar);
  - por cada código, en Redis y nunca en la base: la huella HMAC del código (pepper propio), su vencimiento, el canal (celular o correo) y los intentos. Al usarse se borra;
  - las huellas HMAC de la IP, del email, del celular y de la cuenta en los contadores de envíos, y de la IP, del email y de la cuenta en los contadores de intentos fallidos.
- **Base de licitud:** ejecución del servicio que pide la persona. Para los contadores por huella: [PENDIENTE: consulta legal], como en la entrada 6.
- **Quién accede:** nadie ve el código. Operación ve solo eventos de auditoría (`cuenta.recuperar_solicitar`, `cuenta.recuperar_verificar_fallido`, `cuenta.contrasena_cambiar`) sin datos de contacto, código ni IP.
- **Conservación:** el código, hasta usarse o 10 minutos. Los contadores de envíos, 1 hora y 24 horas. La auditoría, según la entrada de auditoría.
- **Medidas:**
  - código de 6 dígitos, de un solo uso y con 5 intentos como máximo; pedir uno nuevo invalida el anterior;
  - por email, celular y cuenta: 60 segundos entre envíos, 3 por hora y 10 al día. Por IP: 20 por hora y 50 al día, sin espera entre envíos porque varias personas pueden compartirla;
  - la misma respuesta exista o no la cuenta, y aunque se haya alcanzado el límite;
  - el celular se usa solo si está confirmado; si no, el email;
  - al cambiar la contraseña se cierran todas las sesiones, se invalidan los códigos pendientes y se avisa por el otro canal (por el correo si el celular no está confirmado). Un acceso ya emitido puede seguir válido hasta 15 minutos;
  - nunca el código, el celular, el email ni la IP en logs, errores, auditoría ni eventos;
  - en el semestre el envío es simulado: no sale de la máquina y solo se admite con ENTORNO local, pruebas o staging (decisión 105), con datos sintéticos. Si se define `REGISTRO_ENVIOS`, el adaptador simulado escribe el destino y el código en claro en un archivo JSON Lines de `.dev/`. Es un registro de desarrollo: nunca existe en producción, y en staging no debe quedar accesible desde fuera del servidor (revisión de Martín, P3-2). En staging, `REGISTRO_ENVIOS` apunta a `/tmp/matu-envios.jsonl`, dentro del contenedor. La API no lo sirve, se lee solo con `railway ssh` y se borra en cada despliegue, y a más tardar con el cierre de staging (MATU-25).
- **Comunicaciones a terceros:** los proveedores de SMS, WhatsApp y correo, como encargados con contrato. Reciben solo el destino y el texto del mensaje. En el semestre el envío es simulado, sin proveedor real (decisión de Jorge del 03-11). [PENDIENTE: nombrarlos y su país]
- **Transferencia internacional:** [PENDIENTE: proveedor, país y garantía]. Requiere consulta legal.
- **Decisiones automatizadas:** ninguna. La espera después de varios intentos es un control de seguridad.

## 9. Ambiente de staging (MATU-25)

- **Finalidad:** probar MATU por HTTPS y mostrarlo en la demostración del semestre.
- **Proveedor y lugar:** Railway, región `sfo` (California, Estados Unidos), para la API, PostgreSQL 16 y Redis. Anotado el 05-11 en `infra/railway/README.md` del repositorio MATU_PROYECTO. Railway trata estos datos por encargo de MATU. [PENDIENTE: revisar las condiciones de servicio y el acuerdo de tratamiento de datos de Railway]
- **Datos:** solo sintéticos: la semilla de `infra/semillas/demo.py` y cuentas con correos de dominios reservados, lo único que acepta el registro en staging (decisión 105). Datos reales que existen igual:
  - la dirección IP de quien abre staging (el equipo y quien pruebe la demostración), que la API usa solo en memoria para su huella HMAC;
  - las huellas en Redis: 1 hora, y 24 horas como máximo en la recuperación del acceso;
  - los registros HTTP de la plataforma Railway, que guardan la IP de cada conexión (campo `srcIp`, confirmado por Martín el 05-11) [PENDIENTE: su plazo en el plan Hobby];
  - las cuentas de Railway de Jorge y Martín;
  - el registro de la aceptación de la política de las cuentas del equipo (entrada 10).
- **Medidas:** HTTPS terminado por Railway; KEK y secretos nuevos y propios de staging, rotados el 05-11 sin pasar por un chat, solo como variables secretas de Railway, con acceso solo de Jorge y Martín con autenticación en dos pasos (decisión 105, g y h); la API se conecta como `matu_app`; logs JSON sin IP, cuerpo, token ni PIN, verificado con grep tras el e2e (05-11); registro simulado de los códigos de recuperación (`REGISTRO_ENVIOS`) en `/tmp` del contenedor de la API; tareas programadas (MATU-74): tres servicios cron de Railway. Los borrados (destrucción de fichas, conservación del consumo y de las sesiones) corren a las 06:00 UTC y el trabajo diario de quiebres a las 08:00 UTC, de madrugada en Chile todo el año y con dos horas entre uno y otro. El publicador de avisos corre cada 5 minutos, el mínimo de Railway. Los borrados llaman a sus funciones como `matu_scheduler`. Los quiebres recorren los grupos como `matu_scheduler` y hacen el trabajo de cada grupo como `matu_app`. Los avisos toman la cola como `matu_publisher` y envían como `matu_app`. La API nunca recibe las conexiones de `matu_scheduler` ni de `matu_publisher`. Los tres cron reciben `ENTORNO`, `POLITICA_VERSION`, `DATABASE_URL` y la conexión de su rol con su contraseña, y el de avisos además `ENVIADOR_AVISOS` y `ORIGEN_WEB`. Ninguno recibe la KEK ni otros secretos, y el de avisos no escribe archivos (decisión D3-b). El log de cada corrida guarda el nombre de la tarea, un identificador al azar de la corrida, la hora de inicio y de fin, la duración, el resultado, los contadores y el tipo de error. El publicador agrega, por cada aviso, los identificadores internos del aviso y del evento, el canal y el estado (MATU-41). Nunca guarda identificadores de personas ni de grupos, mensajes de error, trazas ni datos de las filas. Mientras no exista un aviso automático de fallas (política, sección 13), Martín revisa a diario el historial de corridas de los tres cron (decisión D6 de Jorge del 09-11). Limitación declarada: la KEK y los respaldos con las claves envueltas quedan en el mismo proveedor.
- **Diagnóstico temporal del proxy (MATU-25, decisión 114, punto 7):** mientras se verifica `PROXY_SALTOS`, una línea de log por petición con la cantidad de cabeceras y de elementos del X-Forwarded-For y la clase de cada uno (interna, privada, pública o inválida), con el `request_id` y sin IP, usuario ni grupo. Apagado por omisión, no carga en producción. Las fechas de encendido y apagado quedan en `infra/railway/README.md` del repositorio MATU_PROYECTO. Plazo: el de los registros de Railway [PENDIENTE].
- **Conservación:** hasta el cierre del semestre. Al cerrar se borran la KEK, la base, los respaldos y Redis, y se anota la fecha (decisión 105, l). [PENDIENTE: fecha de cierre]
- **Transferencia internacional:** staging está en Estados Unidos. Con datos sintéticos, solo salen de Chile la IP de quien lo usa y su huella. **Staging nunca se usa con datos reales.** Antes de datos reales se elige el proveedor y la región de producción (ADR-019), y si quedan fuera de Chile se aplican las reglas de transferencia internacional de la Ley 21.719, con contrato de encargo. [PENDIENTE: consulta legal]
- **Decisiones automatizadas:** ninguna.

## 10. Aceptación de la política de privacidad al crear la cuenta (MATU-75)

- **Finalidad:** dejar constancia de qué versión y qué texto exacto vio y aceptó cada persona.
- **Titulares:** las cuentas creadas desde la versión 0.11. Las anteriores quedan sin registro (D2).
- **Datos:** `usuario_id`, `version`, `huella` (SHA-256 del texto mostrado, con el correo de contacto escrito en el texto) y `aceptada_en`. Sin IP ni navegador.
- **Base de licitud:** ejecución del servicio que pide la persona. [PENDIENTE: CL-50, si «acepto» es un consentimiento o solo un acuse de lectura]
- **Quién accede:** la titular, en «Tu cuenta», y operación para soporte. Nadie lo modifica ni lo borra desde la aplicación.
- **Conservación:** mientras exista la cuenta. [PENDIENTE: CL-49, plazo tras eliminar la cuenta]
- **Medidas:**
  - tabla de solo agregar, con RLS forzado
  - el servidor estampa la versión y la huella, y rechaza una huella que no sea la vigente
  - pruebas de la huella y de la versión
  - `/privacidad` es pública, sin sesión, cookies ni analítica
- **Comunicaciones a terceros:** ninguna.
- **Transferencia internacional:** staging en Railway, Estados Unidos, solo con datos sintéticos (entrada 9).
- **Decisiones automatizadas:** ninguna.

## 11. Buzón de privacidad y de reclamos (MATU-75, D5, y MATU-61, D8)

- **Finalidad:** recibir y responder las solicitudes de derechos y las consultas de privacidad. Desde MATU-61 (D8), también los reclamos de los pedidos, y desde MATU-62, los de los pagos y las devoluciones: es el canal de reclamo de las condiciones del pedido (§8) y del resumen antes de pagar.
- **Titulares:** cualquiera que escriba.
- **Datos:** el correo y el nombre de quien escribe, el mensaje y la respuesta. Un reclamo puede traer además el pedido al que se refiere, sus productos o la dirección. Puede traer datos sensibles, aunque la política pide no incluirlos. **Es un tratamiento de datos reales durante el piloto.**
- **Base de licitud:** atender los derechos del titular. Para los reclamos de un pedido, responder al reclamo de quien compra. [PENDIENTE: consulta legal, junto con CL-48, también para los reclamos]
- **Quién accede:** Jorge y Martín, con una cuenta de la función, verificación en dos pasos y sin reenvío a correos personales.
- **Conservación:** hasta 2 años después de cerrar la solicitud, también un reclamo. Después queda solo una lista con la fecha, el tipo de solicitud y la fecha de respuesta, sin el contenido (decisión de Jorge del 09-11; para los reclamos, decisión de Jorge del 11-11, por confirmar en CL-48).
- **Encargado:** Gmail, de Google LLC, en Estados Unidos. [PENDIENTE: revisar sus condiciones]
- **Transferencia internacional:** Estados Unidos (Google LLC). [PENDIENTE: consulta legal sobre la transferencia internacional, CL-51]
- **Medidas:**
  - el contenido de una solicitud o de un reclamo nunca se copia al repositorio, a Trello, al vault ni a una sesión con agentes
  - plazos: acuse dentro de 2 días hábiles y respuesta a más tardar en 30 días corridos (D4)
- **Decisiones automatizadas:** ninguna.

## Nota sobre la ficha ampliada (ADR-028)

La sección "Sus remedios" se mantiene por decisión de Jorge del 03-11, sin consulta legal previa: quien releva y no conoce los remedios pone en riesgo a la persona cuidada. Se trata como dato sensible, cifrado como la ficha, y al compartir viene sin marcar. Su tratamiento queda descrito en las entradas 3 y 4 (revisión previa de MATU-49 y de cierre de MATU-50, 03-11). La confirmación al compartir Sus remedios se revisa cuando MATU-48 integre el paso de compartir.

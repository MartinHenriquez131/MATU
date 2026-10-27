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
  - [PENDIENTE: consulta legal sobre quién consiente por la persona mayor dependiente: mandato con facultad expresa y titular impedido (arts. 12 y 16 c)]
  - [PENDIENTE: consulta legal sobre si la evaluación de impacto del art. 15 ter es obligatoria, y desde cuándo]
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
  - comercios en convenio, con lo que dice "Quién accede". **La dirección nunca llega al comercio.** Se puede sostener que el comercio no trata datos personales; aun así, el convenio incluye las cláusulas del art. 15 bis [PENDIENTE: consulta legal sobre si la referencia opaca es un dato personal para el comercio]
  - quien despacha, que ve la dirección, el teléfono de contacto y el paquete: **encargado** de MATU, con contrato según el art. 15 bis (instrucciones, confidencialidad, seguridad, reporte de vulneraciones y supresión al terminar)
  - Transbank, que procesa el pago en su propia página. La devolución vuelve a la misma tarjeta, por anulación de Webpay Plus, sin pedir datos nuevos
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna.

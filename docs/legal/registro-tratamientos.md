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

> Borrador ADR-027 (27-10), por aprobar por Jorge.

**Todavía no se trata.** Durante el semestre los pedidos y los pagos se hacen solo con datos sintéticos, precios de ejemplo y el ambiente de integración de Transbank (`figura-legal-piloto.md`, sección 5).

- **Finalidad:** pedir insumos a comercios en convenio, a precio exacto, y cobrar una sola vez el total confirmado. MATU vende y emite una sola boleta por el total, con el envío incluido.
- **Titulares:** el usuario que pide y paga, y la persona cuidada a quien va el pedido.
- **Datos:**
  - productos, cantidades, precios, envío y total. Se tratan como **datos sensibles** mientras se consulta, porque junto con un dato que identifica pueden revelar salud o dependencia [PENDIENTE: consulta legal sobre si lo son según la Ley 21.719]
  - dirección de entrega
  - el pago: monto cobrado, monto devuelto, código de autorización, tipo de tarjeta y últimos 4 dígitos. MATU nunca recibe ni guarda los datos de la tarjeta
- **Base de licitud:** [PENDIENTE: consulta legal].
- **Quién accede:**
  - en el grupo, todos los roles ven los pedidos; administrador y cuidador los crean, y administrador y pagador pagan (arquitectura, sección 11.2)
  - el comercio que prepara ve solo sus productos, la referencia del pedido y el código de retiro. **Ningún nombre**, ni la ficha ni la dirección. El comercio que reemplaza a otro ve lo mismo, solo con lo que le toca
  - operación ve pedidos y pagos para dar soporte, y devuelve por anulación. Nunca la ficha ni el consumo de insumos
- **La consulta de stock no trata datos personales:** lleva solo productos, cantidades y una referencia opaca para apartar. No lleva datos de la familia, de la persona cuidada ni de la dirección, y una prueba sobre el objeto de la consulta lo verifica.
- **Conservación:** pedidos y comprobantes de entrega, 2 años. Pagos y boletas, 6 años, por obligación tributaria (arquitectura, sección 11.8).
- **Medidas:**
  - separación por familia con RLS forzado
  - el comercio ve un pedido solo cuando está pagado y enviado, y nunca la dirección, que vive en una tabla aparte
  - el precio pagado queda fijo en la base desde el pago, y lo devuelto nunca supera lo cobrado
  - registro de transacciones de pasarela que nunca se borra
- **Comunicaciones a terceros:**
  - comercios en convenio, con lo que dice "Quién accede" [PENDIENTE: consulta legal sobre si son encargados o responsables]
  - Transbank, que procesa el pago en su propia página. La devolución vuelve a la misma tarjeta, por anulación de Webpay Plus, sin pedir datos nuevos
- **Transferencia internacional:** [PENDIENTE: proveedor y país].
- **Decisiones automatizadas:** ninguna.

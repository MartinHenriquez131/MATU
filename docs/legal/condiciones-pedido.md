# Condiciones del pedido de MATU

**Versión 0.2 · 11 de noviembre de 2026 (11/11/2026)** · versión del piloto académico. Parte de la 0.1 (MATU-61) y suma el pago (MATU-62): la redactó el analista normativo en la segunda revisión previa de MATU-62 (`revision-previa-matu-62-segunda.md`) y la aprobó el orquestador el 11-11, por delegación de Jorge Espinoza (Product Owner), que la confirmó el 12-11. La §4 se corrigió antes de publicarse: en el piloto el comprobante queda en MATU y no se envía por correo (P-62-5). No es asesoría legal. En el piloto no se cobra dinero real.
**Identificador de versión en el sistema:** `0.2`, con huella SHA-256 `64859e519a0aa19bb56b415256d2d9757f162e278824edffb1092a2985a334b7`. La 0.1 sigue publicada (`GET /v1/condiciones-pedido?version=0.1`) para quien la aceptó.
**Versión propia (D6):** estas condiciones tienen su número, separado del de la política de privacidad. Cambiar una palabra desde la sección 1 hasta el final es publicar una versión nueva, porque cambia la huella del texto que se acepta.
**Dónde se leen:** en la app, en /condiciones-pedido, con el enlace «Condiciones del pedido» del resumen antes de pagar (`GET /v1/condiciones-pedido`), y la versión aceptada desde el comprobante (`?version=`).

---

## 1. Quién vende

Durante el piloto vende MATU, piloto académico, sin persona jurídica. En el piloto no se emite boleta. Los pagos son de prueba: ocurren en el ambiente de prueba de Transbank y no se cobra dinero real. El comprobante no es una boleta. [PENDIENTE: persona jurídica y boleta, CL-46 y CL-47]

## 2. Qué compras y cuánto pagas

- Cada producto tiene un precio exacto, con IVA incluido, del comercio en convenio que lo prepara.
- Se suma un solo envío por pedido, aunque lo preparen varios comercios.
- Antes de pagar confirmamos que haya cada producto. Lo que no hay sale del pedido y lo ves antes de pagar.
- El total confirmado vale 15 minutos. Si vence, se vuelve a confirmar y te mostramos lo que cambió.
- Se cobra una sola vez ese total, con crédito o con débito. No hay reserva ni cobros después.

## 3. Cómo pagas

- Pagan quien administra el grupo y quien paga. Quien paga acepta estas condiciones.
- Pagas en la página de Transbank. MATU no ve los datos de tu tarjeta.
- Mientras un pago está en curso, nadie del grupo puede cambiar el pedido. Sí se puede cancelar.
- Si empezaste a pagar antes de que venciera el total y Transbank lo aprueba después, respetamos ese total.
- Si mientras pagabas el pedido se cambió o se canceló, anulamos el cobro completo el mismo día, a la misma tarjeta, y te avisamos.

## 4. Tu confirmación

Al pagar te mostramos un comprobante, que queda guardado en MATU, con el número del pedido, la fecha, el total, los productos, quién vende, tu derecho a retracto, cómo se devuelve si falta un producto y la versión de estas condiciones que aceptaste. Lo puedes volver a ver cuando quieras en la aplicación. En el piloto, el comprobante no se envía por correo. [PENDIENTE: CL-54]

## 5. Si falta un producto

Antes de pagar eliges, por cada producto, si lo buscamos en otro comercio o si lo sacamos del pedido. Si no eliges, lo buscamos.

- Si lo buscamos y otro comercio lo tiene, pagas lo mismo que aceptaste. La diferencia de precio la asume MATU.
- Nunca lo cambiamos por otra marca ni por otro producto.
- Si nadie lo tiene, o elegiste sacarlo, anulamos su cobro el mismo día, a la misma tarjeta. Si no se entrega ningún producto, devolvemos también el envío. Cuándo lo ves en tu cuenta depende de tu banco.

## 6. Cancelar

- Antes de pagar, no seguir no tiene costo.
- Después de pagar, quien administra el grupo puede cancelar sin costo mientras el comercio no empiece a preparar, y te devolvemos el total.

## 7. Si no podemos devolver

Si la anulación en Transbank no se puede hacer, la reintentamos y te escribimos. Nunca te pedimos los datos de tu tarjeta ni de tu banco por mensaje. [PENDIENTE: CL-55]

## 8. Entrega

Durante el piloto, el pedido llega entre 24 y 48 horas hábiles. Te lo mostramos antes de pagar. Si no podemos cumplirlo, te avisamos y eliges entre esperar o recibir la devolución.

## 9. Derecho a retracto

Tienes 10 días desde que recibes el producto. En los productos de uso personal o de higiene sellados, se pierde solo si abres el sello. MATU devuelve también el envío y paga el retiro. Lo pides en el pedido entregado, con «Arrepentirme de la compra». [PENDIENTE: CL-41, suplemento y bolsas colectoras; medio de devolución si se pasa el plazo de anulación de Transbank]

## 10. Si algo no llega

MATU responde ante ti y devuelve el mismo día lo que no se entregó. Estas condiciones no limitan ninguna indemnización que corresponda.

## 11. Reclamos

Reclamos: escribe a cuidaconmatu@gmail.com.

## 12. Tus datos

Los pedidos se tratan como datos sensibles. Ningún comercio ve tu nombre, el de la persona que cuidas ni la dirección. Lo demás está en la política de privacidad vigente.

## 13. Versión

Guardamos qué versión de estas condiciones aceptaste, quién la aceptó, cuándo, y una huella del texto exacto que viste.

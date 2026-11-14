# Condiciones del pedido de MATU

**Versión 0.3 · 13 de noviembre de 2026 (13/11/2026)** · versión del piloto académico. Parte de la 0.2 y suma lo que pasa después de pagar (MATU-63): cambian §5 (un producto que falta después de pagar se devuelve el mismo día), §6 (se cancela mientras ningún comercio empiece a preparar), §8 (si no hay nadie para recibir) y §9 (cómo se pide el retracto y cuándo se devuelve el envío). La redactó el analista normativo en la revisión previa de MATU-63 (`revision-previa-matu-63.md`, D-63-8 a D-63-11 y D-63-16). Jorge confirmó el 13-11 el plazo de 10 días hábiles (D-63-9) y que el envío se devuelve solo si se devuelve todo (D-63-10 b). **Pendiente de aprobación: la aprueba Jorge al fusionar.** No es asesoría legal. En el piloto no se cobra dinero real.
**Identificador de versión en el sistema:** `0.3`, con huella SHA-256 [PENDIENTE: la recalcula el backend tras el H1-bis del cierre].
**La 0.3 se acepta solo en los pedidos nuevos (D-63-16).** **La 0.2 rige para los pedidos que la aceptaron**, y se cumplen según la 0.2: en un retracto se devuelve también el envío, aunque se devuelva solo una parte (D-63-10 a). La 0.2 (huella `64859e519a0aa19bb56b415256d2d9757f162e278824edffb1092a2985a334b7`) y la 0.1 siguen publicadas (`GET /v1/condiciones-pedido?version=0.2` y `?version=0.1`) para quien las aceptó.
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

Antes de pagar eliges, por cada producto, si lo buscamos en otro comercio o si lo sacamos del pedido. Si no eliges, lo buscamos. Lo hacemos al confirmar el total: si el producto pasa a otro comercio o cambia de precio, lo ves antes de pagar. Nunca lo cambiamos por otra marca ni por otro producto.

Durante el piloto, si después de pagar falta un producto, no lo buscamos en otro comercio: anulamos el cobro de lo que falta el mismo día, a la misma tarjeta. Si falta solo una parte, te devolvemos esas unidades y te llevamos el resto. Si no se entrega ningún producto, devolvemos también el envío. Cuándo lo ves en tu cuenta depende de tu banco.

## 6. Cancelar

- Antes de pagar, no seguir no tiene costo.
- Después de pagar, quien administra el grupo puede cancelar sin costo, y te devolvemos el total, mientras ningún comercio empiece a preparar.

## 7. Si no podemos devolver

Si la anulación en Transbank no se puede hacer, la reintentamos y te escribimos. Nunca te pedimos los datos de tu tarjeta ni de tu banco por mensaje. [PENDIENTE: CL-55]

## 8. Entrega

Durante el piloto, el pedido llega entre 24 y 48 horas hábiles. Te lo mostramos antes de pagar. Si no podemos cumplirlo, te avisamos. Mientras ningún comercio empiece a preparar, puedes cancelar y te devolvemos el total. Si no hay nadie para recibirlo, coordinamos otra entrega o te devolvemos el total.

## 9. Derecho a retracto

Lo piden quien administra el grupo o quien pagó, en el pedido entregado, con «Arrepentirme de la compra», hasta la fecha que te mostramos (10 días hábiles desde la entrega). Puedes elegir qué productos devuelves. Puedes devolverlos en una o varias veces mientras dure el plazo. Pasamos a buscarlos sin costo. Cuando los recibimos con su sello cerrado, te devolvemos su precio a la misma tarjeta, y también el envío si devuelves todo. Si no alcanzas a hacerlo en la aplicación, escríbenos a cuidaconmatu@gmail.com.

En los productos de uso personal o de higiene sellados, el derecho a retracto se pierde solo si abres el sello. [PENDIENTE: CL-41, CL-54, CL-71 y CL-72. Suplemento y bolsas colectoras, cómo se cuenta el plazo, el envío en un retracto parcial y el medio de devolución si se pasa el plazo de anulación de Transbank, CL-55]

## 10. Si algo no llega

MATU responde ante ti y devuelve el mismo día lo que no se entregó. Estas condiciones no limitan ninguna indemnización que corresponda.

## 11. Reclamos

Reclamos: escribe a cuidaconmatu@gmail.com.

## 12. Tus datos

Los pedidos se tratan como datos sensibles. Ningún comercio ve tu nombre, el de la persona que cuidas ni la dirección. Lo demás está en la política de privacidad vigente.

## 13. Versión

Guardamos qué versión de estas condiciones aceptaste, quién la aceptó, cuándo, y una huella del texto exacto que viste.

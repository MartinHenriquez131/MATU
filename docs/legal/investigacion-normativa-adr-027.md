# Investigación normativa del ADR-027 · 27 de octubre de 2026

> **Esto no es asesoría legal.** Jorge (Product Owner) pidió revisar qué dice el texto público de la ley antes de llevar preguntas a una consulta legal, y ajustar el diseño a eso. Se leyeron los textos consolidados en LeyChile (BCN). Las citas textuales son breves. Los ajustes de diseño son propuestas y los aprueba Jorge.

## Fuentes primarias

- **Ley 19.496:** texto refundido, DFL 3 de 2021, con la Ley 21.398 "Pro Consumidor". https://www.bcn.cl/leychile/navegar?idNorma=1160403
- **Decreto 52 de 2024**, Ministerio de Economía: reglamento de exclusión del derecho a retracto. https://www.bcn.cl/leychile/navegar?idNorma=1206144
- **Decreto 6 de 2021**, Ministerio de Economía: Reglamento de Comercio Electrónico. https://www.bcn.cl/leychile/navegar?idNorma=1165504
- **Ley 19.628 en la versión que fija la Ley 21.719**, vigente desde el 1 de diciembre de 2026. https://www.bcn.cl/leychile/navegar?idNorma=141599&idVersion=2026-12-01

De Sernac solo se vieron fragmentos en un buscador. Son fuente secundaria.

## 1. Retracto

**Qué dice el texto**
- **Ley 19.496, art. 3 bis b).** El retracto procede en las compras a distancia, con 10 días desde que se recibe el producto.
  - En los bienes, excluirlo es excepcional, y la exclusión se informa antes del pago de forma "inequívoca, destacada y fácilmente accesible".
  - Si falta la confirmación escrita del art. 12 A, el plazo sube a 90 días.
  - La devolución por retracto se hace sin retención de gastos, dentro de 45 días.
- **Decreto 52, art. 4 N° 4.** Los bienes de uso personal o de higiene sellados quedan excluidos solo si el consumidor abrió el sello después de recibirlos. Entre sus ejemplos nombra las cremas.
- **Decreto 52, art. 6.** La exclusión se informa junto al precio, con una advertencia no menor que el precio, y usando el concepto "derecho a retracto".

**Qué significa para MATU**
- **El retracto aplica.** Pañales, apósitos, guantes y cremas cerrados tienen retracto, que se pierde solo si se abre el sello.
- **Junto al precio y en el resumen previo al pago** va el texto: "Derecho a retracto: tienes 10 días desde que lo recibes. No aplica si abres el sello del producto".
- **En el pedido entregado** aparece "Arrepentirme de la compra" durante 10 días.
- **Al pagar** se envía la confirmación escrita (art. 12 A).
- **La devolución por retracto** usa la misma anulación de Webpay.
- **El Decreto 6 además pide:**
  - identificar al vendedor (art. 7);
  - mostrar el despacho separado del precio (art. 11);
  - informar el plazo de entrega y un canal de reclamo (art. 13);
  - poner un enlace a los términos (art. 16);
  - mostrar un resumen antes del pago (art. 18).

**Certeza**
- **Lo resuelve el texto:** que el retracto aplica y cómo se informa.
- **Requiere interpretación:**
  - si los pañales en paquetes de varias unidades, los guantes y los apósitos caben en el N° 4;
  - si "sin retención de gastos" incluye el envío;
  - quién paga el retiro.

## 2. Plazo de devolución de lo pagado y no entregado

**Qué dice el texto**
- **No se encontró un plazo legal específico.**
- **Ley 19.496, art. 12:** el proveedor respeta los términos de entrega que ofreció.
- **Ley 19.496, art. 3 e):** hay derecho a una reparación "adecuada y oportuna".
- **Decreto 6, arts. 12 y 13:** el contrato se cumple de forma fiel y oportuna, y se informa el plazo de entrega.
- **Los 45 días son solo del retracto.**

**Qué significa para MATU**
- **La devolución el mismo día por anulación parcial** calza con el cumplimiento oportuno.
- **El plazo lo fijan los términos del pedido:** "Si un producto no se puede entregar, anulamos su cobro el mismo día".
- **La pantalla no promete cuándo se ve el dinero,** porque depende del banco. Así ya lo dice la demo.
- **Si la entrega pasa del plazo informado,** se avisa y la familia elige entre esperar o recibir la devolución.

**Certeza**
- **No se encontró** un plazo legal específico.
- **Requiere interpretación:** el deber de devolver de forma oportuna.

## 3. Datos sensibles (Ley 19.628 según la Ley 21.719)

**Qué dice el texto**
- **Art. 2 g), datos sensibles:** son los que "revelen", entre otros, los datos relativos a la salud. La ley no define aparte qué es un "dato relativo a la salud".
- **Art. 16:** se requiere consentimiento expreso, salvo excepciones. Entre ellas, la c): el titular está física o jurídicamente impedido.
- **Art. 16 bis, inciso 1:** aun con consentimiento, los datos de salud se tratan para los fines "previstos por las leyes especiales en materia sanitaria". La letra e) admite la prestación de asistencia sanitaria o social.
- **Art. 12:** el mandatario necesita una facultad expresa. La revocación se hace por un medio equivalente al que se usó para consentir.
- **Art. 15 ter:** hay evaluación de impacto, entre otros casos, al tratar datos sensibles con una excepción al consentimiento.

**Qué significa para MATU**
- **El historial de pedidos y de consumo de la persona cuidada se trata como sensible,** con la misma protección que la ficha. Es una interpretación prudente: un pedido de pañales para adulto vinculado a una persona puede revelar un dato de salud.
- **La titular es la persona cuidada.** Esto refuerza MATU-07: quién consiente y en qué calidad.
- **Minimización:** la capa 3 no usa el nombre ni el diagnóstico, y las categorías de producto no llevan etiquetas clínicas (`docs/lenguaje.md`).
- **El consentimiento para los pedidos es expreso y separado,** y se revoca igual de fácil.

**Certeza**
- **Lo resuelve el texto:** las definiciones y la regla del consentimiento.
- **Requiere interpretación:**
  - si los productos son un dato de salud;
  - el alcance del art. 16 bis, inciso 1, y de su letra e).

## 4. Responsable o encargado

**Qué dice el texto**
- **Art. 2 n), responsable:** decide los fines y los medios.
- **Art. 2 x), encargado:** trata datos por cuenta del responsable.
- **Art. 15 bis:** fija el contrato con el encargado: instrucciones, confidencialidad, seguridad, reporte de vulneraciones y supresión al terminar.
- **Art. 2 k) y l):** el dato anonimizado deja de ser personal, y el seudonimizado no.

**Qué significa para MATU**
- **Se puede sostener que el comercio no trata datos personales** si recibe solo productos, cantidades y una referencia que no puede asociar a nadie.
- **Ajustes:**
  - la referencia opaca es aleatoria **por pedido**, nunca por familia;
  - la dirección nunca llega al comercio;
  - el convenio con el comercio incluye de todos modos las cláusulas del art. 15 bis.
- **Quien despacha** ve la dirección y el paquete, y es **encargado** de MATU.

**Certeza**
- **Lo resuelve el texto:** las definiciones y el contenido del contrato.
- **Requiere interpretación:** si la referencia opaca es un dato personal para el comercio.

## Lo que todavía conviene llevar a un abogado

1. **El art. 16 bis, inciso 1.** Si limita a MATU aunque tenga consentimiento, y si sirve como base la letra e), sobre la asistencia social. Es el riesgo más alto.
2. **Si los productos de un pedido son un dato relativo a la salud.**
3. **Quién consiente por la persona mayor dependiente:** el mandato con facultad expresa y el caso de quien está impedido (arts. 12, 16 c y 16 bis a). Conecta con MATU-07 y con la consulta sobre el cuidador de hecho.
4. **El alcance del Decreto 52, art. 4 N° 4,** en pañales, guantes y apósitos, y si en el retracto se devuelve el envío.
5. **Si la referencia opaca es un dato personal para el comercio.**
6. **La falta de entrega:** si además de devolver procede una indemnización, y cómo se reparte la responsabilidad entre MATU y el comercio.
7. **Si la evaluación de impacto del art. 15 ter es obligatoria,** y desde cuándo.

**Del lado operativo:** Transbank confirma el plazo real de una anulación parcial.

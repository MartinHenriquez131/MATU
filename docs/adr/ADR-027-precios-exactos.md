# ADR-027 · Precios exactos de comercios en convenio, y se cobra el total confirmado

**Estado:** Aprobado por Jorge Espinoza (Product Owner) el 26 de octubre de 2026, con las observaciones de la revisión previa del analista normativo ([`legal/revision-previa-adr-027.md`](../legal/revision-previa-adr-027.md)). **Reemplaza al ADR-006 y al ADR-011.** Lo que queda marcado [PENDIENTE] o en consulta legal se resuelve antes de cobrar dinero real. El ADR-026 (aplicación web) está en [`ADR-026-aplicacion-web.md`](ADR-026-aplicacion-web.md).
**Fecha de decisión:** 26 de octubre de 2026
**Decisor:** Jorge Espinoza (Product Owner)
**Reemplaza:** el ADR-006 (autorización con margen y captura por monto real) y el ADR-011 (el precio de catálogo es referencial)

Las secciones que se citan sin otro documento son de la [arquitectura](../arquitectura.md). Hasta el 8 de noviembre este texto vivía en su sección 14, y se movió sin cambios (MATU-43).

---

## Contexto

El ADR-006 resolvía un precio que no se conocía hasta que el comercio preparaba. Se autorizaba el estimado con un margen del 15% y se capturaba el monto real. La prueba de concepto ([`pruebas-concepto/transbank.md`](../pruebas-concepto/transbank.md)) mostró el costo de ese diseño:
- la captura diferida opera solo con crédito, y el débito es el medio mayoritario del segmento;
- el plan B del débito obligó a cobrar el estimado y a devolver diferencias, con un medio y un plazo que siguen sin definir;
- explicar una retención mayor que el pedido (sección 10.4) es difícil para una familia cansada, y lo observó el análisis normativo de la Ley 19.496.

## Decisión

1. **Precios exactos.** El catálogo muestra precios exactos de comercios preestablecidos en convenio, con IVA incluido y con su stock. El costo del envío se ve desde la lista de reposición. El precio queda fijo cuando la familia paga el total confirmado.
2. **La lista de reposición tiene tres salidas:**
   - exportarla y comprar libremente;
   - enviarla a un miembro del grupo, o compartirla desde el teléfono de la familia;
   - pedir desde MATU al precio exacto más el envío.

   Las dos primeras son gratuitas y no dependen de la capa 3 (ADR-002).
3. **Antes de cobrar se confirma el stock.**
   - MATU consulta el stock de los comercios en convenio. Si el comercio elegido no tiene un producto, lo busca en otro comercio en convenio. Si ninguno lo tiene, el producto sale del pedido.
   - **La consulta de stock lleva solo productos y cantidades**, con una referencia opaca para apartar. No lleva datos de la familia, de la persona cuidada ni de la dirección. Una prueba sobre el objeto de la consulta lo verifica.
   - Si un precio o un comercio cambia respecto de lo que la familia vio en la lista, la pantalla lo marca antes de pagar.
   - El total confirmado vale por **15 minutos** (decisión de Jorge, 26 de octubre). Si vence, se vuelve a confirmar. La familia puede no pagar, sin costo.
4. **Se cobra una sola vez el total exacto.** Son los productos más un **envío único por pedido**, aunque el retiro pase por más de un comercio, y MATU absorbe la parada extra. Es una venta normal de Webpay Plus, y **crédito y débito funcionan igual**. No hay reserva con margen, ni captura diferida, ni ajuste posterior.

   **Antes de pagar**, la familia ve:
   - los productos con cantidad, precio y subtotal;
   - los que salieron por no disponibles;
   - el envío y el total con IVA;
   - quién emite la boleta;
   - la ventana de entrega;
   - qué pasa si al retirar falta un producto (punto 5), con el medio y el plazo de la devolución.

   Acepta las condiciones del pedido y recibe un comprobante.

   **Decisiones de producto del 26 de octubre** (Jorge, sujetas a validación en la consulta legal):
   - **Quién vende.** MATU vende y emite **una sola boleta por el total**, con el envío incluido. Los comercios le cobran a MATU por cuenta corriente (ADR-008) y nunca ven a la familia. Para vender de verdad, MATU necesita existir como persona jurídica con inicio de actividades, y eso queda para después del semestre.
   - **Devolución.** "Si un producto no llega, te devolvemos su precio el mismo día, a la misma tarjeta. Cuándo lo ves en tu cuenta depende de tu banco."
   - **Cancelación.** Antes de pagar, no pedir no tiene costo. Después de pagar, se cancela sin costo mientras el comercio no empiece a preparar.
   - **Sin equivalentes de otra marca.** Si falta un producto, se busca el mismo en otro comercio o sale del pedido.
   - **El comercio no ve ningún nombre**, solo la referencia del pedido y el código de retiro.
5. **El comercio que confirma el stock lo aparta.** Si al retirar el producto ya no está, que es el caso excepcional:
   - el retiro se reasigna a otro comercio en convenio **con el mismo producto**, y MATU asume la diferencia de precio. La familia paga lo mismo que aceptó, y queda escrito como garantía en las condiciones del pedido;
   - nunca se reemplaza por otra marca ni por otro producto (decisión del 26 de octubre);
   - si la familia eligió quitarlo (RF-21), o ningún comercio lo tiene, se devuelve el precio de ese producto a la misma tarjeta, por anulación de Webpay Plus, y se avisa a la familia en el momento. Si no se entrega ningún producto, se devuelve también el envío. Es la única devolución por falta de producto; la del retracto se rige por la sección 18.1.
6. **Los comercios, los precios y el stock entran por un puerto**, `CatalogoComercio`, en el módulo `catalog` (ADR-021). Hoy no hay convenio con distribuidores, así que el adaptador es simulado, con un catálogo semilla, y la interfaz rotula los precios como de ejemplo. Cuando exista un convenio, que posiblemente llegue después del semestre, se agrega un adaptador real sin tocar los módulos que lo usan.

## Consecuencias

- **Se simplifica el pago.** Desaparecen la captura diferida, la reserva del 15%, el plan B del débito y su nota de crédito. Si la devolución excepcional obliga a corregir un documento tributario, se resuelve con la consulta legal sobre quién emite la boleta.
- **El cumplimiento ya no informa un monto real.** Desaparecen `precio_real` y el paso "monto real" del comercio. El comercio confirma el stock y prepara.
- **La sección 11.7 cambia de sentido.** Con precio exacto, `monto_boleta` contra el precio pagado ya no mide una desviación del comercio cuando MATU retiró en otro comercio. El tope y la conciliación se rediseñan.
- **ADR-024 se ajusta.** Un pedido de la familia puede abastecerse en más de un comercio, con un solo cobro y un solo envío. El registro por comercio se mantiene para preparar y liquidar (ADR-008). Cada comercio recibe solo sus líneas del pedido, y el que reemplaza a otro recibe la misma proyección que el original (sección 11.2).
- **Cambia el esquema.** Hay que ajustar `pedido` (`total_estimado` y `total_autorizado`), `cargo` y `participacion` (`monto_autorizado` y `monto_capturado`) y sus estados (`autorizado`, `captura_pendiente`). Va en una migración reversible.
- **Aparece una espera corta** entre pedir y pagar, mientras se confirma el stock. Con el adaptador simulado es inmediata.

## Alcance en el semestre

- **Se construye:** el catálogo con precios exactos detrás del puerto con el adaptador simulado, la confirmación de stock entre comercios antes de pagar y el cobro del total exacto.
- **Queda en la fase 2:** la reasignación del retiro a otro comercio después de pagar, porque requiere la aplicación de repartidor y la asignación en cascada (ADR-010 y ADR-025). En el semestre se muestra simulada en la demo y queda diseñada aquí.

## Riesgo declarado

- **Devolución excepcional.** Hay que verificar en el ambiente de integración que se admita la anulación parcial de una venta normal con crédito y con débito, y los plazos máximos de anulación de Transbank. Si no se admite, se define otro medio antes del sprint 4, sin pedir datos bancarios a la familia salvo que se apruebe como tratamiento nuevo en la política de privacidad y en el registro de tratamientos. **Verificado el 10 de noviembre:** la anulación parcial funciona con crédito y con débito ([prueba de concepto](../pruebas-concepto/transbank.md)). Los plazos máximos de anulación no se miden en integración, y quedan como supuesto de hasta 90 días, por confirmar con Transbank.
- **La prueba de concepto verificó la captura diferida, no la venta normal.** Faltan los casos de venta normal con crédito y con débito, la anulación parcial con los dos y el retorno duplicado en venta normal. **Se corrieron el 10 de noviembre y cumplen** (estrategia de pruebas, sección 10.2).
- **Precios al día.** Los precios exactos dependen de que el comercio mantenga su catálogo al día, y el convenio debe obligarlo a hacerlo. Sin convenio, el piloto usa precios de ejemplo y lo declara en la interfaz.
- **Consulta legal antes de cobrar dinero real.** Hay que validar las decisiones de producto del 26 de octubre (MATU como vendedor, devolución y cancelación) y resolver:
  - el retracto;
  - el plazo legal de la devolución, si existe;
  - si los productos del pedido son datos sensibles;
  - si los comercios son encargados o responsables.

## Alternativas descartadas

- **Cobrar primero y devolver lo que falte.** Es más rápido para la familia, pero convierte la devolución en una operación rutinaria y vuelve a depender de devoluciones con débito, que no están verificadas.
- **Mantener el ADR-006 con el plan B del débito.** Funciona, pero deja dos experiencias de pago distintas según la tarjeta y textos con plazos por definir.

---

## Notas posteriores

**MATU-63 (13 de noviembre de 2026).** Precisan cómo se cumple este ADR en el piloto, sin cambiar la decisión. Las aprobó Jorge el 13-11 (D-63-5, D-63-9 y D-63-10). El resto lo aplicó el orquestador por delegación. Detalle en [`legal/revision-previa-matu-63.md`](../legal/revision-previa-matu-63.md).
- **El código de retiro:** donde el contexto dice que el comercio ve «la referencia del pedido y el código de retiro», el comercio ve solo la referencia, creada al azar por cada comercio que prepara. El código lo dice quien retira por MATU, operación en el piloto, y el comercio solo puede revisar si es correcto: no lo ve. Hay un código por cada comercio del pedido, y la familia no lo recibe, porque MATU despacha a la casa.
- **Un producto que falta después de pagar (punto 5):** en el piloto no se reasigna a otro comercio. Se anula el cobro de las unidades que faltan el mismo día, a la misma tarjeta. La reasignación queda para la fase 2.
- **El envío en el retracto:** con las condiciones del pedido 0.3, el envío se devuelve solo si se devuelve todo lo entregado. Los pedidos que aceptaron la 0.2 se respetan como estaban, con el envío siempre, que fue la decisión del 27-10 (P5). Pendiente: CL-72.
- **El plazo del retracto:** 10 días hábiles desde la entrega, que marca operación, mientras la CL-71 siga abierta.
- **El apartado de stock:** MATU aparta el stock automáticamente al confirmar el total, contra el stock que mantiene el comercio (punto 5, primera frase).

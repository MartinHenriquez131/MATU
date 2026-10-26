# Revisión previa del ADR-027 · analista normativo

> **Borrador de trabajo del 25 de octubre de 2026.** Es el informe del analista normativo sobre el borrador del ADR-027 (precios exactos y cobro del total confirmado). **No es asesoría legal** y nada de esto está aprobado: Jorge Espinoza (Product Owner) decide qué entra en el ADR y en `docs/legal/`. Lo que queda en REQUIERE CONSULTA LEGAL va a la tarjeta de consulta legal en Trello.

## Resumen

| # | Punto | Veredicto |
|---|---|---|
| 1a | Modelo: precio exacto más envío, stock confirmado y cobro del total que se mostró | **CUMPLE** (Ley 19.496, art. 3 letra b y art. 30). Precios y envío con IVA incluido |
| 1b | Qué ve la familia antes de pagar | **NO CUMPLE** todavía: el ADR no lo define |
| 1c | Cuánto dura el total confirmado, y cambios de precio o de comercio antes de pagar | **NO CUMPLE** todavía: sin definir |
| 1d | Retracto, condiciones generales, quién es el proveedor y quién emite la boleta | **REQUIERE CONSULTA LEGAL** |
| 1e | Precios simulados en el piloto | **CUMPLE**, con el rótulo del punto 6 |
| 2a | Qué se informa antes de pagar sobre la única devolución | **NO CUMPLE** todavía |
| 2b | Medio de la devolución | **CUMPLE** si es "a la misma tarjeta, por anulación de Webpay Plus". El respaldo "manual desde el backoffice" **NO CUMPLE** tal como está escrito |
| 2c | Plazo de la devolución | **REQUIERE CONSULTA LEGAL**, más un [PENDIENTE] técnico (plazos de anulación de Transbank) |
| 2d | Documento tributario cuando hay devolución | **REQUIERE CONSULTA LEGAL** (tributaria) |
| 3a | "MATU asume la diferencia" frente al consumidor | **CUMPLE**, si se escribe como garantía en las condiciones del pedido |
| 3b | Reemplazo por otra marca | **NO CUMPLE** si se mantiene sin consentimiento previo |
| 3c | Boleta del comercio por un monto distinto del cobrado | **REQUIERE CONSULTA LEGAL** (tributaria) |
| 5a | Consultar stock en varios comercios | **CUMPLE**, si la consulta lleva solo productos, cantidades y una referencia opaca (condición de diseño con prueba) |
| 5b | Los productos del pedido revelan salud o dependencia | **REQUIERE CONSULTA LEGAL**. Mientras tanto se tratan como sensibles |
| 5c | Dirección de despacho y nombre de quien recibe | Dirección: **CUMPLE** (el comercio no la recibe). Nombre de quien recibe: **NO CUMPLE** si se agrega sin declararlo |
| 5d | Boleta a nombre de quien paga (ADR-008) contra la sección 11.2 | **REQUIERE CONSULTA LEGAL** y una decisión de Jorge |
| 5e | Comercio que reemplaza a otro | **CUMPLE**, con cambio en la política |
| 5f | Comercios como encargados o como responsables | **REQUIERE CONSULTA LEGAL** |
| 5g | "Enviar la lista a otro familiar" | **NO CUMPLE** todavía si MATU envía a alguien fuera del grupo |
| 6 | Rótulo de precios simulados y aviso de piloto en la demo | Rótulo propuesto abajo. Aviso de piloto académico en todas las pantallas (figura legal 4.1): **NO CUMPLE**, no está en la demo |

## Qué debe ver la familia antes de pagar (1b)

1. Cada producto con cantidad, precio unitario y subtotal, en pesos enteros
2. Los productos que salieron por no disponibles, a la vista, con su efecto en el total
3. Los productos que cambiaron de comercio o de precio respecto de la lista, marcados
4. El envío único en una línea aparte, y el total a pagar con IVA incluido
5. "Se cobra una sola vez este total, con crédito o con débito. No hay reserva ni cobros después."
6. La única devolución posible, con su medio y su plazo
7. Quién vende y quién emite la boleta
8. La ventana de entrega
9. Un enlace a las condiciones del pedido, que se aceptan antes de pagar, y un comprobante después (art. 12 A)
10. Una salida para no pagar, sin costo

**Sobre 1c:** el precio queda fijo **al pagar el total confirmado**, no "al confirmar". El total confirmado vale por [PENDIENTE: N minutos]. Si vence, se vuelve a confirmar y la pantalla lo dice.

## Cambios de texto propuestos para el ADR-027

- **Punto 1:** "El catálogo muestra precios exactos de comercios en convenio, con IVA incluido, y el costo del envío se ve desde la lista de reposición. El precio queda fijo cuando la familia paga el total confirmado."
- **Punto 2, segunda salida:** "enviarla a un miembro del grupo, o compartirla desde el teléfono de la familia".
- **Punto 3, agregar:** la consulta de stock lleva solo productos y cantidades, más una referencia opaca para apartar. No lleva datos de la familia, de la persona cuidada ni de la dirección. Los cambios de precio o de comercio se marcan antes de pagar. Además, va la vigencia del total confirmado y la salida sin costo.
- **Punto 4, agregar:** la lista de lo que la familia ve antes de pagar (arriba). La familia acepta las condiciones y recibe un comprobante.
- **Punto 5, reemplazar:** el retiro se reasigna a otro comercio **con el mismo producto**, y MATU asume la diferencia de precio. No se reemplaza por otra marca sin aceptación previa. Si ningún comercio lo tiene, se devuelve el precio de ese producto a la misma tarjeta, por anulación de Webpay Plus, y se avisa en el momento. Si no se entrega ningún producto, se devuelve también el envío.
- **Consecuencias, agregar:**
  - La sección 11.7 cambia de sentido, porque `monto_boleta` contra el precio pagado ya no mide una desviación del comercio.
  - El comercio que reemplaza recibe la misma proyección que el original, solo con sus líneas.
  - Si la devolución excepcional obliga a corregir un documento tributario, se resuelve con la consulta legal.
- **Riesgo, reemplazar el respaldo del backoffice:** se verifican también los plazos máximos de anulación con crédito y con débito. Si no se admite la anulación parcial, se define otro medio antes del sprint 4, sin pedir datos bancarios salvo que se apruebe como tratamiento nuevo.
- **Riesgo, agregar:**
  - La prueba de concepto verificó la captura diferida, no la venta normal. Faltan los casos de venta normal con crédito y con débito, anulación parcial y retorno duplicado.
  - Proveedor, boleta, retracto y plazo de la devolución quedan en consulta legal antes de cobrar dinero real.

**Secciones de `arquitectura.md` que el ADR deja desactualizadas:** 7.4 (`oferta.precio_referencia`, `pedido`, `cargo`, `consumo_comercio`), 7.6 c, 8.1, 8.2, 8.3, 10.4 a, 11.2, 11.7, 17 y 18.1. También `estrategia-pruebas.md`, línea 219.

## Cambios propuestos para `docs/legal/` (borradores, por aprobar)

**`figura-legal-piloto.md`**
- **Sección 1:** nota de que el ADR-027 reemplazó la captura diferida.
- **Sección 4.1:**
  - pago de prueba en venta normal con crédito y débito, con [PENDIENTE: verificar que el comercio de integración de venta normal ofrece débito];
  - catálogo con precios de ejemplo rotulados.
- **Sección 4.2:** no presentar precios de ejemplo como reales, ni usar el nombre de un comercio real.
- **Sección 5, completa:** se reemplaza por "Cómo se paga (ADR-027)": un solo cobro del total confirmado, lo que se informa antes de pagar, la única devolución con su plazo [PENDIENTE], la anulación parcial por verificar y que no hay dinero real en el semestre.
- **Sección 6:**
  - punto 2: alta en Webpay Plus venta normal;
  - punto 3: la consulta legal deja el plan B del débito y suma proveedor, boleta, retracto y plazo de devolución;
  - punto 5: los convenios fijan precios, stock y cómo se aparta.
- **Secciones 7 y 8:** los precios fueron de ejemplo, y una nueva condición: un comercio entrega precios reales.

**`politica-privacidad.md`**
- **Sección 6, comercios en convenio:** la consulta de stock no lleva datos. El comercio que prepara, o el que lo reemplaza, ve solo sus productos, nunca la ficha ni la dirección. Hay dos [PENDIENTE]: el nombre de pila y el nombre de quien paga si la boleta va a su nombre.
- **Sección 6, Transbank:** crédito o débito, un solo cobro del total que se vio. Si hay devolución, va a la misma tarjeta, sin pedir datos nuevos.
- **Sección 4, nueva subsección "De tus pedidos"** (todavía no disponible): productos, precios, envío y total, el comercio que preparó, la dirección, el pago y la devolución. Los productos pueden revelar salud o dependencia.
- **Versión:** publicar como versión nueva, por ejemplo 0.10, y cambiar `POLITICA_VERSION`. Decide Jorge.

**`registro-tratamientos.md`:** nueva entrada "Pedidos y pagos de insumos (ADR-027), todavía no se trata". Contiene:
- finalidad, titulares y datos (los productos se tratan como sensibles mientras se consulta);
- base de licitud [PENDIENTE] y quién accede;
- la consulta de stock, que no trata datos;
- conservación (2 y 6 años), comunicaciones a comercios [PENDIENTE: encargados o responsables] y Transbank, y medidas.

**`pruebas-concepto/transbank.md`:** no reescribirlo. Agregar una actualización del 25 de octubre con dos ideas:
- La decisión de no limitar formas de pago se cumple mejor con venta normal.
- Los dos [PENDIENTE] se reemplazan por casos nuevos de venta normal, anulación parcial y retorno duplicado.

## Para la tarjeta de consulta legal

1. Figura de MATU frente a la familia: ¿revende o intermedia? ¿Aplica el art. 43 de la Ley 19.496?
2. Quién emite la boleta, a nombre de quién, y qué pasa si se retira en otro comercio a otro precio o si hay devolución (también tributario)
3. Retracto (art. 3 bis) en estos pedidos, y si hay excepciones para productos de higiene
4. Plazo legal de la devolución excepcional, si existe
5. Requisitos del reglamento de comercio electrónico de la Ley 19.496
6. Si los productos de un pedido, junto con un dato que identifica, son datos sensibles según la Ley 21.719, y con qué base de licitud se tratan
7. Comercios en convenio: ¿encargados o responsables?

Sale de la consulta legal: el plan B del débito.

## Hallazgos para la demo del viernes 30

- **Falta el aviso de piloto académico** con datos de prueba, en todas las pantallas (figura legal 4.1). Hoy solo dice "Demo con datos simulados".
- **Rótulo junto a los precios** (catálogo, lista, pedido y pago): "Precios de ejemplo. MATU todavía no tiene convenio con comercios, y en esta demo no se cobra dinero real." En la pasarela: "Pago de prueba. No se cobra dinero real." Se lee con texto al 200% y no se distingue solo por el color.
- **Nombres de comercios y productos ficticios**, sin marcas reales. Hay que verificar que "Farmacia Los Aromos" no sea un comercio real.
- **Si se aprueba el ADR-027,** dejan de corresponder los textos de la demo sobre la reserva del 15%, el monto real y la devolución con débito.

## Grado de certeza de las citas

- **Ley 19.496:**
  - art. 3 letra b, art. 12, art. 12 A y art. 30: seguro;
  - art. 3 bis: seguro de que regula el retracto, no de su alcance actual;
  - art. 43: seguro de su contenido general, no de que se aplique a MATU.
- **Ley 21.719:** sin citas de artículos.
- **Plazos de anulación de Transbank:** por verificar.

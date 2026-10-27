# Figura legal del piloto (MATU-27)

**Decisión:** tomada por Jorge Espinoza (Product Owner) el 24/10/2026
**Redacción:** analista normativo del equipo de agentes, a partir de la arquitectura, el backlog y la prueba de concepto de Transbank. Este documento no es asesoría legal.
**Aprobación del texto:** aprobado por Jorge Espinoza (Product Owner) el 25/10/2026. La revisión la hizo el orquestador del equipo de agentes, por delegación.
**Borrador ADR-027:** las secciones que empiezan con esa nota adaptan el texto al ADR-027 (arquitectura, sección 14) y a la revisión previa del analista normativo (`revision-previa-adr-027.md`). No están aprobadas. Hasta que Jorge las apruebe, rige el texto aprobado el 25/10/2026, que está en el historial del repositorio.

## 1. Contexto

> Borrador ADR-027 (27-10), por aprobar por Jorge.

- MATU es el proyecto de título de dos estudiantes. Hoy no existe una persona jurídica que lo respalde.
- Para cobrar con Webpay en producción se necesita un comercio dado de alta en Transbank, y el alta exige el RUT del comercio (arquitectura, sección 17).
- El objetivo del semestre se formuló sobre un entorno de demostración (arquitectura, secciones 17 y 18.1). Ninguna historia del semestre necesita cobros reales para darse por terminada.
- La política de privacidad v0.9 declara que el piloto no trata datos reales. Las versiones 0.x significan sin datos reales. La 1.0 es la primera revisada por un abogado.
- La Ley 21.719 entra en vigencia plena el 01/12/2026, antes del cierre del semestre. La consulta legal sobre el cuidador de hecho sigue abierta.
- La prueba de concepto de Transbank (S0-E) confirmó que la captura diferida cobra el monto real y revierte sin cobrar, y que opera solo con crédito.
- El ADR-027, aprobado por Jorge el 26/10/2026, reemplazó la captura diferida y el plan B del débito (ADR-006): MATU cobra una sola vez el total confirmado, en venta normal de Webpay Plus, y crédito y débito funcionan igual. La prueba de concepto verificó la captura diferida, no la venta normal.

## 2. Opciones consideradas

| Opción | Qué exige | Resultado |
|---|---|---|
| Constituir una persona jurídica durante el semestre | Constitución, inicio de actividades y alta comercial en Transbank. Plazo y costo: [PENDIENTE, no se estimaron porque se descartó la opción] | Descartada. No cabe en la ventana de construcción y el entregable no la necesita |
| Operar en el ambiente de integración de Transbank y declararlo en el informe | Nada externo al equipo | **Elegida** |

## 3. Decisión

Durante el semestre, el piloto de MATU opera solo en el ambiente de integración de Transbank, con datos sintéticos y sin cobros reales. Esto se declara en el informe.

La constitución de una persona jurídica y el alta comercial en Transbank quedan para después del semestre. Por eso el trámite de alta comercial no se inicia durante el semestre, como pide el criterio de MATU-27.

## 4. Qué implica

### 4.1 Lo que se puede hacer

> Borrador ADR-027 (27-10), por aprobar por Jorge.

- Demostrar el flujo de pago completo con las credenciales de integración de Transbank y sus tarjetas de prueba, en venta normal de Webpay Plus, con crédito y con débito. [PENDIENTE: verificar que el comercio de integración de venta normal ofrece débito]
- Mostrar un catálogo con precios de ejemplo, rotulados como tales junto a cada precio. Texto propuesto por el analista normativo: "Precios de ejemplo. MATU todavía no tiene convenio con comercios, y en esta demo no se cobra dinero real." [PENDIENTE: texto definitivo del diseñador y de docs/lenguaje.md]
- Usar datos sintéticos generados por las fábricas de prueba o escritos por el equipo.
- Mostrar la aplicación al profesor, a la comisión y a quienes evalúan el proyecto.
- Desplegar un ambiente de demostración con un aviso visible en todas las pantallas: es un piloto académico y usa solo datos de prueba. Texto exacto: [PENDIENTE, sale de docs/lenguaje.md]
- Conversar con comercios sobre un eventual convenio, sin compromisos de dinero ni pedidos reales.

### 4.2 Lo que no se hace

> Borrador ADR-027 (27-10), por aprobar por Jorge.

- Presentar precios de ejemplo como si fueran reales, o usar el nombre de un comercio real.
- Ingresar datos de personas reales: ni de personas cuidadas, ni de familias, ni de cuidadoras, ni de las personas entrevistadas.
- Cobrar dinero real o usar credenciales de producción de Transbank.
- Recibir, ver o guardar datos de tarjetas. Webpay captura la tarjeta en su propio formulario, y MATU solo recibe el resultado de la transacción.
- Abrir el registro al público o captar familias.
- Enviar mensajes a teléfonos o correos de personas fuera del equipo. Los envíos de prueba van a buzones y números del equipo o a un servicio de pruebas.
- Despachar pedidos reales con un comercio.

### 4.3 Los pocos datos reales que existen igual

Aunque el producto use datos sintéticos, existen algunos datos personales reales: las cuentas que use el equipo y los registros técnicos del servidor de demostración.

- Las cuentas de prueba usan correos ficticios de dominios reservados para ejemplos (example.com, .test o .invalid).
- Si una persona fuera del equipo prueba la demostración, usa una cuenta de prueba que le entrega el equipo.
- Si el ramo exige pruebas de usabilidad con personas: [PENDIENTE, definir cómo se hacen sin que ingresen datos reales]
- Si entra un dato real por error, se borra de inmediato, como compromete la política v0.9.

### 4.4 Responsable del tratamiento durante el piloto académico

Durante el semestre, el responsable es el equipo del proyecto, Jorge Espinoza y Martín Henríquez, como personas naturales.

- Contacto: [PENDIENTE, correo del proyecto]
- Qué trata: cuentas de prueba y registros técnicos de la demostración. Ningún dato real de salud ni de dependencia.
- Rol de la institución: [PENDIENTE, confirmar con el ramo si la institución tiene algún rol respecto de los datos del piloto]
- Las entrevistas de validación se rigen por su propio protocolo y no por este documento.

## 5. Cómo se paga (ADR-027)

> Borrador ADR-027 (27-10), por aprobar por Jorge.

La aplicación no debe limitar las formas de pago (decisión del 24/10/2026, registrada en `docs/pruebas-concepto/transbank.md`). El ADR-027 lo cumple con un solo cobro que funciona igual con crédito y con débito, y reemplaza el plan B del ADR-006 que ocupaba esta sección.

- **Un solo cobro del total confirmado.** Productos a precio exacto con IVA más un envío único por pedido, en venta normal de Webpay Plus. No hay reserva con margen, captura diferida ni cobros después.
- **El total confirmado vale 15 minutos.** Si vence, se vuelve a confirmar y la pantalla lo dice. No pagar no tiene costo.
- **Antes de pagar, la familia ve:** los productos con cantidad, precio y subtotal; los que salieron por no disponibles; los que cambiaron de precio o de comercio respecto de la lista; el envío y el total con IVA; quién emite la boleta; la ventana de entrega; y qué pasa si falta un producto, con el medio y el plazo de la devolución. Acepta las condiciones del pedido y recibe un comprobante.
- **Quién vende.** MATU vende y emite una sola boleta por el total, con el envío incluido. Los comercios le cobran a MATU por cuenta corriente y no ven el nombre de nadie, solo la referencia del pedido y el código de retiro. Vender de verdad exige la persona jurídica de la sección 6. [PENDIENTE: consulta legal y tributaria sobre MATU como vendedor y sobre el documento tributario cuando hay devolución]
- **Cancelación.** Después de pagar, la familia puede cancelar sin costo mientras el comercio no empiece a preparar, y se le devuelve el total.
- **La única devolución.** Si al retirar falta un producto, se busca el mismo producto en otro comercio en convenio, y MATU asume la diferencia de precio. Nunca se cambia por otra marca. Si ningún comercio lo tiene, se devuelve su precio a la misma tarjeta, por anulación de Webpay Plus, y se avisa a la familia en el momento. Si no se entrega ningún producto, se devuelve también el envío. Texto que ve la familia: "Si un producto no llega, te devolvemos su precio el mismo día, a la misma tarjeta. Cuándo lo ves en tu cuenta depende de tu banco." [PENDIENTE: consulta legal sobre el plazo legal de la devolución, si existe]
- [PENDIENTE: verificar en integración, antes del sprint 4, que se admite la anulación parcial de una venta normal con crédito y con débito, y los plazos máximos de anulación de Transbank. Si no se admite, se define otro medio sin pedir datos bancarios a la familia, salvo que se apruebe como tratamiento nuevo]
- [PENDIENTE: consulta legal sobre el retracto en estos pedidos]
- Nada de esto mueve dinero real durante el semestre. Después del semestre, el alta comercial cubre la venta normal de Webpay Plus.

## 6. Qué se hace después del semestre

> Borrador ADR-027 (27-10), por aprobar por Jorge.

Antes de tratar datos reales o cobrar dinero real, en este orden:

1. Constituir la persona jurídica, con inicio de actividades, porque MATU vende y emite la boleta (sección 5). Tipo, plazo y costo: [PENDIENTE]
2. Alta comercial en Transbank a nombre de la persona jurídica, en Webpay Plus venta normal (sección 5).
3. Resolver la consulta legal: cuidador de hecho, registro escrito por una cuidadora remunerada, y lo que abrió el ADR-027: MATU como vendedor y la boleta, el retracto, el plazo legal de la devolución, si los productos del pedido son datos sensibles y si los comercios en convenio son encargados o responsables. [PENDIENTE: consulta legal]
4. Política de privacidad 1.0 revisada por un abogado, con la persona jurídica como responsable. `POLITICA_VERSION` pasa a 1.0, y los consentimientos otorgados con versiones 0.x no sirven para datos reales.
5. Registro de tratamientos y contratos con los encargados de tratamiento: infraestructura y comercios. [PENDIENTE: consulta legal sobre si los comercios son encargados o responsables] Los convenios fijan los precios exactos, el stock y cómo se aparta un producto.
6. Clave maestra en un servicio de custodia, fuera del servidor de aplicación (arquitectura, sección 11.4 y ADR-016).
7. El aviso de piloto académico se retira solo cuando los puntos 1 a 6 están cumplidos.

## 7. Cómo se declara en el informe

> Borrador ADR-027 (27-10), por aprobar por Jorge.

Texto propuesto:

> Durante el semestre, MATU operó como piloto académico. Todos los datos de personas cuidadas, familias y pedidos fueron sintéticos, y los precios del catálogo fueron de ejemplo, sin convenio con comercios. Los pagos se demostraron en el ambiente de integración de Transbank, en venta normal, con tarjetas de prueba y sin cobros reales. MATU no recibe ni guarda datos de tarjetas. El proyecto no cuenta con persona jurídica, y por eso no inició el alta comercial en Transbank. Operar con familias reales exige constituirla, completar el alta comercial, resolver la consulta legal sobre quién autoriza el tratamiento de los datos de una persona sin capacidad para consentir y publicar una política de privacidad revisada por un abogado.

## 8. Cuándo se revisa esta decisión

> Borrador ADR-027 (27-10), por aprobar por Jorge.

- Si aparece la necesidad de operar con una familia real durante el semestre. Esta decisión no lo permite, así que se reabre.
- Si un comercio acepta un convenio con dinero real.
- Si un comercio entrega precios reales para el catálogo.
- Si el ramo exige operación real.

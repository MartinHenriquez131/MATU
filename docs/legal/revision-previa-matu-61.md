# Revisión previa del analista normativo · MATU-61 · Pedido: carrito y qué hacer si falta un producto (RF-21)

**10 de noviembre de 2026, noche** · Agente analista normativo, a pedido de Jorge · Estado: **decisiones de Jorge en curso el 11-11 (sección 7)**

Esto no es asesoría legal. El informe sirve para que Jorge decida. Lo que queda en REQUIERE CONSULTA LEGAL va a [`consulta-legal.md`](consulta-legal.md); la próxima pregunta es la CL-52. Nota del orquestador: la revisión de MATU-55 del mismo día también propuso una CL-52 distinta; esa queda como CL-53.

**Qué se revisó.** En `docs/`: el ADR-027, la arquitectura (8.1 a 8.4, 11, 11.8, 18 y 18.1), el modelo de datos 4.5, la política v0.11, el registro de tratamientos, `consulta-legal.md`, `investigacion-normativa-adr-027.md`, `revision-previa-adr-027.md`, `revision-matu-72.md`, `figura-legal-piloto.md` y `lenguaje.md` (11, 24 y 27). En el código, solo para saber qué existe: `0002_precios_exactos_un_cobro.py`, `backend/db/01_esquema.sql` y `care_circle` (borrado, autorizaciones y personas).

**Cuatro avisos:**
- El ADR-024 no tiene archivo propio. Está en la arquitectura, sección 14.
- `docs/sprints/` no tiene el backlog del sprint 4.
- `condiciones-pedido.md` no existe (R13). El borrador está en la sección 6.
- El módulo `ordering` no existe todavía, así que los veredictos son sobre el diseño de la tarjeta y el esquema actual.

**Nota del orquestador:** el analista leyó solo el README del spike de Transbank y dijo que no había resultados registrados. Sí los hay: están en [`pruebas-concepto/transbank.md`](../pruebas-concepto/transbank.md), sección «Venta normal», fusionada en MATU #64 el 10-11.

## 1. Veredicto por punto

| # | Punto | Veredicto | Condición |
|---|---|---|---|
| 1 | **R1 · Resumen completo antes de pagar** | **NO CUMPLE** todavía | Está diseñado (arquitectura 8.2), pero falta construirlo. Es de MATU-61, porque se muestra con el total confirmado. **C1:** el resumen lleva:<br>• productos con cantidad, precio y subtotal;<br>• los que salieron y los que cambiaron de precio o de comercio;<br>• la elección de RF-21;<br>• el envío aparte;<br>• el total con IVA y hasta qué hora vale;<br>• quién vende, con «piloto académico, sin persona jurídica», y quién emite la boleta;<br>• la ventana de entrega (`pedido.ventana_entrega` existe, pero nadie la llena);<br>• qué pasa si falta un producto, con el medio y el plazo de devolución;<br>• el retracto, el canal de reclamo, el enlace a las condiciones y una salida sin costo |
| 2 | **R2 · Retracto junto al precio** | **CUMPLE** con condiciones | Los textos ya existen y están aprobados (`lenguaje.md` 27), y siguen el Decreto 52, art. 6, según la investigación del 27-10. **C2:** van en cada línea del carrito y del resumen, con letra no menor que la del precio. **C3:** al confirmar, la línea guarda una copia de `producto.retracto_pierde_al_abrir` |
| 3 | **R3 · «Arrepentirme de la compra» durante 10 días** | **NO CUMPLE**, fuera del alcance | Necesita un pedido entregado, que llega con MATU-63. **C4:** confirmar que está en el checklist de MATU-63. Los 10 días dependen de la confirmación escrita (R4, MATU-62). Sin ella, el plazo es de 90 días (Ley 19.496, art. 3 bis, según la investigación) |
| 4 | **R5 · Versión aceptada de las condiciones** | **NO CUMPLE** | **C5:** en `pedido`, `condiciones_version`, `condiciones_aceptadas_en` y `condiciones_huella` (SHA-256, como la política 0.11), y un `CHECK`: no hay `pagado_en` sin `condiciones_aceptadas_en` |
| 5 | **R13 · Condiciones del pedido** | **NO CUMPLE** | No existe. Borrador en la sección 6 |
| 6 | **R12 · Autorización de pedidos, expresa y separada** | **NO CUMPLE** | El `CHECK` de `consentimiento.finalidad` admite `despacho`, pero la finalidad falta en el código:<br>• `FINALIDADES_QUE_SE_OTORGAN` (`autorizaciones.py:105`) y `FINALIDADES_RETIRABLES` (`retiro.py:29`) no la tienen;<br>• el borrado no la toca;<br>• no hay declaración.<br><br>La política (§3 y §4) promete «una autorización aparte». Ver D1 |
| 7 | **R15 · Cancelar sin costo también en `enviado_a_comercio`** | **CUMPLE** en el diseño | **C6:** la prueba de las 289 transiciones lo cubre, y también prueba que la familia **no** cancela desde `preparando`. En MATU-61 solo se cancela antes de pagar |
| 8 | **Dirección y minimización (A5)** | **CUMPLE** con condiciones | **C7:** pedirla antes de confirmar el total. **C8:** `lat` y `lng` siempre nulas en `direccion` y en `pedido_entrega`, con un `CHECK` o quitando las columnas (la política §4 dice «No guardamos su ubicación en el mapa»). **C9:** `referencia` con largo máximo y una ayuda contra los datos de salud. **C10:** la cambian el admin y el cuidador; el pagador la ve y no la cambia; otro grupo recibe 404; se audita sin el contenido. **C11:** la política §4 todavía dice «al registrarla». Ver D4 |
| 9 | **RF-21 · Si falta un producto** | **CUMPLE** con condiciones | Nunca otra marca: lo aseguran el `CHECK` `otro_comercio`/`quitar` y el trigger `pedido_linea_mismo_producto`. Que la opción por omisión sea otro comercio es aceptable, porque la familia paga lo mismo y la ve antes de pagar. **C12 (R9):** la regla queda fija al pagar, y hoy ningún trigger lo asegura (`pedido_linea_pagada_fija` no cubre `regla_sustitucion`). **C13 (R9):** solo el admin y el cuidador escriben la regla, con políticas por operación. **C14:** el texto no promete más que «lo buscamos y, si nadie lo tiene, anulamos su cobro» |
| 10 | **Borrado de la persona (MATU-72)** | **NO CUMPLE** con el esquema actual | En el pedido quedan `destinatario_nombre_pila`, la dirección y el teléfono de `pedido_entrega`. Los pedidos sin pagar no se tocan. Si hay una reposición programada, el borrado falla: `plan_reposicion_linea.perfil_consumo_id` no tiene `ON DELETE`, y `efecto_retiro.py:27` borra los perfiles. Ver D2 y D3 |
| 11 | **Auditoría** | **NO CUMPLE** todavía | `EntidadAuditoria` no tiene `pedido` ni `direccion`, y `test_auditoria.py` hoy rechaza `direccion`. Ver D12 |
| 12 | **Conservación de los pedidos** | **REQUIERE CONSULTA LEGAL** (CL-28) y **NO CUMPLE** en los no pagados | Nada justifica guardar 2 años un borrador abandonado, un total vencido o un cancelado sin pago. Además, `idempotencia.respuesta` guarda el cuerpo completo (productos y dirección), con `expira_en` de 24 h, y ninguna tarea lo borra. Ver D5 |
| 13 | **Ley 19.496 · Precio, cobro y retracto** | **CUMPLE** en el diseño, con dos puntos en consulta | Cumplen el precio exacto con IVA, el envío separado, el total fijo al pagar, la salida sin costo y los cambios marcados (arts. 3 b) y 30; Decreto 6, arts. 11 y 18, según la investigación). **C15:** el cambio de precio se marca contra el precio que la familia vio en el carrito, que se guarda en el borrador. En consulta: CL-41 (retracto del suplemento y las bolsas) y CL-46 (boleta) |
| 14 | **Ley 21.719 · El pedido como dato de salud indirecto** | **REQUIERE CONSULTA LEGAL** (CL-11 y CL-12) | Mientras tanto, se trata como dato sensible:<br>• **C16 (R7):** `pedido.destinatario_nombre_pila` sale en la migración de MATU-61, y la proyección del comercio excluye `grupo_id`, `persona_cuidada_id`, `creado_por` y las transiciones;<br>• **C17:** productos, cantidades, dirección y teléfono nunca en logs, errores, eventos, auditoría ni URL, con `Cache-Control: no-store`;<br>• **C18:** el carrito vive en el servidor como borrador, nunca en `localStorage` ni `sessionStorage`;<br>• **C19:** `pedido_transicion.motivo` es una lista cerrada;<br>• **C20:** el servidor no lee `perfil_consumo` para crear el pedido, así no se mezclan finalidades y CL-17 no se activa;<br>• **C21:** la autorización de pedidos debe estar VIGENTE según el `Reloj`, con la revisión de 12 meses al día; si no, 403 |
| 15 | **R6 · Consulta de stock sin datos** | **CUMPLE** en el diseño | **C22:** una referencia opaca aleatoria por pedido, y mejor una distinta por comercio, con prueba |
| 16 | **R8 · Cada comercio ve solo sus líneas** | **NO CUMPLE** en el esquema | `pedido.comercio_id` es `NOT NULL` y único (ADR-024), y las líneas heredan por esa columna. Con dos comercios, uno vería las líneas del otro o ninguno vería las suyas. Ver D7 |
| 17 | **Accesibilidad (Ley 20.422 como marco, WCAG)** | **CUMPLE** con condiciones | **C23 (WCAG 2.2.1):** avisar antes de que venzan los 15 minutos y ofrecer «Volver a confirmar» con un toque, sin perder el carrito. **C24 (U4):** cantidad con botones de 48 px, con nombre accesible y un campo numérico. **C25:** «salió», «cambió» y «vencido» con texto y región viva, no solo con color. Sin desplazamiento horizontal a 320 px con el texto al 200 % |
| 18 | **«Pedir» desde la lista** | **REQUIERE DECISIÓN** | `lenguaje.md` dice «La lista nunca ofrece comprar». Ver D10 |

## 2. Decisiones para Jorge (con la recomendación del analista)

- **D1 · Autorización de pedidos (R12):**
  - **Qué finalidad:** (A) `despacho`, que ya está en el `CHECK`, o (B) una nueva, `pedidos`. Se recomienda **A**.
  - **Cuándo se pide:** la primera vez que se toca «Pedir».
  - **Quién la da:** el admin y el cuidador, en la calidad de MATU-07, con revisión a los 12 meses y `declaracion_pedidos_<calidad>` con su huella.
  - **Cómo se retira:** en Grupo familiar, sumándola a `FINALIDADES_RETIRABLES` y al borrado.
  - **Al retirarla:** los pedidos sin pagar pasan a `cancelado` y se borra su `pedido_entrega`. Los pagados siguen su plazo (CL-44).
- **D2 · El pedido de una persona borrada:**
  - **El nombre:** sale con C16.
  - **La dirección y el teléfono, tres opciones:**
    - (A) en la misma transacción, los pedidos sin pagar se cancelan y se borra su entrega; los cerrados quedan solo con la comuna; los pagados en curso, hasta cerrarse; productos y montos siguen su plazo, sin verse después del retracto;
    - (B) conservar la dirección completa 2 años;
    - (C) responder 409 si hay un pedido en curso, lo que contradice la política §10.
  - Se recomienda **A**, con la CL-52 nueva y la CL-44 ampliada. En MATU-61 solo hay pedidos sin pagar.
- **D3 · `plan_reposicion_linea.perfil_consumo_id`:** (A) `ON DELETE SET NULL` con su prueba, (B) `CASCADE` o (C) no tocarlo. Se recomienda **A**, en la migración de MATU-61. También afecta a `consumo_conservar`. Queda una condición para la fase 2: el borrado y el retiro cancelan los `plan_reposicion` de la persona.
- **D4 · La dirección:**
  - (A) en `direccion`, unida por `persona_cuidada.direccion_entrega_id`, copiada a `pedido_entrega` al confirmar, o (B) solo en `pedido_entrega`, pedida cada vez. Se recomienda **A**.
  - **La ruta:** una propia (por ejemplo `PUT /v1/personas/{id}/direccion`), con `If-Match`, para el admin y el cuidador, con 404 a otro grupo y auditando `direccion.cambiar`.
  - **El teléfono de contacto:** por omisión el celular verificado de quien pide, editable. Si es el de otra persona, se le pide avisarle (CL-33).
- **D5 · Lo que no se pagó:** (A) borrarlo a los 30 días con el programador de MATU-74, y que `idempotencia` guarde solo el estado y el id y se borre al vencer, o (B) guardar todo 2 años. Se recomienda **A**. Hace falta que `pedido_transicion` se borre en cascada o un orden de borrado.
- **D6 · Las condiciones:**
  - la casilla «Leí y acepto las condiciones del pedido.» va en el resumen;
  - se guarda al tocar «Pagar» (MATU-62);
  - las columnas y el `CHECK` se crean en MATU-61;
  - las condiciones tienen versión propia.
- **D7 · Varios comercios (R8):** (A) un registro por comercio, como dice el ADR-027, o (B) visibilidad por línea según `oferta.comercio_id`. Se decide en esta migración. Las dos cumplen si cada comercio ve solo sus líneas y su referencia, así que elige el backend.
- **D8 · El resumen en el piloto:**
  - vendedor: «MATU, piloto académico, sin persona jurídica»;
  - boleta: «En este piloto no se emite boleta»;
  - una ventana de entrega fija de ejemplo;
  - **canal de reclamo:** lo decide Jorge. Si es `cuidaconmatu@gmail.com`, se amplía la finalidad del buzón (registro, entrada 11).
- **D9 · «(comercio ficticio)»:** (A) agregar `comercio.ficticio boolean NOT NULL DEFAULT true` y entregarlo en la API, o (B) dejarlo para el convenio real. Se recomienda **A**. El convenio debe autorizar a publicar el nombre de fantasía, los precios y el stock.
- **D10 · «Pedir» en la lista:** agregar «Pedir estos productos» solo con la autorización vigente, y cambiar `lenguaje.md` a «La lista nunca compra sola». La alerta sigue sin generar pedidos.
- **D11 · La política:** activar los pedidos agrega usos, datos y destinatarios, así que corresponde publicar la 0.12 en el mismo PR.
- **D12 · Qué se audita:**
  - `consentimiento.otorgar` y `consentimiento.revocar` de `despacho`;
  - `direccion.cambiar`;
  - `pedido.crear`, `pedido.confirmar` y `pedido.cancelar`;
  - `pedido.regla_faltante`.

  Todo sin contenido. Las lecturas no se auditan (decisión 52), porque la línea de tiempo la da `pedido_transicion`.

## 3. Documentos que habría que actualizar

- **`registro-tratamientos.md`:**
  - **entrada 2:** la dirección, el teléfono de contacto, la autorización `despacho`, las condiciones con versión y huella, la conservación de lo no pagado (D5), los efectos del borrado (D2) y del retiro, la auditoría (D12), el cierre del [PENDIENTE] de R7 y el retracto copiado por línea;
  - **entrada 1:** la dirección se pide con el primer pedido;
  - **entrada 5:** «Pedir» y C20;
  - **entrada 11:** solo si el buzón pasa a ser canal de reclamo.
- **`politica-privacidad.md` 0.12:**
  - §3.6 y §4, «De tus pedidos»;
  - §4, la dirección (C11) y que no se guarda la ubicación;
  - §6, sin nombre (R7) y cada comercio solo sus líneas (R8);
  - §8, los plazos;
  - §10, el borrado y el retiro;
  - §12, la versión.
- **`condiciones-pedido.md`:** nuevo, con el borrador de la sección 6.
- **`consulta-legal.md`:** la CL-52 nueva, y ampliar las CL-44, CL-33 y CL-28.
- **`figura-legal-piloto.md` §5:** remitir a las condiciones.
- **Fuera de `docs/legal/`:** el modelo de datos 4.5 (columnas nuevas, `destinatario_nombre_pila` y R8) y la arquitectura 11.8 (la conservación de lo no pagado).

## 4. Textos propuestos para `lenguaje.md`, sección «Pedido (MATU-61)» [PROPUESTO]

Sin términos prohibidos y sin «stock».

- **Autorización:**
  - «Para pedir desde MATU, primero autoriza los pedidos. Sin esta autorización igual puedes imprimir o compartir la lista.»
  - Botón: «Autorizar los pedidos».
  - Declaración: «Autorizo a MATU a guardar los pedidos de insumos para `{nombre_pila}`, con los productos, la dirección de entrega, el teléfono de contacto y el pago, para preparar, entregar y responder por cada pedido, según la política de privacidad vigente.», con una variante por calidad, como `declaracion_consumo_<calidad>`.
- **Carrito:**
  - Título: «Tu pedido». Bajada: «Revisa los productos y cuántos quieres. Antes de pagar confirmamos que haya.»
  - Cantidad: «Agregar uno», «Quitar uno» y «Cantidad de `{producto}`».
  - «Sacar del pedido».
  - Vacío: «Tu pedido está vacío. Agrega productos desde el catálogo o desde tu lista de insumos.»
- **RF-21, en cada línea:**
  - Pregunta: «Si falta este producto».
  - Primera opción, marcada: «Buscarlo en otro comercio», con la ayuda «El mismo producto. Pagas lo mismo.».
  - Segunda opción: «Sacarlo del pedido y devolverme su precio».
  - Nota: «Nunca lo cambiamos por otra marca ni por otro producto.»
- **Dirección:**
  - Título: «¿Dónde lo entregamos?». Ayuda: «La usamos solo para entregar tus pedidos. Ningún comercio la ve.»
  - Campos: Calle, Número, Depto (opcional), Comuna y Referencia (opcional).
  - Ayuda de la referencia: «Por ejemplo: portón verde. No escribas datos de salud.»
  - Teléfono de contacto: «Para que quien entrega pueda avisarte. Si es el de otra persona, avísale.»
  - Botón: «Cambiar dirección».
- **Confirmar y resumen:**
  - «Ver el total», y mientras espera: «Estamos confirmando que haya cada producto…»
  - Título: «Antes de pagar».
  - Cambios: «Ya no hay `{producto}`. Salió del pedido.», «Ahora lo prepara `{comercio}`.» y «Cambió el precio: antes `{precio}`, ahora `{precio}`.»
  - Montos: «Envío (uno por pedido)» y «Total con IVA».
  - Plazo: «Este total vale hasta las `{HH:MM}`.» y «Quedan 2 minutos para pagar este total.»
  - Vencido: «Pasaron 15 minutos y el total venció. Vuelve a confirmar para ver lo que hay y su precio.», con el botón «Volver a confirmar».
  - Cobro: «Se cobra una sola vez este total, con crédito o con débito. No hay reserva ni cobros después.»
  - Vendedor: «Vende: MATU, piloto académico, sin persona jurídica. En este piloto no se emite boleta.»
  - Entrega: «Entrega: `{ventana}`».
  - Si falta: «Si al retirar falta un producto, lo buscamos en otro comercio y pagas lo mismo. Si nadie lo tiene, o elegiste sacarlo, anulamos su cobro el mismo día, a la misma tarjeta. Cuándo lo ves en tu cuenta depende de tu banco.»
  - Retracto: los textos de la sección 27, en cada línea.
  - Reclamos: «Reclamos: escríbenos a `{correo}`.» (según D8).
  - Condiciones: «Leí y acepto las condiciones del pedido.», con el enlace «Condiciones del pedido».
  - Salida: «No pagar no tiene costo.»
  - El aviso de piloto de la sección 11, una vez por pantalla.
- **Cancelar y errores:**
  - «Cancelar pedido», con la confirmación «¿Cancelar este pedido? No tiene costo.» y los botones «Cancelar pedido» y «Seguir con el pedido».
  - 404: «No encontramos este pedido.»

## 5. Consulta legal

- **CL-52 (nueva):** después de un borrado pedido por la persona, ¿se puede conservar la dirección y el teléfono de entrega durante el plazo de los pedidos, o basta la comuna una vez cerrado el pedido? ¿Cuánto tiempo después de la entrega se justifica guardar la dirección completa por reclamos? Se relaciona con las CL-27 y CL-28.
- **CL-44 (ampliar):** el borrado de la persona con un pedido pagado en curso.
- **CL-33 (ampliar):** la base de licitud del teléfono de contacto de alguien que no es usuario.
- **CL-28 (ampliar):** confirmar que lo nunca pagado no se guarda 2 años.
- **Siguen abiertas y aplican:** CL-11, CL-12, CL-17 (C20 evita activarla), CL-41 y CL-46.

## 6. Borrador de `condiciones-pedido.md` (R13), por aprobar

```markdown
# Condiciones del pedido de MATU

**Versión 0.1 · borrador para el piloto académico.** La aprueba Jorge Espinoza. No es asesoría legal. En el piloto no se cobra dinero real.

## 1. Quién vende
Durante el piloto vende MATU, piloto académico, sin persona jurídica. En el piloto no se emite boleta. [PENDIENTE: persona jurídica y boleta, CL-46 y CL-47]

## 2. Qué compras y cuánto pagas
- Cada producto tiene un precio exacto con IVA, del comercio en convenio que lo prepara.
- Se suma un solo envío por pedido, aunque lo preparen varios comercios.
- Antes de pagar confirmamos que haya cada producto. Lo que no hay sale del pedido y lo ves antes de pagar.
- El total confirmado vale 15 minutos. Si vence, se vuelve a confirmar y te mostramos lo que cambió.
- Se cobra una sola vez ese total, con crédito o con débito. No hay reserva ni cobros después.

## 3. Si falta un producto
Antes de pagar eliges, por cada producto, si lo buscamos en otro comercio o si lo sacamos del pedido. Si no eliges, lo buscamos.
- Si lo buscamos y otro comercio lo tiene, pagas lo mismo que aceptaste. La diferencia de precio la asume MATU.
- Nunca lo cambiamos por otra marca ni por otro producto.
- Si nadie lo tiene, o elegiste sacarlo, anulamos su cobro el mismo día, a la misma tarjeta. Si no se entrega ningún producto, devolvemos también el envío. Cuándo lo ves en tu cuenta depende de tu banco.

## 4. Cancelar
- Antes de pagar, no seguir no tiene costo.
- Después de pagar, puedes cancelar sin costo mientras el comercio no empiece a preparar, y te devolvemos el total.

## 5. Entrega
Te informamos la ventana de entrega antes de pagar. Si no podemos cumplirla, te avisamos y eliges entre esperar o recibir la devolución. [PENDIENTE: ventana y zona de entrega]

## 6. Derecho a retracto
Tienes 10 días desde que recibes el producto. En los productos de uso personal o de higiene sellados, se pierde solo si abres el sello. MATU devuelve también el envío y paga el retiro. Lo pides en el pedido entregado, con «Arrepentirme de la compra». [PENDIENTE: CL-41, suplemento y bolsas colectoras; medio de devolución si se pasa el plazo de anulación de Transbank]

## 7. Si algo no llega
MATU responde ante ti y devuelve el mismo día lo que no se entregó. Estas condiciones no limitan ninguna indemnización que corresponda.

## 8. Reclamos
[PENDIENTE: canal de reclamo, decisión D8]

## 9. Tus datos
Los pedidos se tratan como datos sensibles. Ningún comercio ve tu nombre, el de la persona que cuidas ni la dirección. Lo demás está en la política de privacidad vigente.

## 10. Versión
Guardamos qué versión de estas condiciones aceptaste, cuándo, y una huella del texto exacto que viste.
```

## Certeza de las citas

- **Seguras:** Ley 19.496, arts. 3 b), 12 A y 30, y WCAG 2.2.1.
- **Según la investigación del 27-10, sin releerlas:** el art. 3 bis b) de la Ley 19.496, y los Decretos 52 (art. 4 N° 4 y art. 6) y 6 (arts. 11 y 18).
- **Sin citas propias:** la Ley 21.719. La Ley 20.422 no se cita por artículo.

## 7. Decisiones de Jorge (11 de noviembre)

- **D1 · Autorización de pedidos:** se acepta la recomendación completa. Finalidad `despacho`. Se pide la primera vez que se toca «Pedir». La dan el admin y el cuidador, en la calidad de MATU-07, con revisión a los 12 meses y `declaracion_pedidos_<calidad>` con su huella. Se retira en Grupo familiar (`FINALIDADES_RETIRABLES` y el borrado). Al retirarla, los pedidos sin pagar pasan a `cancelado` y se borra su `pedido_entrega`, y los pagados siguen su plazo (CL-44).
- **D2 · El pedido de una persona borrada:** opción **A**. El nombre de pila sale del pedido (C16). En la misma transacción del borrado, los pedidos sin pagar se cancelan y se borra su `pedido_entrega`, los cerrados quedan solo con la comuna, y los pagados en curso conservan la dirección hasta cerrarse. Productos y montos siguen su plazo, sin verse después del retracto. En MATU-61 aplica solo la regla de los sin pagar. Con la CL-52 nueva y la CL-44 ampliada.
- **D3 · `plan_reposicion_linea.perfil_consumo_id`:** opción **A**, `ON DELETE SET NULL` con su prueba, en la migración de MATU-61. Para la fase 2 queda la condición: el borrado y el retiro cancelan los `plan_reposicion` de la persona.
- **D4 · La dirección:** opción **A**. Se guarda en `direccion`, unida por `persona_cuidada.direccion_entrega_id`, y se copia a `pedido_entrega` al confirmar. Ruta propia `PUT /v1/personas/{id}/direccion`, con `If-Match`, solo para el admin y el cuidador; el pagador la ve y no la cambia; otro grupo recibe 404; se audita `direccion.cambiar` sin el contenido. `lat` y `lng` siempre nulas (C8). El teléfono de contacto es por omisión el celular verificado de quien pide, editable, y si es de otra persona se le pide avisarle (CL-33).

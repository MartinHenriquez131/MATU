# Revisión previa del analista normativo · MATU-62 · Pago: cobrar el total exacto confirmado (ADR-027) · segunda revisión

**11 de noviembre de 2026, tarde** · Agente analista normativo, a pedido de Jorge · **Segunda revisión.** Para las decisiones reemplaza a la primera (`revision-previa-matu-62.md`, madrugada del 11-11). Las D-62-1 a D-62-12 quedan reescritas aquí y se agregan las D-62-13 a D-62-17. **Las decisiones las tomó el orquestador el 11-11 por delegación de Jorge (sección 7).**

Esto no es asesoría legal. Es un borrador para decidir. Lo que queda en REQUIERE CONSULTA LEGAL va a `consulta-legal.md`.

**Qué se leyó:**
- la primera revisión de MATU-62;
- la revisión de MATU-61, con las decisiones D1 a D12 de Jorge;
- los documentos de MATU-61 en la rama `docs/matu-61-pedido`: política 0.12, condiciones 0.1, registro, consulta legal, arquitectura (8.1 a 8.4, 9.4, 11.2, 11.8, 12.3 y 12.4), modelo de datos 4.5 y `lenguaje.md` 31;
- lo construido en la rama `matu-61-pedido` de MATU_PROYECTO: la migración 0023, la 0002 (para `cargo`, `participacion`, `transaccion_pasarela` y `pedido_pagado_fijo`), el esquema, el módulo `ordering`, el contrato (decisiones 188 a 221) y la especificación de pantallas;
- el informe de Transbank de Martín y `docs/pruebas-concepto/transbank.md`.

**Avisos:** `modules/payments/` no existe todavía, así que los veredictos son sobre el diseño, la 0023 y la 0002. Si la 0023 cambia antes de fusionarse, hay que revisar los puntos 2, 12 y 15.

## 1. Veredicto por punto

### 1.1 Los que cambian con MATU-61

| # | Punto | Veredicto | Por qué y qué falta |
|---|---|---|---|
| 2 | **R5 · versión aceptada de las condiciones** | **NO CUMPLE** todavía, por otros motivos | Las columnas ya existen (D6, 0023): `condiciones_version`, `condiciones_aceptadas_en` y `condiciones_huella`, y el `CHECK pedido_pago_con_condiciones` en `NOT VALID`. Quedan cuatro brechas: (a) la base no deja escribir al pagador (`pedido_familia_editar` exige admin o cuidador); (b) no queda quién aceptó (D-62-16); (c) las condiciones se pueden cambiar después del pago (`pedido_pagado_fijo` no las congela); (d) el `CHECK` sigue `NOT VALID` |
| 3 | **R10 · pago aprobado después de vencido** | **NO CUMPLE.** La contradicción de los documentos sigue, más acotada (sección 4) | MATU-61 agregó cinco caminos para que un pago llegue cuando su total ya no está: volver a confirmar un total vigente (C1), «Cambiar el pedido» (C1 y C9), cancelar sin pagar, el retiro de `despacho` (D1) y el borrado de la persona (D2). Ninguna regla los ordena frente a una venta en curso (D-62-4) |
| 5 | **R13 · condiciones del pedido** | **CUMPLE en parte.** Falta una versión 0.2 | Le faltan el pago tardío y el pago en curso, la confirmación escrita, qué pasa si la anulación falla, quién paga y quién cancela después de pagar, y que el comprobante no es una boleta. **Hallazgo:** «En el piloto no se cobra dinero real» está en la cabecera, fuera de la huella (decisión 221), así que no forma parte de lo que se acepta. Borrador en la sección 5.3 |
| 7 | **Idempotencia** | Diseño **CUMPLE**. Base **NO CUMPLE** todavía | Resuelto con D5: `idempotencia` ya no guarda el cuerpo. Faltan `transaccion_pasarela.token` único, una sola venta aprobada y no anulada por cargo, y que el retorno sea idempotente por token |
| 12 | **Conservación de los cargos** | **REQUIERE CONSULTA LEGAL** (CL-28 ampliada) y **NO CUMPLE** por un defecto nuevo | `cargo.pedido_id` es `NOT NULL UNIQUE REFERENCES pedido(id)` sin `ON DELETE`. `pedido_conservar` (0023) borra todo pedido sin pagar a los 30 días. Si un pedido sin pagar tiene un cargo (pago rechazado o abandonado), el `DELETE` falla por la clave foránea y **la conservación se detiene para todas las familias**. Va en la migración de MATU-62 (D-62-13) |
| 13 | **Ley 19.496** | **CUMPLE** en el diseño, con condiciones | El IVA va incluido en todos los precios. Con C1 el total cambia antes de pagar: la venta debe quedar atada al total pagado (`total_confirmado_en` y monto), y el `commit` los compara antes de marcar `pagado` (D-62-4) |
| 15 | **Políticas del pago** | **NO CUMPLE** | `cargo_familia`, `participacion_hereda` y `transaccion_hereda` siguen en `FOR ALL` sin rol. Además la 0023 dejó `pedido_operacion` en solo lectura y `transicion_crear` exige admin o cuidador: hoy nadie puede marcar `pagado`. MATU-62 agrega esos caminos, acotados (sección 2) |
| 17 | **Nuevo · el pagador y los 15 minutos** (WCAG 2.2.1) | **NO CUMPLE** la C23 de MATU-61 para el pagador | Con C3 el pagador no confirma, así que tiene un plazo que no puede extender. No es seguro que la excepción «esencial» aplique (D-62-14) |
| 18 | **Nuevo · pago en curso frente a cambios del pedido** | **NO CUMPLE** | Mientras se paga en Webpay, admin o cuidador pueden reconfirmar, volver al carrito, cambiar la regla o el teléfono, o cancelar. Nada lo impide ni lo registra (D-62-4) |
| 19 | **Nuevo · capa 3 apagada con un pago en curso** | **CUMPLE con una condición** | La conciliación sigue corriendo con la capa apagada (D-62-17) |

### 1.2 Los que siguen igual

1 (R4, confirmación escrita): NO CUMPLE, con la CL-54. 4 (R11, plazos de anulación): CUMPLE en el semestre. 6 (R14, `payload_respuesta`): NO CUMPLE. 8 (conciliación): NO CUMPLE, con `matu_scheduler` y una función `SECURITY DEFINER` como `pedido_conservar`. 9 (devolución): CUMPLE; después de pagar cancela solo el admin. 10 (datos de tarjeta): CUMPLE. 11 (logs): CUMPLE con condiciones; `token_ws` llega por GET. 14 (condiciones de Transbank): CUMPLE en integración. 16 (el retorno llega sin sesión): igual.

## 2. Migración de MATU-62

Lleva migración, después de la 0023. Contenido propuesto (la forma la decide el backend):
1. **Políticas por operación y por rol, sin `FOR ALL`:** `cargo` lo leen admin, cuidador y pagador (el observador no); lo crean admin y pagador; lo actualizan `sistema` (retorno y conciliación) y operación (anulación). `participacion` y `transaccion_pasarela` con las mismas reglas. `pedido` con dos caminos de `UPDATE` acotados por triggers: `sistema` u operación pasan `total_confirmado` o `vencido` a `pagado`; el pagador escribe solo las columnas de las condiciones. `pedido_transicion` admite actor `sistema` u `operacion` en esos casos. `REVOKE DELETE` a `matu_app` sobre `cargo`, `participacion` y `transaccion_pasarela`.
2. **Integridad del cobro:** la venta guarda `total_confirmado_en` y el monto, y un trigger exige que sean los del pedido al insertarla; al marcar `pagado`, monto igual al total y el mismo `total_confirmado_en`; una sola venta aprobada y no anulada por cargo; `token` único.
3. **R5:** las condiciones quedan fijas con `pagado_en`; `condiciones_aceptadas_por` (D-62-16); `VALIDATE CONSTRAINT pedido_pago_con_condiciones` si no hay filas que lo violen.
4. **R14:** `CHECK (payload_respuesta IS NULL)` y `ultimos4 ~ '^[0-9]{4}$'`.
5. **Conservación (D-62-13):** se reemplaza `pedido_conservar`.
6. **Conciliación:** `pagos_por_conciliar(limite)` `SECURITY DEFINER`, solo para el rol de la tarea, que devuelve solo identificadores.
7. **Pruebas:** en `test_aislamiento.py`, el observador y el cuidador no pagan, el pagador solo escribe las condiciones, otro grupo 404, nadie borra cargos. En `test_migraciones.py`, el ciclo completo y `pedido_conservar` con un cargo rechazado y con un pago tardío anulado.

## 3. Decisiones (recomendaciones del analista)

- **D-62-1 · Número de la migración:** (a) 0025 después de MATU-55, o (b) **0024**, intercambiada con MATU-55, que pasa a la 0025. Se recomienda (b), si MATU-55 sigue sin rama de código y la fila se actualiza el mismo día. Las 0026 a 0028 no cambian.
- **D-62-2 · Quién ve el detalle del pago:** se recomienda (c): quien pagó, y operación para soporte. El estado y los montos los ven admin, cuidador y pagador; el observador ve solo que está pagado.
- **D-62-3 · Correo de confirmación (R4):** (b) sin la lista de productos, solo a correos verificados; en el piloto se prueba sin enviarse. CL-54 ampliada.
- **D-62-4 · Pago en curso, pago tardío y total reemplazado:** tres reglas. (1) Con una venta `iniciada` o `autorizando`, los cambios voluntarios responden 409 `pago-en-curso`; cancelar, el retiro de `despacho` y el borrado no se bloquean. (2) El `commit` aprobado del mismo total (mismo `total_confirmado_en` y monto, estado `total_confirmado` o `vencido`) se respeta: se declara `vencido → pagado` (Ley 19.496, art. 12). (3) El `commit` aprobado de un total que ya no es el del pedido se anula completo el mismo día, a la misma tarjeta, se avisa, y el pedido no cambia de estado.
- **D-62-5 · Venta autorizada sin `commit`:** (a) el job hace el `commit`, midiendo antes en integración cuánto acepta Transbank un `commit` tardío.
- **D-62-6 · La anulación falla:** (a) reintentos, alerta a operación y aviso a la familia, sin pedir datos bancarios. La transferencia va a la CL-55.
- **D-62-7 · Comprobante del piloto:** «Pago de prueba. No se cobró dinero real. Este comprobante no es una boleta.» La regla de «Boleta» de `lenguaje.md` 31 admite este uso.
- **D-62-8 · Quién toca «Pagar»:** (a) admin y pagador. Exige la autorización `despacho` vigente (403), el total vigente y la casilla marcada por quien paga. El cuidador ve el resumen sin casilla ni botón, con una línea que dice quién paga. Un rol que no alcanza recibe 404.
- **D-62-9 · `payload_respuesta`:** (a) siempre nulo, con `CHECK`.
- **D-62-10 · Conservación de `transaccion_pasarela`:** (a) no se borra en el semestre, con PENDIENTE de 6 años (CL-28), acotado por D-62-13.
- **D-62-11 · Dónde nace el cargo:** al tocar «Pagar», en la misma transacción que la aceptación de las condiciones y la venta `iniciada`. Ruta `POST /v1/pedidos/{id}/pagar` con `Idempotency-Key`. Un cargo por pedido (`UNIQUE (pedido_id)`): un reintento reutiliza el cargo `pendiente` o `rechazado`. El pago tardío de un total reemplazado queda solo en `transaccion_pasarela`, como venta y anulación. Se corrigen la arquitectura 8.4 y 9.4.
- **D-62-12 · `Idempotency-Key`:** obligatoria en `pagar` (428, 422 `idempotencia-reutilizada`, 409 `idempotencia-en-curso`), y aparte 409 `pago-en-curso`. El retorno es idempotente por token.
- **D-62-13 · Nueva · La conservación con cargos:** (c) separar por dinero. Sin dinero (cargo `pendiente` o `rechazado`, ninguna venta aprobada), se borra con el pedido a los 30 días. Con dinero, aunque se haya anulado completo, se conservan el cargo, las transacciones y el pedido sin entrega 6 años, y las líneas, reglas y transiciones se borran a los 30 días si nunca quedó `pagado`. CL-28 ampliada.
- **D-62-14 · Nueva · El pagador y los 15 minutos:** (a) en el semestre se mantiene C3 y se mitiga: el aviso de los 2 minutos también para el pagador, y «Avisar a quien armó el pedido» cuando vence (puede quedar para MATU-41 o MATU-63). Martín mide en la usabilidad si un pagador alcanza a pagar, y se revisa C3 si no.
- **D-62-15 · Nueva · `pagar` con el total vencido:** 409 `estado-pedido` con `estado: vencido`, sin llamar a la pasarela ni crear la venta. Se corrige la 9.4, que decía 410. La transición `total_confirmado → vencido` la guarda la siguiente escritura de admin o cuidador (decisión 204).
- **D-62-16 · Nueva · Quién aceptó las condiciones:** (a) `pedido.condiciones_aceptadas_por`, dentro del `CHECK` «juntas o ninguna», congelado con `pagado_en`.
- **D-62-17 · Nueva · Capa 3 apagada con pagos en curso:** la conciliación y la anulación corren aunque la capa esté apagada; solo se apagan las rutas de la familia. Prueba en `test_capa3_desacoplable.py`.

## 4. La contradicción entre la arquitectura 8.1 y la 12.4

Sigue, más acotada. La 8.1 ya tiene `vencido → borrador` como acción de la familia (C9, decisión 218). La 12.4, caso 8, dice que `pagar` con el total vencido «vuelve a `borrador`» por sí solo. Eso no conviene: el pagador no puede cambiar el pedido (C3) ni la base lo deja, volver a borrador descarta el total y la entrega sin que nadie lo pida, y «Volver a confirmar» desde `vencido` es un solo toque.

**Recomendación: manda la 8.1.** La 12.4, caso 8, queda: «Con el `Reloj` adelantado, `pagar` responde 409 `estado-pedido` con `vencido`, no se llama a la pasarela, no se crea la venta y el pedido queda en `vencido`. Para seguir, quien armó el pedido vuelve a confirmar o usa "Cambiar el pedido".» En la 8.1 se agrega `vencido → pagado`, solo para un pago iniciado con el total vigente, y que un pago aprobado de un total que ya no es el del pedido se anula sin mover el estado. En la 8.4, el cargo al pagar, la ruta `POST /v1/pedidos/{id}/pagar` y el PENDIENTE de la vida del token, que fija cuánto dura `pago-en-curso`.

## 5. Documentos para el pago (borradores)

### 5.1 Política de privacidad, la versión que toque al fusionar

- **Cabecera y §12:** la versión nueva agrega el pago. No se pide aceptar de nuevo: el pago tiene su propia aceptación (las condiciones) y `despacho` ya cubre los productos (CL-24).
- **§3.6:** «…y pagarlo en la página de Transbank. Te mostramos un comprobante y te lo enviamos por correo.»
- **§4, «De tus pedidos»:** las condiciones que aceptó quien pagó, con versión, fecha y huella; el pago (monto, fecha, código de autorización, crédito o débito, últimos 4 dígitos y lo devuelto); el correo de quien paga para el comprobante; y «Si un pago llega cuando el pedido ya cambió o se canceló, lo anulamos completo el mismo día y guardamos el cobro y su anulación.».
- **§6:** Transbank recibe solo el monto y un número de orden que no identifica a nadie; los datos de la tarjeta se escriben en su página. Débito y devolución verificados el 10-11 en integración. Quién paga y quién ve el pago (D-62-2 y D-62-8). Después de pagar, cancela solo el administrador.
- **§8:** «Un pago que se intentó y no se cobró se borra con su pedido a los 30 días. Un cobro que se anuló completo se guarda 6 años, sin la dirección ni los productos.» (D-62-13, CL-28 ampliada).
- **§10:** «Si en ese momento hay un pago en curso y Transbank lo aprueba, lo anulamos completo el mismo día.» (CL-44 ampliada).
- **§13:** los pagos son de prueba, en el ambiente de prueba de Transbank, sin dinero real; el comprobante no es una boleta; el correo se prueba sin enviarse.

### 5.2 Registro de tratamientos

Entrada 2: titulares (suma quien paga), datos del pago (`cargo`, `participacion`, `transaccion_pasarela`, `condiciones_aceptadas_por`, correo de quien paga), base de licitud (ejecución de la compra, sin artículo hasta la consulta legal), quién accede (D-62-2 y D-62-8), conservación (D-62-10 y D-62-13), medidas (sección 2 y logs sin `token_ws`, `buy_order`, correo ni respuesta), comunicaciones (Transbank y el proveedor de correo, PENDIENTE) y la anulación automática como decisión automatizada que siempre devuelve. Entrada 11: el buzón recibe también reclamos de pagos y devoluciones.

### 5.3 Condiciones del pedido, borrador de la versión 0.2

```markdown
# Condiciones del pedido de MATU

**Versión 0.2 · borrador para el piloto académico.** La aprueba Jorge Espinoza. No es asesoría legal.

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
Al pagar te mostramos un comprobante y te lo enviamos al correo de tu cuenta, con el número del pedido, la fecha, el total, quién vende, tu derecho a retracto, cómo se devuelve si falta un producto y estas condiciones completas. El detalle de los productos está en la aplicación. [PENDIENTE: CL-54]

## 5. Si falta un producto
(igual que la §3 de la versión 0.1)

## 6. Cancelar
- Antes de pagar, no seguir no tiene costo.
- Después de pagar, quien administra el grupo puede cancelar sin costo mientras el comercio no empiece a preparar, y te devolvemos el total.

## 7. Si no podemos devolver
Si la anulación en Transbank no se puede hacer, la reintentamos y te escribimos. Nunca te pedimos los datos de tu tarjeta ni de tu banco por mensaje. [PENDIENTE: CL-55]

## 8. Entrega
(igual que la §5 de la versión 0.1)

## 9. Derecho a retracto
(igual que la §6 de la versión 0.1)

## 10. Si algo no llega
(igual que la §7 de la versión 0.1)

## 11. Reclamos
(igual que la §8 de la versión 0.1)

## 12. Tus datos
(igual que la §9 de la versión 0.1)

## 13. Versión
Guardamos qué versión de estas condiciones aceptaste, quién la aceptó, cuándo, y una huella del texto exacto que viste.
```

### 5.4 `lenguaje.md`, sección nueva «Pago (MATU-62)» (número al fusionar)

Sin «rechazado» ni «fallido». No se repite lo que ya está en la 31.

| Dónde | Texto |
|---|---|
| Antes de Webpay | Te llevamos a Webpay, la página de pago de Transbank. MATU no ve los datos de tu tarjeta. |
| Cuidador, en el resumen (D-62-8) | Pagan quien administra el grupo y quien paga. |
| Al volver | Estamos confirmando tu pago. No cierres esta pantalla. |
| La respuesta tarda | Todavía no tenemos la respuesta de Transbank. Si pagaste, no pagues de nuevo: te avisamos aquí apenas la tengamos, en menos de 15 minutos. |
| Pago en curso, para quien quiere cambiar | Hay un pago en curso para este pedido. Espera su resultado antes de cambiarlo. |
| Pago en curso, para quien quiere pagar | Ya hay un pago en curso para este pedido. Espera su resultado antes de intentar de nuevo. |
| Aprobado | Pagaste tu pedido |
| Comprobante, campos | Pedido {referencia} · {DD/MM/AAAA} a las {HH:MM} · productos con cantidad y precio · Envío {monto} · Total pagado {monto} · {Débito/Crédito} terminada en {últimos 4} · Código de autorización {código} · Vende: MATU, piloto académico, sin persona jurídica · Entrega: {ventana} · Condiciones aceptadas: versión {v}, el {fecha} |
| Comprobante, garantías | Derecho a retracto: tienes 10 días desde que lo recibes. · Si un producto no llega, te devolvemos su precio el mismo día, a la misma tarjeta. Cuándo lo ves en tu cuenta depende de tu banco. · Quien administra el grupo puede cancelar sin costo mientras el comercio no empiece a preparar. · ¿Algo no está bien? Escríbenos a {correo}. |
| Comprobante, piloto | Pago de prueba. No se cobró dinero real. Este comprobante no es una boleta. |
| Correo | Te enviamos este comprobante a {correo}. · En el piloto, el correo se prueba sin enviarse. |
| No se aprobó | El pago no se hizo. Transbank no lo aprobó y no se cobró nada. Puedes intentarlo con otra tarjeta mientras el total siga vigente. · Intentar de nuevo |
| Salió sin pagar | Saliste de Webpay sin pagar. No se cobró nada. |
| Webpay no responde | Webpay no responde ahora. No se cobró nada. Inténtalo en unos minutos. |
| Retorno repetido | Este pago ya está registrado. No se cobró dos veces. |
| Pago tardío respetado | Tu pago llegó después de que venció el total, y lo respetamos: pagaste {total}, el precio que aceptaste. |
| Pago tardío anulado | El pedido cambió o se canceló mientras pagabas. Anulamos tu pago de {total} completo, a tu tarjeta terminada en {últimos 4}. Cuándo lo ves en tu cuenta depende de tu banco. |
| Devolución hecha | Devolvimos {monto} a tu tarjeta terminada en {últimos 4}, por {producto}. Cuándo lo ves en tu cuenta depende de tu banco. |
| Devolución en curso | Estamos devolviendo {monto} a tu tarjeta. Si no se completa hoy, te escribimos. MATU nunca te pide los datos de tu banco por mensaje. |
| Retirar `despacho`, línea nueva en la 31 | Si hay un pago en curso y se aprueba, lo anulamos completo el mismo día. |

Ajustes a la 31: la regla de «Boleta» admite «Este comprobante no es una boleta.»; con D-62-14 (a), el pagador también ve «Quedan 2 minutos para pagar este total.».

### 5.5 Fuera de `docs/legal/`

Arquitectura 8.1, 8.4, 9.4, 11.8 y 12.4 (sección 4 y D-62-13, D-62-15); modelo de datos (venta atada a `total_confirmado_en`, `condiciones_aceptadas_por`); `figura-legal-piloto.md` §5 (cerrar el PENDIENTE de la anulación parcial, verificada el 10-11).

## 6. Consulta legal

- **Se mantienen:** CL-54 (confirmación escrita, ampliada: si quien paga no es quien armó el pedido, ¿a quién se le debe?), CL-55 (devolución si la anulación no es posible) y CL-56 (rol de Transbank). Las tres bloquean el dinero real o los datos reales.
- **CL-64 (nueva) · Qué se guarda de un pago que no se cobró o que se anuló completo.** ¿Se puede borrar a los 30 días un intento rechazado o abandonado? ¿Un cobro anulado completo el mismo día cuenta como registro de pagos con 6 años? Mientras tanto, D-62-13 (c). Bloquea el dinero real.
- **CL-65 (nueva) · El pago aprobado de un total que ya no estaba vigente.** ¿Basta con anular completo y avisar, o el pago aprobado obliga a entregar ese total (art. 12)? ¿Se debe respetar un pago del mismo total que llega después de los 15 minutos? Mientras tanto, D-62-4, reglas 2 y 3. Bloquea el dinero real.
- **CL-66 (nueva) · Quién es el consumidor cuando paga una persona y arma otra.** ¿Quién ejerce el retracto, quién reclama y a quién se le devuelve? Mientras tanto, la aceptación queda con quien pagó (D-62-16) y la devolución va siempre a la misma tarjeta. Bloquea el dinero real.
- **Se amplían:** CL-44 (retiro o borrado con un pago en curso) y CL-28 (apunta a la CL-64).
- La próxima libre es la **CL-67**.

**Certeza de las citas:** Ley 19.496, arts. 3 b), 12, 12 A y 30 según la investigación del 27-10; del art. 12 es seguro que obliga a respetar los términos convenidos; el texto exacto del 12 A no es seguro. Ley 21.719 sin citas nuevas. WCAG 2.2.1 segura en su objeto; la excepción «esencial» no es segura. Transbank, por verificar: la vida del token, el `commit` tardío, el plazo de anulación con débito y el paso a producción.

## 7. Decisiones tomadas (11-11, tarde)

**Las tomó el orquestador por delegación de Jorge**, que estaba fuera y pidió decidir «manteniendo la visión del proyecto y a quién va dirigido». Se aceptan todas las recomendaciones del analista, con estas razones:

- **D-62-1 (b), la 0024 para MATU-62, y MATU-55 pasa a la 0025.** MATU-62 vence el 12-11 y es el objetivo 6 del proyecto. MATU-55 no tiene rama de código y no toca el pago. La fila se actualiza el mismo día en el vault y en Trello.
- **D-62-2 (c) y D-62-8 (a).** Minimización: el detalle de la tarjeta lo ven quien pagó y soporte. Pagan el admin y el pagador, como dice la arquitectura 11.2.
- **D-62-3 (b), D-62-5 (a), D-62-6 (a), D-62-7 sí, D-62-9 (a), D-62-10 (a) y D-62-12 obligatoria.** Sin cambios respecto de la primera revisión.
- **D-62-4, las tres reglas.** Protegen a la familia: nunca se cobra un total que ya no es el que vio, y el pago que hizo con el total vigente se respeta. Cancelar siempre es posible.
- **D-62-11, el cargo al tocar «Pagar».** Así no existe un cargo para un pedido que nadie intentó pagar.
- **D-62-13 (c).** Ni se guardan 6 años los productos de un pedido no pagado, que son sensibles, ni se borra un registro contable.
- **D-62-14 (a).** Se mantiene C3, que ya decidió Jorge. Se mitiga con el aviso de los 2 minutos también para el pagador, y Martín lo mide en la usabilidad.
- **D-62-15, 409 `estado-pedido`.** Coherente con todo el pedido.
- **D-62-16 (a) y D-62-17.**
- **Contradicción 8.1 y 12.4:** manda la 8.1, y la 12.4, caso 8, se corrige como dice la sección 4.
- **Condiciones del pedido 0.2:** se aprueba el borrador de la sección 5.3 para publicarlo con MATU-62. La frase del piloto queda dentro del texto con huella.
- **Consultas legales:** se abren las CL-64 a CL-66 y se amplían las CL-28, CL-44 y CL-54.

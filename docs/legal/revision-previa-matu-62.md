# Revisión previa del analista normativo · MATU-62 · Pago: cobrar el total exacto confirmado (ADR-027)

**11 de noviembre de 2026, madrugada** · Agente analista normativo, a pedido de Jorge · Estado: **decisiones D-62-1 a D-62-12 pendientes de Jorge**

Esto no es asesoría legal. Es un borrador para que Jorge decida.

**Decisión de Jorge (11-11):** esta revisión se repite cuando MATU-61 esté lista, con su informe, sus D1 a D12 y lo que construyó a la vista. Las D-62 se deciden recién después. Mientras tanto, la 0023 de MATU-61 no crea el cargo ni la transición `vencido → pagado`.

**Limitación declarada por el analista:** no pudo leer `revision-previa-matu-61.md`, que estaba en una rama, y se apoyó en la nota del vault de MATU-61. **Antes de que Jorge decida, el orquestador cruza las D-62 con las D1 a D12 de MATU-61:** R5/D6, D11 (dónde nace el cargo), R12 y la 0023.

**Fuentes que leyó:**
- el ADR-027;
- la arquitectura: 7.7, 8.1 a 8.4, 11, 12.3, 12.4, 18 y 18.1;
- la estrategia de pruebas: 10.2;
- `pruebas-concepto/transbank.md`;
- el modelo de datos: 4.6 y 8;
- la política 0.11, el registro (entrada 2), `consulta-legal.md`, `revision-previa-adr-027.md`, `investigacion-normativa-adr-027.md` y `figura-legal-piloto.md` §5;
- `lenguaje.md`;
- en el código: `01_esquema.sql`, `02_rls.sql`, las migraciones 0002, 0017, 0020 y 0021, y `core/logs.py`.

`modules/payments/` no existe.

## 1. Veredicto por punto

| # | Punto | Veredicto | Por qué y qué falta |
|---|---|---|---|
| 1 | **R4 · confirmación escrita** (Ley 19.496, art. 12 A) | **NO CUMPLE** todavía. Su contenido mínimo **REQUIERE CONSULTA LEGAL** (CL-54) | No existe ni el comprobante ni el correo. Sin confirmación, el retracto sube de 10 a 90 días (art. 3 bis, según la investigación del 27-10). El texto exacto del art. 12 A («copia íntegra») no es seguro |
| 2 | **R5 · versión aceptada de las condiciones**, al tocar «Pagar» | **NO CUMPLE** todavía | Depende de la D6 de MATU-61. Si la 0023 trae la columna (versión, huella y fecha, como `aceptacion_politica` de la 0021), MATU-62 solo la escribe en la transacción del `create`. Si no la trae, la agrega su migración. La acepta **quien paga** |
| 3 | **R10 · pago aprobado después de vencido el total** | **NO CUMPLE**, y **los documentos se contradicen** | La arquitectura 8.1 no declara `vencido → pagado`. El caso 8 de la 12.4 dice «vuelve a `borrador`», y la 8.1 dice `vencido`: **Jorge decide cuál manda.** Falta la regla para un pago tardío cuando el pedido ya se volvió a confirmar con otro total, o ya se canceló (D-62-4) |
| 4 | **R11 · plazos de anulación** | **CUMPLE** en el semestre. Antes de dinero real hay una condición con Transbank | La anulación parcial se verificó el 10-11 con crédito y débito, y el ADR-027 anula el mismo día. Los 90 días vienen de una fuente de terceros sobre la **captura diferida, que es solo con crédito**. **Del débito no hay dato.** Importa para un retracto ejercido tarde (CL-55) |
| 5 | **R13 · condiciones del pedido** | **NO CUMPLE** todavía | El borrador está en la revisión de MATU-61, sin aprobar. Para el pago debe decir: un solo cobro, crédito y débito iguales, 15 minutos, el pago tardío (R10), el comprobante y el correo, la devolución el mismo día a la misma tarjeta, qué pasa si la anulación falla (D-62-6), que el piloto no cobra dinero real y que el comprobante no es una boleta |
| 6 | **R14 · `payload_respuesta`** | **NO CUMPLE** | Es un `jsonb` libre, y la respuesta del `commit` trae más datos. Los cuatro permitidos ya tienen sus columnas. Se propone `CHECK (payload_respuesta IS NULL)` y `CHECK (ultimos4 ~ '^[0-9]{4}$')` (D-62-9) |
| 7 | **Idempotencia** | En el diseño **CUMPLE**. En la base **NO CUMPLE** todavía | Existen `idempotencia` (24 h, 422 con otro cuerpo), `transaccion_pasarela.idempotency_key UNIQUE` e `indice_token` `pago_retorno`. Faltan dos cosas: que `token` sea único y que haya una sola venta aprobada por cargo. Además, `idempotencia.respuesta` guarda la URL y el token de Webpay, y ninguna tarea borra las filas vencidas |
| 8 | **Conciliación del retorno perdido** | **NO CUMPLE** todavía | Con RLS forzado, sin contexto no se ven las transacciones en `autorizando`. Hace falta una función `SECURITY DEFINER` que exija `operacion`, devuelva solo identificadores (arquitectura 7.7) y después procese cada grupo con `app.rol = 'sistema'`. El cron va en MATU-74. No se sabe cuánto acepta Transbank un `commit` tardío (8.4, PENDIENTE). Ver D-62-5 |
| 9 | **Devolución** (anulación parcial, misma tarjeta, mismo día) | **CUMPLE** | Los `CHECK` de la 0002 impiden devolver más de lo cobrado y amarran el estado con los montos. Faltan la clave de idempotencia por línea (8.4) y qué hacer si la anulación falla. Un respaldo que pida datos bancarios NO CUMPLE (D-62-6) |
| 10 | **Datos de tarjeta** | **CUMPLE** | Se paga en Webpay y MATU guarda solo el resultado. Condiciones: ningún esquema ni columna acepta número, vencimiento ni CVV, con una prueba de contrato. La `PasarelaFalsa` es sintética. Sin iframe propio. La pantalla dice que MATU no ve la tarjeta |
| 11 | **Logs** | **CUMPLE**, con condiciones que se prueban | `core/logs.py` quita el query y el fragmento. Falta: (a) que los loggers del SDK de Transbank y de su cliente HTTP no registren cuerpos; (b) no registrar `token_ws`, `buy_order`, el correo ni la respuesta cruda, tampoco en los errores RFC 7807; (c) si el retorno llega por GET con `token_ws` en la URL, Railway puede guardarlo (PENDIENTE en el registro, entrada 9) |
| 12 | **Conservación de los cargos** | **REQUIERE CONSULTA LEGAL** (la CL-28 que ya existe) | Se declaran 6 años, pero `transaccion_pasarela` «nunca se borra» y no hay nada que borre a los 6 años. No bloquea el semestre. El borrado de la persona (MATU-72) no alcanza a los cargos, y está bien |
| 13 | **Ley 19.496** | **CUMPLE** en el diseño, con condiciones. El contenido de la confirmación queda en la CL-54 | Se cobra exactamente lo mostrado (arts. 3 b, 12 y 30). Condiciones: (a) **un trigger para que `cargo.monto_cobrado` sea igual a `pedido.total`**, porque hoy la base no lo garantiza; (b) el botón dice el monto; (c) el vendedor es «piloto académico, sin persona jurídica»; (d) el comprobante dice que **no es una boleta**; (e) hay un canal de reclamo. La boleta sigue en la CL-46 |
| 14 | **Condiciones de Transbank** | **CUMPLE** en integración. Para producción no se puede evaluar | Sin el contrato. Probablemente exige un alta comercial con RUT (CL-47) y una validación |
| 15 | **Las políticas `FOR ALL` del pago** | **NO CUMPLE** | Hoy `cargo_familia FOR ALL` deja que el observador y el cuidador inserten o cambien cargos. La arquitectura 11.2 dice que pagan el admin y el pagador. Ver la sección 2 |
| 16 | **Hallazgo: el retorno llega sin sesión** | Es una condición técnica que afecta a RLS | La cookie de refresh es `SameSite=Strict` y el access token vive en memoria, así que **el retorno de Webpay llega sin usuario**. Se resuelve con `indice_token` (`pago_retorno → grupo_id`) y `app.rol = 'sistema'` (arquitectura 7.7 b). Las políticas deben admitir ese contexto. El token de la URL se limpia con `history.replaceState` |

## 2. ¿Migración?

**Sí.** Va después de la 0023 de MATU-61, sí o sí, porque escribe sobre `pedido` y la versión de las condiciones puede venir de ahí. Con la 0024 de MATU-55 no hay dependencia técnica.
- **Recomendación:** **0025**, apilada después de MATU-55.
- **Salvo:** que MATU-55 no tenga rama cuando MATU-62 esté lista, porque MATU-62 vence el 12-11. En ese caso se intercambian.

Lo decide Jorge (D-62-1).

**Contenido propuesto** (la forma la decide el backend):
1. **Políticas por operación y por rol, sin `FOR ALL`:**
   - **`cargo`:** lo lee todo el grupo. Lo crea quien diga D-62-11. Lo cobra o lo devuelve `sistema` (el retorno y la conciliación), o el admin o el pagador. Operación lo lee y solo lo actualiza para devolver.
   - **`participacion`:** lo mismo, heredado del cargo.
   - **`transaccion_pasarela`:** se lee según D-62-2. La venta la crean el admin y el pagador. La anulación la crean operación o `sistema`. La actualizan `sistema` y operación.
   - **`idempotencia`:** solo con `usuario_id = app_usuario()` dentro del grupo.
   - **`REVOKE DELETE`** a `matu_app` sobre `cargo`, `participacion` e `idempotencia`. Una función de conservación borra lo vencido de `idempotencia`.
2. **Integridad del cobro:**
   - un trigger: `cargo.monto_cobrado` (si es mayor que 0) es igual a `pedido.total`, y el `monto` de una `venta` es igual a `pedido.total`;
   - un índice único parcial: una sola `venta` `aprobada` por participación;
   - un índice único parcial sobre `token` no nulo.
3. **R14:** `CHECK (payload_respuesta IS NULL)` y el formato de `ultimos4`.
4. **Conciliación:** `pagos_por_conciliar(limite)` como `SECURITY DEFINER`, que exige `operacion`, devuelve solo identificadores y da `EXECUTE` solo a `matu_app`.
5. **R5:** la columna de las condiciones, **solo si la 0023 no la trae**.
6. **Pruebas:**
   - en `test_aislamiento.py`: el observador y el cuidador no pagan, otro grupo recibe 404 y nadie borra;
   - en `test_migraciones.py`: el ciclo completo.

## 3. Decisiones para Jorge (con la recomendación del analista)

| # | Decisión | Opciones | Recomendación |
|---|---|---|---|
| D-62-1 | Número y orden de la migración | (a) 0025 después de MATU-55; (b) 0024, intercambiando | (a), salvo que MATU-55 no tenga rama |
| D-62-2 | Quién ve el detalle del pago (tipo de tarjeta, últimos 4 y código) | (a) todo el grupo; (b) quien pagó y el admin; (c) quien pagó, y operación para soporte | **(c)**, por minimización. El grupo ve el estado y los montos |
| D-62-3 | Contenido del correo de confirmación (R4) | (a) con los productos; (b) sin productos: referencia, fecha, total, vendedor, retracto, devolución, enlace al comprobante y condiciones íntegras; (c) (b) más un PDF | **(b)** en el piloto, con la CL-54. Los productos se tratan como sensibles. Solo a correos verificados. En el piloto se prueba sin enviarse |
| D-62-4 | Pago tardío (R10) y una confirmación o cancelación nueva con una venta en curso | (a) mientras haya una venta `iniciada` o `autorizando`, no se puede volver a confirmar ni cancelar; (b) se permite, y un pago tardío de un total viejo se anula completo el mismo día; (c) las dos | **(c).** El pago tardío del total vigente se respeta, declarando `vencido → pagado`. Si falta stock, se sigue la regla de faltante |
| D-62-5 | La conciliación encuentra una venta autorizada sin `commit` | (a) el job hace el `commit`; (b) la deja vencer | **(a).** Antes, medir en integración cuánto acepta Transbank un `commit` tardío |
| D-62-6 | La anulación falla, o venció su plazo | (a) reintentos, alerta a operación y aviso a la familia, sin datos bancarios; (b) transferencia con datos bancarios | **(a).** La (b) es un tratamiento nuevo y va a la CL-55 |
| D-62-7 | El comprobante del piloto dice «Pago de prueba. No se cobró dinero real. Este comprobante no es una boleta.» | sí / no | **Sí** |
| D-62-8 | Quién puede tocar «Pagar» | (a) admin y pagador (11.2); (b) además el cuidador | **(a).** Verifica la autorización de pedidos vigente (R12) y guarda la aceptación de quien paga (R5) |
| D-62-9 | `payload_respuesta` | (a) siempre nulo, con un `CHECK`; (b) `jsonb` con lista permitida | **(a)** |
| D-62-10 | Conservación de `transaccion_pasarela` | (a) «nunca se borra» en el semestre, con un PENDIENTE para los 6 años; (b) construirla ahora | **(a)**, porque sigue en la CL-28 |
| D-62-11 | Dónde nace el cargo | (a) al confirmar (8.4), en `pendiente`; (b) al pagar, por quien paga | **(b)** si MATU-61 lo permite. Si la 0023 lo crea al confirmar, (a), con el cobro limitado a `sistema`, admin y pagador. **Cruzar con MATU-61** |
| D-62-12 | `Idempotency-Key` | obligatoria o no | **Obligatoria** en `pagar`: 428 si falta, 422 si cambia el cuerpo y 409 si hay un pago en curso |

## 4. Documentos que habría que actualizar (borradores)

- **`registro-tratamientos.md`, entrada 2:**
  - **datos:** el correo de quien paga (art. 12 A), los identificadores opacos de la pasarela y el estado del cargo y de las transacciones;
  - **quién accede:** el detalle lo ve quien pagó, y operación para soporte (D-62-2), y el grupo ve el estado y los montos;
  - **medidas:** lo cobrado es igual al total, una sola venta aprobada, R14, la conciliación con una función que solo devuelve identificadores, y logs sin tokens, correos ni respuestas;
  - **comunicaciones:** Transbank recibe el monto, la orden opaca y el retorno, nunca nombres ni productos, y el proveedor de correo recibe el comprobante [PENDIENTE: proveedor y país].
- **`politica-privacidad.md` 0.12,** la misma versión de MATU-61 y MATU-55:
  - §3: el comprobante por correo;
  - §4, «De tus pedidos»: el pago;
  - §6, Transbank: se cierra el PENDIENTE con la prueba del 10-11, y se agrega quién ve el detalle;
  - §13: los pagos son de prueba y el comprobante no es una boleta.
- **`figura-legal-piloto.md` §5:** se cierra el PENDIENTE de la anulación parcial, y se agrega que los 90 días vienen de la captura diferida, sin datos para el débito.
- **`consulta-legal.md`:**
  - las CL-54, CL-55 y CL-56 nuevas, y «la próxima es CL-57»;
  - la fila de MATU-62;
  - en las condiciones antes de datos reales, la anulación parcial queda verificada y queda «confirmar con Transbank el plazo de anulación con crédito y débito, y el `commit` tardío».
- **`condiciones-pedido.md`:** las secciones de pago (punto 5).
- **Fuera de `docs/legal/`:** la contradicción entre la 12.4 (caso 8) y la 8.1, y el PENDIENTE de la 8.4.

## 5. Textos propuestos para `lenguaje.md`

Van en una sección nueva, después de la de MATU-61. Sin «rechazado» ni «fallido» (3.2).

| Dónde | Texto |
|---|---|
| Botón | Pagar $57.460 |
| Bajo el botón | Se cobra una sola vez este total, con crédito o con débito. No hay reserva ni cobros después. |
| Vigencia | Este total vale hasta las {HH:MM}. |
| Antes de Webpay | Te llevamos a Webpay, la página de pago de Transbank. MATU no ve los datos de tu tarjeta. |
| Al volver | Estamos confirmando tu pago. No cierres esta pantalla. |
| La respuesta tarda | Todavía no tenemos la respuesta de Transbank. Si pagaste, no pagues de nuevo: te avisamos aquí apenas la tengamos, en menos de 15 minutos. |
| Aprobado, título | Pagaste tu pedido |
| Comprobante, campos | Pedido {referencia} · {DD/MM/AAAA} a las {HH:MM} · productos con cantidad y precio · Envío {monto} · Total pagado {monto} · {Débito/Crédito} terminada en {últimos 4} · Código de autorización {código} · Vende: MATU, piloto académico, sin persona jurídica · Entrega: {ventana} · Condiciones aceptadas: versión {v}, el {fecha} |
| Comprobante, garantías | Derecho a retracto: tienes 10 días desde que lo recibes. · Si un producto no llega, te devolvemos su precio el mismo día, a la misma tarjeta. Cuándo lo ves en tu cuenta depende de tu banco. · Puedes cancelar sin costo mientras el comercio no empiece a preparar. · ¿Algo no está bien? Escríbenos a {correo}. |
| Comprobante, piloto | Pago de prueba. No se cobró dinero real. Este comprobante no es una boleta. |
| Correo enviado | Te enviamos este comprobante a {correo}. (En el piloto: «En el piloto, el correo se prueba sin enviarse.») |
| Asunto | MATU: comprobante de tu pedido {referencia} |
| Cuerpo (D-62-3 b) | Pagaste {total} el {fecha}. Vende MATU, piloto académico, sin persona jurídica. El detalle de tu pedido está en la aplicación, en Pedidos. Derecho a retracto: tienes 10 días desde que lo recibes. Si un producto no llega, te devolvemos su precio el mismo día, a la misma tarjeta. Las condiciones que aceptaste van al final de este correo. MATU nunca te pide los datos de tu tarjeta ni de tu banco. |
| No se aprobó | El pago no se hizo. Transbank no lo aprobó y no se cobró nada. Puedes intentarlo con otra tarjeta mientras el total siga vigente. · Intentar de nuevo |
| Salió sin pagar | Saliste de Webpay sin pagar. No se cobró nada. |
| Total vencido | Este total ya no vale. Pasaron 15 minutos, y los precios y lo que hay pueden haber cambiado. No se cobró nada. Confírmalo de nuevo para pagar. · Confirmar de nuevo |
| Webpay no responde | Webpay no responde ahora. No se cobró nada. Inténtalo en unos minutos. |
| Pago en curso (409) | Ya hay un pago en curso para este pedido. Espera su resultado antes de intentar de nuevo. |
| Retorno repetido | Este pago ya está registrado. No se cobró dos veces. |
| Pago tardío (R10) | Tu pago llegó después de que venció el total, y lo respetamos: pagaste {total}, el precio que aceptaste. |
| Devolución hecha | Devolvimos {monto} a tu tarjeta terminada en {últimos 4}, por {producto}. Cuándo lo ves en tu cuenta depende de tu banco. |
| Devolución en curso | Estamos devolviendo {monto} a tu tarjeta. Si no se completa hoy, te escribimos. MATU nunca te pide los datos de tu banco por mensaje. |
| Sin permiso para pagar | Pagan quien administra el grupo y quien paga. (Falta decidir si la API responde 404, como en MATU-44, o muestra esto.) |

## 6. Consulta legal (desde la CL-54)

- **CL-54 · El contenido de la confirmación escrita (art. 12 A).**
  - **Pregunta:** ¿cumple el art. 12 A un correo sin la lista de productos, que remite el detalle a la aplicación? ¿Basta el comprobante dentro de la aplicación?
  - **Mientras tanto:** D-62-3 (b). Bloquea el dinero real. Si falta la confirmación, el retracto sube a 90 días.
- **CL-55 · La devolución si la anulación no es posible.**
  - **Pregunta:** ¿qué medio cumple el art. 3 bis (45 días, sin retención)? ¿Pedir datos bancarios exige una base de licitud nueva?
  - **Mientras tanto:** D-62-6 (a). Bloquea el dinero real.
- **CL-56 · El rol de Transbank respecto de los datos de quien paga.**
  - **Pregunta:** ¿es responsable por su cuenta o encargado de MATU? Bloquea los datos reales.

Sin número nuevo: la conservación de 6 años sigue en la **CL-28** y la boleta en la **CL-46**.

## Certeza de las citas

- **Ley 19.496:** los arts. 3 b, 12, 12 A y 30 son seguros, según la investigación del 27-10. El texto exacto del 12 A no lo es.
- **Decreto 6:** solo lo que cita esa investigación.
- **Ley 21.719:** sin citas nuevas.
- **Transbank:** los campos del `commit`, la vida del token, el `commit` tardío y el paso a producción quedan por verificar.

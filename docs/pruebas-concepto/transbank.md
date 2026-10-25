# Prueba de concepto · Transbank Webpay Plus diferido

> **Estado al 24 de octubre de 2026: completa.** Los cinco casos tienen su resultado real. La captura diferida cobra el monto real y revierte sin cobrar, y opera solo con crédito. El débito se acepta con el plan B del ADR-006 (decisión del 24 de octubre, más abajo).

**Sprint:** 0, se completa en el sprint 1 · **Responsables:** Martín Henríquez y Jorge Espinoza
**Verifica:** ADR-006 (autorización diferida y captura por el monto real) y el riesgo de la sección 17 de la arquitectura sobre el débito
**Guion:** [estrategia de pruebas, sección 10](../estrategia-pruebas.md)
**Código:** [MATU_PROYECTO · spikes/transbank](https://github.com/MartinHenriquez131/MATU_PROYECTO/tree/main/spikes/transbank)

---

## Qué se quería saber

MATU cobra el monto real de un pedido, que puede ser menor al estimado si falta un producto. Para eso el ADR-006 eligió Webpay Plus diferido: se autoriza el monto estimado, se captura el real y, si el pedido se cancela, se revierte. La prueba responde cinco preguntas antes de construir el módulo de pagos.

## Ambiente

- Ambiente de integración de Transbank, con las credenciales públicas de captura diferida (código de comercio 597055555540)
- SDK oficial de Python, `transbank-sdk` 6.1.0
- Tarjeta VISA de crédito de prueba `4051 8856 0044 6623`

## Resultados

| # | Caso | Resultado esperado | Resultado real | Evidencia |
|---|---|---|---|---|
| 1 | Autorizar y capturar el mismo monto | Captura aprobada | **Cumple.** 24/10, `orden-poc-101`: commit `AUTHORIZED` por $69.000 (código 1213, respuesta 0). Captura aprobada por $69.000 (código 872051, respuesta 0). Estado final `CAPTURED` | [Evidencia del 24/10](evidencia/2026-10-24-casos-1-2-3-5.txt) |
| 2 | Autorizar $69.000 y capturar $51.340 | Se cobra $51.340 y se libera el resto | **Cumple.** 24/10, `orden-poc-102`: commit `AUTHORIZED` por $69.000. Captura por $51.340 (código 196611, respuesta 0). El estado final queda en `CAPTURED` con `amount` 51.340: se cobra solo el monto real | [Evidencia del 24/10](evidencia/2026-10-24-casos-1-2-3-5.txt) |
| 3 | Autorizar y revertir sin capturar | Autorización anulada, nada cobrado | **Cumple.** 24/10, `orden-poc-103`: commit `AUTHORIZED` por $69.000. La reversa responde `REVERSED` y el estado final queda en `REVERSED`, sin captura | [Evidencia del 24/10](evidencia/2026-10-24-casos-1-2-3-5.txt) |
| 4 | Débito | Registrar qué pasa | **No admite captura diferida.** El formulario del comercio de captura diferida solo ofrece "Tarjetas · Crédito". No hay opción de débito. La autorización del 7 de octubre lo confirma: VN es "Venta Normal", una venta con crédito. Una venta con débito aparecería como VD | [Captura 2](capturas/02-formulario-solo-credito.png) |
| 5 | Retorno de la pasarela recibido dos veces | Un solo cobro | **Cumple, con un hallazgo.** Hay un solo cobro, pero el segundo commit **no falla**, como esperaba el README del spike. Transbank devuelve la misma transacción, ya en `CAPTURED`, con el mismo código de autorización y el mismo monto. Ver "Hallazgo para el módulo de pagos" | [Evidencia del 24/10](evidencia/2026-10-24-casos-1-2-3-5.txt) |

**Hallazgo para el módulo de pagos (sprint 4).** El commit repetido es idempotente y no da error. El módulo no puede detectar un retorno duplicado esperando una excepción. Tiene que registrar el token y el estado del cargo en su propia base, y si el token ya está procesado, no confirmar el pedido otra vez ni crear un segundo cargo. Lo cubre el caso de "retorno duplicado" de la estrategia de pruebas, con la `PasarelaFalsa` programada para responder como Transbank.

![Autenticación en el banco simulado](capturas/01-autenticacion-rut-incorrecto.png)

![Formulario de Webpay con solo crédito](capturas/02-formulario-solo-credito.png)

La tarjeta que empieza con `4111` en la captura 2 no es una tarjeta de prueba de Transbank, así que su rechazo no dice nada sobre la captura diferida.

## Qué significa el caso 4

**Se confirma el riesgo declarado en la sección 17 de la arquitectura:** la captura diferida opera solo sobre crédito, y el débito es el medio de pago mayoritario en el segmento. Quien pague con débito no puede pasar por el flujo del ADR-006.

El plan B ya está escrito en el ADR-006: con débito se cobra el monto estimado en el momento y se emite una nota de crédito por la diferencia. Es peor experiencia, pero no bloquea el semestre.

## Decisión sobre el débito · 24 de octubre de 2026

**Decisión de Jorge Espinoza (Product Owner): MATU no limita las formas de pago.** La aplicación tiene que facilitarle la vida a las familias, y el débito es el medio de pago mayoritario del segmento. Por eso se descarta un MVP solo con crédito y **se aplica el plan B del ADR-006**:

- **Con crédito:** el flujo del ADR-006 sin cambios. Se autoriza el monto estimado con margen y se captura el monto real del pedido.
- **Con débito:** se cobra el monto estimado al confirmar el pedido. Cuando el comercio arma el pedido real y el monto es menor, se devuelve la diferencia y se emite la nota de crédito.
- **Lo que se informa a la familia antes de pagar** (Ley 19.496): con débito se cobra el estimado, y la diferencia se devuelve cuando el comercio arma el pedido. El texto exacto lo fija la historia de pago del sprint 4.

**Qué hay que verificar antes de construir el pago (sprint 4):**
- [PENDIENTE] Cómo se devuelve la diferencia con débito en Webpay Plus: si admite una anulación parcial sobre el cobro de débito, o si hace falta otro mecanismo. Se prueba en el ambiente de integración, igual que los casos de esta prueba de concepto.
- [PENDIENTE] Qué código de comercio se usa para débito, porque el comercio de captura diferida de integración solo ofrece crédito.

Mientras dure el piloto académico, todo esto ocurre solo en el ambiente de integración, sin cobros reales (MATU-27).

## Intentos

| Fecha | Quién | Qué pasó |
|---|---|---|
| 7 de octubre | Martín | Un pago de $69.000 se detuvo en la autenticación del banco simulado por RUT incorrecto (captura 1). Otra ejecución quedó autorizada con `payment_type_code` VN, y se registró en Trello como prueba de que el débito funciona. **Esa lectura no es correcta:** VN corresponde a crédito, así que la prueba confirma la captura diferida con crédito, no con débito. La captura 2 responde el caso 4 |
| 13 de octubre | Jorge y Martín | Dos pagos nuevos. En los dos, el `commit` respondió `Transaction has an invalid finished state: aborted` (422): Transbank registró el pago como anulado. La causa no se identificó |
| 24 de octubre | Orquestador de Jorge | Casos 1, 2, 3 y 5 completos, sin ningún anulado. Para no depender de leer la barra de direcciones, un receptor local en `localhost:8000` registró el `token_ws` del retorno, que llega por GET, y el commit se hizo apenas volvió el pago. La causa de los anulados del 13 de octubre no se confirmó. La explicación más probable es que el pago se cancelaba en el navegador o que el commit llegaba tarde |

**Para repetir la prueba:** los pasos están en el README del spike. Si la dirección de retorno dice `TBK_TOKEN` en vez de `token_ws`, el pago se anuló en el navegador. En ese caso, antes de reintentar, revisar el estado con `poc_estado.py TOKEN`.

# 2026-11-10 · MATU-62 · Transbank en venta normal, antes de construir el pago (R11)

**Historia:** MATU-62 ([tarjeta](https://trello.com/c/z00lvOh6)) · **Qué se probó:** los 4 casos de la estrategia de pruebas, 10.2, contra el ambiente de integración de Transbank
**Probó:** Martín Henríquez · **Fecha:** 10/11/2026, de 12:10 a 12:45
**Veredicto general:** PASS en los 4 casos. **Se cierra el riesgo del ADR-027:** la anulación parcial funciona con débito
**PR:** MartinHenriquez131/MATU#64 (resultados en `docs/pruebas-concepto/transbank.md` y estrategia 10.2) y MartinHenriquez131/MATU_PROYECTO#77 (spike `spikes/transbank-venta-normal`)

## Casos

| # | Caso | Resultado (hora de Chile) | Veredicto |
|---|---|---|---|
| 1 | Crédito por $57.460 | `vn-102`, 12:42. AMEX terminada en 2032, `AUTHORIZED`, `VN`, autorización 1617, respuesta 0 | PASS |
| 2 | Débito por $57.460 | `vn-101`, 12:32. Redcompra terminada en 7763, `AUTHORIZED`, `VD`, autorización 1415, respuesta 0. El formulario ofrece «Crédito, Débito, Prepago» | PASS |
| 3 | Anulación parcial de $8.990 | Crédito: `NULLIFIED` (307162). Débito: `NULLIFIED` (168026). Las dos quedan `PARTIALLY_NULLIFIED` con saldo $48.470 | PASS |
| 4 | Retorno duplicado | El segundo commit de `vn-102` no falla: devuelve la misma transacción, con un solo cobro | PASS |

## Hallazgos

| ID | Severidad | Hallazgo | Qué pido |
|---|---|---|---|
| H1 | P3 | La tarjeta de MATU-62 pide los casos «1, 2, 3 y 5 de la arquitectura 12.4», y la estrategia 10.2 los numera del 1 al 4. Se usaron los de 10.2, porque `docs/` manda | Alinear el texto de la tarjeta |
| H2 | P3 | En el comercio de venta normal, la VISA y la Mastercard de crédito de prueba se rechazan con «Intenta pagar con otra tarjeta». La AMEX pasa | Para quien repita la prueba, y para la prueba en el teléfono de MATU-62 |
| H3 | P3 | El plazo máximo de anulación (R11) no se mide en integración. **Supuesto de trabajo, decidido por Martín el 10-11: hasta 90 días**, según fuentes de terceros (Kushki), no oficiales y descritas para la captura diferida. No está confirmado para el débito | Confirmarlo con Transbank antes de salir de integración. Mientras tanto, MATU anula el mismo día (ADR-027), dentro de cualquier plazo |
| H4 | Para Jorge | Después de una anulación parcial, el estado es `PARTIALLY_NULLIFIED` con `balance`. El duplicado no da error | Que la `PasarelaFalsa` responda igual |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | La tarjeta nombra los casos 1 a 4 de la estrategia 10.2, en la descripción y en sus dos ítems | MATU-62 en Trello (10-11) | |
| H2 | La prueba en el teléfono de MATU-62 usa la AMEX y la Redcompra de integración, y el README del spike también | ítem de MATU-62 y MATU_PROYECTO #78 | |
| H3 | De acuerdo con el supuesto de 90 días mientras se está en integración. Antes de salir de integración se confirma con Transbank. La arquitectura y el ADR-027 lo dicen | MATU #66 e ítem de MATU-62 | |
| H4 | La `PasarelaFalsa` responderá `PARTIALLY_NULLIFIED` con `balance`, y el duplicado se detecta con el registro propio del token | ítem de MATU-62 | |

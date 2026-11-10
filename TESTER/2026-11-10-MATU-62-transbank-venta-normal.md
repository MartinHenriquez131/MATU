# 2026-11-10 · MATU-62 · Transbank en venta normal, antes de construir el pago (R11)

**Historia:** MATU-62 ([tarjeta](https://trello.com/c/z00lvOh6)) · **Qué se probó:** los 4 casos de la estrategia de pruebas, 10.2, contra el ambiente de integración de Transbank
**Probó:** Martín Henríquez · **Fecha:** 10/11/2026
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
| H3 | Pendiente | El plazo máximo de anulación con crédito y con débito (R11, frente a 10 y 90 días) no se mide en integración, y no hay una fuente oficial a mano | Confirmarlo con la documentación o la mesa de ayuda de Transbank |
| H4 | Para Jorge | Después de una anulación parcial, el estado es `PARTIALLY_NULLIFIED` con `balance`. El duplicado no da error | Que la `PasarelaFalsa` responda igual |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | | | |
| H2 | | | |
| H3 | | | |
| H4 | | | |

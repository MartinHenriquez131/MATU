# TESTER · MATU-92 · Tus pedidos

**Revisor:** Martín Henríquez (modo Martín, con agentes) · **Fecha:** 17-11-2026
**PR:** MartinHenriquez131/MATU_PROYECTO#100 (head e578242) y MATU#103 (head a65f099)
**Resultado:** **PASS**, sin P1

## Revisiones

| Revisión | Resultado |
|---|---|
| QA | PASS. CI en verde. Rutas de lista, seguimiento y retractos iguales al contrato; `Idempotency-Key` en retracto y cancelar; bloqueo contra dos retractos a la vez; el 500 de `retracto` en `Devolucion.motivo` corregido con prueba; 409 al cancelar dos veces; otro grupo responde 404; el código de retiro no llega a la familia; el observador ve solo fecha, productos y «Pagado»; la huella de la 0.20 coincide con el texto |
| Analista | CUMPLE. Código de retiro nunca visible, retracto de 10 días hábiles (más protector mientras siga la CL-71), cancelación a la misma tarjeta, 2 años desde el cierre. La 0.20 se publica sin volver a aceptar (decisión de Jorge del 17-11, con la CL-28) |
| Documentos | Sin P1. H1 (conflicto de `lenguaje.md`) y H2 («10 días hábiles») corregidos por Jorge antes de fusionar |
| Diseñador | APROBADA: lista, vacío y observador, a 360, 1280 y 1920 px, claro y oscuro, y 320 px con texto al 200 % |

## Despliegue (17-11)

- Fusionados con merge commit: MATU_PROYECTO#100 (7fceca1) y MATU#103 (775952a), después de MATU-112.
- `matu-api` desplegado desde `main` en staging y en la demo, con `POLITICA_VERSION=0.20` y `POLITICA_ACTUALIZADA_EN=2026-11-17` en el mismo despliegue. Sin migración.

## Teléfono (demo, 17-11, 13:10 a 13:19)

| Paso | Qué se probó | Resultado |
|---|---|---|
| T1 | Carmen (Motorola) ve «Tus pedidos» con los pedidos pagados y su estado | OK |
| T2 | El pedido retirado muestra productos, la devolución del faltante y el comprobante, **sin código de retiro** | OK |
| T3 | «Arrepentirme de la compra» en el pedido entregado muestra la vista previa del monto (sin confirmar) | OK |
| T4 | Un pedido nuevo pagado se cancela antes de que el comercio lo prepare y queda «Cancelado» con la devolución a la misma tarjeta | OK |
| T5 | Javiera, observadora (iPhone), ve solo fecha, productos y «Pagado», sin montos ni botones | OK |

## Hallazgos

| ID | Severidad | Hallazgo | Destino |
|---|---|---|---|
| H1 | P2 | El observador todavía recibe montos en `GET /v1/pedidos/{id}` (viene de MATU-61) | MATU-113, bloqueante antes de datos reales |
| H2 | P3 | El summary de `GET …/pedidos` en `openapi.json` dice «2 años desde la entrega o la cancelación», sin «con devolución» (el código sí lo aplica) | Jorge |
| H3 | P3 | No se encontró en la CL-28 la nota de que la 0.20 se publica sin volver a aceptar | Jorge |

# TESTER · MATU-112 · Correcciones de la revisión del 15-11

**Revisor:** Martín Henríquez (modo Martín, con agentes) · **Fecha:** 17-11-2026
**PR:** MartinHenriquez131/MATU_PROYECTO#99 (head 8cc1960) y MATU#102, junto con MATU#100 (`lenguaje.md` 31) y MATU#97 (Decreto 52)
**Resultado:** **PASS**, sin P1 ni P2

## Revisiones

| Revisión | Resultado |
|---|---|
| QA | PASS. CI en verde (ci y web), rama al día con `main` y sin conflictos con MATU_PROYECTO#100. La prueba de H1 falla con el código de `main` y pasa con la corrección |
| Analista | CUMPLE en H1, H6, H7 y en el resumen antes de pagar. CL-72 y CL-73 siguen abiertas en la consulta legal |
| Documentos | MATU#97, #100 y #102 sin hallazgos; se fusionan limpio entre sí |
| Diseñador | APROBADA: resumen antes de pagar y «Si falta», a 360, 1280 y 1920 px, claro y oscuro, y 320 px con texto al 200 %. Un P3 opcional: el enlace del correo dentro de una frase mide 21 px de alto (exento por WCAG 2.5.8) |

## Despliegue (17-11)

- Fusionados con merge commit: MATU_PROYECTO#99 (493459b), MATU#100, MATU#97 y MATU#102.
- `matu-api` desplegado desde `main` en staging y en la demo. Sin migración ni variables nuevas.
- **Semilla en la demo**, sin `--restablecer`: `comercio2@example.com` quedó **creada**; las otras siete cuentas ya existían y conservan su contraseña. No se imprimió ninguna contraseña.
- **H1-e, solo lectura:**

| Entorno | `pedido_condiciones_completas` | `pedido_pago_con_condiciones` | Pedidos pagados sin versión |
|---|---|---|---|
| Demo | validado | validado | 0 |
| Staging | validado | validado | 0 |

## Teléfono (demo, 17-11, 10:22 a 10:38)

Carmen en el Motorola; las dos cuentas de comercio en el iPhone. Pedido con pañal (Almacén El Ejemplo) y toallitas (Bodega La Muestra), pagado con la AMEX de prueba.

| Paso | Qué se probó | Resultado |
|---|---|---|
| P1 | «Si falta» dice «El mismo producto. Si cambia el precio, lo ves antes de pagar.» | OK |
| P2 | El resumen antes de pagar ya no promete buscar el producto en otro comercio después de pagar | OK |
| P3 | `comercio2@example.com` ve solo las toallitas en «Pedidos de hoy» | OK |
| P4 | `comercio@example.com` ve solo el pañal | OK |

Con P3 y P4, cada comercio ve solo su parte de un pedido mixto (D-63-1). **H7 queda cerrado.**

## Hallazgos

| ID | Severidad | Hallazgo | Destino |
|---|---|---|---|
| — | P3 | El enlace `cuidaconmatu@gmail.com` del resumen mide 21 px de alto | Opcional, a criterio de Jorge |

**Pendientes de Jorge que no bloquean:** la propuesta del diseñador «Si falta antes de pagar: lo buscamos en otro comercio.» y `Demo/`, que todavía dice «Pagas lo mismo».

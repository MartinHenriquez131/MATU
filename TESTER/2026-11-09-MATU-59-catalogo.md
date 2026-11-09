# 2026-11-09 · MATU-59 · Catálogo curado

**Historia:** MATU-59 · Catálogo curado con los productos de las entrevistas ([tarjeta](https://trello.com/c/MarLqrLi))
**PR revisado:** MartinHenriquez131/MATU_PROYECTO#67 (head 6589d2f y, al día con `main`, 615f260). Documentos: MartinHenriquez131/MATU#55 (**sin fusionar**: va apilado sobre MATU #53)
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor` y `disenador-revisor` · **Fecha:** 09/11/2026
**Veredicto general:** PASS en el código, la normativa y el teléfono. No hay P1. **Queda pendiente fusionar MATU #55**

## Contexto de la revisión

- **CI:** verde en `ci` y en `web`, en 6589d2f y en 615f260.
- **Entorno:** staging, desplegado desde `main` en 237a7f6 el 09-11 a las 10:57 (hora de Chile). En el log, `Running upgrade 0018 -> 0019` corre antes de Uvicorn y `/v1/salud` responde 200. `CAPA3_HABILITADA=true` en staging desde las 10:56.
- **Revisión obligatoria:** sí, porque toca dinero.
- **Teléfono:** Motorola Edge 50 con Microsoft Edge, de 11:20 a 11:40.

## Criterios de aceptación

| # | Criterio | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Los seis productos de las entrevistas | PASS | `infra/semillas/catalogo_demo.py`; teléfono, paso B1 |
| 2 | Dos comercios simulados, con precio entero y stock por comercio | PASS | 12 `OfertaSemilla`, con precio entero y stock distinto en cada comercio |
| 3 | El puerto `CatalogoComercio` y un adaptador simulado | PASS | `application/ports.py`; `infrastructure/catalogo_simulado.py`, sin red |
| 4 | La consulta de stock lleva solo productos, cantidades y una referencia opaca | PASS | `ConsultaStock` con `lineas` y `secrets.token_urlsafe(16)`; `test_consulta_stock_dominio.py` |
| 5 | Los precios dicen que son de ejemplo | PASS | `Catalogo.tsx:205`; teléfono, paso B2 |
| 6 | El aviso de derecho a retracto va junto al precio, con letra no menor | PASS | `Catalogo.tsx:188-190` (`text-lg`, igual que el precio); el diseñador midió 19,1 px en los dos; teléfono, paso B3 |
| 7 | Categorías sin términos clínicos | PASS | «Higiene y cuidado personal», «Cuidado de la piel» y «Alimentación» |
| 8 | La capa 3 se puede quitar: apagada, responde 404 y la app dice «El catálogo no está disponible por ahora.» | PASS | `ROUTERS_CAPA_3`; `test_capa3_desacoplable.py`; `Catalogo.tsx:51,82`; el diseñador lo vio en `catalogo-apagado@` |
| 9 | La 0019 se puede bajar y cuelga de la 0018 | PASS | `down_revision="0018"`; `test_migraciones.py` |
| 10 | Dinero en pesos enteros y con formato `$15.990` | PASS | `textosCatalogo.ts` (`pesos`); teléfono, paso B2 |

## Definición de terminado

| Punto | Veredicto | Evidencia |
|---|---|---|
| 1 y 2. Pruebas | PASS | `test_catalogo_dominio`, `test_consulta_stock_dominio`, `test_catalogo_api` |
| 3. Contrato | PASS | `GET /v1/catalogo` con 200 y 401. `precio` es un entero y `disponible` un booleano, nunca la cantidad |
| 4. Accesibilidad | PASS | El diseñador de Martín da APROBADA la pantalla Catálogo. La disponibilidad va con ícono y texto |
| 5. Revisión de la otra persona | PASS | Fusionado por Martín el 09-11 a las 10:45 (9c4b692) |
| 6. Prueba que falla sin la corrección | No aplica | |

## Revisión normativa (analista-revisor)

- **CUMPLE:**
  - precio exacto por comercio, con IVA incluido y «Precio de ejemplo»;
  - el retracto en cada producto, del mismo tamaño que el precio;
  - la consulta de stock sin datos de la familia;
  - categorías sin términos clínicos.
- **REQUIERE CONSULTA LEGAL:** el retracto del suplemento y de las bolsas (`retracto_pierde_al_abrir=false` en la semilla).

## Prueba en el teléfono

Staging, en Insumos → Catálogo:
1. **B1:** aparecen los seis productos.
2. **B2:** cada precio dice «Precio de ejemplo» y se ve como `$15.990`.
3. **B3:** cada producto tiene el aviso de derecho a retracto.
4. **B4:** un producto sin stock lo dice con texto.

**Resultado:** PASS (informado por Martín el 09-11, de 11:20 a 11:40).

## Hallazgos

| ID | Severidad | Hallazgo | Evidencia | Qué pido corregir |
|---|---|---|---|---|
| H1 | P3 | La «Bolsa colectora» va en «Higiene y cuidado personal» | `catalogo_demo.py` | Que lo confirme el PO |
| H2 | P3 | El rótulo «(comercio ficticio)» no depende de si el comercio es de ejemplo. La tarjeta ya lo deja para MATU-61 | Tarjeta MATU-59 | Se ve en MATU-61 |

## Para decidir (PO)

- H1: la categoría de la bolsa colectora.

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | | | |
| H2 | | | |

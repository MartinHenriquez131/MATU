# 2026-11-12 · MATU-54 · Mis datos: ver y descargar la copia de los datos

**PR revisados:** MartinHenriquez131/MATU_PROYECTO#92 (0028, política 0.17) y MartinHenriquez131/MATU#87
**Revisó:** Martín Henríquez, con `qa-tester-revisor`, `analista-revisor`, `disenador-revisor` y `revisor-documental` · **Fecha:** 12/11/2026
**Revisión obligatoria:** sí (datos sensibles, derecho de acceso)
**Veredicto general:** PASS, sin P1

## Revisiones

- **QA: PASS.**
  - La 0028 es reversible y su bajada nunca borra la auditoría.
  - Otro grupo, el pagador, el observador y una persona borrada reciben 404, nunca 403.
  - El límite es de 10 copias por hora, y un 404 no gasta cupo.
  - Si la auditoría falla, la ruta de la persona no entrega nada.
  - La copia nunca trae tokens, PIN, IP, datos de tarjeta ni teléfonos de terceros.
  - Los logs no llevan la copia.
  - La descarga usa `Blob` y no guarda nada en el navegador.
- **Analista: CUMPLE** en quién la pide, qué trae, el formato, el límite, la auditoría, la política y el dinero. REQUIERE CONSULTA LEGAL: CL-61, CL-62, CL-63, CL-68 y CL-70.
- **Diseñador:** APROBADAS «Datos de…» y «Tus datos», a 320 px al 200 %, a 360, 1280 y 1920 px, en tema claro y oscuro, con los estados vacío, 503 y límite.
- **Documentos:** sin P1.

## Fusión y despliegue (hora de Chile)

- **Fusiones:** #92 (521cad3) y MATU#87 (3f5e5fe), con merge commit, después de poner las ramas al día con `main`.
- **Política:** `POLITICA_VERSION=0.17` en staging y en la demo.
- **Migración:** `Running upgrade 0027 -> 0028` sin errores, a las 16:12 en staging y a las 16:13 en la demo.

## Prueba en el teléfono

Demo, Motorola Edge 50 con Edge, el 12-11 de 16:15 a 16:22 (informado por Martín). D7 se repitió después.

| # | Prueba | Resultado |
|---|---|---|
| D1 | Carmen (admin) ve «Datos de…» sin teléfonos ni datos de tarjeta | OK |
| D2 | Descarga el `.json` sin volver a entrar | OK |
| D3 | Luisa (cuidadora) ve la pantalla, y en el historial solo lo suyo | OK |
| D4 | Rodrigo (pagador) no ve «Datos de…» | OK |
| D5 | Rodrigo descarga «Tus datos», con su cuenta y sus pagos | OK |
| D6 | Con la letra al máximo y en tema oscuro, los montos no se cortan y no hay desplazamiento hacia el lado | OK |
| D7 | Al abrir la pantalla 11 veces en una hora aparece el aviso de esperar con la hora | OK, en el segundo intento |

**Sobre D7:** en el primer intento se tocó «Descargar» unas 20 veces y no apareció el aviso. Los logs mostraron solo 3 pedidos de copia. Es lo diseñado: la descarga usa la copia ya cargada, y lo que cuenta es abrir la pantalla. Al abrirla varias veces, el aviso apareció.

**Resultado:** PASS.

## Hallazgos

| ID | Severidad | Hallazgo | Qué pido |
|---|---|---|---|
| H1 | P2 | En `/v1/yo/datos` falta la prueba de que no se entrega nada si falla la auditoría. Solo la tiene la ruta de la persona (QA) | Agregar la prueba, en el sprint 5 |
| H2 | P2 | Documentos: el registro, entrada 13, cita «350 a 361 y 401», pero `lenguaje.md` §35 usa la 377 y la 384. Además, la revisión previa §0 y §2 describe otra migración | Corregir el rango y marcar la revisión previa como reemplazada |
| H3 | P3 | Abrir la pantalla ya gasta una de las 10 copias. Quien solo quería mirar puede llegar al límite. Además, tocar «Descargar» varias veces no gasta nada, y eso puede confundir a quien prueba | Se anota. Revisar el texto del aviso si confunde en usabilidad |
| H4 | P3 | El enlace del correo de MATU mide 21 px de alto, aunque va dentro del texto y por eso cumple la excepción de WCAG. «Cobrado · Devuelto» se parte después del «·» | Se anota |

**Para decidir (PO):** la política §6 dice que el cuidador ve solo lo que hizo él, pero §10 y el registro agregan «y las aperturas del relevo». Hay que dejarlas iguales.

**A la consulta legal:** CL-61, CL-62, CL-63, CL-68 y CL-70.

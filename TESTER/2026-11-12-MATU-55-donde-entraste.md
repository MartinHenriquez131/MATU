# 2026-11-12 · MATU-55 · Dónde entraste, tus últimos ingresos y los avisos en este teléfono

**PR revisados:** MartinHenriquez131/MATU_PROYECTO#88 (0025, política 0.14) y MartinHenriquez131/MATU#81. Además, la corrección de Martín #91 (`Dockerfile`), que fusionó Jorge.
**Revisó:** Martín Henríquez, con `qa-tester-revisor` y `analista-revisor` · **Fecha:** 12/11/2026
**Revisión obligatoria:** sí (datos personales y auditoría de la cuenta)
**Veredicto general:** PASS, después de la corrección #91

## Revisiones

- **QA:** PASS, sin P1.
  - La 0025 se puede revertir.
  - `auditoria_cuenta_propia` solo deja leer la auditoría de la propia cuenta, y hay pruebas de aislamiento.
  - El CHECK se agrega con `NOT VALID` y después `VALIDATE`.
  - La API arranca sin `VAPID_CLAVE_PRIVADA`, y la clave nunca aparece en errores.
  - `sw.js` no tiene manejador de fetch, y «Salir» borra la inscripción.
- **Analista:** CUMPLE en minimización, derecho de acceso y C14 en los documentos.
  - REQUIERE CONSULTA LEGAL: los 3 años del registro de la cuenta (CL-53) y el proveedor del servicio push del fabricante (CL-37).
  - Martín verificó que el `push_token` no entra en la auditoría (`sesiones.py:356`, sin `detalle`).
- **CI:** `pedido.test.tsx` («fuera de rango al salir del campo») falló una vez y pasó al volver a correrlo. Es intermitente (P3).

## Fusión y despliegue (hora de Chile)

- **Fusiones:** #88 (feabcef) y MATU #81 (93c0cf3), con merge commit.
- **La consulta previa a la 0025 no se pudo hacer.** Con `SET row_security = off`, la base respondió `InsufficientPrivilege`, porque `auditoria` tiene FORCE RLS también para el dueño. No se apagó la protección a mano. Se dejó que la 0025 validara las filas dentro de su transacción: si fallaba, no se desplegaba.
- **Staging:**
  - antes de desplegar, `VAPID_CLAVE_PRIVADA` (generada en el PC de Martín), `POLITICA_VERSION=0.14` y `POLITICA_ACTUALIZADA_EN=2026-11-12`;
  - en el mismo despliegue se aplicó el borrado de `DIAGNOSTICO_PROXY`, que estaba guardado sin desplegar desde el 05-11;
  - a las 12:44: `Running upgrade 0024 -> 0025` sin errores y `diagnostico_proxy=apagado`.
- **Demo:** lo mismo, con su propia clave VAPID, a las 12:47.
- **Una clave VAPID se pegó por error en el chat.** Se descartó antes de usarla, y las dos que están en Railway son nuevas.

## Prueba en el teléfono

iPhone 11 con iOS 26.6.2 y Safari, en la demo con la cuenta de Carmen. El 12-11, de 12:52 a 13:15 (informado por Martín). Para cerrar a distancia (S8) se usó el Motorola Edge 50.

| # | Prueba | Resultado |
|---|---|---|
| S1 | Sin instalar: estado E con tres pasos, sin botón, también con el texto grande | OK |
| S2 | El menú Compartir de iOS dice «Agregar a inicio», igual que MATU | OK |
| S3 | Ícono en la pantalla de inicio | **FALLA:** sale una «T» con el título «Tu cuenta. MATU» |
| S4 | Instalada: sin la barra de Safari y en «Sin activar» | No se pudo evaluar sin S3 |
| S5 | Activar | **FALLA:** «No pudimos activar los avisos. Revisa tu conexión…». La petición nunca llegó a la API |
| S6 y S7 | Desactivar y bloquear | No se pudieron probar |
| S8 | «Cerrar en ese teléfono» desde el Motorola | **OK:** de 13:03 a 13:14, 11 minutos (el límite es 15). En los logs se ve el `DELETE /v1/dispositivos/{id}` 204 y después 404 en el iPhone |
| S9 | Salir borra la inscripción | No se pudo probar: depende de S5 |

**Causa de S3 y S5 (P1):**
- `infra/railway/Dockerfile` no copiaba `web/public`, así que la demo respondía 404 en `/manifest.webmanifest` y `/apple-touch-icon.png`, y no tenía `sw.js`. Martín lo comprobó en Safari.
- Martín lo corrigió en MartinHenriquez131/MATU_PROYECTO#91, con una prueba que falla sin el arreglo. Jorge lo fusionó, y se desplegó en staging y la demo.

## Segunda prueba en el teléfono, después de #91

iPhone 11 con iOS 26.6.2 y Safari, en la demo con la cuenta de Carmen. Se borró antes el ícono «T». Terminó a las 15:44 del 12-11 (informado por Martín).

| # | Prueba | Resultado |
|---|---|---|
| S3 | Ícono: corazón blanco sobre turquesa, con el nombre «MATU» | OK |
| S4 | Instalada: sin la barra de Safari, en «Sin activar» y sin pedir permiso al cargar | OK |
| S5 | Activar: «Activados», y «Activaste los avisos en Safari en iPhone» en Dónde entraste | OK |
| S6 | Desactivar: vuelve a «Sin activar» | OK |
| S9 | Salir borra la inscripción: al volver a entrar, «Sin activar» | OK |
| S7 | Bloqueado en Ajustes de iOS: aparece la nota «Tu navegador no deja…» | OK |

**Resultado:** PASS. Los nueve pasos están OK. S8 ya había pasado en la primera prueba.

## Hallazgos

| ID | Severidad | Hallazgo | Estado |
|---|---|---|---|
| H1 | P1 | La imagen de Railway no tenía `web/public`: sin manifest, ícono ni service worker | Corregido en #91 y verificado en el iPhone |
| H2 | P2 | C14 (avisos solo en teléfonos del equipo) se cumple solo por procedimiento, sin un control técnico (analista) | Para decidir (PO) |
| H3 | P3 | `pedido.test.tsx` es intermitente en el CI | Se anota |

## Respuesta de Jorge

| ID | Respuesta | Commit o PR | Verificado (Martín) |
|---|---|---|---|
| H1 | Fusionó #91 | a5f39ae | Sí: S3 a S7 y S9 OK, terminado a las 15:44 |
| H2 | | | |
| H3 | | | |

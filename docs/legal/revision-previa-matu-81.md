# Revisión previa del analista normativo · MATU-81 · Backoffice mínimo de operación

**17 de noviembre de 2026** · Agente analista normativo, a pedido del orquestador · Estado: **decisiones D-81-1 a D-81-12 tomadas por el orquestador con el mandato de Jorge del 16-11**

Esto no es asesoría legal: sirve para que Jorge decida. Este archivo es el resumen de la revisión previa del 17-11, con las decisiones que se tomaron. Lo que queda en REQUIERE CONSULTA LEGAL va a `consulta-legal.md`, como ampliación de la CL-28, la CL-67 y la CL-72. Jorge delegó las decisiones el 16-11: «según tu recomendación, foco en el usuario final». El orquestador aceptó todas las recomendaciones del analista, de la D-81-1 a la D-81-12.

**Dónde está lo construido:** la migración `0030_backoffice_operacion.py` (`down_revision = "0029"`) y las decisiones 449 a 465 de `docs/api/README.md` del repositorio MATU_PROYECTO, en la rama `matu-81-backoffice`. La especificación de pantallas es `docs/diseno/matu-81-operacion.md`, del mismo repositorio.

## 0. Resumen para la planificación

- **Hoy operación entra solo con contraseña.** `operador()`, en `backoffice/api/dependencias.py`, revisa solo `es_operacion`. Además, la ruta del código de retiro (`POST /v1/operacion/partes/{parte_id}/codigo`, decisión 418) quedó sin uso con la decisión 426, porque no puede existir una cuenta de operación sin MFA (el `CHECK` `usuario_operacion_mfa` exige `mfa_secreto_cifrado`). Se cierra con la D-81-1: el segundo factor entra en MATU-81.
- **Hoy operación lee de más en la base.** RLS le deja leer `persona_cuidada`, `consentimiento`, `direccion` y `aceptacion_politica`, y le deja escribir `pedido_entrega` (`FOR ALL`). Se cierra con la D-81-2 y la D-81-6.
- **La tabla `incidencia` no sirve como está.** Tiene tipos que perdieron su sentido con el ADR-027, una `descripcion` libre sin largo, una política `incidencia_operacion FOR ALL` que permite borrar y una FK sin `ON DELETE CASCADE`. Se cierra con la D-81-3 y las C10 a C16.
- **Las lecturas de operación se empiezan a registrar.** Abrir el detalle, la línea de tiempo o el cobro de un pedido se audita, y la familia lo ve en la copia de sus datos (D-81-5). Esto responde, por diseño, a la recomendación de la CL-67.
- **La política sube a la 0.21** (D-81-12). Nadie vuelve a aceptarla.

## 1. Veredicto por punto

| # | Punto | Veredicto | Condiciones y notas |
|---|---|---|---|
| P1 | **El catálogo de los comercios ficticios** | **CUMPLE** con la D-81-7 y las C1 a C4 | Operación cambia el precio, el stock y si se ofrece solo en comercios con `ficticio = true`, y la base lo impide en los demás. Un precio nuevo vale solo para las confirmaciones nuevas, nunca para un total vigente ni un pedido pagado |
| P2 | **Lo que operación lee de un pedido** | Hoy **NO CUMPLE**. Con la D-81-2, la D-81-6 y las C5 a C8 y C34, **CUMPLE** | Las respuestas de operación nunca traen datos de la persona cuidada, del grupo ni de la cuenta de la familia, con `extra="forbid"` y una prueba de contrato. Salen `persona_operacion`, `aceptacion_operacion_leer` y la lectura del consentimiento desde la aplicación. La entrega queda solo de lectura |
| P3 | **Registrar las lecturas de operación** | **CUMPLE** con la D-81-5 y la C9. Si basta con auditar el detalle y no las listas **REQUIERE CONSULTA LEGAL** (CL-67 ampliada) | Se audita `operacion.pedido_ver`, con grupo y persona y sin contenido. Las listas no se auditan |
| P4 | **Las incidencias** | Hoy **NO CUMPLE**. Con la D-81-3, la D-81-4 y las C10 a C16, **CUMPLE**. El plazo **REQUIERE CONSULTA LEGAL** (CL-28 ampliada) | Tipos nuevos, nota y resolución de hasta 500 caracteres con una ayuda contra los datos de salud, solo sobre pedidos pagados, sin borrado desde la aplicación y con `ON DELETE CASCADE`. La familia las ve en la copia como «Lo que pasó con tu pedido». Siguen al pedido: 2 años desde su cierre |
| P5 | **La conciliación** | **CUMPLE** con la D-81-8, la D-81-11 y las C17 a C19 | Se ven el total, lo cobrado, lo devuelto y cada anulación, sin la tarjeta ni el código de autorización. `buy_order` se muestra, nunca en la URL ni en los logs. `consumo_comercio` es solo de lectura |
| P6 | **El código de retiro en la pantalla** | **CUMPLE** con la D-81-10 y las C20 y C21 | El código vive solo en la memoria de la pantalla y se muestra una vez. Regenerarlo pide confirmar y anula el anterior. La tarea `codigo-retiro` queda como respaldo |
| P7 | **Los estados y los retractos** | **CUMPLE** con la D-81-9 y las C22 a C25. Quién prueba que el sello se abrió **REQUIERE CONSULTA LEGAL** (CL-72 ampliada) | Toda acción con dinero pide confirmar y muestra el monto que vuelve a la misma tarjeta. Rechazar exige un motivo de una lista cerrada (`sello_abierto` o `producto_no_recibido`), que la familia ve. El retracto por correo de un admin no lista nunca a los miembros del grupo |
| P8 | **El segundo factor de operación** | Hoy **NO CUMPLE**. Con la D-81-1 y las C26 a C33, **CUMPLE** | TOTP según el RFC 6238, con el secreto cifrado, la entrada en dos pasos, la marca del segundo factor en el token y en la sesión, una sesión de 12 horas como máximo y 5 intentos por cuenta. Una cuenta de operación no es miembro de un grupo ni de un comercio |
| P9 | **La accesibilidad** | **CUMPLE** con la C35 | El checklist de la estrategia de pruebas, sección 7 |
| P10 | **Política, registro, consulta legal, modelo y arquitectura** | **NO CUMPLE** hasta que se publiquen (D-81-12 y C36) | La política dice que el equipo de MATU «ve los pedidos y los pagos» sin decir cómo entra, qué registra ni qué no ve. El registro deja el MFA y la CL-67 como pendientes. Ver la sección 6 |

## 2. Decisiones

| Id | Qué se eligió | Quién |
|---|---|---|
| D-81-1 | **a)** El MFA con TOTP va dentro de MATU-81 (C26 a C33). La pantalla no se usa sin segundo factor, ni siquiera con datos sintéticos | Orquestador, por delegación |
| D-81-2 | **a)** La 0030 quita `aceptacion_operacion_leer`. Operación no lee las aceptaciones de la política | Orquestador, por delegación |
| D-81-3 | Los tipos de incidencia pasan a `faltante`, `entrega_fallida`, `reclamo_familia`, `cobro_sin_respuesta`, `devolucion_pendiente` y `otro`. Salen `desviacion_monto` y `captura_rechazada` | Orquestador, por delegación |
| D-81-4 | **a)** La familia ve sus incidencias en la copia de los datos (MATU-54): tipo, estado, fechas, nota y resolución. La pantalla, más adelante. Lo que ve la familia nunca dice «incidente» ni «incidencia»: dice «Lo que pasó con tu pedido» | Orquestador, por delegación |
| D-81-5 | **a)** Abrir el detalle, la línea de tiempo o el cobro de un pedido se audita como `operacion.pedido_ver`, con grupo y persona y sin contenido. En la copia se lee «El equipo de MATU revisó el pedido {referencia}». Las listas no se auditan | Orquestador, por delegación |
| D-81-6 | **a)** La 0030 quita `persona_operacion` y `consentimiento_operacion`, si nada las usa (se verifica con búsqueda y pruebas). `entrega_operacion` queda solo de lectura y `direccion_operacion_leer` se mantiene | Orquestador, por delegación |
| D-81-7 | El catálogo se edita solo en los comercios ficticios | Orquestador, por delegación |
| D-81-8 | La conciliación no muestra la tarjeta ni el código de autorización, pero sí `buy_order` | Orquestador, por delegación |
| D-81-9 | **a)** El retracto por correo de un admin lleva `correo_solicitante` en el cuerpo. El servidor lo busca entre los admins activos del grupo y responde 422 si no está. Nunca lista a nadie ni lo escribe en los logs | Orquestador, por delegación |
| D-81-10 | **a)** La tarea `codigo-retiro` queda como respaldo documentado | Orquestador, por delegación |
| D-81-11 | `consumo_comercio` es solo de lectura. Conciliar la boleta es RF-31 y queda fuera | Orquestador, por delegación |
| D-81-12 | La política sube a la **0.21** (la 0.20 es de MATU-92), sin volver a aceptar | Orquestador, por delegación |

**La migración 0030.** MATU-112 y MATU-92 no traen migración. Si MATU-76 lleva una, va después de esta.

**Ajustes al construir** (decisiones 449 a 465 del contrato):
- `consentimiento_operacion` no se quita del todo: pasa a `consentimiento_conservacion`, `TO matu_owner` (decisión 452). `plan_destruir_claves` y `consumo_conservar`, que corren como `matu_owner` con `app.rol = 'operacion'`, siguen leyendo el consentimiento para borrar a tiempo. Operación ya no lo lee desde la aplicación, y una prueba lo verifica.
- Se agrega `retracto.motivo_rechazo`, con un `CHECK` que lo admite solo en un retracto rechazado (C24, decisión 460).
- El TOTP se escribe con `hmac` y `hashlib`, sin dependencias nuevas, probado con los vectores del RFC 4226 y del RFC 6238. La sesión de operación dura como máximo 12 horas desde el segundo factor (decisiones 449 a 451).
- El alta se hace con `python -m app.tareas operacion-alta`, interactiva y con `matu_scheduler` (decisión 453).

## 3. Condiciones

**Catálogo**
- **C1.** Operación cambia `precio`, `stock` y `disponible` solo en ofertas de comercios con `ficticio = true`. En un comercio real, 409 o 404. La restricción va en la base (trigger o política), no solo en la API.
- **C2.** El precio es un entero en pesos, mayor que 0 y con IVA incluido, y se muestra como `$69.000`.
- **C3.** Un precio nuevo vale solo para las confirmaciones nuevas. No cambia `pedido_linea`, un total vigente ni un pedido pagado. Va con su prueba.
- **C4.** El cambio pide `If-Match`/`ETag` (412). Se audita sin grupo, como `catalogo.oferta_cambiar` (hay que ampliar el `CHECK` `auditoria_cuenta_acotada`), sin el valor anterior ni el nuevo.

**Pedidos y línea de tiempo**
- **C5.** Las respuestas de operación nunca traen datos de la persona cuidada: nombre, nivel de apoyo, dirección, teléfono, `persona_cuidada_id`, `grupo_id` ni el nombre del grupo. Tampoco el `usuario_id` ni el nombre de quien pidió o pagó. Va con `extra="forbid"` y con una prueba de contrato que recorra la respuesta, como `test_contrato_comercio.py`.
- **C6.** El actor de la línea de tiempo es `familia`, `comercio` (con `nombre_fantasia`), `operacion` o `sistema`. Nunca aparece el `actor_ref` de una cuenta de familia.
- **C7.** La búsqueda por referencia usa `POST`, con la referencia en el cuerpo. Nunca va en la URL, los logs, los errores ni la auditoría.
- **C8.** La lista incluye los pedidos cerrados y cancelados, y responde con `Cache-Control: no-store`.
- **C9.** Abrir el detalle, la línea de tiempo o el cobro se audita según la D-81-5. Las listas no.

**Incidencias**
- **C10.** Se usan los tipos de la D-81-3.
- **C11.** `descripcion` y `resolucion` llevan un `CHECK` de hasta 500 caracteres. La ayuda de la pantalla dice: «No escribas nombres, datos de salud ni la dirección. La familia puede leer esta nota.» El texto nunca va a logs, errores, eventos ni auditoría.
- **C12.** Solo se crean sobre pedidos pagados (trigger), y `pedido_id` tiene `ON DELETE CASCADE`.
- **C13.** Las políticas se separan en leer, crear y editar, sin DELETE (`REVOKE DELETE` para `matu_app`). Solo se pueden editar `estado`, `asignada_a`, `resolucion` y `resuelta_en` (`GRANT UPDATE (columnas)`). `creada_por` y `asignada_a` tienen que ser cuentas `es_operacion` (trigger).
- **C14.** Se auditan `incidencia.crear` e `incidencia.resolver`, con grupo y persona y sin el texto.
- **C15.** La familia las ve según la D-81-4: en la copia de MATU-54, con el texto «Lo que pasó con tu pedido».
- **C16.** En `test_aislamiento.py`: otro grupo no las ve, y una sesión de comercio lee cero filas.

**Conciliación**
- **C17.** Por pedido se ven el total confirmado, lo cobrado, lo devuelto, cada anulación (motivo, monto, estado e instante) y el estado de la venta. Además, una lista de ventas sin respuesta por más de 15 minutos y de anulaciones sin terminar.
- **C18.** Nunca se muestran el token, el `session_id`, `payload_respuesta`, los últimos 4, el tipo de tarjeta, las cuotas ni el código de autorización. `buy_order` se muestra, pero nunca va en la URL ni en los logs.
- **C19.** `consumo_comercio` es solo de lectura, sin acciones.

**Código de retiro**
- **C20.** El código va solo en la memoria de la pantalla y se muestra una vez. Nunca va en `localStorage`, `sessionStorage`, la URL, `history.state` ni el título, ni se copia al portapapeles, y se borra al salir. La pantalla dice cuándo vence y que regenerarlo anula el anterior.
- **C21.** Regenerar pide confirmar.

**Estados y retractos**
- **C22.** «Entregado», «no entregado», «cancelar con devolución» y «devolver» piden confirmar y muestran el monto que se devuelve a la misma tarjeta.
- **C23.** Las líneas del retracto (productos y cantidades) entran en la vista de operación. Para un retracto por correo, la pantalla usa las líneas del pedido.
- **C24.** «Rechazar» exige un motivo de una lista cerrada (`sello_abierto` o `producto_no_recibido`), que la familia ve en MATU-92. `producto_no_recibido` significa que MATU no recibió el producto de vuelta.
- **C25.** La D-81-9. Nunca se lista a los miembros del grupo.

**MFA**
- **C26.** TOTP según el RFC 6238: 6 cifras, pasos de 30 segundos y ventana de ±1. El secreto tiene 160 bits o más y va cifrado en `mfa_secreto_cifrado` con AES-256-GCM, la KEK y un AAD `mfa:<usuario_id>`. Nunca va en logs, errores ni respuestas.
- **C27.** `matu_app` sigue sin leer la columna. Una función `SECURITY DEFINER` (`matu_owner`, `search_path` fijo) entrega lo cifrado solo de la cuenta que está entrando, igual que `iam_credencial`.
- **C28.** El alta se hace con una tarea de consola interactiva: marca `es_operacion`, guarda el secreto y muestra la URI `otpauth` una sola vez. Sin SMS ni códigos de recuperación en el piloto: si se pierde el teléfono, se repite el alta.
- **C29.** La entrada tiene dos pasos. Con la contraseña correcta de una cuenta de operación, la respuesta no trae tokens: trae un desafío de 5 minutos, guardado solo como huella en Redis. `POST /v1/sesiones/mfa`, con el desafío y el código, entrega los tokens con la marca de MFA en el token y en `sesion_refresh`.
- **C30.** `operador()` exige la marca. Sin ella responde 401 `mfa-requerido`. Si la cuenta no es de operación, sigue respondiendo 404.
- **C31.** La sesión de operación dura como máximo 12 horas, sin el deslizante de 30 días.
- **C32.** Se permiten 5 códigos fallidos por cuenta (HMAC en Redis). Sin Redis, 503. Un paso ya usado no se acepta de nuevo. Se auditan `cuenta.mfa_alta`, `sesion.mfa_correcto` y `sesion.mfa_fallido`, sin grupo.
- **C33.** Una cuenta de operación no puede ser miembro de un grupo ni de un comercio, ni al revés (trigger, como la D-63-14).

**Base, accesibilidad y textos**
- **C34.** Una prueba asegura que ninguna ruta de `/v1/operacion` lee `persona_cuidada`, `direccion`, `pedido_entrega`, `consentimiento`, `plan_*` ni `perfil_consumo`. Las políticas siguen la D-81-6.
- **C35.** Se cumple el checklist de accesibilidad: 360 px, texto al 200 %, áreas de 48 px, foco visible y estado nunca solo por color.
- **C36.** Los borradores de documentos van en el PR de MATU.

## 4. Rutas

**Ya existen** (decisiones 418, 431 y 432 del contrato): `GET /v1/operacion/pedidos` (solo los pagados en curso), `POST /v1/operacion/partes/{parte_id}/codigo`, `POST /v1/operacion/pedidos/{id}/en-camino`, `…/entregado`, `…/no-entregado`, `…/cancelar-con-devolucion`, `POST …/pedidos/{id}/retractos` (por correo), `GET /v1/operacion/retractos` y `POST /v1/operacion/retractos/{id}/resolver`.

**Se agregan en MATU-81:**
1. `GET /v1/operacion/pedidos/{id}`: las partes, las líneas (producto, cantidad, precio pagado, estado y faltantes) y la línea de tiempo.
2. `POST /v1/operacion/pedidos/buscar`, con la referencia en el cuerpo, y un filtro por estado en la lista, incluidos los cerrados y cancelados.
3. `GET /v1/operacion/pedidos/{id}/cobro`: la conciliación del pedido.
4. `GET /v1/operacion/cobros/pendientes`: ventas sin respuesta y anulaciones sin terminar.
5. Las líneas del retracto en la vista de operación, `GET /v1/operacion/retractos/{id}` y el motivo del rechazo en `SolicitudResolverRetracto`.
6. `GET /v1/operacion/incidencias?estado=`, `POST /v1/operacion/pedidos/{id}/incidencias` y `PATCH /v1/operacion/incidencias/{id}` con `If-Match`.
7. `GET /v1/operacion/catalogo` y `PATCH /v1/operacion/ofertas/{id}`.
8. MFA: `POST /v1/sesiones` responde `mfa-requerido` con el desafío, y `POST /v1/sesiones/mfa` entrega los tokens.
9. `correo_solicitante` en `SolicitudRetractoPorCorreo` (D-81-9).

## 5. La migración 0030

- **a)** `incidencia`: el `CHECK` de los tipos, los largos, `ON DELETE CASCADE`, el trigger de solo pagados, el de cuentas de operación, las políticas sin DELETE y `GRANT UPDATE` por columnas. La bajada falla si hay filas con los tipos nuevos.
- **b)** `DROP POLICY aceptacion_operacion_leer`, y el ajuste de `test_migraciones.py`.
- **c)** Las acciones nuevas en los `CHECK` de la auditoría.
- **d)** MFA: la función del secreto, la marca en `sesion_refresh` y el trigger de separación de cuentas.
- **e)** La D-81-6, con `consentimiento_conservacion` para las funciones de conservación.
- **f)** `retracto.motivo_rechazo` (C24).
- **g)** El trigger del catálogo de los comercios ficticios (C1).

## 6. Documentos que cambian

En el PR de documentos de MATU-81 (rama `docs/matu-81-operacion`, sobre `docs/matu-92-tus-pedidos`):
- `revision-previa-matu-81.md`, este archivo.
- `registro-tratamientos.md`: las entradas 1, 2, 10, 13 y 14, y la entrada 15, nueva, para las cuentas de operación y el segundo factor.
- `politica-privacidad.md`, versión 0.21: §6, §8, §12 y §13. El párrafo del equipo de MATU en §6 pasa a: «**El equipo de MATU:** para operar los pedidos ve cada pedido con sus productos, cantidades, montos, su referencia y lo que pasó con él, y los pagos y las devoluciones, sin los datos de tu tarjeta. No ve el nombre de la persona que cuidas, su ficha ni el consumo de insumos. Entra con su contraseña y un código de su teléfono, y MATU registra cuándo revisa tu pedido. Si hay un problema con un pedido, lo anota con lo que pasó y cómo se resolvió, y lo ves en la copia de tus datos.» Desde la 0030 esa frase es cierta en la base, porque sale `persona_operacion`.
- `consulta-legal.md`: la CL-28, la CL-67 y la CL-72, ampliadas.
- `modelo-datos.md` y `arquitectura.md`: `incidencia`, la cuenta de operación con TOTP, `retracto.motivo_rechazo`, las rutas nuevas, el diseño del MFA y la 0030 en las tablas de migraciones.
- `lenguaje.md`: «Lo que pasó con tu pedido» y «El equipo de MATU revisó el pedido {referencia}», con la pantalla de la copia.

## 7. Consulta legal

Ninguna pregunta nueva. Se amplían:
- **CL-67:** si basta con registrar la apertura del detalle, la línea de tiempo y el cobro, sin registrar las listas, y si la familia debe ver esas aperturas en la copia de sus datos.
- **CL-28:** si las incidencias deben seguir al pedido (2 años desde su cierre), y cuánto se guarda el registro de la cuenta de operación y de su segundo factor.
- **CL-72:** quién prueba que MATU no recibió el producto de vuelta o que el sello venía abierto, y si basta con un motivo de una lista cerrada para que la familia sepa por qué se rechazó su retracto.

La próxima libre sigue siendo la **CL-74**. Ninguna bloquea el semestre, que trabaja solo con datos sintéticos y sin dinero real.

## 8. Si las horas no alcanzan

Se recorta en este orden: primero los indicadores (que no se piden), después la edición del catálogo y al final la búsqueda. **No se recortan** el MFA, las incidencias ni la conciliación.

# Revisión previa del analista normativo · MATU-63 · La vista del comercio, el código de retiro, el despacho y el retracto

**13 de noviembre de 2026** · Agente analista normativo, a pedido de Jorge · Estado: **decisiones D-63-1 a D-63-16 tomadas el 13-11**

Esto no es asesoría legal: sirve para que Jorge decida. Este archivo es el resumen de la revisión previa del 13-11, con las decisiones que se tomaron. Lo que queda en REQUIERE CONSULTA LEGAL va a `consulta-legal.md`, desde la CL-71. Jorge delegó el 13-11: «todo de acuerdo a tu recomendación, siempre poniendo foco en el usuario final», y confirmó él mismo la D-63-5, la D-63-9 y la D-63-10. El resto sigue la recomendación del analista, con las precisiones del orquestador.

**Dónde está lo construido:** la migración `0029_vista_comercio.py` (`down_revision = "0028"`) y las decisiones 407 a 430 de `docs/api/README.md` del repositorio MATU_PROYECTO. La especificación de pantallas es `docs/diseno/matu-63-comercio.md`, v1.1, del mismo repositorio.

## 0. Resumen para la planificación

- **Hoy el comercio lee y escribe de más en la base.** RLS filtra filas, no columnas. Con `pedido_comercio_ver`, el comercio lee la fila completa de `pedido` una vez enviado, con `grupo_id`, `persona_cuidada_id`, `creado_por`, `total` y `costo_envio`, y por herencia las líneas, las transiciones y las reglas si falta. Con `pedido_comercio_actualizar` puede escribir el pedido, **también `grupo_id`**, que es el hallazgo P1 de esta revisión. Se cierra con la D-63-1 y la D-63-2: el comercio lee y escribe solo por funciones.
- **El código de retiro cambia de dueño y de forma.** Hoy los documentos dicen que el comercio «ve» el código y que hay uno por pedido. Pasa a uno por parte, que el comercio solo puede **validar** y que dice quien retira por MATU (D-63-3 a D-63-5).
- **El ADR-027, punto 5, ahora sí se cumple:** MATU aparta el stock al confirmar (D-63-7).
- **R3 y R15 tienen regla y ruta en MATU-63, y pantalla en MATU-92.** El retracto queda con preguntas abiertas para la consulta legal (CL-71 y CL-72).
- **Hay que publicar la política 0.19 y las condiciones del pedido 0.3** (D-63-16). Nadie vuelve a aceptar la política. Las condiciones 0.3 se aceptan solo en los pedidos nuevos.

## 1. Veredicto por punto

| # | Punto | Veredicto | Condiciones y notas |
|---|---|---|---|
| P1 | **Lo que el comercio lee y escribe hoy en la base** | Hoy **NO CUMPLE**. Con la D-63-1 y la D-63-2, **CUMPLE** | Hallazgo P1: con `pedido_comercio_actualizar` el comercio puede cambiar `grupo_id` de un pedido. La 0029 quita `pedido_comercio_ver`, `pedido_comercio_actualizar`, `pedido_comercio_propio` y `linea_comercio_ver`. El comercio lee y escribe solo por funciones `SECURITY DEFINER`, con una prueba de que una sesión de comercio lee cero filas de las tablas del pedido y del pago, y de que no cambia `grupo_id`, el estado, las líneas de otro comercio ni el dinero |
| P2 | **El código de retiro** | **CUMPLE** con condiciones (D-63-3 a D-63-5) | Uno por parte, de 6 cifras, guardado solo como HMAC-SHA256, de un solo uso, vence a los 90 minutos y se bloquea al quinto intento. La huella se borra al usarse, al vencer o al bloquearse. Nunca en la URL, los logs, los eventos ni la auditoría. Lo recibe operación, que es quien retira en el piloto. La familia no lo ve y el comercio solo lo valida |
| P3 | **El stock apartado** | **CUMPLE** con la D-63-7 | El apartado lleva la referencia opaca, sin datos de la familia. El comercio ve por producto lo disponible y lo apartado |
| P4 | **Un producto que falta después de pagar** | **CUMPLE** con la D-63-8 | Se devuelve el mismo día, por anulación parcial a la misma tarjeta, y la dispara `sistema`, nunca la sesión del comercio. En el piloto no se busca en otro comercio después de pagar: las condiciones y `lenguaje.md` 31 prometían lo contrario y se corrigen |
| P5 | **R3, el derecho a retracto** | **CUMPLE** con condiciones (D-63-9 y D-63-10). Cómo se cuenta el plazo, el envío y el sello **REQUIEREN CONSULTA LEGAL** (CL-71 y CL-72, y las CL-54, CL-55 y CL-66 ampliadas) | El botón dura 10 días hábiles desde `entregado_en` y el correo acepta retractos hasta 90 días. Se pide por producto. El envío se devuelve solo si se devuelve todo, desde las condiciones 0.3. Los pedidos que aceptaron la 0.2 se respetan como estaban |
| P6 | **R15, cancelar después de pagar** | **CUMPLE** con la D-63-11 | Solo el admin, mientras ningún comercio empezó a preparar, con `FOR UPDATE` sobre la misma fila en los dos caminos. Se devuelve todo con el envío |
| P7 | **Quién marca «entregado»** | **CUMPLE** con la D-63-6 | El comercio llega hasta «retirado». «En camino», «entregado» y «no entregado» los marca operación. `entregado_en` es el inicio del retracto |
| P8 | **La auditoría** | **CUMPLE** con condiciones (D-63-12). Que el encargado no vea su propio registro **REQUIERE CONSULTA LEGAL** (CL-73) | Las acciones del comercio van sin grupo ni persona, con `actor_tipo = 'comercio'`, sin productos, cantidades, referencia ni código. En la línea de tiempo del pedido el comercio aparece por su `comercio_id`, nunca por la cuenta del encargado |
| P9 | **La conservación** | **CUMPLE** con la D-63-13. El borrado a los 2, 6 y 3 años queda **[PENDIENTE: MATU-89]** | Las partes, las líneas y los retractos siguen al pedido (2 años), las anulaciones de un retracto siguen al pago (6 años), la huella del código se borra al usarse, al vencer o al bloquearse, y el registro del comercio dura 3 años |
| P10 | **La cuenta del encargado del comercio** | **CUMPLE** para el piloto con la D-63-14. La base de licitud, quién responde y el plazo **REQUIEREN CONSULTA LEGAL** (CL-73) | Una cuenta de comercio no puede ser miembro de un grupo, y al revés. Una sesión de comercio nunca fija `app.grupo_id`. En el piloto, solo la cuenta de prueba `@example.com`, con datos sintéticos |
| P11 | **La ubicación de la evidencia** | **CUMPLE** con la D-63-15 | Sin fotos en MATU-63. `evidencia.lat` y `evidencia.lng` siempre nulas, con un `CHECK` |
| P12 | **Política, registro, condiciones y `lenguaje.md`** | **NO CUMPLE** hasta que se publiquen (D-63-16) | La política dice que el comercio ve el código, las condiciones prometen buscar en otro comercio después de pagar, y `lenguaje.md` 31 lo repite. Ver la sección 3 |

## 2. Decisiones

| Id | Qué se eligió | Quién |
|---|---|---|
| D-63-1 | **a)** El comercio lee solo por funciones `SECURITY DEFINER` (dueño `matu_owner`, `search_path` fijo, `EXECUTE` solo para `matu_app`), igual que `pago_resolver_venta`. Por parte ve `parte_id`, la referencia opaca (al azar por parte, nunca por familia), el estado, `enviado_en`, «preparar antes de» y el estado del código. Por línea, el producto con su presentación, la cantidad y el estado. Nunca `pedido_id`, `grupo_id`, `persona_cuidada_id`, `creado_por`, las condiciones, la referencia corta de la familia, montos, precios, lo devuelto, la oferta del carrito, las transiciones, la entrega ni la huella | Por delegación |
| D-63-2 | El comercio nunca escribe en `pedido`. Escribe solo por `comercio_preparar`, `comercio_marcar_linea`, `comercio_listo` y `comercio_validar_codigo`, que revisan la cuenta activa, el comercio activo, que no haya grupo y que la transición sea válida. El estado del pedido lo lleva `sistema`. En `oferta` cambia solo `stock` y `disponible` (trigger). En `consumo_comercio`, solo lee. En `evidencia`, nada. Su auditoría se limita a `actor_tipo = 'comercio'` | Por delegación |
| D-63-3 | Un código por parte (`pedido_comercio`), con su huella, vencimiento, uso, intentos y bloqueo, y el estado de la parte (`enviada`, `preparando`, `lista`, `retirada` o `cancelada`). `pedido.codigo_retiro_*` queda sin uso | Por delegación |
| D-63-4 | 6 cifras con `secrets`, generadas al pasar la parte a «lista». Solo el HMAC-SHA256 con `CODIGO_RETIRO_SECRETO`. 90 minutos, un solo uso, bloqueo al quinto intento fallido. Operación puede regenerarlo y queda auditado. Solo en el cuerpo del POST. Límite por cuenta de comercio por hora, en Redis | Por delegación |
| D-63-5 | **a)** El código lo recibe operación, que es quien retira por MATU en el piloto. Se muestra una sola vez y **la familia no lo ve**. La pantalla de operación va en MATU-81, y mientras tanto se genera desde la consola | **Jorge, 13-11** |
| D-63-6 | El comercio llega hasta «retirado», al validar el código. «En camino», «entregado» y «no entregado» los marca operación. `entregado_en` es el inicio del retracto | Por delegación |
| D-63-7 | **a)** MATU aparta el stock al confirmar, hasta `total_vence_en` más `VIDA_VENTA_WEBPAY_MINUTOS`. Se libera al cancelar, al usar «Cambiar el pedido» o al vencer sin un pago en curso, y se consume al pagar | Por delegación |
| D-63-8 | **a)** Un producto que falta después de pagar se devuelve el mismo día, por anulación parcial a la misma tarjeta. Si falta una parte, se devuelven las unidades que faltan y se entrega el resto. Si no se entrega nada, se devuelve todo con el envío | Por delegación |
| D-63-9 | **c)** El botón «Arrepentirme de la compra» dura **10 días hábiles** desde `entregado_en`, lo más protector mientras la CL-71 siga abierta, y la pantalla muestra la fecha exacta. El correo acepta retractos hasta 90 días mientras la CL-54 siga abierta | **Jorge, 13-11** |
| D-63-10 | Lo piden el admin o quien pagó, si sigue activo, por producto. Se devuelve cantidad × precio al recibir el producto con el sello intacto, por anulación a la misma tarjeta y antes de 45 días. **Envío (b): solo si se devuelve todo lo entregado**, desde las condiciones 0.3. Los pedidos que aceptaron la 0.2 se respetan con la opción (a). Las pantallas van en MATU-92 | **Jorge, 13-11** |
| D-63-11 | R15: el admin cancela después de pagar mientras ningún comercio haya empezado a preparar, y se devuelve todo con el envío | Por delegación |
| D-63-12 | La auditoría del comercio, de la familia y de MATU, sin productos, cantidades, montos, referencia ni código. Motivos nuevos de la línea de tiempo: `producto_faltante` y `retracto` | Por delegación |
| D-63-13 | La conservación de la sección 1, P9 | Por delegación |
| D-63-14 | Una cuenta de comercio no es miembro de un grupo, y al revés (trigger). La cuenta de prueba usa `@example.com` | Por delegación |
| D-63-15 | Sin fotos, y `evidencia` sin ubicación (`CHECK`) | Por delegación |
| D-63-16 | La política pasa a la **0.19**, después de la 0.18 de MATU-107. Las condiciones del pedido pasan a la **0.3**, y solo se aceptan en los pedidos nuevos. Nadie vuelve a aceptar la política | Por delegación |

**Faltantes asignados:**
- La pantalla de operación (código, «en camino», «entregado» y retractos): MATU-81. Las rutas van en MATU-63.
- R3 y R15 en la app de la familia: MATU-92.
- La copia de los datos (MATU-54) suma las partes, los faltantes y los retractos: hecho en MATU-63 (decisión 427 del contrato).
- El encargado del comercio no ve su propio registro en la aplicación: CL-73.

## 3. Documentos que cambian

En el PR de documentos de MATU-63 (rama `docs/matu-63-comercio`):
- `politica-privacidad.md`, versión 0.19: §3, §4, §6, §8, §12 y §13.
- `registro-tratamientos.md`: la entrada 2 y la entrada 14, nueva.
- `condiciones-pedido.md`, versión 0.3: §5, §6, §8 y §9.
- `consulta-legal.md`: CL-71, CL-72 y CL-73, y las CL-28, CL-54, CL-55 y CL-66 ampliadas.
- `lenguaje.md`: la sección 36, nueva, y la corrección de la 31.
- `arquitectura.md` y `modelo-datos.md`: las correcciones de la sección 4.

## 4. Contradicciones que se corrigen

1. **El comercio «ve» el código** (arquitectura 6.2, 9.5 y 11.2 con su tabla, política §6, registro, entrada 2, y `figura-legal-piloto.md`). Pasa a: el comercio **valida** el código, y lo dice quien retira por MATU.
2. **Un código por pedido** (arquitectura 7.4 y modelo 4.5). Pasa a un código por parte (`pedido_comercio`).
3. **Los estados que mueve el comercio** (arquitectura 8.7 y 9.5). Pasan a ser estados de la parte, y el estado del pedido lo mueve `sistema`.
4. **La invariante 3 de la arquitectura 8.3** vale para los faltantes. En el retracto, el envío se devuelve solo si se devuelve todo (condiciones 0.3), y la 0.2 se respeta. Lo mismo en lo resuelto por diseño de P5 (`consulta-legal.md`, `figura-legal-piloto.md` y arquitectura 18.1), que decía que el envío se devuelve siempre.
5. **La búsqueda en otro comercio después de pagar** (`lenguaje.md` 31 y condiciones §5) se cambia por la devolución el mismo día, en el piloto.
6. **El ADR-027, punto 5, ahora sí se cumple:** MATU aparta el stock al confirmar. Se cierra el PENDIENTE de la arquitectura 8.4.
7. **Quién marca «entregado»** (arquitectura 6.2, 8.7 y la tabla de estados): operación, no el comercio.
8. **El vault de MATU-92:** la familia no ve el código. Lo corrige el orquestador en el vault.
9. **La matriz del modelo 5.3, «Liquidación: los suyos»:** el comercio solo lee `consumo_comercio`.
10. **El modelo de datos** suma lo nuevo de la 0029: las partes con su estado, código y apartado, las unidades faltantes, `entregado_en`, `retracto` y `retracto_linea`, y los motivos `producto_faltante` y `retracto`.

## 5. Consulta legal (desde la CL-71)

- **CL-71 · Cómo se cuenta el retracto (nueva).** Bloquea el dinero real.
- **CL-72 · El envío y el sello en el retracto (nueva).** Bloquea el dinero real.
- **CL-73 · Los datos de quienes trabajan en el comercio (nueva).** Bloquea los datos reales.
- **Se amplían:** CL-28 (retractos, código y registro del comercio), CL-54 (el plazo del retracto si el comprobante queda solo en la aplicación), CL-55 (un retracto fuera del plazo de anulación de Transbank) y CL-66 (quién pide el retracto cuando paga una persona y arma otra).

La próxima libre es la **CL-74**. Ninguna bloquea el semestre, que trabaja solo con datos sintéticos y sin dinero real.

# Consulta legal de MATU

**Versión 1 · 8 de noviembre de 2026** (MATU-82). La redactó el orquestador del equipo de agentes con las preguntas del analista normativo, de las revisiones de Martín Henríquez y de las decisiones de Jorge Espinoza (Product Owner), que la aprueba.

## Qué es este archivo

- Es **la lista única de preguntas para el abogado y para el contador** que hay que responder antes de operar con datos reales o con dinero real.
- **No es asesoría legal.** Las preguntas las formuló el analista normativo, que no es abogado, y sirven para preparar la consulta. Las respuestas las dan el abogado y el contador.
- **El semestre opera solo con datos sintéticos**, en el ambiente de integración de Transbank y sin cobros reales (`figura-legal-piloto.md`). Por eso ninguna de estas preguntas bloquea el semestre.
- **La regla de ahora en adelante:** cada pregunta nueva entra aquí con el número siguiente, dentro de su tema. La última de MATU-61 es la CL-52. La CL-53 es de MATU-55, en otra rama, y puede haber otros números tomados en ramas abiertas: el número se confirma al fusionar. La tarjeta de Trello «Antes de datos reales · Consulta legal sobre el cuidador de hecho» solo enlaza a este archivo.
- **Las numeraciones antiguas dejan de usarse.** Las CL-1 a CL-4 de MATU-60, las CL-1 a CL-8 de MATU-44 y MATU-72, las 1 a 17 de MATU-26 y MATU-04, las del ADR-027 y las de cada revisión se traducen con la tabla de equivalencias del final.
- **Cuando llega una respuesta,** se anota en su casilla con la fecha y quién respondió. Después se lleva a la política de privacidad, al registro de tratamientos o al ADR que corresponda, y se cierra el `[PENDIENTE]` que indica la pregunta.

**Fuentes que se juntaron aquí:**
- la descripción y los 26 comentarios de la tarjeta de Trello, del 21 de octubre al 8 de noviembre de 2026
- `revision-matu-44.md`, `revision-matu-51.md`, `revision-matu-60.md`, `revision-previa-adr-027.md`, `investigacion-normativa-adr-027.md` y `figura-legal-piloto.md`
- los `[PENDIENTE]` de `politica-privacidad.md` y `registro-tratamientos.md`
- lo que al 8 de noviembre de 2026 todavía estaba en pull requests abiertos: `revision-matu-72.md` y los cambios de la política y del registro de MATU-72 y MATU-74, el cambio de la política de MATU-68 y la sección 27 de `lenguaje.md` de MATU-59.

## Cómo leer cada pregunta

- **Pregunta:** el texto para el abogado o el contador.
- **Origen:** la historia, la fecha y el comentario o el archivo de donde sale. Si se juntaron duplicados, aparecen todos.
- **Mientras tanto:** lo que MATU hace hoy, si se decidió algo.
- **Bloquea:**
  - **datos reales:** no se opera con personas reales sin la respuesta
  - **dinero real:** no se vende ni se cobra de verdad sin la respuesta
  - **ninguno:** conviene responderla, pero no detiene ninguna de las dos cosas.
- **Se cierra en:** el `[PENDIENTE]` que se cierra con la respuesta. Si no hay uno, lo dice.
- **Respuesta:** se completa después de la consulta.

En los orígenes, «Trello» es un comentario de la tarjeta de consulta legal, con su fecha. La política es `politica-privacidad.md` y el registro es `registro-tratamientos.md`, los dos en `docs/legal/`.

---

## 1. Quién autoriza y quién responde

### CL-01 · El cuidador de hecho

- **Pregunta:** ¿basta la autorización de una cuidadora o un cuidador de hecho, sin representación legal, para tratar los datos de salud de una persona adulta que no puede consentir y no tiene curador, bajo la Ley 21.719? ¿Sirve de base alguna excepción al consentimiento, como la del titular física o jurídicamente impedido (art. 16 c) o el mandato con facultad expresa (art. 12)?
- **Origen:**
  - descripción de la tarjeta de Trello (backlog v1.3, sección 9), la pregunta base
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 1
  - ADR-027, P3, en `investigacion-normativa-adr-027.md`, punto 3 de «Lo que todavía conviene llevar a un abogado» (27 de octubre de 2026). Lo que quedó abierto de P3 se une aquí
  - `figura-legal-piloto.md`, sección 6, punto 3
  - Trello del 3 de noviembre de 2026, como pregunta ya registrada.
- **Mientras tanto:** MATU-07 registra la calidad de quien autoriza, fija la revisión a los 12 meses y muestra el aviso `aviso_cuidador_de_hecho` (política, sección 5).
- **Bloquea:** datos reales.
- **Se cierra en:** registro, entrada 1, base de licitud («Cuidadora o cuidador de hecho: [PENDIENTE: consulta legal]»), entrada 3, base de licitud, y entrada 5, base de licitud. `figura-legal-piloto.md`, sección 6, punto 3.
- **Respuesta:** —

### CL-02 · La declaración del titular que registra otro usuario

- **Pregunta:** cuando la propia persona cuidada decide y otro miembro del grupo registra su decisión en MATU, ¿eso cumple la autorización expresa y por escrito? ¿Qué evidencia conviene agregar?
- **Origen:** MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 2.
- **Mientras tanto:** se guarda la declaración `declaracion_titular` con su versión, la fecha y quién la registró.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio. Afecta la base de licitud del registro, entrada 1.
- **Respuesta:** —

### CL-03 · Cómo se acredita el representante legal

- **Pregunta:** ¿qué documentos acreditan al representante legal para este fin? ¿Basta con una referencia que MATU no verifica?
- **Origen:** MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 3.
- **Mientras tanto:** MATU registra la calidad declarada y no pide documentos.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio.
- **Respuesta:** —

### CL-04 · Quién ejerce los derechos de la persona cuidada

- **Pregunta:** si la persona cuidada no puede ejercer sus derechos (ver, corregir, borrar, oponerse) y no tiene representante, ¿quién los ejerce? En particular, ¿puede una cuidadora o un cuidador de hecho pedir el borrado de sus datos por su cuenta?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 4
  - MATU-72, CL-7, segunda parte, en `revision-matu-72.md` (rama `docs/matu-72-borrar-al-tiro`) y en Trello del 8 de noviembre de 2026.
- **Mientras tanto:** en la aplicación borran y retiran el admin y el cuidador, sin preguntar en qué calidad (MATU-44 y MATU-72, decisión D1).
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 10, «Quién puede pedirlo» («[PENDIENTE: si la cuidadora o el cuidador de hecho puede pedirlo en su nombre…]»). Política, sección 10, «Borrar los datos de la persona que cuidas», en la rama de MATU-72.
- **Respuesta:** —

### CL-05 · Informar a la persona cuidada

- **Pregunta:** ¿cómo y cuándo hay que informar a la persona cuidada que otra persona entregó sus datos a MATU?
- **Origen:** MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 5.
- **Mientras tanto:** el aviso del cuidador de hecho le pide a quien autoriza contarle a la persona qué guarda en MATU, si puede comprenderlo.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio.
- **Respuesta:** —

### CL-06 · La revisión de los 12 meses y la ficha en pausa

- **Pregunta:** si la revisión de los 12 meses no se confirma, ¿corresponde suspender, bloquear o borrar, sin sacrificar la ficha de relevo? ¿Cuánto tiempo puede seguir guardada una ficha en pausa si nunca se renueva? ¿La revisión vencida cuenta como «fin de la autorización» para los 90 días de la sección 8 de la política?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 6
  - MATU-48, revisión de cierre, Trello del 4 de noviembre de 2026, pregunta 4.
- **Mientras tanto:** la ficha queda en pausa: nadie la ve, los enlaces de relevo no abren y lo escrito sigue guardado y cifrado.
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 5, al final de «Aviso para quien cuida sin ser representante legal» («[PENDIENTE: qué pasa si nunca se renueva y cuánto tiempo se guarda una ficha en pausa…]»).
- **Respuesta:** —

### CL-07 · Retirar una autorización que dio otra persona

- **Pregunta:** ¿una cuidadora o un cuidador de hecho, o cualquier admin o cuidador del grupo, puede retirar una autorización que dio la propia persona o su representante legal? Si la persona pide retirar una autorización que dio su representante, ¿qué pesa más?
- **Origen:** MATU-44, CL-2, revisión previa (Trello del 6 de noviembre de 2026, pregunta 2) y revisión de cierre (Trello del 7 de noviembre de 2026, y `revision-matu-44.md`).
- **Mientras tanto:** retiran el admin y el cuidador, sin importar quién la dio (MATU-44, decisión D1).
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio. El texto está en la política, sección 10, «Retirar una autorización».
- **Respuesta:** —

### CL-08 · El retiro de una persona sin cuenta

- **Pregunta:** si la persona cuidada no tiene cuenta, ¿basta con que un miembro del grupo registre su retiro «en su presencia»? ¿Qué evidencia hace falta?
- **Origen:** MATU-44, CL-3, revisión previa (Trello del 6 de noviembre de 2026, pregunta 3) y revisión de cierre (Trello del 7 de noviembre de 2026, y `revision-matu-44.md`).
- **Mientras tanto:** el retiro lo registra el admin o el cuidador en «Grupo familiar», sin evidencia adicional.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio.
- **Respuesta:** —

### CL-09 · Lo que escribe una cuidadora con contrato

- **Pregunta:** si quien escribe la ficha es una cuidadora remunerada, ¿de quién es lo que escribe? ¿Puede la familia usarlo como antecedente laboral?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 7
  - `figura-legal-piloto.md`, sección 6, punto 3 («registro escrito por una cuidadora remunerada»).
- **Mientras tanto:** nada decidido.
- **Bloquea:** datos reales.
- **Se cierra en:** `figura-legal-piloto.md`, sección 6, punto 3.
- **Respuesta:** —

### CL-10 · El responsable sin persona jurídica

- **Pregunta:** hoy el responsable del tratamiento son Jorge Espinoza y Martín Henríquez como personas naturales. ¿Se puede operar con datos reales así, o hace falta una persona jurídica antes?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 9 (MATU-27)
  - `figura-legal-piloto.md`, secciones 4.4 y 6, punto 1.
- **Mientras tanto:** el piloto opera solo con datos sintéticos, y la política dice que el responsable cambia en la versión 1.0 (política, sección 2). El tipo de persona jurídica va al contador en CL-47.
- **Bloquea:** datos reales y dinero real.
- **Se cierra en:** política, sección 2. `figura-legal-piloto.md`, sección 6, punto 1.
- **Respuesta:** —

## 2. Datos de salud y finalidades

### CL-11 · El art. 16 bis, inciso 1, y la asistencia social

- **Pregunta:** ¿el art. 16 bis, inciso 1, de la Ley 19.628 según la Ley 21.719 limita que esta plataforma trate datos de salud aunque tenga consentimiento expreso? ¿Sirve como base su letra e), sobre la prestación de asistencia sanitaria o social?
- **Origen:**
  - ADR-027, Trello del 27 de octubre de 2026, pregunta 1
  - ADR-027, P1, en `investigacion-normativa-adr-027.md`, sección 3 y punto 1 de «Lo que todavía conviene llevar a un abogado». Es el riesgo más alto
  - `revision-previa-adr-027.md`, «Para la tarjeta de consulta legal», punto 6, en lo que toca a la base de licitud
  - `figura-legal-piloto.md`, sección 6, punto 3.
- **Mientras tanto:** consentimiento expreso y separado por finalidad (ficha, consumo y pedidos).
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 4, «De tus pedidos» («[PENDIENTE: consulta legal sobre… si el art. 16 bis, inciso 1, de la ley limita su tratamiento…]»). Registro, entrada 2, base de licitud. `figura-legal-piloto.md`, sección 6, punto 3.
- **Respuesta:** —

### CL-12 · Los productos de un pedido como dato de salud

- **Pregunta:** un historial de pedidos de pañales para adulto, apósitos, bolsas de ostomía y otros insumos de cuidado, vinculado a una persona identificada, ¿es un dato relativo a la salud (art. 2 g)? ¿Requiere una autorización aparte para los pedidos y el despacho?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 11, en lo que toca a las compras y el despacho
  - ADR-027, Trello del 27 de octubre de 2026, pregunta 2
  - ADR-027, P2, en `investigacion-normativa-adr-027.md`
  - `revision-previa-adr-027.md`, punto 5b del resumen y punto 6 de «Para la tarjeta de consulta legal»
  - `figura-legal-piloto.md`, sección 6, punto 3.
- **Mientras tanto:** los pedidos se tratan como dato sensible, con una autorización expresa y aparte de la de la ficha (política, sección 4, «De tus pedidos»).
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 4, «De tus pedidos» («[PENDIENTE: consulta legal sobre si los productos de un pedido son un dato relativo a la salud…]»). Registro, entrada 2, datos. `figura-legal-piloto.md`, sección 6, punto 3.
- **Respuesta:** —

### CL-13 · El consumo declarado como dato de salud

- **Pregunta:** el consumo de insumos que declara la familia (pañales, sondas y otros), ¿es un dato relativo a la salud bajo la Ley 21.719? Si lo es, ¿basta protegerlo con la separación entre familias de la base de datos (RLS), sin cifrado propio? ¿Requiere una autorización aparte de la de la ficha, o la cubre la misma?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 11, en lo que toca al consumo
  - MATU-32, decisión 9 de Jorge, Trello del 31 de octubre de 2026
  - Trello del 3 de noviembre de 2026, como pregunta ya registrada
  - MATU-60, CL-2, que se relaciona con esta pregunta.
- **Mientras tanto:** se trata como dato sensible, con autorización propia de finalidad `consumo` y minimización, sin cifrado propio (decisión 63).
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 4, «De la persona que cuidas» («[PENDIENTE: consulta legal sobre si el consumo es un dato relativo a la salud y si basta esta protección]»). Registro, entrada 5, datos.
- **Respuesta:** —

### CL-14 · El nivel de apoyo en la autorización de la ficha

- **Pregunta:** la autorización de la ficha («guardar su ficha de relevo… y compartirla») no nombra el nivel de apoyo, que la política trata como dato sensible y que se guarda en el alta. ¿Lo cubre igual?
- **Origen:** MATU-68, revisión de los textos del alta, Trello del 8 de noviembre de 2026.
- **Mientras tanto:** se guarda con la autorización actual. Si la respuesta es que no lo cubre, cambian las tres declaraciones y se publica una versión nueva de la política.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` todavía. Afectaría la política, secciones 4 y 5.
- **Respuesta:** —

### CL-15 · La declaración de consumo y la lista de insumos

- **Pregunta:** la declaración de consumo autoriza «guardar…, calcular cuándo se acaban y avisarme». ¿Alcanza para que MATU arme una lista que la familia imprime o comparte con terceros? ¿O la declaración debe nombrar esa salida de forma expresa, como la de la ficha nombra «compartirla con el relevo»?
- **Origen:** MATU-60, CL-1, revisión previa, Trello del 6 de noviembre de 2026, y `revision-matu-60.md`.
- **Mientras tanto:** la lista se arma con la autorización de `consumo` vigente y la política dice «imprimir o compartir».
- **Bloquea:** datos reales.
- **Se cierra en:** registro, entrada 5, «Lista de insumos (MATU-60)», base de licitud («[PENDIENTE: consulta legal sobre si la declaración de consumo debe nombrar la lista y su salida antes de la versión 1.0]»).
- **Respuesta:** —

### CL-16 · La responsabilidad al compartir la lista

- **Pregunta:** un miembro del grupo imprime o comparte por WhatsApp una lista que puede revelar algo de la salud de la persona cuidada. ¿Ese acto queda fuera de la responsabilidad de MATU, que solo se la mostró a un miembro autorizado? ¿Basta el aviso en pantalla y en la política?
- **Origen:** MATU-60, CL-2, revisión previa, Trello del 6 de noviembre de 2026, y `revision-matu-60.md`.
- **Mientras tanto:** hay un aviso siempre visible sobre los botones de la lista, y la política dice que las copias impresas o compartidas quedan fuera de MATU.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio. Se relaciona con CL-13.
- **Respuesta:** —

### CL-17 · Usar un pedido para el cálculo del consumo

- **Pregunta:** cuando un pedido entregado por MATU sume al stock de insumos, los datos de un pedido se usarían en el cálculo del consumo. ¿Basta la autorización de consumo, o hace falta también la de pedidos? ¿Hay que exigir las dos vigentes al procesar ese suceso?
- **Origen:**
  - MATU-51, revisión previa, Trello del 7 de noviembre de 2026
  - `revision-matu-51.md`, punto 6 (capa 3), que daba REQUIERE CONSULTA LEGAL.
- **Mientras tanto:** MATU-51 queda 100 % a mano (decisión C de Jorge). Un pedido no suma al stock todavía (MATU-61 a 63). Cuando entre, exigirá una versión nueva de la política.
- **Bloquea:** datos reales, cuando entre la capa 3.
- **Se cierra en:** no tiene un `[PENDIENTE]` todavía.
- **Respuesta:** —

### CL-18 · La base del aviso a un pagador o a un observador

- **Pregunta:** el pagador y el observador reciben avisos de insumos solo si los activan, pero la autorización de consumo la dan el admin o el cuidador. ¿Basta esa autorización que dio otra persona del grupo, o el aviso a esos roles necesita una base propia?
- **Origen:** MATU-41, revisión de Martín (`TESTER/2026-11-05-MATU-41-avisos.md`, MATU #39), Trello del 5 de noviembre de 2026.
- **Mientras tanto:** el envío es simulado, y esos roles reciben avisos solo si los activan.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio.
- **Respuesta:** —

### CL-19 · Si el aviso fijo revela un dato sensible

- **Pregunta:** el aviso fijo «MATU: un insumo se está acabando. Abre la app para ver cuál», enviado por un proveedor de push o de correo, ¿revela un dato sensible?
- **Origen:** MATU-37, Trello del 3 de noviembre de 2026, pregunta 1.
- **Mientras tanto:** el aviso no dice qué insumo ni de quién, y el push va sin contenido.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio.
- **Respuesta:** —

### CL-20 · El diseño de «Sus remedios» (informativa)

- **Pregunta:** ¿el diseño de «Sus remedios» es suficiente para un dato de salud? Es opcional, de texto libre escrito por la familia y cifrado con la ficha. No va marcado al compartir, pide confirmación y muestra el aviso «Esto lo escribe la familia. No reemplaza la indicación del médico.». No tiene catálogo ni dosis estructuradas.
- **Origen:** ADR-028, MATU-49 y MATU-50, Trello del 3 de noviembre de 2026 («Pregunta informativa»), por recomendación de Martín y del analista.
- **Mientras tanto:** la decisión de Jorge se mantiene: «Sus remedios» va, por la seguridad del cuidado. La pregunta solo busca confirmar o ajustar el diseño.
- **Bloquea:** ninguno.
- **Se cierra en:** no tiene un `[PENDIENTE]`.
- **Respuesta:** —

### CL-21 · El nombre del grupo como texto libre

- **Pregunta:** el nombre del grupo es texto libre, sin cifrar y visible para todos los miembros. Podría traer un dato de salud o el nombre completo de la persona cuidada. ¿Basta la ayuda en pantalla como mitigación? Texto propuesto: «Un nombre corto, como Familia Soto. No incluyas el nombre completo de la persona que cuidas ni datos de salud. Lo verán las personas que invites al grupo.»
- **Origen:** MATU-06, revisión normativa de MATU-04, 05a y 06, Trello del 24 de octubre de 2026, pregunta 17.
- **Mientras tanto:** la ayuda en pantalla.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio.
- **Respuesta:** —

## 3. La cuenta, las autorizaciones y las versiones de la política

### CL-22 · La base de licitud de los datos de la cuenta

- **Pregunta:** ¿con qué base se tratan los datos de la cuenta (nombre, email, contraseña y celular)? Con la Ley 19.628 vigente, ¿basta con informar o hace falta un consentimiento expreso? Con la Ley 21.719, ¿se puede usar la ejecución de la relación contractual? ¿Basta el contrato de servicio, o hay que registrar la aceptación de la política? ¿Con qué base se pide el celular como obligatorio, si sirve para recuperar el acceso?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 14
  - MATU-04, revisión normativa de MATU-04, 05a y 06, Trello del 24 de octubre de 2026, pregunta 15
  - MATU-57, revisión de Martín (TESTER, P2-3), Trello del 5 de noviembre de 2026, pregunta 2.
- **Mientras tanto:** el registro usa «ejecución del servicio que pide la persona». Desde la política 0.11 (MATU-75) se guarda qué versión aceptó cada cuenta nueva, con la huella del texto. Si esa aceptación es un consentimiento está en CL-50.
- **Bloquea:** datos reales.
- **Se cierra en:** Registro, entradas 6, 7 y 10, base de licitud.
- **Respuesta:** —

### CL-23 · El identificador de versión de la política

- **Pregunta:** para que una autorización sirva como prueba, ¿basta guardar el número de versión de la política si el texto cambió dentro de la misma versión? Hoy `0.10` identifica varios textos (MATU-36, 41, 50, 25 y 60). ¿O cada texto publicado necesita su propio identificador o su huella?
- **Origen:** MATU-60, CL-3, revisión previa, Trello del 6 de noviembre de 2026, y `revision-matu-60.md`.
- **Mientras tanto:** desde la política 0.11 (MATU-75), `POLITICA_VERSION` es `0.11`. Antes, `0.10` identificó varios textos con el criterio del 6 de noviembre de 2026. Las declaraciones y el aviso tienen identificador y el aviso tiene su huella SHA-256. Desde la 0.11 cada texto de la política tiene su número y su huella (MATU-75).
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio. Afecta la política, sección 12.
- **Respuesta:** —

### CL-24 · Cuándo hay que publicar una versión nueva de la política

- **Pregunta:** con datos reales, ¿qué cambios obligan a publicar una versión nueva y a renovar las autorizaciones ya otorgadas, y cuáles basta con informar en la política vigente, a la que remiten las declaraciones con «según la política de privacidad vigente»? En particular:
  - agregar un dato opcional, como las unidades por envase, o una función nueva dentro de la misma finalidad, como la lista que se imprime o se comparte
  - activar un proveedor real, como el de correo. La política, sección 12, pide una autorización nueva «si un cambio agrega… personas que reciben datos». ¿Cuenta un encargado como «persona que recibe datos»?
- **Origen:**
  - MATU-60, CL-4, revisión de cierre, Trello del 6 de noviembre de 2026, y `revision-matu-60.md`
  - MATU-41, revisión de cierre, Trello del 4 de noviembre de 2026, pregunta 3.
- **Mientras tanto:** un cambio que no agrega usos, datos ni destinatarios no cambia la versión (criterio del 6 de noviembre de 2026). Si un encargado no cuenta, igual se publica una versión nueva de la política con sus nombres y su país.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]` propio. El texto está en la política, sección 12.
- **Respuesta:** —

### CL-50 · Si «Leí y acepto» es un consentimiento o un acuse de lectura

- **Pregunta:** la casilla obligatoria de crear cuenta, ¿es un consentimiento según la Ley 21.719 o solo deja constancia de que se informó? Si es un consentimiento, ¿vale siendo obligatoria? Si es un acuse, ¿qué base cubre los datos de la cuenta (CL-22)? ¿Basta la huella del texto puesto a disposición como prueba? ¿Hay que cambiar la frase «una huella del texto exacto que viste»? ¿Hay que pedir la aceptación de nuevo cuando cambia la versión?
- **Origen:** MATU-75 (CL-75-3). Se relaciona con CL-22, CL-23 y CL-24.
- **Mientras tanto:** casilla obligatoria sin marcar, con base «ejecución del servicio». Desde la 0.11 cada texto tiene su número y su huella. No se pide aceptar de nuevo al cambiar la versión, salvo que se agreguen usos, datos o destinatarios (§12).
- **Bloquea:** datos reales.
- **Se cierra en:** política §12. Registro, entrada 10, base de licitud.
- **Respuesta:** —

## 4. Conservación y borrado

### CL-25 · Los 90 días después de retirar una autorización

- **Pregunta:** ¿se pueden guardar la ficha y el consumo 90 días después de un retiro, sin que nadie los lea, solo para permitir volver a autorizar? ¿O hay que borrarlos de inmediato si no hay otra base?
- **Origen:** MATU-44, CL-1, revisión previa (Trello del 6 de noviembre de 2026, pregunta 1) y revisión de cierre (Trello del 7 de noviembre de 2026, y `revision-matu-44.md`).
- **Mientras tanto:** se guardan 90 días sin lectura y después se borran. El borrado a pedido no espera (MATU-72).
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 10, «Retirar una autorización» («[PENDIENTE: consulta legal sobre si se pueden guardar esos 90 días después del retiro]»).
- **Respuesta:** —

### CL-26 · El plazo del registro de autorizaciones

- **Pregunta:** ¿cuánto tiempo se guarda el registro de autorizaciones, también el de las retiradas? ¿Se puede anonimizar en vez de conservarlo?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 12, segunda parte
  - MATU-44, CL-4, revisión previa (Trello del 6 de noviembre de 2026, pregunta 4) y revisión de cierre (Trello del 7 de noviembre de 2026, y `revision-matu-44.md`).
- **Mientras tanto:** no se borra (trigger `consentimiento_sin_borrado`).
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 8, «Registro de autorizaciones» («[PENDIENTE: plazo, en consulta legal]»). Registro, entrada 1, conservación.
- **Respuesta:** —

### CL-27 · Lo que se conserva después de un borrado pedido

- **Pregunta:** después de un borrado pedido por la persona, ¿es proporcional conservar 3 años, sin texto, la auditoría, el registro de autorizaciones y los accesos y las aperturas del relevo, para demostrar cómo se usaron los datos? La auditoría guarda, por ejemplo, que existió una sección como «Sus remedios». ¿Cuánto puede quedar la fila de la persona borrada, solo con su número interno? ¿Y conservar 90 días el registro de avisos (a qué cuenta iba cada aviso, por qué canal y si salió, sin texto, destino ni nombres), también los avisos que se registran como «omitidos» después del borrado?
- **Origen:**
  - MATU-72, CL-8, en `revision-matu-72.md` (rama `docs/matu-72-borrar-al-tiro`, decisión D4)
  - Trello del 8 de noviembre de 2026.
- **Mientras tanto:** se conservan por sus plazos, sin texto, y ya no se ven en la aplicación. Se piden por correo.
- **Bloquea:** datos reales.
- **Se cierra en:** en la rama de MATU-72, política, sección 8, «La persona que cuidas, si pides borrar sus datos» («[PENDIENTE: plazo, en consulta legal]»), y registro, entrada 1, conservación (dos veces «[PENDIENTE: plazo, CL-27]»).
- **Respuesta:** —

### CL-28 · El plazo de los pagos y los pedidos

- **Pregunta:** ¿corresponde guardar 6 años los pagos y las boletas, y 2 años los pedidos y los comprobantes de entrega? **Ampliada con MATU-61:** ¿basta con borrar a los 30 días lo que nunca se pagó (el pedido en armado, el de total vencido y el cancelado sin pago), con su línea de tiempo, en vez de guardarlo 2 años? ¿Se puede guardar 24 horas, para no repetir un pedido, solo el estado y el número del pedido?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 12, primera parte
  - MATU-61, revisión previa, 10 de noviembre de 2026 (`revision-previa-matu-61.md`, punto 12 y sección 5), con la decisión D5 de Jorge del 11 de noviembre de 2026.
- **Mientras tanto:** el registro declara 2 años para los pedidos pagados y 6 años para pagos y boletas (arquitectura, sección 11.8). Lo no pagado se borra a los 30 días con una tarea del programador de MATU-74, y `idempotencia` guarda solo el estado y el id del pedido y se borra a las 24 horas (D5).
- **Bloquea:** dinero real. Lo no pagado, también datos reales.
- **Se cierra en:** política, sección 4, «De tus pedidos» («PENDIENTE: confirmar en la versión 1.0. CL-28 y CL-44»), y sección 8, «Pedidos que no se pagaron» («PENDIENTE: CL-28 ampliada»). Registro, entrada 2, conservación.
- **Respuesta:** —

### CL-29 · Destruir la clave y las copias de respaldo

- **Pregunta:** ¿destruir la clave de la persona cuenta como supresión? ¿Basta que lo borrado siga en las copias de respaldo hasta que venzan, incluidos los insumos y las compras anotadas, que no tienen una clave propia que destruir? ¿Qué plazo máximo de copias es aceptable?
- **Origen:**
  - MATU-44, CL-6, revisión de cierre, Trello del 7 de noviembre de 2026, y `revision-matu-44.md`
  - MATU-72, CL-6 ampliada, Trello del 8 de noviembre de 2026, y `revision-matu-72.md` (decisión D3)
  - Trello del 3 de noviembre de 2026, «respaldos», como pregunta ya registrada.
- **Mientras tanto:** se destruye la clave y, en la misma transacción, se borran el texto cifrado y las secciones. Si se restaura una copia, antes de usarla se vuelve a borrar lo pedido, con la auditoría `persona.borrar` como lista.
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 8, «Copias de respaldo» («[PENDIENTE: plazo]»). Registro, entrada 3, conservación, y entrada 5, conservación («copias de respaldo: [PENDIENTE]»).
- **Respuesta:** —

### CL-30 · El borrado que se pide por correo

- **Pregunta:** ¿cómo se verifica la identidad de una persona sin cuenta, o de su representante legal, que pide el borrado por correo? ¿Puede la familia volver a registrar y autorizar a la persona contra la voluntad de quien pidió el borrado?
- **Origen:** MATU-72, CL-7, primera y tercera parte, en `revision-matu-72.md` y en Trello del 8 de noviembre de 2026. La segunda parte, si un cuidador de hecho puede pedirlo, está en CL-04.
- **Mientras tanto:** en la aplicación borran el admin y el cuidador. El borrado por correo, sin pasar por el grupo, queda para antes de los datos reales (política, sección 13).
- **Bloquea:** datos reales.
- **Se cierra en:** en la rama de MATU-72, política, sección 10, «Borrar los datos de la persona que cuidas» («[PENDIENTE: consulta legal sobre cómo verificar la identidad de la persona sin cuenta…]»).
- **Respuesta:** —

### CL-31 · El margen de un día en los borrados por plazo

- **Pregunta:** con datos reales, ¿basta un margen técnico de un día, declarado en la política («a más tardar el día siguiente»), para los borrados por plazo?
- **Origen:** MATU-74, revisión previa, Trello del 8 de noviembre de 2026.
- **Mientras tanto:** las tareas de borrado corren cada madrugada, hora de Chile, y si una corrida falla, la siguiente borra lo pendiente.
- **Bloquea:** datos reales.
- **Se cierra en:** no tiene un `[PENDIENTE]`. El texto está en la política, sección 8, «Cuándo se borra», en la rama `docs/matu-74-programador-tareas`.
- **Respuesta:** —

### CL-32 · La cuenta y el celular después de eliminar la cuenta

- **Pregunta:** ¿cuánto tiempo se pueden guardar los datos de la cuenta, y en particular el celular, después de que la persona elimina su cuenta?
- **Origen:**
  - MATU-57, Trello del 3 de noviembre de 2026, pregunta 3
  - MATU-57, revisión de Martín (TESTER, P2-3), Trello del 5 de noviembre de 2026, pregunta 1.
- **Mientras tanto:** se guardan mientras exista la cuenta.
- **Bloquea:** datos reales.
- **Se cierra en:** registro, entrada 7, conservación («[PENDIENTE: plazo tras eliminar la cuenta]»). Política, sección 8, «Tu cuenta y las versiones de esta política que aceptaste».
- **Respuesta:** —

### CL-49 · La aceptación de la política después de eliminar la cuenta

- **Pregunta:** ¿cuánto tiempo se puede o se debe guardar el registro de la aceptación (versión, fecha y huella) después de que la persona elimina su cuenta? ¿Se guarda completo o sin el vínculo con la persona? ¿Es el mismo plazo de CL-32 y de CL-26?
- **Origen:** MATU-75 (CL-75-2). Se relaciona con CL-32 y CL-26.
- **Mientras tanto:** se guarda mientras exista la cuenta. La aceptación no se borra en cascada con la cuenta (migración 0021), y ninguna ruta borra cuentas.
- **Bloquea:** datos reales.
- **Se cierra en:** política §8. Registro, entrada 10, conservación.
- **Respuesta:** —

### CL-52 · La dirección de entrega después de un borrado pedido

- **Pregunta:** después de un borrado pedido por la persona, ¿se puede conservar la dirección y el teléfono de entrega de sus pedidos durante el plazo de los pedidos, o basta la comuna una vez cerrado el pedido? ¿Cuánto tiempo después de la entrega se justifica guardar la dirección completa para responder reclamos? **Ampliada en el cierre de MATU-61 (11-11):** si se retira la autorización de pedidos, ¿se puede conservar sin plazo la dirección de la persona, cuya única finalidad declarada es entregar sus pedidos, para cuando se vuelva a autorizar? ¿O corresponde un plazo, como los 90 días de la ficha y los insumos?
- **Origen:** MATU-61, revisión previa, 10 de noviembre de 2026 (`revision-previa-matu-61.md`, punto 10 y sección 5), con la decisión D2 de Jorge del 11 de noviembre de 2026. Se relaciona con CL-27, CL-28 y CL-44.
- **Mientras tanto:** en la misma transacción del borrado, los pedidos sin pagar se cancelan y se borran su dirección y su teléfono. Cuando existan los pagos, los pedidos cerrados quedarán solo con la comuna, y los pagados en curso conservarán la dirección hasta cerrarse (D2). El pedido no guarda el nombre de la persona (C16). En MATU-61 aplica solo la regla de los sin pagar. Al retirar la autorización, la dirección de la persona se conserva y la familia la puede vaciar cuando quiera, sin la autorización (C6 y C8). El plazo después del retiro queda para MATU-89.
- **Bloquea:** datos reales y dinero real.
- **Se cierra en:** política, sección 10, «Borrar los datos de la persona que cuidas» («PENDIENTE: CL-52 y CL-44»). Registro, entrada 2, conservación («[PENDIENTE: CL-52 y CL-44]»).
- **Respuesta:** —

## 5. El relevo y otras personas que anota la familia

### CL-33 · La base de licitud de los datos del relevo y de «A quién llamar»

- **Pregunta:** el relevo no tiene cuenta. MATU recibe su nombre y su teléfono de quien comparte, no de él, y guarda sus aperturas. Lo mismo pasa con los nombres y teléfonos de «A quién llamar». ¿Qué base de licitud aplica a esos datos? ¿Cómo se cumple el deber de informar a quien no entregó sus propios datos, si se guardan antes de que el relevo vea el aviso? ¿Basta con que la familia declare que le avisó? **Ampliada con MATU-61:** el teléfono de contacto de un pedido es por omisión el celular de quien pide, pero se puede cambiar por el de otra persona que no es usuaria, por ejemplo quien recibe el pedido. ¿Qué base de licitud aplica a ese teléfono? ¿Basta la ayuda «Si es el de otra persona, avísale.»?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 8
  - MATU-09, Trello del 27 de octubre de 2026, pregunta 4
  - MATU-48, revisión de cierre, Trello del 4 de noviembre de 2026, preguntas 1 y 2
  - MATU-61, revisión previa, 10 de noviembre de 2026 (`revision-previa-matu-61.md`, sección 5), con la decisión D4 de Jorge del 11 de noviembre de 2026.
- **Mientras tanto:** interés legítimo de la familia, informado. Quien comparte marca la casilla «Le avisé a {nombre}…» (decisión 34) y el relevo ve el aviso de `lenguaje.md`, sección 7.5, antes del PIN. La política pide avisar a quienes se anotan en «A quién llamar». En el pedido, la pantalla pide avisar a la persona cuyo teléfono se anota, y el teléfono se borra al cancelar el pedido.
- **Bloquea:** datos reales.
- **Se cierra en:** registro, entrada 4, base de licitud de los datos del relevo («[PENDIENTE: consulta legal]»). Registro, entrada 3, «personas anotadas en "A quién llamar"» («[PENDIENTE: consulta legal sobre su base de licitud]»). Registro, entrada 2, el teléfono de contacto («[PENDIENTE: consulta legal, CL-33 ampliada]»).
- **Respuesta:** —

### CL-34 · Los 3 años del registro de aperturas del relevo

- **Pregunta:** ¿es proporcional conservar 3 años la fecha, la hora y el nombre del relevo, que es un tercero? ¿Cómo encaja con su derecho a pedir el borrado frente a un registro de auditoría que no se modifica ni se borra?
- **Origen:**
  - MATU-45, Trello del 3 de noviembre de 2026, pregunta 1
  - MATU-48, revisión de cierre, Trello del 4 de noviembre de 2026, pregunta 3.
- **Mientras tanto:** 3 años desde que el acceso vence o se corta (política 0.10, sección 6).
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 6, «Quién abrió el enlace de relevo» («[PENDIENTE: consulta legal sobre si 3 años es proporcional…]»).
- **Respuesta:** —

## 6. Proveedores y transferencia internacional

### CL-35 · El alojamiento fuera de Chile

- **Pregunta:** si producción queda en Railway o en otro proveedor sin región en Chile, ¿qué garantías de transferencia internacional y qué cláusulas del contrato de encargo exige la Ley 21.719?
- **Origen:**
  - MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 10
  - MATU-25, revisión normativa del PR #29 (staging en Railway, región `sfo`, California), Trello del 5 de noviembre de 2026, pregunta 1
  - Trello del 3 de noviembre de 2026, «proveedores», como pregunta ya registrada.
- **Mientras tanto:** staging trata solo datos sintéticos y nunca se usa con datos reales. El proveedor de producción se elige antes (ADR-019).
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 7 («[PENDIENTE: proveedor y país donde se alojarán los datos reales]»). Registro, transferencia internacional de las entradas 1, 2, 3 y 4, y entrada 9 («[PENDIENTE: consulta legal]»).
- **Respuesta:** —

### CL-36 · Los proveedores de correo, SMS y WhatsApp

- **Pregunta:** ¿qué exige la Ley 21.719 para el contrato de encargo con el proveedor de correo, de SMS y de WhatsApp, y para la transferencia internacional si sus servidores están fuera de Chile? ¿WhatsApp (Meta) es encargado o responsable independiente?
- **Origen:**
  - MATU-37, MATU-41 y MATU-57, Trello del 3 de noviembre de 2026, pregunta 2
  - MATU-41, revisión previa, Trello del 4 de noviembre de 2026, pregunta 1
  - MATU-41, revisión de cierre, Trello del 4 de noviembre de 2026, pregunta 2.
- **Mientras tanto:** los envíos son simulados y no salen de la máquina (MATU-41, decisión 112).
- **Bloquea:** datos reales.
- **Se cierra en:** registro, entrada 5, comunicaciones a terceros («[PENDIENTE: nombrarlo, su país y el contrato]»), y entrada 8, comunicaciones y transferencia internacional. Política, sección 6, «Los avisos de insumos» y «Proveedores de tecnología».
- **Respuesta:** —

### CL-37 · El servicio de push del navegador

- **Pregunta:** el servicio de push lo elige el navegador del usuario (Google, Mozilla, Apple), no MATU, y recibe solo la dirección de avisos y un push sin contenido. ¿Es encargado de MATU bajo la Ley 21.719, o un tercero de otra calidad? ¿Cómo se informa la transferencia internacional?
- **Origen:**
  - MATU-37, MATU-41 y MATU-57, Trello del 3 de noviembre de 2026, pregunta 2, en lo que toca al push
  - MATU-41, revisión previa, Trello del 4 de noviembre de 2026, pregunta 2
  - MATU-41, revisión de cierre, Trello del 4 de noviembre de 2026, pregunta 1.
- **Mientras tanto:** push sin contenido (decisión 50 del contrato, confirmada el 9 de noviembre de 2026). El texto fijo lo pone el teléfono. El comentario 16 de la tarjeta, que hablaba de un push cifrado, quedó reemplazado por esa decisión: con solo el endpoint no se puede cifrar, y cifrar exigiría las claves `p256dh` y `auth`, que MATU no pide. En el semestre el envío es simulado.
- **Bloquea:** datos reales.
- **Se cierra en:** registro, entrada 5, comunicaciones a terceros («[PENDIENTE: consulta legal sobre la calidad del servicio de push del navegador y la transferencia internacional]»), y entrada 6, comunicaciones a terceros.
- **Respuesta:** —

### CL-38 · El dictado por voz

- **Pregunta:** el reconocimiento de voz del navegador (en Chrome, Google) envía el audio a servidores del fabricante, que pueden estar fuera de Chile, y ese audio es contenido de la ficha. ¿Basta con informarlo en la política, o hace falta un aviso en pantalla o un consentimiento? En «Sus remedios», que es un dato de salud, ¿se puede enviar ese audio a un encargado extranjero con la autorización actual? ¿Qué hay que informar o contratar?
- **Origen:**
  - MATU-39, Trello del 3 de noviembre de 2026, pregunta 2
  - MATU-50, revisión de cierre, Trello del 3 de noviembre de 2026.
- **Mientras tanto:** el botón de dictar está oculto solo en «Sus remedios» (decisión de Jorge del 3 de noviembre de 2026). Se reactiva quitando una condición en `web/src/familia/EditorSeccion.tsx`. En el resto de la ficha se informa en la política.
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 6, «Dictar en vez de escribir» («[PENDIENTE: consulta legal sobre el envío de audio de un dato sensible…]»). Registro, entrada 3, dictado.
- **Respuesta:** —

### CL-51 · El buzón de privacidad en una cuenta personal de Gmail

- **Pregunta:** cuidaconmatu@gmail.com es una cuenta personal de Gmail, de Google LLC, en Estados Unidos, y ya recibe correos reales que pueden traer datos de salud. Sin un contrato de encargo, ¿Google es encargado de MATU o un tercero de otra calidad? ¿Qué exige la Ley 21.719 para esa transferencia internacional? ¿Basta informarla en la política (§2 y §6), o hace falta una cuenta con un acuerdo de tratamiento de datos? ¿Es aceptable que dos personas compartan una sola cuenta?
- **Origen:** MATU-75, D5 y revisión de cierre, 9 de noviembre de 2026. Se relaciona con CL-35 y CL-36.
- **Mientras tanto:** una dirección de la función, con verificación en dos pasos y sin reenvío. Se pide no incluir datos de salud. El contenido nunca se copia al repositorio, a Trello, al vault ni a una sesión con agentes. Los correos se guardan 2 años. Quien responde cada solicitud queda anotado en la lista de solicitudes.
- **Bloquea:** datos reales. Conviene responderla antes, porque el buzón ya trata datos reales.
- **Se cierra en:** registro, entrada 11, encargado y transferencia. Política §6.
- **Respuesta:** —

## 7. Seguridad, huellas de IP y derechos

### CL-39 · La base de las huellas de IP y de email

- **Pregunta:** para limitar los intentos de crear una cuenta, entrar, recuperar el acceso y abrir un enlace de relevo, MATU guarda una huella de la IP y, al entrar o recuperar el acceso, una del email, que duran una hora o 24 horas como máximo y no permiten recuperar el dato. ¿Ese conteo necesita una base de licitud propia, o basta el deber de seguridad?
- **Origen:**
  - MATU-09, Trello del 27 de octubre de 2026, pregunta 5
  - Trello del 3 de noviembre de 2026, «base de las huellas de IP y email», como pregunta ya registrada
  - MATU-48, revisión de cierre, Trello del 4 de noviembre de 2026, pregunta 5
  - MATU-25, revisión normativa del PR #29, Trello del 5 de noviembre de 2026, pregunta 2, que la amplía a la creación de cuentas (5 por hora, decisión 114)
  - MATU-57, revisión de Martín, Trello del 5 de noviembre de 2026, pregunta 2, que la cita.
- **Mientras tanto:** las huellas no guardan la IP ni el email, y la IP no queda en la base de datos ni en los registros de MATU.
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 4, «Tu dirección IP y tu email, para limitar intentos» («[PENDIENTE: consulta legal sobre la base de este conteo]»). Registro, entrada 4, «para la dirección IP», entrada 6 y entrada 8, base de licitud de los contadores.
- **Respuesta:** —

### CL-40 · Los plazos de los derechos y de las filtraciones

- **Pregunta:** desde el 1 de diciembre de 2026, ¿qué plazo hay para responder las solicitudes de derechos? ¿Qué plazo y qué contenido debe tener la notificación de una filtración?
- **Origen:** MATU-26, revisión previa, Trello del 21 de octubre de 2026, pregunta 13.
- **Mientras tanto:** la meta interna es avisar dentro de 72 horas desde que se sabe de la filtración. Para los derechos, acuse dentro de 2 días hábiles y respuesta a más tardar en 30 días corridos (MATU-75, D4).
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 10, «Cómo» (`<!-- PENDIENTE: CL-48, plazo legal de respuesta antes y después del 01-12-2026 -->`), y sección 11 (`<!-- PENDIENTE: procedimiento escrito ante una filtración -->`).
- **Respuesta:** —

### CL-48 · El plazo para responder los derechos antes y después del 1 de diciembre de 2026

- **Pregunta:** MATU promete acusar recibo dentro de 2 días hábiles y responder a más tardar en 30 días corridos. ¿Cumple ese plazo con la Ley 19.628 mientras rija su texto actual, hasta el 30 de noviembre de 2026, y con la Ley 21.719 desde el 1 de diciembre de 2026? ¿Desde cuándo corre el plazo si pedimos confirmar la identidad? ¿Se puede prorrogar? ¿La respuesta debe informar el derecho a reclamar ante la Agencia? ¿Con qué base se tratan los datos que llegan al buzón?
- **Origen:** MATU-75, revisión previa (D4) y de cierre, 9 de noviembre de 2026 (CL-75-1). Amplía CL-40.
- **Mientras tanto:** acuse dentro de 2 días hábiles y respuesta a más tardar en 30 días corridos (D4).
- **Bloquea:** datos reales. Conviene responderla antes del 1 de diciembre de 2026, porque el buzón ya está activo.
- **Se cierra en:** política §10 «Cómo». Registro, entrada 11, base de licitud.
- **Respuesta:** —

## 8. Consumidor y catálogo

### CL-41 · El retracto del suplemento y de las bolsas colectoras

- **Pregunta:** ¿el suplemento nutricional y las bolsas colectoras caben en la exclusión de los bienes de uso personal o de higiene sellados del Decreto 52 de 2024, art. 4 N° 4, de modo que pierden el retracto si se abre el sello?
- **Origen:**
  - MATU-59, revisión previa, Trello del 8 de noviembre de 2026, pregunta 1, que la suma a P5 del ADR-027
  - `lenguaje.md`, sección 27, «Pendiente de la consulta legal» (rama `docs/matu-59-catalogo`).
- **Mientras tanto:** esos dos productos usan el texto del retracto sin la exclusión («Derecho a retracto: tienes 10 días desde que lo recibes.»), que es la opción más protectora. El resto de P5 está resuelto por diseño (ver «Lo que ya se resolvió por diseño»).
- **Bloquea:** dinero real.
- **Se cierra en:** `lenguaje.md`, sección 27, en la rama de MATU-59, y el campo `producto.retracto_pierde_al_abrir` de esos productos.
- **Respuesta:** —

### CL-42 · Las reglas sanitarias de venta y de rotulado

- **Pregunta:** ¿qué reglas sanitarias de venta y de rotulado aplican al suplemento (alimento), a la crema y a las bolsas (cosmético, producto farmacéutico o dispositivo médico)?
- **Origen:** MATU-59, revisión previa, Trello del 8 de noviembre de 2026, pregunta 2.
- **Mientras tanto:** el catálogo es de ejemplo y no se vende.
- **Bloquea:** dinero real.
- **Se cierra en:** no tiene un `[PENDIENTE]`.
- **Respuesta:** —

### CL-43 · Los productos que requieren receta

- **Pregunta:** ¿puede MATU mostrar con precio, o vender, productos que requieren receta (`requiere_receta`)?
- **Origen:** MATU-59, revisión de cierre, Trello del 8 de noviembre de 2026, pregunta 4.
- **Mientras tanto:** se recomienda excluirlos del catálogo, igual que ya los excluye la lista de insumos. Los medicamentos con receta están fuera del MVP (arquitectura, decisión 12, y ADR-022).
- **Bloquea:** dinero real.
- **Se cierra en:** no tiene un `[PENDIENTE]`.
- **Respuesta:** —

### CL-44 · Un pedido pagado cuando se retira la autorización de pedidos

- **Pregunta:** ¿qué pasa con un pedido pagado y en curso si se retira la autorización de pedidos? **Ampliada con MATU-61:** ¿y si se piden borrar los datos de la persona cuidada con un pedido pagado en curso? ¿Se puede terminar de entregar el pedido, con su dirección, aunque se haya pedido el borrado?
- **Origen:**
  - MATU-44, CL-5 (capa 3, R12), revisión previa (Trello del 6 de noviembre de 2026, pregunta 5) y revisión de cierre (Trello del 7 de noviembre de 2026, y `revision-matu-44.md`)
  - MATU-61, revisión previa, 10 de noviembre de 2026 (`revision-previa-matu-61.md`, punto 10 y sección 5), con las decisiones D1 y D2 de Jorge del 11 de noviembre de 2026.
- **Mientras tanto:** al retirar la autorización o borrar a la persona, los pedidos sin pagar se cancelan sin costo y se borran su dirección y su teléfono (D1 y D2). Los pagados siguen hasta entregarse, conservan la dirección hasta cerrarse y después quedan solo con la comuna, y se guardan el plazo de la sección 8, para responder reclamos y por obligación tributaria. En MATU-61 no hay pedidos pagados.
- **Bloquea:** datos reales y dinero real.
- **Se cierra en:** política, sección 4, «De tus pedidos» («PENDIENTE: confirmar en la versión 1.0. CL-28 y CL-44»), y sección 10, en el retiro de la autorización de los pedidos («PENDIENTE: CL-44») y en el borrado («PENDIENTE: CL-52 y CL-44»). Registro, entrada 2, conservación.
- **Respuesta:** —

### CL-45 · Un RUT reservado para ejemplos

- **Pregunta:** ¿existe un RUT o un rango de RUT reservado para ejemplos, como example.com para los correos?
- **Origen:** MATU-59, revisión previa, Trello del 8 de noviembre de 2026, pregunta 3.
- **Mientras tanto:** la semilla usa un RUT con el dígito verificador incorrecto a propósito.
- **Bloquea:** ninguno.
- **Se cierra en:** no tiene un `[PENDIENTE]`.
- **Respuesta:** —

## 9. Para el contador

### CL-46 · La boleta, la devolución y la compra al comercio

- **Pregunta:** MATU vende y emite una sola boleta por el total, con el envío incluido.
  - ¿Qué documento corresponde si se anula parte del cobro después de emitir la boleta, por un producto que no se entregó?
  - ¿La boleta de MATU lleva un nombre, por ejemplo el de quien paga?
  - ¿Cómo se documenta la compra de MATU al comercio, incluida la diferencia de precio que MATU asume si el producto se retira en otro comercio?
- **Origen:**
  - ADR-027, Trello del 27 de octubre de 2026, pregunta 3
  - ADR-027, P8, en `investigacion-normativa-adr-027.md`, «Decisiones de Jorge (27-10)»
  - `revision-previa-adr-027.md`, puntos 2d, 3c y 5d del resumen y punto 2 de «Para la tarjeta de consulta legal»
  - `figura-legal-piloto.md`, secciones 5 y 6, punto 3.
- **Mientras tanto:** no hay dinero real en el semestre.
- **Bloquea:** dinero real.
- **Se cierra en:** `figura-legal-piloto.md`, sección 5, «Quién vende» («[PENDIENTE: consulta tributaria sobre el documento tributario cuando hay devolución]»), y sección 6, punto 3.
- **Respuesta:** —

### CL-47 · El tipo de persona jurídica

- **Pregunta:** ¿qué tipo de persona jurídica conviene constituir para que MATU venda y emita la boleta, con su inicio de actividades? ¿Qué plazo y qué costo tiene?
- **Origen:** `figura-legal-piloto.md`, sección 2 (opción descartada sin estimar plazo ni costo) y sección 6, punto 1. Se relaciona con CL-10.
- **Mientras tanto:** el semestre opera sin persona jurídica y sin alta comercial en Transbank (MATU-27).
- **Bloquea:** datos reales y dinero real.
- **Se cierra en:** `figura-legal-piloto.md`, sección 6, punto 1 («Tipo, plazo y costo: [PENDIENTE]»), y sección 2.
- **Respuesta:** —

---

## 10. Pago (MATU-62)

### CL-54 · El contenido de la confirmación escrita

- **Pregunta:** ¿cumple el art. 12 A de la Ley 19.496 un comprobante dentro de la aplicación, sin correo? ¿Basta un correo sin la lista de productos, que remite el detalle a la aplicación? **Ampliada en la segunda revisión:** si quien paga no es quien armó el pedido, ¿a quién se le debe la confirmación? **Ampliada en el cierre de MATU-62:** si quien paga elige en Webpay cuotas con interés de su banco, ¿debe la confirmación decir algo más que «Pagaste {total} una sola vez»? Mientras tanto, el comprobante muestra «en {n} cuotas» y MATU cobra una sola vez.
- **Origen:** MATU-62, revisión previa, 10 de noviembre de 2026 (`revision-previa-matu-62.md`, sección 6); ampliada en la MATU-62, segunda revisión previa, 11 de noviembre de 2026 (`revision-previa-matu-62-segunda.md`, sección 6), con las decisiones del orquestador del 11-11 por delegación de Jorge.
- **Mientras tanto:** el comprobante queda en MATU, con los productos, y en el piloto no se envía por correo (P-62-5; verificar el correo va en MATU-91). Si falta la confirmación, el retracto podría subir de 10 a 90 días.
- **Bloquea:** dinero real.
- **Se cierra en:** condiciones del pedido 0.2, §4 («[PENDIENTE: CL-54]»).
- **Respuesta:** —

### CL-55 · La devolución si la anulación no es posible

- **Pregunta:** ¿qué medio cumple el art. 3 bis (45 días, sin retención) si Transbank no permite anular? ¿Pedir datos bancarios exige una base de licitud nueva?
- **Origen:** MATU-62, revisión previa, 10 de noviembre de 2026 (`revision-previa-matu-62.md`, sección 6).
- **Mientras tanto:** se reintenta la anulación, se avisa a operación y se le escribe a la familia, sin pedir datos bancarios (D-62-6 a).
- **Bloquea:** dinero real.
- **Se cierra en:** condiciones del pedido 0.2, §7 («[PENDIENTE: CL-55]»).
- **Respuesta:** —

### CL-56 · El rol de Transbank respecto de los datos de quien paga

- **Pregunta:** ¿Transbank es responsable por su cuenta de los datos de la tarjeta y de quien paga, o es encargado de MATU?
- **Origen:** MATU-62, revisión previa, 10 de noviembre de 2026 (`revision-previa-matu-62.md`, sección 6).
- **Mientras tanto:** MATU solo le envía el monto y un número de orden que no identifica a nadie, y nunca recibe ni guarda los datos de la tarjeta.
- **Bloquea:** datos reales.
- **Se cierra en:** política, sección 6, y registro, entrada 2, comunicaciones.
- **Respuesta:** —

### CL-64 · Qué se guarda de un pago que no se cobró o que se anuló completo

- **Pregunta:** ¿se puede borrar a los 30 días un intento rechazado o abandonado? ¿Un cobro anulado completo el mismo día cuenta como registro de pagos, con 6 años?
- **Origen:** MATU-62, segunda revisión previa, 11 de noviembre de 2026 (`revision-previa-matu-62-segunda.md`, sección 6), con las decisiones del orquestador del 11-11 por delegación de Jorge. Amplía la CL-28.
- **Mientras tanto:** la tarea de los 30 días separa por dinero (D-62-13 c): sin dinero, el pedido se borra con su cargo; con dinero, se guarda el cobro y su anulación, sin la dirección ni los productos.
- **Bloquea:** dinero real.
- **Se cierra en:** política, sección 8, y registro, entrada 2, conservación.
- **Respuesta:** —

### CL-65 · El pago aprobado de un total que ya no estaba vigente

- **Pregunta:** ¿basta con anular completo y avisar, o el pago aprobado obliga a entregar ese total (art. 12)? ¿Se debe respetar un pago del mismo total que llega después de los 15 minutos?
- **Origen:** MATU-62, segunda revisión previa, 11 de noviembre de 2026 (`revision-previa-matu-62-segunda.md`, sección 6), con las decisiones del orquestador del 11-11 por delegación de Jorge.
- **Mientras tanto:** un pago tardío del mismo total se respeta, y uno de un total reemplazado o cancelado se anula completo el mismo día (D-62-4, reglas 2 y 3).
- **Bloquea:** dinero real.
- **Se cierra en:** condiciones del pedido 0.2, §3.
- **Respuesta:** —

### CL-66 · Quién es el consumidor cuando paga una persona y arma otra

- **Pregunta:** ¿quién ejerce el retracto, quién reclama y a quién se le devuelve? **Ampliada en el cierre de MATU-62:** ¿cuál es la base de licitud de los datos del pago de quien paga sin haber armado el pedido: la ejecución de la compra que acepta, u otra?
- **Origen:** MATU-62, segunda revisión previa, 11 de noviembre de 2026 (`revision-previa-matu-62-segunda.md`, sección 6), con las decisiones del orquestador del 11-11 por delegación de Jorge.
- **Mientras tanto:** la aceptación de las condiciones queda con quien pagó (`condiciones_aceptadas_por`, D-62-16) y la devolución va siempre a la misma tarjeta.
- **Bloquea:** dinero real.
- **Se cierra en:** condiciones del pedido 0.2, §3 y §9.
- **Respuesta:** —

**Se amplían con MATU-62:** CL-44 (el retiro o el borrado con un pago en curso: si se aprueba, se anula completo el mismo día) y CL-28 (apunta a la CL-64). La CL-67 es de MATU-94 y la CL-53 de MATU-55, que entran con sus ramas. La próxima libre es la **CL-68**.

## Condiciones antes de datos reales

Estas no son preguntas legales. Son trabajo del equipo que tiene que estar hecho antes de operar con datos reales o con dinero real.

- **Enviar correo solo a emails verificados.** Hoy cualquiera puede registrar un email ajeno (MATU-41, revisión previa, Trello del 4 de noviembre de 2026, punto 3, y política, sección 13).
- **El correo de contacto** de privacidad (política, secciones 2 y 10). **Hecho en MATU-75, 09-11.**
- **Borrar los datos de la persona cuando lo pide por correo,** sin pasar por su grupo (MATU-72, política, sección 13).
- **Ver o descargar los datos desde la aplicación,** incluidas las compras anotadas. Mientras tanto, por el correo (política, sección 13, y `revision-matu-51.md`).
- **Borrar el teléfono del relevo a los 30 días** (MATU-46).
- **Renovar la autorización desde la aplicación** cuando vence la revisión de los 12 meses (MATU-69).
- **La clave maestra en un servicio de custodia,** fuera del servidor de aplicación (ADR-016, política, sección 9, y registro, entrada 3).
- **Un usuario propio para las tareas programadas,** con permiso solo para leer los identificadores (registro, entrada 5).
- **Nombrar los proveedores y su país** en la política: nube, push, WhatsApp, correo, SMS y registro de errores (política, secciones 6 y 7).
- **Revisar las condiciones de servicio y el acuerdo de tratamiento de datos de Railway,** y el plazo de sus registros HTTP (registro, entrada 9).
- **El procedimiento escrito ante una filtración** (política, sección 11).
- **Guardar qué versión de la política aceptó cada usuario** al crear su cuenta (política, sección 12). Es la evidencia mínima mientras se responde CL-22. **Hecho en MATU-75, 09-11.**
- **La proyección del comercio sin identificadores de la familia,** con una migración nueva antes de construir la vista del comercio (registro, entrada 2).
- **Verificar en integración la anulación parcial de una venta normal** con crédito y con débito, y los plazos de anulación de Transbank, antes del sprint 4 (política, sección 6, y `figura-legal-piloto.md`, sección 5). Es una verificación técnica, no legal.
- **La evaluación de impacto del art. 15 ter,** sea obligatoria o no (ADR-027, P7).
- **La persona jurídica y el alta comercial en Transbank** (`figura-legal-piloto.md`, sección 6, puntos 1 y 2), y **la política 1.0 revisada por un abogado** (punto 4).
- **El rol de la institución** respecto de los datos del piloto, que se confirma con el ramo, no con el abogado (`figura-legal-piloto.md`, sección 4.4).

## Lo que ya se resolvió por diseño

Estas preguntas se hicieron en algún momento y ya no van a la consulta.

- **El límite de intentos antes del 1 de diciembre de 2026** (MATU-04, Trello del 24 de octubre de 2026, pregunta 16): el límite ya está activo desde MATU-25, también al crear cuentas (decisión 114). La base de sus huellas sigue en CL-39.
- **Si un borrado puede esperar los 90 días de gracia** (MATU-26, Trello del 21 de octubre de 2026, pregunta 12, tercera parte): no espera. El borrado a pedido es inmediato desde MATU-72 (decisión de Jorge del 7 de noviembre de 2026).
- **Quién consiente por la persona mayor dependiente** (ADR-027, P3): con MATU-07, con la calidad de quien autoriza y la revisión a los 12 meses. Lo que quedó abierto está en CL-01.
- **Si la referencia opaca es un dato personal para el comercio** (ADR-027, P4, y `revision-previa-adr-027.md`, punto 7, comercios encargados o responsables): MATU trata al comercio como si fuera encargado, y el convenio lleva siempre las cláusulas del art. 15 bis.
- **El alcance del retracto** (ADR-027, P5, y `revision-previa-adr-027.md`, punto 3): aplica a todo producto sellado y se pierde solo si se abre el sello. MATU devuelve también el envío y paga el retiro. El suplemento y las bolsas siguen en CL-41.
- **La falta de entrega y si MATU revende o intermedia** (ADR-027, P6, y `revision-previa-adr-027.md`, punto 1, art. 43 de la Ley 19.496): MATU vende, devuelve el mismo día, responde ante la familia y después repite contra el comercio según el convenio.
- **La evaluación de impacto** (ADR-027, P7): se hace antes de operar con datos reales, sea obligatoria o no. Está en las condiciones.
- **El plazo legal de la devolución y el reglamento de comercio electrónico** (`revision-previa-adr-027.md`, puntos 4 y 5): los resolvió el texto de la ley (`investigacion-normativa-adr-027.md`, secciones 1 y 2). No hay un plazo legal específico, y los términos del pedido dicen «anulamos su cobro el mismo día».
- **El plan B del débito** (`revision-previa-adr-027.md`): salió de la consulta con el ADR-027, que cobra igual con crédito y con débito.
- **Las preguntas 1 a 3 del acceso de relevo** (MATU-09, Trello del 27 de octubre de 2026): resueltas por diseño en las decisiones de Jorge del 27 de octubre de 2026 (PR MATU_PROYECTO #19).

---

## Tabla de equivalencias

Cada fila traduce un número antiguo a su número nuevo. «Sin número» es una pregunta que su fuente no numeró.

### MATU-26 y MATU-04, 05a y 06 (Trello del 21 y del 24 de octubre de 2026)

| Historia | Número antiguo | Número nuevo |
|---|---|---|
| MATU-26 | 1 | CL-01 |
| MATU-26 | 2 | CL-02 |
| MATU-26 | 3 | CL-03 |
| MATU-26 | 4 | CL-04 |
| MATU-26 | 5 | CL-05 |
| MATU-26 | 6 | CL-06 |
| MATU-26 | 7 | CL-09 |
| MATU-26 | 8 | CL-33 |
| MATU-26 (MATU-27) | 9 | CL-10 |
| MATU-26 | 10 | CL-35 |
| MATU-26 | 11 | CL-12 (compras y despacho) y CL-13 (consumo) |
| MATU-26 | 12 | CL-28 (pagos), CL-26 (registro de autorizaciones) y resuelta (los 90 días) |
| MATU-26 | 13 | CL-40 |
| MATU-26 | 14 | CL-22 |
| MATU-04 | 15 | CL-22 |
| MATU-25 (desde MATU-04) | 16 | Resuelta |
| MATU-06 | 17 | CL-21 |

### ADR-027 (27 de octubre de 2026)

| Fuente | Número antiguo | Número nuevo |
|---|---|---|
| Trello del 27 de octubre de 2026 | 1 | CL-11 |
| Trello del 27 de octubre de 2026 | 2 | CL-12 |
| Trello del 27 de octubre de 2026 | 3 (contador) | CL-46 |
| `investigacion-normativa-adr-027.md` | P1 | CL-11 |
| `investigacion-normativa-adr-027.md` | P2 | CL-12 |
| `investigacion-normativa-adr-027.md` | P3 | Resuelta, y lo abierto en CL-01 |
| `investigacion-normativa-adr-027.md` | P4 | Resuelta |
| `investigacion-normativa-adr-027.md` | P5 | Resuelta, salvo el suplemento y las bolsas en CL-41 |
| `investigacion-normativa-adr-027.md` | P6 | Resuelta |
| `investigacion-normativa-adr-027.md` | P7 | Resuelta, y en las condiciones |
| `investigacion-normativa-adr-027.md` | P8 | CL-46 |
| `revision-previa-adr-027.md` | 1 (revende o intermedia) | Resuelta (P6) |
| `revision-previa-adr-027.md` | 2 (boleta) | CL-46 |
| `revision-previa-adr-027.md` | 3 (retracto) | Resuelta (P5) y CL-41 |
| `revision-previa-adr-027.md` | 4 (plazo de devolución) | Resuelta por el texto |
| `revision-previa-adr-027.md` | 5 (comercio electrónico) | Resuelta por el texto |
| `revision-previa-adr-027.md` | 6 (productos sensibles) | CL-11 y CL-12 |
| `revision-previa-adr-027.md` | 7 (comercios) | Resuelta (P4) |
| `figura-legal-piloto.md`, sección 6 | Cuidador de hecho | CL-01 |
| `figura-legal-piloto.md`, sección 6 | Cuidadora remunerada | CL-09 |
| `figura-legal-piloto.md`, sección 6 | Persona jurídica | CL-47 |

### MATU-09 a MATU-57 (27 de octubre al 5 de noviembre de 2026)

| Historia | Fecha | Número antiguo | Número nuevo |
|---|---|---|---|
| MATU-09 | 27 de octubre de 2026 | 1 a 3 | Resueltas |
| MATU-09 | 27 de octubre de 2026 | 4 | CL-33 |
| MATU-09 | 27 de octubre de 2026 | 5 | CL-39 |
| MATU-32 | 31 de octubre de 2026 | Sin número | CL-13 |
| MATU-45 | 3 de noviembre de 2026 | 1 | CL-34 |
| MATU-39 | 3 de noviembre de 2026 | 2 | CL-38 |
| MATU-37 | 3 de noviembre de 2026 | 1 | CL-19 |
| MATU-37, 41 y 57 | 3 de noviembre de 2026 | 2 | CL-36 y CL-37 |
| MATU-57 | 3 de noviembre de 2026 | 3 | CL-32 |
| MATU-49 y MATU-50 (Sus remedios) | 3 de noviembre de 2026 | Sin número | CL-20 |
| MATU-50 | 3 de noviembre de 2026 | Sin número | CL-38 |
| MATU-48 | 4 de noviembre de 2026 | 1 | CL-33 |
| MATU-48 | 4 de noviembre de 2026 | 2 | CL-33 |
| MATU-48 | 4 de noviembre de 2026 | 3 | CL-34 |
| MATU-48 | 4 de noviembre de 2026 | 4 | CL-06 |
| MATU-48 | 4 de noviembre de 2026 | 5 | CL-39 |
| MATU-41, revisión previa | 4 de noviembre de 2026 | 1 | CL-36 |
| MATU-41, revisión previa | 4 de noviembre de 2026 | 2 | CL-37 |
| MATU-41, revisión previa | 4 de noviembre de 2026 | 3 | Condición (emails verificados) |
| MATU-41, revisión de cierre | 4 de noviembre de 2026 | 1 | CL-37 |
| MATU-41, revisión de cierre | 4 de noviembre de 2026 | 2 | CL-36 |
| MATU-41, revisión de cierre | 4 de noviembre de 2026 | 3 | CL-24 |
| MATU-57, revisión de Martín | 5 de noviembre de 2026 | 1 | CL-32 |
| MATU-57, revisión de Martín | 5 de noviembre de 2026 | 2 | CL-22 |
| MATU-25 (PR #29) | 5 de noviembre de 2026 | 1 | CL-35 |
| MATU-25 (PR #29) | 5 de noviembre de 2026 | 2 | CL-39 |
| MATU-41, revisión de Martín | 5 de noviembre de 2026 | Sin número | CL-18 |

### MATU-60, MATU-44, MATU-51 y MATU-72 (6 al 8 de noviembre de 2026)

| Historia | Número antiguo | Número nuevo |
|---|---|---|
| MATU-60 | CL-1 | CL-15 |
| MATU-60 | CL-2 | CL-16 |
| MATU-60 | CL-3 | CL-23 |
| MATU-60 | CL-4 | CL-24 |
| MATU-44 | CL-1 | CL-25 |
| MATU-44 | CL-2 | CL-07 |
| MATU-44 | CL-3 | CL-08 |
| MATU-44 | CL-4 | CL-26 |
| MATU-44 | CL-5 | CL-44 |
| MATU-44 | CL-6 | CL-29 |
| MATU-51 | Sin número (punto 6, capa 3) | CL-17 |
| MATU-72 | CL-6 ampliada | CL-29 |
| MATU-72 | CL-7 | CL-30 (identidad y volver a autorizar) y CL-04 (cuidador de hecho) |
| MATU-72 | CL-8 | CL-27 |

### MATU-74, MATU-68 y MATU-59 (8 de noviembre de 2026)

| Historia | Número antiguo | Número nuevo |
|---|---|---|
| MATU-74 | Sin número (margen de un día) | CL-31 |
| MATU-68 | Sin número (nivel de apoyo) | CL-14 |
| MATU-59, revisión previa | 1 (retracto) | CL-41 |
| MATU-59, revisión previa | 2 (reglas sanitarias) | CL-42 |
| MATU-59, revisión previa | 3 (RUT de ejemplo) | CL-45 |
| MATU-59, revisión de cierre | 4 (receta) | CL-43 |
| Descripción de la tarjeta | Pregunta base (cuidador de hecho) | CL-01 |

### MATU-75 (9 de noviembre de 2026)

| Historia | Número antiguo | Número nuevo |
|---|---|---|
| MATU-75 | CL-75-1 | CL-48 |
| MATU-75 | CL-75-2 | CL-49 |
| MATU-75 | CL-75-3 | CL-50 |
| MATU-75 | Sin número (buzón en Gmail) | CL-51 |

### MATU-61 (10 y 11 de noviembre de 2026)

| Historia | Número antiguo | Número nuevo |
|---|---|---|
| MATU-61 | Sección 5, pregunta nueva (la dirección después de un borrado) | CL-52 |
| MATU-61 | Sección 5, ampliar CL-44 (borrado con un pedido pagado en curso) | CL-44 |
| MATU-61 | Sección 5, ampliar CL-33 (teléfono de contacto de quien no es usuario) | CL-33 |
| MATU-61 | Sección 5, ampliar CL-28 (lo nunca pagado no se guarda 2 años) | CL-28 |

### MATU-62 (10 y 11 de noviembre de 2026)

| Historia | Número antiguo | Número nuevo |
|---|---|---|
| MATU-62 | Revisión previa, sección 6 | CL-54, CL-55 y CL-56 |
| MATU-62 | Segunda revisión previa, sección 6 | CL-64, CL-65 y CL-66 |
| MATU-62 | Segunda revisión previa, ampliar CL-44 y CL-28 | CL-44 y CL-28 |

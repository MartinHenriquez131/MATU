# Política de privacidad de MATU

**Versión 0.12 · 11 de noviembre de 2026 (11/11/2026)** · agrega los pedidos de insumos hasta el total confirmado, con su autorización aparte, la dirección de entrega de la persona cuidada y el canal de reclamo (MATU-61). La versión 0.11 era del 09/11/2026
**Estado:** borrador para el piloto académico. Todavía no sirve para tratar datos reales.
**Aprobación:** aprobada como borrador v0.9 por Jorge Espinoza (Product Owner) el 25/10/2026. La revisión la hizo el orquestador del equipo de agentes, por delegación. Se confirman los tres compromisos del texto: MATU no vende datos, borra de inmediato los datos reales que entren por error, y ejercer los derechos es gratis. Los pendientes que quedan (plazos, proveedores y procedimiento ante filtraciones) se resuelven en la versión 1.0, antes de tratar datos reales.
**Identificador de versión en el sistema:** `0.12`
**Versión 0.10 (03-11):** la redactó el analista normativo con las decisiones de Jorge del 31-10, del 02-11 y del 03-11 (contrato de MATU-32, MATU-36 y MATU-38). Aprobada por Jorge el 05-11 como borrador del piloto, que trabaja solo con datos sintéticos. Antes de tratar datos reales pasa por la consulta legal. `POLITICA_VERSION` pasa a `0.10` en el backend con MATU-36
**ADR-027 (27-10):** las secciones que empiezan con esa nota adaptan el texto a los pedidos y pagos del ADR-027. Aprobado por Jorge el 27-10 como diseño. Las frases de §4 y §6 sobre lo que el comercio ve o no ve se publican en futuro («cuando existan los pedidos») y se cumplen con la capa 3 (MATU-61 a 63).
**MATU-50 (03-11):** se precisan las secciones 4, 6, 8 y 9 con la ficha ampliada ya construida, y se agrega que la ficha no se imprime (ADR-029). No agregan usos, datos ni destinatarios, y no cambian las declaraciones. No cambian la versión: `POLITICA_VERSION` sigue en `0.10`. Aprobado por Jorge el 03-11.

**MATU-09 (27-10):** se ajustan las secciones 4, 6, 8, 9, 10 y 13 con el acceso de relevo. Aprobado por Jorge el 27-10 como diseño. No cambian la versión: `POLITICA_VERSION` sigue en `0.9`.
**MATU-41 (04-11):** se ajustan las secciones 3, 6, 8 y 13 con los avisos por notificación y por correo. No agregan usos ni datos. No cambian la versión: `POLITICA_VERSION` sigue en `0.10`. Aprobado por Jorge el 04-11. Mientras el envío sea simulado no hay destinatarios nuevos. Activar un proveedor real de correo o de notificaciones exige una versión nueva de esta política, con sus nombres y su país.

**MATU-25 (05-11):** se ajustan las secciones 4, 7, 8 y 9 con el ambiente de prueba en Railway y el límite por IP. No cambian la versión: `POLITICA_VERSION` sigue en `0.10`, porque el ambiente de prueba trata solo datos inventados y ninguna persona real dio una autorización en él. Aprobado por Jorge el 05-11. La versión 1.0 nombrará el proveedor y el país donde se alojen los datos reales.

**MATU-60 (06-11):** se ajustan las secciones 3, 5, 6, 8 y 9 con la lista de insumos. La lista se arma con lo que el grupo ya ve, MATU no la guarda ni la envía, y quien la imprime o la comparte lo hace desde su teléfono. El único dato nuevo es cuántas unidades trae cada envase de un insumo, que describe el envase y no a la persona. No agregan usos ni destinatarios de MATU, así que no cambian la versión: `POLITICA_VERSION` sigue en `0.10`. **Criterio desde el 06-11 (decisión de Jorge):** la versión cambia cuando una declaración deja de cubrir lo que se trata. Un dato o una función nueva dentro de la misma finalidad se informa en la política vigente sin cambiar la versión. La consulta legal lo confirma antes de la versión 1.0 (CL-24). Aprobado por Jorge el 06-11.

**MATU-44 (06-11):** se ajustan las secciones 4, 5, 6, 8, 10 y 13 con el retiro de las autorizaciones desde la aplicación, volver a autorizar la ficha y el borrado de la ficha 90 días después del retiro. No agregan usos, datos ni destinatarios, y no cambian las declaraciones, así que no cambian la versión: `POLITICA_VERSION` sigue en `0.10` (criterio del 06-11). Aprobado por Jorge el 06-11.

**MATU-51 (07-11):** se ajustan las secciones 6 y 8 con «Compré» y «Me quedan», que anotan una compra o lo que queda en cualquier insumo, haya aviso o no, y las compras anotadas pasan a guardarse 90 días. No agregan usos, datos ni destinatarios, y un plazo más corto no cambia las declaraciones, así que no cambian la versión: `POLITICA_VERSION` sigue en `0.10` (criterio del 06-11). Aprobado por Jorge el 07-11.

**MATU-74 (08-11):** se ajustan las secciones 8 y 13 con el programador de tareas: los borrados por plazo corren solos cada madrugada. No agregan usos, datos ni destinatarios, así que no cambian la versión: `POLITICA_VERSION` sigue en `0.10` (criterio del 06-11). Aprobado por Jorge el 08-11.

**MATU-68 (08-11):** se precisa la sección 5: al dar de alta a la persona, «eliges quién la da» en vez de «eliges en qué calidad la das». No es una declaración y no agrega usos, datos ni destinatarios, así que no cambia la versión: `POLITICA_VERSION` sigue en `0.10`. Aprobado por Jorge el 08-11.

**MATU-72 (08-11):** se ajustan las secciones 4, 6, 8, 10 y 13 con el borrado sin espera de los datos de la persona. No agrega usos, datos ni destinatarios, y acorta plazos, así que no cambia la versión: `POLITICA_VERSION` sigue en `0.10` (criterio del 06-11). Aprobado por Jorge el 08-11.

**MATU-75 (09-11) · versión 0.11 (opción B, decisión D1 de Jorge del 09-11):** la política se muestra en la aplicación, en /privacidad, desde «En un minuto» hasta el final, y al crear la cuenta se registra qué versión se aceptó, con la huella SHA-256 del texto exacto que se mostró. Cambios: §2 y §10 publican el correo de contacto `cuidaconmatu@gmail.com` y los plazos (acuse en 2 días hábiles, respuesta en 30 días corridos, D4); §4, §8, §12 y §13 informan la aceptación con huella; §6 nombra el proveedor del buzón; cada [PENDIENTE] visible pasa a una frase completa, y su nota queda en un comentario HTML; las referencias internas y los identificadores de §5 pasan a comentarios. Cambia la versión porque cada texto aceptado con huella necesita su propio número. **Las declaraciones de §5 y el aviso no cambian**, así que nadie vuelve a autorizar: las autorizaciones dadas con 0.10 siguen con 0.10. Las cuentas creadas antes de la 0.11 quedan sin registro de aceptación (D2). Desde ahora, cualquier cambio de texto desde «En un minuto» hasta el final es una versión nueva, porque cambia la huella. Pendiente para la consulta legal: CL-48, CL-49 y CL-50. Aprobado por Jorge el 09-11.

**MATU-61 (11-11) · versión 0.12 (decisión D11 de Jorge del 11-11: una versión por fusión, numerada al fusionar):** se activan los pedidos de insumos hasta el total confirmado. El pago llega con MATU-62. Cambios, según la sección 3 de `revision-previa-matu-61.md` y las decisiones D1 a D12:
- §2 y §10: el correo de contacto recibe también los reclamos de los pedidos (D8).
- §3.6 y §4 «De tus pedidos»: qué se guarda de un pedido, sin el nombre de la persona (R7).
- §4: la dirección se pide con el primer pedido, sin ubicación en el mapa, y se puede vaciar (C8, C11, D4 y C6 de Jorge).
- §5: la autorización de pedidos, aparte, con sus tres declaraciones `declaracion_pedidos_<calidad>` (D1).
- §6: quién ve el pedido según su rol, y cada comercio ve solo sus productos y su referencia (R8, D7).
- §8: lo no pagado se borra a los 30 días (D5).
- §9: el pedido no se guarda en el teléfono (C18).
- §10: el retiro de la autorización de pedidos y el borrado de la persona con sus pedidos sin pagar (D1 y D2).
- §12 y §13: la versión y lo que todavía no funciona.

Cambia la versión porque agrega usos, datos y destinatarios. **Nadie vuelve a aceptar la política** ni a dar las autorizaciones de la ficha y de los insumos: el uso nuevo tiene su propia autorización expresa, con su declaración (D1). Las declaraciones de la ficha, de los insumos y el aviso del cuidador de hecho no cambian. Queda con la CL-24. Pendiente para la consulta legal: CL-52, y las CL-28, CL-33 y CL-44 ampliadas. **Pendiente de aprobación: la aprueba Jorge al fusionar**, junto con el texto de las tres declaraciones nuevas.

---

## En un minuto

- MATU te ayuda a organizar el cuidado de una persona mayor. Su parte principal es una ficha de relevo para quien te reemplaza.
- **Hoy MATU es un piloto académico y no guarda datos reales.** Si lo pruebas, usa nombres y datos inventados.
- MATU **no pide diagnósticos** ni fichas clínicas. Solo pide lo necesario para cuidar. Si quieres, puedes anotar en la ficha qué remedios toma y a qué hora, para que quien te reemplaza no se equivoque.
- La ficha se guarda cifrada. La ven solo las personas de tu grupo que tienen permiso y el relevo al que tú se la compartes, por el tiempo que tú elijas.
- MATU no usa publicidad ni analítica de terceros, y no vende datos.
- MATU nunca ve ni guarda los datos completos de tu tarjeta.
- Puedes pedir ver, corregir o borrar los datos escribiendo a cuidaconmatu@gmail.com. La sección 10 explica cómo.

---

## 1. Esto es un borrador del piloto académico

- MATU es un proyecto de título. Esta versión es un borrador escrito para su piloto académico, y **todavía no la revisa un abogado**.
- **Durante el piloto, MATU no trata datos reales.** Todo lo que hay en el sistema son datos inventados para probarlo, en los ambientes de prueba y de demostración. Lo único real es lo que explican las secciones 7 y 10: tu dirección IP al conectarte y los correos que nos escribas.
- Si estás probando MATU, **no escribas datos reales**, ni tuyos ni de otra persona.
- Si alguien ingresa datos reales por error, los borramos apenas lo sepamos.
- Antes de usar MATU con personas reales, publicaremos una versión nueva, revisada por un abogado, y te pediremos aceptarla.
- Algunas funciones que se describen aquí todavía se están construyendo. La sección 13 dice cuáles.

## 2. Quién es responsable de los datos

- **Responsable durante el piloto académico:** el equipo del proyecto, Jorge Espinoza y Martín Henríquez, como personas naturales. MATU todavía no tiene persona jurídica. Eso cambia en la versión 1.0, antes de tratar datos reales. <!-- decisión MATU-27 del 24/10/2026 -->
- **Contacto para temas de privacidad:** cuidaconmatu@gmail.com. Es una dirección del proyecto, no personal, y la leen solo Jorge Espinoza y Martín Henríquez.
- **Reclamos de un pedido:** al mismo correo, cuidaconmatu@gmail.com, como dicen las condiciones del pedido. <!-- D8 de MATU-61 -->

## 3. Para qué usamos los datos

1. Crear tu cuenta y dejarte entrar.
2. Formar tu grupo de cuidado y dar a cada persona su permiso.
3. Registrar a la persona que cuidas y la autorización para usar sus datos.
4. Guardar la ficha de relevo y compartirla con quien tú elijas.
5. Calcular cuándo se acaba cada insumo de la persona que cuidas, mostrarte cuáles se acaban pronto y avisarte. Con los que se acaban pronto, MATU arma una lista de insumos con una cantidad sugerida, que puedes imprimir o compartir desde tu teléfono. Los avisos dentro de la aplicación ya funcionan. En el piloto, los avisos por notificación y por correo se prueban sin enviarse: no salen de los equipos de MATU.
6. Hacer pedidos de insumos para la persona que cuidas: armar el pedido, elegir qué hacer si falta un producto, confirmar que haya cada producto y mostrarte el total antes de pagar, y entregarlo en la dirección que nos des. Pagar un pedido todavía no está disponible (sección 13).
7. Cuidar la seguridad: registrar quién abrió la ficha, detectar accesos extraños y responder si hay una filtración.

**Cada uso se autoriza por separado.** MATU pide una autorización para la ficha de relevo, otra para el cálculo de insumos y otra para los pedidos. La del cálculo se pide la primera vez que anotas un insumo. Los avisos de insumos van dentro de esa misma autorización: no se pide otra. La de los pedidos se pide la primera vez que haces un pedido (sección 5). Sin ella igual puedes imprimir o compartir la lista de insumos.

MATU no usa los datos para publicidad ni los vende. Tampoco toma decisiones automáticas sobre las personas. La fecha en que se acaba un insumo es solo una estimación para avisarte.

## 4. Qué datos guardamos

### De ti

- **Tu nombre, tu email y tu celular.** Para crear tu cuenta no pedimos nada más.
- **Tu celular** lo pedimos para enviarte un código cuando quieras recuperar tu contraseña. Antes de usarlo para eso, te pedimos confirmarlo con un código; mientras no lo confirmes, el código te llega a tu correo. Guardamos si lo confirmaste y si prefieres recibir los códigos por SMS o por WhatsApp. Si cambias el número, tendrás que confirmarlo de nuevo. El mensaje solo trae el código: nunca tu nombre, el de la persona que cuidas ni nada de su cuidado. No lo mostramos a otras personas del grupo ni lo usamos para publicidad. Del código guardamos solo una huella que no permite reconstruirlo, cuándo vence y cuántas veces se intentó, y la borramos al usarlo o a los 10 minutos. Cuando cambias tu contraseña, cerramos tu sesión en todos tus dispositivos (ver «Tu sesión») y te avisamos por el otro canal, o por tu correo si tu celular no está confirmado. **En el piloto, el código se prueba sin enviarse:** no sale de los equipos de MATU, así que no te llega un SMS, un WhatsApp ni un correo.
- **Tu email se guarda legible**, porque lo necesitamos para que entres y para escribirte. Lo protege la separación entre familias de la base de datos. Para iniciar sesión usamos además una huella del email que no permite recuperarlo.
- **Tu contraseña**, guardada transformada de una forma que no se puede revertir. Nadie en MATU puede leerla.
- **Los grupos a los que perteneces** y tu rol en cada uno.
- **Registros técnicos.** Por cada acción guardamos la fecha y hora, el tipo de acción sin su contenido, si resultó o no, cuánto tardó y un número interno que te identifica a ti y a tu grupo. En esos registros no guardamos tu email, tu contraseña, tus códigos de acceso, el nombre del grupo ni tu dirección IP.
- **Tu dirección IP y tu email, para limitar intentos.** Para evitar abusos, MATU limita cuántas veces se puede, desde una misma dirección IP, crear una cuenta, entrar, pedir un código para recuperar el acceso y abrir un enlace de relevo. Si alguien se equivoca varias veces al entrar, MATU hace esperar antes del siguiente intento. Para contarlos guardamos una huella de tu dirección IP y, al entrar o al recuperar el acceso, otra de tu email, que no permiten recuperarlos. La mayoría se borra sola en una hora; las de recuperar el acceso, en 24 horas como máximo (sección 8). No guardamos tu IP en la base de datos ni en los registros de MATU. Un abogado revisará la base legal de este conteo antes de usar MATU con datos reales. <!-- PENDIENTE: consulta legal sobre la base de este conteo -->
- **Tus dispositivos.** Por cada navegador donde entras guardamos un nombre general, como «Chrome en Android», y cuándo lo usaste por última vez. No guardamos los datos de tu navegador. Si activas los avisos, guardamos además la dirección que tu navegador nos da para enviártelos. Los avisos no dicen el nombre de la persona ni del insumo.
- **Cuando aceptas esta política al crear tu cuenta:** la versión que aceptaste, la fecha y la hora, y una huella del texto exacto que viste, que permite comprobar después cuál era. No guardamos tu dirección IP ni tu navegador. Puedes verlo en «Tu cuenta» (sección 12).
- **Cuando des una autorización** para la persona que cuidas: la fecha y la hora, en qué calidad la diste, qué declaración viste y la versión de esta política. En la de los pedidos, también una huella del texto exacto de la declaración que viste. Si eres cuidadora o cuidador de hecho, también qué aviso viste: su identificador, su versión y una huella de su texto. Si registras la decisión de la propia persona, queda anotado que la registraste tú, en su presencia. No guardamos tu dirección IP ni tu navegador.
- **Cuando retires una autorización:** la fecha y la hora, y quién la retiró. No guardamos tu dirección IP ni tu navegador. La autorización retirada no se borra: queda como respaldo de que se dio y de cuándo se retiró (sección 8).
- **Cuando pidas borrar los datos de la persona que cuidas:** la fecha y la hora, y quién lo hizo. Las autorizaciones que estaban vigentes quedan retiradas en ese momento.

### Tu sesión

- Cuando entras, MATU deja en tu navegador una cookie protegida que ninguna página puede leer. Mientras uses MATU al menos una vez cada 30 días, no te pedirá la contraseña de nuevo. Si pasan 30 días sin usarla, tendrás que volver a entrar.
- Si alguien copia esa cookie y la usa, MATU lo detecta y cierra todas las sesiones que salieron de esa entrada.
- Si cierras la sesión, sacas un dispositivo, se bloquea tu cuenta o cambias tu contraseña, una sesión que ya estaba abierta en ese dispositivo puede seguir activa hasta 15 minutos.
- Si alguien te saca de un grupo, dejas de verlo en ese mismo momento.

### De tu grupo

- El nombre del grupo, que eliges tú. No se cifra.
- Usa un nombre corto, como «Familia Soto». No incluyas el nombre completo de la persona que cuidas ni datos de salud.

### De la persona que cuidas

La persona que cuidas no tiene cuenta en MATU. Sus datos los ingresas tú.

- Su nombre y el nombre con que la llaman.
- Su nivel de apoyo: autovalente con supervisión, apoyo parcial o apoyo total.
- Su dirección de entrega: calle, número, depto, comuna y una referencia, si la escribes. No la pedimos al registrarla: la pedimos con el primer pedido y la guardamos para los próximos. La usamos solo para entregar sus pedidos. No guardamos su ubicación en el mapa. En la referencia no escribas datos de salud. Quien administra el grupo o quien la cuida puede cambiarla o vaciarla cuando quiera, aunque se haya retirado la autorización de los pedidos. <!-- D4, C8, C9 y C11 de MATU-61, y C6 y C8 de Jorge -->
- La autorización: quién la dio, en qué calidad y cuándo, y la referencia al documento si quien autoriza es su representante legal.
- Si diste la autorización como cuidadora o cuidador de hecho, la fecha en que te pediremos confirmar que sigues a cargo, 12 meses después.
- La ficha de relevo, con sus tres campos: **Su día**, **Si se altera** y **A quién llamar**. También guardamos quién escribió cada campo y cuándo.
- **Su consumo de insumos:** qué insumos usa, en qué unidad, cuánto usa cada cuántos días, cuánto quedaba la última vez que lo anotaste, con cuántos días de anticipación quieres saberlo y, si lo anotas, cuántas unidades trae cada envase. Con eso MATU calcula una fecha estimada. Si el insumo no está en el catálogo, guardamos el nombre que escribas: usa el nombre del envase, sin remedios ni para qué lo usa. Los remedios van en la ficha, no en los insumos.
- **Secciones adicionales de la ficha**, si decides agregarlas: Quién es, Lo que le hace bien, Comer y beber, Moverse y descansar, Cómo hablarle y Sus remedios. Todas son opcionales y se escriben con tus palabras, hasta 500 caracteres cada una (800 en Sus remedios). Se guardan cifradas, como la ficha, y siguen sus mismos plazos. Si quitas una sección, su texto se borra en ese momento y quien tenga un enlace deja de verla. Si la vuelves a agregar, ningún enlace anterior la ve. **Sus remedios** guarda en texto libre qué remedios toma la persona y a qué hora, tal como se los da la familia. No es una receta y no reemplaza la indicación del médico. Al compartir con un relevo, tú marcas qué secciones ve. Sus remedios viene siempre sin marcar. Te recomendamos no escribir diagnósticos ni nombres de enfermedades en ninguna sección. Ya puedes agregarlas, editarlas y quitarlas.

**El nivel de apoyo y la ficha son datos sensibles**, porque hablan de la salud y de la dependencia de la persona. Por eso los protegemos de forma especial.

**El consumo de insumos también lo tratamos como un dato sensible**, porque puede revelar algo de la salud o de la dependencia de la persona. A diferencia de la ficha, no se cifra con una clave propia: lo protege la separación entre familias de la base de datos. Un abogado revisará si esta protección basta antes de usar MATU con datos reales. <!-- PENDIENTE: consulta legal sobre si el consumo es un dato relativo a la salud y si basta esta protección -->

### De otras personas que tú anotas

- **Relevo:** su nombre y su teléfono, qué campos y qué secciones adicionales le compartiste, hasta cuándo, el motivo, cada vez que abrió el enlace, aunque no haya escrito el PIN, cuántas veces abrió la ficha y cada PIN incorrecto. Su teléfono es obligatorio: sirve para que tú le envíes el enlace desde tu teléfono, con la aplicación de mensajes que elijas, y para que quien administra el grupo o lo cuida pueda llamarlo. MATU no le envía mensajes. El PIN no va en el mensaje: se lo dictas por teléfono. Avísale que lo anotaste: cuando abra el enlace, MATU le muestra qué guarda de él, y también tu nombre de pila y el de la persona que cuidas. Tu grupo puede ver ese registro en "Quién la vio" (ver "Quién ve tus datos").
- **"A quién llamar":** los nombres y teléfonos que escribas. Avísales que los anotaste.
- **Invitaciones a tu grupo:** el email o el teléfono de la persona invitada. *Todavía no disponible.*

### De tus pedidos

<!-- ADR-027 (27-10), aprobado por Jorge. MATU-61 (11-11): los pedidos existen hasta el total confirmado, y el pago llega con MATU-62. -->

Desde esta versión puedes armar un pedido para la persona que cuidas y ver su total antes de pagar. Pagarlo todavía no está disponible (sección 13). De cada pedido guardamos:

- Los productos, con su cantidad, el comercio que prepara cada uno y su precio. Guardamos el precio que viste al agregarlo y el precio que confirmamos antes de pagar, para mostrarte si cambió. Todos los precios llevan el IVA incluido.
- Qué elegiste hacer si falta cada producto: buscarlo en otro comercio o sacarlo del pedido.
- Si cada producto pierde el derecho a retracto al abrir el sello, tal como te lo mostramos.
- El envío, que es uno por pedido, y el total confirmado, con la hora hasta la que vale.
- La dirección de entrega y el teléfono de contacto, copiados al pedido cuando confirmas el total. El teléfono es por omisión tu celular, y puedes cambiarlo. Si pones el de otra persona, avísale.
- La línea de tiempo del pedido: cuándo se creó, se confirmó, venció o se canceló, y si lo hizo una persona del grupo o MATU, con un motivo de una lista cerrada. No guarda productos, cantidades ni la dirección.
- **Cuando existan los pagos:** las condiciones del pedido que aceptaste, su versión, cuándo las aceptaste y una huella del texto exacto que viste, y el pago: el monto cobrado y, si hubo, la devolución.

**El pedido no guarda el nombre de la persona que cuidas.** Se une a ella por un número interno. <!-- R7 y C16 de MATU-61 -->

**Tus pedidos y el consumo de insumos de la persona que cuidas se tratan como datos sensibles**, porque pueden revelar algo de su salud o de su dependencia. Tus pedidos los ven las personas de tu grupo, según su rol (sección 6), y el equipo de MATU para dar soporte. El consumo de insumos lo ven solo las personas de tu grupo. Ningún comercio los ve junto a un nombre. A diferencia de la ficha, no se cifran con una clave propia de cada persona. MATU no usa tus pedidos para calcular el consumo de insumos, ni el consumo para armar un pedido: el pedido lleva solo los productos que tú agregas. <!-- C20 de MATU-61 -->

**Para los pedidos pedimos una autorización expresa y aparte**, distinta de la de la ficha y de la de los insumos (sección 5). Puedes retirarla igual de fácil que la diste (sección 10). Si la retiras, ya no podrás pedir desde MATU, pero sí imprimir o compartir la lista. Los pedidos sin pagar se cancelan sin costo. Los pedidos ya pagados, cuando existan los pagos, se guardan el plazo de la sección 8, para responder reclamos y por obligación tributaria. Confirmaremos estos plazos antes de usar MATU con datos reales. <!-- PENDIENTE: confirmar en la versión 1.0. CL-28 y CL-44 -->

Antes de usar MATU con datos reales, un abogado revisará si los productos de un pedido son un dato de salud y qué límites pone la ley a su uso. <!-- PENDIENTE: consulta legal sobre si los productos de un pedido son un dato relativo a la salud, y si el art. 16 bis, inciso 1, de la ley limita su tratamiento aunque haya autorización -->

### Lo que MATU no pide

- Diagnósticos, nombres de enfermedades, recetas, exámenes ni fichas clínicas. Si quieres, puedes anotar qué remedios toma y a qué hora, para que quien te reemplaza no se equivoque. Esa sección es opcional y solo la ven tu grupo y los relevos a quienes tú se la muestres. La pedimos por la seguridad del cuidado. <!-- decisión de Jorge del 03-11 -->
- El RUT de nadie.
- Copias de documentos. Si eres representante legal, guardamos solo una referencia al documento.
- Los datos de tu tarjeta.

**Un consejo para la ficha:** escribe qué ayuda, no qué enfermedad tiene. Por ejemplo: "se tranquiliza si bajas las persianas".

## 5. La autorización para usar los datos de la persona que cuidas

Para guardar la ficha necesitamos una autorización. Al dar de alta a la persona, eliges quién la da. Si después se retira, quien administra el grupo o quien cuida a la persona puede volver a darla desde «Grupo familiar», con la misma declaración y eligiendo de nuevo la calidad (sección 10).

**La propia persona (titular).** La persona que cuidas decide por sí misma y tú registras su decisión. Al registrarla declaras:

> Declaro que la persona que cuido me dijo hoy, en persona, que autoriza a MATU a guardar su ficha de relevo, incluidas las secciones adicionales y sus remedios si se agregan, y a compartirla con el relevo que elija el grupo, según la política de privacidad vigente. Yo solo registro su decisión.

**Su representante legal.** Tienes un nombramiento legal para representarla. Declaras:

> Declaro que soy representante legal de la persona que cuido y que la referencia que indico corresponde al documento que lo acredita. Como su representante, autorizo a MATU a guardar su ficha de relevo, incluidas las secciones adicionales y sus remedios si se agregan, y a compartirla con el relevo que elija el grupo, según la política de privacidad vigente.

**Cuidadora o cuidador de hecho.** La cuidas en el día a día, pero no tienes un nombramiento legal para representarla. Declaras:

> Declaro que cuido a esta persona y que no soy su representante legal. Autorizo a MATU a guardar su ficha de relevo, incluidas las secciones adicionales y sus remedios si se agregan, y a compartirla con el relevo que elija el grupo, según la política de privacidad vigente. Leí el aviso sobre el límite de esta autorización.

### Aviso para quien cuida sin ser representante legal

Este es el texto exacto que MATU muestra al elegir esta calidad. Es la versión 1.1 del aviso: <!-- identificador aviso_cuidador_de_hecho, versión 1.1. La 1.0 asumía que la persona cuidada es mujer; cambio aprobado por Jorge el 03-11 -->

> **Aviso: tu autorización tiene un límite**
>
> Declaraste que cuidas a esta persona y que no eres su representante legal. Con esa declaración puedes organizar su cuidado en MATU, pero tu autorización no equivale a la de la propia persona ni a la de su representante legal. MATU no puede comprobar lo que declaras. Por eso deja registrado que la autorización la diste tú, como cuidadora o cuidador de hecho, con la fecha y la versión de la política.
>
> Te pedimos tres cosas: anota solo lo necesario para su cuidado, cuéntale qué guardas en MATU si puede comprenderlo, y respeta lo que esa persona decida. La persona o su representante legal pueden pedir en cualquier momento que se borren sus datos.
>
> En 12 meses te pediremos confirmar que sigues a cargo de su cuidado.

<!-- Huella del aviso en el sistema (SHA-256): 8dfbca33f5c58a2c1f5c43a672b3e0fcd2ed4adcc971dcccd0f8879814b10489 -->

Con cada autorización guardamos qué declaración viste y la versión de esta política vigente cuando la diste. Cambiar una sola palabra de una declaración o del aviso es publicar una versión nueva. <!-- identificadores: declaracion_titular, declaracion_representante_legal, declaracion_cuidador_de_hecho -->

Si pasan los 12 meses sin confirmarlo, la ficha queda en pausa: nadie del grupo la puede ver ni cambiar, pero lo escrito sigue guardado. Los enlaces de relevo dejan de abrir mientras tanto, y quien tenga uno ve que por ahora la ficha no se puede ver, sin el motivo. Puedes cortar un enlace igual. Cuando se renueva, vuelven a abrir los enlaces que no hayan vencido. Esto es distinto de retirar la autorización: si la retiras, los enlaces se cortan y no vuelven a abrir (sección 10). Todavía no definimos qué pasa si nunca se confirma ni cuánto tiempo se guarda una ficha en pausa. Lo publicaremos antes de usar MATU con datos reales. <!-- PENDIENTE: qué pasa si nunca se renueva y cuánto tiempo se guarda una ficha en pausa. Está en consulta legal -->

### La autorización para calcular insumos

Es aparte de la de la ficha y se da en la misma calidad. Se pide la primera vez que anotas un insumo, y la dan el administrador o el cuidador del grupo. Si eres cuidadora o cuidador de hecho, MATU te vuelve a mostrar el aviso de arriba y a los 12 meses te pedirá confirmar. Las declaraciones son:

**La propia persona (titular):**

> Declaro que la persona que cuido me dijo hoy, en persona, que autoriza a MATU a guardar qué insumos usa, cuánto usa y cuánto queda, y a calcular cuándo se acaban y avisarme cuando se esté por acabar, según la política de privacidad vigente. Yo solo registro su decisión.

**Su representante legal:**

> Declaro que soy representante legal de la persona que cuido y que la referencia que indico corresponde al documento que lo acredita. Como su representante, autorizo a MATU a guardar qué insumos usa, cuánto usa y cuánto queda, y a calcular cuándo se acaban y avisarme cuando se esté por acabar, según la política de privacidad vigente.

**Cuidadora o cuidador de hecho:**

> Declaro que cuido a esta persona y que no soy su representante legal. Autorizo a MATU a guardar qué insumos usa, cuánto usa y cuánto queda, y a calcular cuándo se acaban y avisarme cuando se esté por acabar, según la política de privacidad vigente. Leí el aviso sobre el límite de esta autorización.

<!-- identificadores: declaracion_consumo_titular, declaracion_consumo_representante_legal, declaracion_consumo_cuidador_de_hecho. Aprobadas por Jorge el 03-11 -->

### La autorización para los pedidos

Es aparte de la de la ficha y de la de los insumos, y se da en la misma calidad. Se pide la primera vez que haces un pedido, y la dan el administrador o el cuidador del grupo. Si eres cuidadora o cuidador de hecho, MATU te vuelve a mostrar el aviso de arriba y a los 12 meses te pedirá confirmar. Mientras no esté vigente, nadie del grupo puede armar ni confirmar un pedido, pero sí cancelarlo y cambiar o vaciar la dirección de entrega. Las declaraciones son:

**La propia persona (titular):**

> Declaro que la persona que cuido me dijo hoy, en persona, que autoriza a MATU a guardar los pedidos de sus insumos, con los productos, la dirección de entrega, el teléfono de contacto y el pago, para preparar, entregar y responder por cada pedido, según la política de privacidad vigente. Yo solo registro su decisión.

**Su representante legal:**

> Declaro que soy representante legal de la persona que cuido y que la referencia que indico corresponde al documento que lo acredita. Como su representante, autorizo a MATU a guardar los pedidos de sus insumos, con los productos, la dirección de entrega, el teléfono de contacto y el pago, para preparar, entregar y responder por cada pedido, según la política de privacidad vigente.

**Cuidadora o cuidador de hecho:**

> Declaro que cuido a esta persona y que no soy su representante legal. Autorizo a MATU a guardar los pedidos de sus insumos, con los productos, la dirección de entrega, el teléfono de contacto y el pago, para preparar, entregar y responder por cada pedido, según la política de privacidad vigente. Leí el aviso sobre el límite de esta autorización.

Con esta autorización guardamos, además, una huella del texto exacto de la declaración que viste.

<!-- identificadores: declaracion_pedidos_titular, declaracion_pedidos_representante_legal, declaracion_pedidos_cuidador_de_hecho. Finalidad `despacho` (D1 de MATU-61). Redactadas desde el texto de la sección 4 de revision-previa-matu-61.md, con el armado de las de consumo. Pendientes de aprobación de Jorge al fusionar -->

## 6. Quién ve los datos

<!-- ADR-027 (27-10), aprobado por Jorge. Cambian los párrafos de comercios, de quien reparte y de Transbank. -->

**Tu cuenta:** tu email y tu celular los ven solo tú y el equipo que opera MATU. Las personas de tus grupos ven tu nombre. Si algún día pudieran ver también tu email, lo diremos aquí antes. <!-- PENDIENTE: si también ven tu email, se define con la lista de miembros del grupo -->

**El nombre del grupo:** lo ven las personas del grupo y el equipo que opera MATU.

**Tu grupo, según el rol de cada persona:**
- **Administrador y cuidador:** ven todo, incluida la calidad en que se dio la autorización, y pueden editar y compartir la ficha. La referencia al documento del representante legal no se muestra en la aplicación: queda guardada solo como respaldo.
- **Pagador:** ve el nombre y la dirección. Ve la ficha solo si le dan ese permiso. Con ese permiso también ve la lista de enlaces de relevo (el nombre del relevo, el motivo, las fechas y quién lo creó), sin su teléfono, y no puede crear ni cortar enlaces.
- **Observador:** ve el nombre. Nunca ve la ficha.

**El estado de las autorizaciones**: todas las personas del grupo ven, en «Grupo familiar», si cada autorización de la persona está vigente, por renovar, retirada o ya borrada, con sus fechas y hasta cuándo se guarda lo escrito. La calidad en que se dio la ven solo el administrador y el cuidador, que son también los únicos que pueden retirarla o volver a darla. Solo la autorización de una cuidadora o un cuidador de hecho se revisa a los 12 meses, así que quien ve esa fecha, o que está por renovar, puede deducir en qué calidad se dio. Si se borran los datos de la persona, deja de aparecer en «Grupo familiar» y su estado ya no se muestra (sección 10). <!-- MATU-44 -->

**Quién abrió o editó la ficha**: cada vez que un miembro del círculo de cuidado abre o edita la ficha de relevo, MATU registra quién lo hizo, qué acción realizó y cuándo. Si la acción fue agregar, editar o quitar una sección adicional, también queda registrado cuál sección fue, por ejemplo «Sus remedios», aunque después la quites. Nunca su texto. Este registro no guarda el contenido de la ficha ni tu dirección IP. Puede consultarlo la persona administradora del grupo, y cada miembro puede ver sus propios registros. Se guarda 3 años (sección 8). <!-- aprobado por Jorge el 28-10, MATU-14 -->

**Quién abrió el enlace de relevo**: cada vez que un relevo abre el enlace, aunque no escriba el PIN, abre la ficha, escribe mal el PIN o el enlace se bloquea, MATU registra la fecha, la hora y el nombre del relevo. Cuando abre la ficha, también registra qué secciones adicionales vio, sin su texto. Lo ven en "Quién la vio" la persona administradora, quien cuida y quien paga si tiene permiso para ver la ficha. El observador no lo ve. Este registro no muestra el teléfono del relevo, su dirección IP, el enlace ni el PIN. Se guarda 3 años desde que el acceso vence o se corta. Un abogado revisará si este plazo es proporcional para los datos del relevo antes de usar MATU con datos reales. <!-- PENDIENTE: consulta legal sobre si 3 años es proporcional para los datos de un tercero, el relevo --> <!-- MATU-45, aprobado por Jorge el 03-11 -->

**El consumo de insumos** lo ven todas las personas del grupo, incluido el observador. Solo el administrador y el cuidador lo anotan, lo cambian, dejan de seguir un insumo o lo eliminan. Cada vez que alguien lo hace, MATU registra quién y cuándo, sin el nombre del insumo ni las cantidades. El equipo de MATU no puede leerlo.

**Los avisos de insumos**. Cuando un insumo está por acabarse, MATU te avisa en la aplicación. MATU también está preparado para avisarte por correo y con una notificación en los teléfonos donde activaste los avisos, pero **en el piloto esos avisos se prueban sin enviarse: no salen de los equipos de MATU** (sección 13). Cuando se activen, saldrán desde las 9:00, hora de Chile. Por defecto avisan al administrador y al cuidador. El pagador y el observador reciben avisos solo si los activan. Tu elección es tuya, no del grupo, y vale para todos tus grupos. El aviso dice solo «MATU: un insumo se está acabando. Abre la app para ver cuál»: no dice qué insumo ni de quién, porque a veces el teléfono está a la vista de otras personas. Su enlace lleva a la aplicación y no dice quién eres. El correo no sabe si lo abriste ni si hiciste clic. Antes de enviar cada aviso, MATU revisa que la autorización de insumos siga vigente y al día, que el aviso siga abierto y que sigas en el grupo. Si algo de eso falla, no lo envía. Cuando se activen los envíos, un servicio de correo recibirá ese texto y tu correo, y el servicio de notificaciones de tu navegador recibirá solo la dirección de avisos de tu navegador, sin ningún texto: el texto lo pone tu teléfono. Nada más. Antes de activar los envíos, diremos aquí qué servicios son y en qué país están. <!-- PENDIENTE: nombres y país, antes de activar los envíos --> Puedes dejar de recibir los avisos por correo o por notificación cuando quieras, en «Tu cuenta» (sección 13), y dejar de recibirlos en un teléfono si cierras la sesión en él o lo sacas de tus dispositivos. Solo el administrador y el cuidador pueden marcar un aviso como resuelto («Ya lo resolví») y anotar, en cualquier momento, que compraron un insumo («Compré») o cuánto queda («Me quedan»), haya aviso o no. Si anotan una compra, MATU guarda la cantidad, la fecha y quién la anotó, y la suma a lo que calculaba que quedaba. Si anotan cuánto queda, MATU reemplaza lo que calculaba y no guarda una compra. Si retiras la autorización de insumos, MATU deja de avisar en ese momento. El aviso nunca hace un pedido. <!-- MATU-37 y MATU-41 -->

**La lista de insumos**. Con los insumos que se acaban pronto, MATU arma una lista con el nombre de cada insumo y una cantidad sugerida: lo que falta para cubrir 30 días, descontando lo que MATU calcula que queda, en envases si anotaste cuántas unidades trae cada uno. En la pantalla ves también cuántos días le quedan, pero eso no sale en lo que imprimes o compartes. La ven todas las personas del grupo. Quien administra, cuida o paga puede imprimirla, guardarla como PDF o compartirla como texto desde su teléfono, con la aplicación que elija. El observador la ve, sin esas opciones. Antes de imprimirla o compartirla puedes agregar otros insumos y cambiar las cantidades. Eso queda solo en tu pantalla y MATU no lo guarda. La lista no lleva el nombre de la persona que cuidas, ni nada de su ficha, ni precios, pero el nombre de un insumo puede decir algo de su salud. MATU no envía la lista, no crea un enlace para verla y no sabe si la imprimiste ni a quién se la mandaste. Lo que imprimas o compartas sale de MATU: queda en el papel, en tu teléfono o en la aplicación que usaste, y MATU no puede borrarlo, aunque después elimines el insumo o retires la autorización. Compártela solo con quien la necesita para comprar. <!-- MATU-60 -->

**Los pedidos**, según el rol de cada persona del grupo: <!-- C3 de Jorge y D12 de MATU-61 -->
- **Administrador y cuidador:** arman el pedido, eligen qué hacer si falta cada producto, agregan, cambian o vacían la dirección de entrega, cambian el teléfono de contacto, confirman el total y cancelan un pedido sin pagar.
- **Pagador:** ve el pedido, la dirección, el teléfono de contacto y el resumen antes de pagar, sin cambiar nada.
- **Observador:** ve los productos del pedido, sin la dirección, el teléfono de contacto ni el resumen.
- Cada vez que alguien da o retira la autorización de los pedidos, crea, confirma o cancela un pedido, elige qué hacer si falta un producto, o cambia o vacía la dirección, MATU registra quién y cuándo, sin los productos, las cantidades, la dirección ni el teléfono. Mirar un pedido no se registra.

**El relevo**, la persona que te reemplaza:
- Ve solo el nombre con que llaman a la persona, tu nombre de pila, los tres campos de la ficha y las secciones adicionales que marcaste al compartir. Si agregas una sección después, no la ve hasta que le des un acceso nuevo.
- Al abrir el enlace, y antes de escribir el PIN, ve tu nombre de pila y el de la persona que cuidas.
- Entra con un enlace y un PIN de 4 dígitos. El acceso vence en 24 horas, o en el plazo que elijas hasta un máximo de 30 días, y puedes cortarlo cuando quieras.
- Si la autorización de la ficha está en pausa porque no se confirmó a los 12 meses, el enlace deja de abrir mientras tanto. Si la autorización se retira, el enlace se corta y no vuelve a abrir. En los dos casos el relevo no ve el motivo.
- Cada vez que abre la ficha queda registrado, y también cada PIN incorrecto y cada bloqueo. También queda registrado cada vez que abre el enlace, aunque no escriba el PIN.
- Lo que el relevo lea puede anotarlo o fotografiarlo, y MATU no puede impedirlo. Comparte solo lo que necesita y por el tiempo justo.

**Comercios en convenio**:
- Para saber si tienen los productos, al confirmar el total MATU les pregunta solo por los productos y las cantidades, con una referencia que se crea al azar para cada pedido y cada comercio y no permite saber de quién es. Esa consulta no lleva tus datos, ni los de la persona que cuidas, ni la dirección. En el piloto los comercios son ficticios y la consulta es simulada.
- Cuando existan los pagos, el comercio que prepara tu pedido verá solo sus productos, su referencia del pedido y el código de retiro. **Si un pedido lo preparan varios comercios, cada uno ve solo sus productos y su referencia**, nunca los de otro comercio ni el total. Si falta un producto y otro comercio lo reemplaza, ese comercio ve lo mismo, solo con lo que le toca preparar. <!-- R8 y D7 de MATU-61 -->
- **Ningún comercio ve un nombre**, ni el tuyo ni el de la persona que cuidas. Tampoco ven la ficha. **La dirección nunca llega al comercio.** MATU vende, así que el comercio no necesita saber quién paga. En el piloto no se emite boleta (condiciones del pedido).
- Aun así, MATU trata a cada comercio como si tratara datos por encargo: su convenio le exige siempre confidencialidad y seguridad.

**Quien reparte**, si en el futuro hay despacho: ve la dirección de entrega y el teléfono de contacto solo mientras lleva el pedido. Lo hace por encargo de MATU y con un contrato que le exige confidencialidad, seguridad y borrar los datos al terminar.

**Transbank**, cuando existan los pagos: el pago se hace en su página. MATU no ve el número de tu tarjeta ni su código. Solo guarda el resultado: el monto, el código de autorización, el tipo de tarjeta y sus últimos 4 dígitos. Puedes pagar con crédito o con débito, y funcionan igual: se cobra una sola vez el total que viste antes de pagar. Si hay una devolución, va a la misma tarjeta, y no te pedimos datos nuevos para hacerla. Durante el piloto los pagos ocurren solo en el ambiente de prueba de Transbank, sin cobros reales. Antes de activar los pagos, confirmaremos en ese ambiente de prueba que el débito y la devolución funcionan así. <!-- PENDIENTE: que el débito y la devolución parcial funcionen así se confirma con la prueba en el ambiente de integración de Transbank, antes del sprint 4 -->

**El equipo de MATU:** para dar soporte ve los pedidos y los pagos. Sus herramientas no permiten leer la ficha ni el consumo de insumos.

**Dictar en vez de escribir:** en la ficha puedes dictar con el botón del micrófono. El reconocimiento de voz lo hace el servicio de tu navegador, no MATU. Por ejemplo, en Chrome el audio se envía a Google para convertirlo en texto, y puede salir de Chile. MATU no guarda el audio, solo el texto que revisas y guardas tú. Si no quieres que el audio salga de tu teléfono, escribe o usa el dictado de tu teclado. Por ahora, el botón de dictar no aparece en «Sus remedios». Un abogado revisará este envío de audio antes de usar MATU con datos reales, y entonces diremos aquí qué servicios lo reciben y en qué país están. <!-- PENDIENTE: consulta legal sobre el envío de audio de un dato sensible a un tercero, y nombrar los servicios y sus países. Decisión de Jorge del 03-11 -->

**Proveedores de tecnología** que guardan o procesan datos por encargo de MATU:
- **Railway**, en California, Estados Unidos, aloja el ambiente de prueba, que tiene solo datos inventados (sección 7).
- **Gmail, de Google LLC**, en Estados Unidos, recibe y guarda los correos que nos escribes a cuidaconmatu@gmail.com, también los reclamos de los pedidos.

Antes de usar MATU con datos reales, diremos aquí los demás: dónde se guardan los datos, y los servicios de avisos, mensajes de texto, WhatsApp, correo y registro de errores, con qué datos recibe cada uno. <!-- PENDIENTE: proveedor de nube, de notificaciones push, de WhatsApp, de correo, de SMS y de registro de errores, con qué datos recibe cada uno -->

**Autoridades:** solo cuando una ley o un tribunal lo exige.

## 7. Dónde se guardan los datos

- Durante el semestre, MATU corre en los computadores del equipo y en un ambiente de prueba en Railway, un proveedor de servidores, en su región de California, Estados Unidos. Ese ambiente tiene solo datos inventados y se borra al terminar el semestre.
- Aunque los datos sean inventados, cuando usas el ambiente de prueba tu dirección IP pasa por los servidores de Railway en Estados Unidos. MATU no la guarda: solo una huella que no permite recuperarla, por el plazo de la sección 8. Railway puede guardar la dirección IP de cada conexión en sus propios registros técnicos. Todavía no confirmamos qué registra ni por cuánto tiempo lo guarda. Lo diremos aquí cuando lo confirmemos. <!-- PENDIENTE: confirmar qué registra Railway y por cuánto tiempo -->
- Todavía no elegimos dónde se guardarán los datos reales. Lo diremos aquí antes de usarlos. <!-- PENDIENTE: proveedor y país donde se alojarán los datos reales -->
- Si los datos reales se guardan fuera de Chile, lo diremos aquí y aplicaremos lo que la ley exige para ese caso.

## 8. Cuánto tiempo guardamos los datos

- **Cuándo se borra:** las tareas que borran los datos vencidos corren solas cada madrugada (hora de Chile). Por eso un dato se borra a más tardar el día siguiente al que vence su plazo. Si una corrida falla, la siguiente borra lo que quedó pendiente.
- **Ficha de relevo:** mientras la autorización esté vigente y hasta 90 días después de que se retire o termine. Pasado ese plazo, MATU la borra destruyendo su clave y borrando el texto cifrado. Esa tarea corre cada madrugada. Desde el día 90, y hasta que corre, la ficha ya no se puede ver ni recuperar, aunque su clave todavía exista. Si después se vuelve a autorizar, la ficha empieza en blanco y lo de antes no vuelve. Si pides borrar los datos de la persona, no esperamos los 90 días: en ese mismo momento destruimos su clave y borramos el texto cifrado y todas las secciones (sección 10). Una sección adicional que quitas se borra en ese momento. Hasta que vence la última copia de respaldo que la contiene, sigue en esa copia, cifrada.
- **Consumo de insumos:** mientras la autorización para calcular insumos esté vigente y hasta 90 días después de que termine, también los insumos que dejaste de seguir. Un insumo que eliminas se borra en ese momento. Si pides borrar todo el consumo, lo borramos de la base de datos: no se deja ilegible, se borra. Si pides borrar los datos de la persona, sus insumos, sus avisos y las compras anotadas se borran en ese momento, aunque la autorización siga vigente o se haya retirado hace menos de 90 días. El registro de los avisos sigue su propio plazo de 90 días: dice a qué cuenta iba cada aviso, por qué canal y si salió, sin el texto, sin tu correo y sin el nombre de la persona ni del insumo.
- **Lista de insumos:** MATU no la guarda. Se arma cada vez que la abres, con lo que ya está anotado. Lo que agregas o cambias a mano se pierde al salir de la pantalla. Las copias que imprimas, guardes como PDF o compartas quedan fuera de MATU y no siguen estos plazos.
- **La persona que cuidas, si pides borrar sus datos:** su nombre, el nombre con que la llaman y su nivel de apoyo se borran en ese momento. Su dirección también, salvo que sea la de otra persona que cuidan en el grupo: en ese caso queda solo para esa otra persona. Queda un número interno sin datos, que une los registros que sí conservamos, por el plazo de esos registros. Todavía no definimos ese plazo. Lo publicaremos antes de usar MATU con datos reales. <!-- PENDIENTE: plazo, en consulta legal -->
- **Tu sesión:** cada sesión se borra 30 días después de vencer o de cerrarse.
- **Tus dispositivos:** se borran 90 días después de su último uso. La dirección para enviarte avisos se borra cuando cierras la sesión, sacas el dispositivo o desactivas los avisos en él, o cuando el servicio de notificaciones informa que ya no existe.
- **Huellas para limitar intentos** al crear una cuenta, al entrar y al abrir un enlace de relevo: 1 hora desde el primer intento.
- **Avisos de insumos:** los avisos cerrados, 90 días. El registro de avisos, que dice a quién, por qué canal y si salió o por qué no salió, sin el texto ni tu correo: 90 días desde que se crea. Los eventos internos ya procesados, y los que no se pudieron procesar, 30 días. Las compras anotadas, 90 días desde que se anotan.
- **Código para recuperar el acceso:** hasta que se usa o 10 minutos. Los contadores de envíos, 24 horas como máximo. <!-- MATU-57 -->
- **Copias de respaldo:** guardamos copias de la base, que se borran solas al vencer su plazo. Todavía no definimos su plazo. Lo publicaremos antes de usar MATU con datos reales. <!-- PENDIENTE: plazo --> No se pueden cambiar una por una. Lo que borras, o pides borrar, sigue en las copias hechas antes, hasta que vencen: la ficha, cifrada, y los insumos y las compras anotadas, protegidos igual que en la base. Nadie usa esas copias para ver datos. Si alguna vez tenemos que recuperar la base desde una copia, antes de volver a usarla borramos otra vez todo lo que se pidió borrar. El borrado queda completo cuando vence la última copia.
- **Registro de quién abrió la ficha:** 3 años.
- **Pedidos que no se pagaron:** el pedido que quedó armado, el que tiene el total vencido y el cancelado sin pagar se borran a los 30 días, con sus productos y su línea de tiempo. La dirección y el teléfono copiados a un pedido cancelado se borran al cancelarlo. Para no repetir un pedido si tocas dos veces el mismo botón, MATU guarda 24 horas solo el número del pedido y el resultado, sin su contenido. <!-- D5 de MATU-61. PENDIENTE: CL-28 ampliada -->
- **La dirección de entrega de la persona que cuidas:** mientras esté registrada, hasta que la vacíes o pidas borrar sus datos. Retirar la autorización de los pedidos no la borra.
- **Pedidos pagados y comprobantes de entrega**, cuando existan los pagos: 2 años.
- **Pagos y boletas**, cuando existan: 6 años, por obligación tributaria.
- **Tu cuenta y las versiones de esta política que aceptaste:** mientras tengas tu cuenta. Todavía no definimos cuánto tiempo se guardan después de que la elimines. Lo publicaremos antes de usar MATU con datos reales. <!-- PENDIENTE: CL-49 -->
- **Registro de autorizaciones:** cada autorización, también las retiradas, con su fecha de retiro. Hoy no se borran. Todavía no definimos su plazo. Lo publicaremos antes de usar MATU con datos reales. <!-- PENDIENTE: plazo, en consulta legal -->
- **Accesos de relevo:** el nombre del relevo, el motivo y las fechas, 3 años desde que vence o se corta el acceso, igual que el registro de quién abrió la ficha. El teléfono del relevo se borra 30 días después de que el acceso vence o se corta.
- **Registros técnicos del sistema:** todavía no definimos su plazo. Lo publicaremos antes de usar MATU con datos reales. <!-- PENDIENTE -->
- **Los correos que nos escribas sobre privacidad o con un reclamo de un pedido:** los guardamos hasta 2 años después de cerrar tu solicitud. Después queda solo una lista con la fecha, el tipo de solicitud y la fecha de respuesta, sin el contenido.

## 9. Cómo protegemos los datos

- La conexión con MATU va cifrada.
- Cada campo y cada sección adicional de la ficha se cifra por separado con una clave propia de cada persona cuidada. Esa clave está protegida por una clave maestra. Durante el piloto, que usa solo datos inventados, la clave maestra está en el mismo servidor que la aplicación. Antes de usar MATU con personas reales, pasará a un servicio de custodia separado del servidor. <!-- PENDIENTE: confirmar el servicio de custodia de claves -->
- MATU no imprime ni exporta la ficha. Solo se comparte con el enlace con PIN. <!-- ADR-029 -->
- La lista de insumos sí se puede imprimir o compartir, porque no lleva la ficha ni el nombre de la persona. MATU no la guarda, no la envía y no crea un enlace para verla. Tampoco la guarda en tu teléfono ni en tu navegador: si cierras la pantalla, se pierde. <!-- ADR-031 -->
- La base de datos separa a cada familia: una familia no puede ver los datos de otra, aunque la aplicación tenga un error.
- El registro de quién abrió la ficha no se puede modificar ni borrar.
- Los registros técnicos de MATU no guardan el texto de la ficha, ni tu email, ni contraseñas, ni códigos de acceso, ni enlaces de relevo, ni PIN, ni el nombre del grupo, ni tu dirección IP. El proveedor de servidores puede registrar la dirección IP de cada conexión (sección 7).
- El enlace de relevo se bloquea después de 5 PIN incorrectos. Cada PIN incorrecto y cada bloqueo quedan registrados. Además, desde una misma dirección IP se admite un número limitado de intentos por hora para crear una cuenta, entrar y abrir un enlace de relevo: para contarlos se guarda una huella de la IP que no permite recuperarla y que se borra sola en el plazo de la sección 8. La IP no se guarda en la base de datos ni en los registros de MATU.
- La aplicación no guarda en tu teléfono ni en tu navegador la ficha, el consumo de insumos, tu pedido ni tu código de acceso, que vive solo en la memoria de la página. Tu pedido se guarda en MATU mientras lo armas. No usa analítica ni programas de terceros.
- Los productos, las cantidades, la dirección y el teléfono de un pedido nunca van en la dirección de la página ni en los registros técnicos de MATU.
- Los avisos al teléfono no llevan el nombre de la persona ni del insumo.

Ningún sistema es completamente seguro. Si algo falla, la sección 11 dice qué hacemos.

## 10. Tus derechos y cómo ejercerlos

Puedes pedir:
- **Ver** qué datos tenemos.
- **Corregir** un dato equivocado.
- **Borrar** los datos.
- **Oponerte** a un uso de los datos.
- **Recibir una copia** de los datos para llevarla a otro lugar.
- **Retirar una autorización.** Ver «Retirar una autorización», más abajo.

### Retirar una autorización

Puedes retirar cada autorización por separado, cuando quieras y sin dar un motivo, también si su revisión de los 12 meses ya venció. Quien administra el grupo o quien cuida a la persona lo hace en la aplicación, en «Grupo familiar», con un botón y una confirmación. No importa quién la dio. Si la persona que cuidas o su representante legal te pide retirarla, hazlo desde ahí. También pueden pedirlo por el correo de esta sección. El retiro vale desde ese momento.

**Si retiras la autorización de la ficha:**
- Nadie del grupo puede ver ni cambiar la ficha, desde ese momento.
- Se cortan en ese mismo momento todos los enlaces de relevo que todavía abrían, también los que estaban en pausa. Si un relevo tenía la ficha abierta, se le cierra cuando vuelve a mirarla. No recibe aviso ni ve el motivo. Un enlace cortado no vuelve a abrir, aunque des una autorización nueva.
- Los enlaces que ya habían vencido no cambian.
- Lo escrito sigue guardado y cifrado, sin que nadie lo pueda leer, hasta 90 días. Si en ese plazo das una autorización nueva, vuelve a verse. Si no, se borra destruyendo su clave (sección 8). Si autorizas después de ese plazo, la ficha empieza en blanco.
- «Quién la vio» y la lista de enlaces se siguen viendo, sin el texto de la ficha, por el plazo de la sección 8.
- Las autorizaciones de los insumos y de los pedidos no cambian.

**Si retiras la autorización de los insumos:**
- MATU deja de calcular cuándo se acaban y de avisar, desde ese momento. Un aviso que estaba por salir ya no sale, y los avisos abiertos se descartan.
- Nadie del grupo puede ver los insumos anotados.
- Lo anotado se guarda hasta 90 días. Si en ese plazo das una autorización nueva, vuelve a verse tal como estaba. Si no, se borra (sección 8). Si autorizas después de ese plazo, hay que anotar los insumos de nuevo.
- Una lista de insumos que ya imprimiste o compartiste no se borra, porque está fuera de MATU.
- La ficha, los enlaces de relevo y los pedidos no cambian.

**Si retiras la autorización de los pedidos:** <!-- D1 de MATU-61, y C6 de Jorge -->
- Ya no se pueden hacer pedidos para la persona desde MATU, desde ese momento.
- Cancelamos sin costo sus pedidos sin pagar y borramos la dirección y el teléfono que se copiaron en ellos. Lo demás de esos pedidos se borra a los 30 días (sección 8).
- Los pedidos ya pagados, cuando existan los pagos, siguen hasta que se entreguen y se guardan el plazo de la sección 8. <!-- PENDIENTE: CL-44 -->
- La dirección de entrega de la persona queda guardada para cuando vuelvas a autorizar. Puedes vaciarla cuando quieras, también sin la autorización.
- La lista de insumos se puede seguir imprimiendo y compartiendo.
- La ficha, los insumos y los enlaces de relevo no cambian.

Un abogado revisará, antes de usar MATU con datos reales, si se pueden guardar esos 90 días después del retiro. <!-- PENDIENTE: consulta legal sobre si se pueden guardar esos 90 días después del retiro -->

### Borrar los datos de la persona que cuidas

Quien administra el grupo o quien cuida a la persona puede borrar todo lo guardado de ella, en «Grupo familiar», con una confirmación. Si la persona que cuidas o su representante legal te lo pide, hazlo desde ahí. También pueden pedirlo por el correo de esta sección. No esperamos ningún plazo:
- En ese momento borramos su ficha, con todas sus secciones, destruyendo su clave, y borramos sus insumos, sus avisos y las compras anotadas.
- Se cortan todos sus enlaces de relevo, y no vuelven a abrir. El relevo no ve el motivo.
- Sus autorizaciones quedan retiradas, también la de los pedidos.
- Cancelamos sin costo sus pedidos sin pagar y borramos la dirección y el teléfono que se copiaron en ellos. Lo demás de esos pedidos se borra a los 30 días (sección 8). Ningún pedido guarda su nombre.
- Cuando existan los pagos, un pedido ya cerrado queda solo con la comuna de entrega, y uno pagado que todavía no se entrega conserva la dirección hasta cerrarse. Los productos y los montos siguen el plazo de la sección 8. <!-- D2 de MATU-61. PENDIENTE: CL-52 y CL-44 -->
- Borramos su nombre, el nombre con que la llaman, su nivel de apoyo y su dirección (salvo que sea la de otra persona que cuidan en el grupo), y deja de aparecer en MATU. Si quieren volver a usar MATU para cuidarla, hay que registrarla de nuevo y todo empieza en blanco.
- Conservamos, sin nada de la ficha ni de los insumos, el registro de las autorizaciones, de los enlaces de relevo (el nombre del relevo, el motivo y las fechas; su teléfono, hasta 30 días) y de quién abrió la ficha, por los plazos de la sección 8, y el registro de los avisos (sin el texto ni tu correo), 90 días desde que se creó cada aviso, para poder demostrar cómo se usaron los datos. Esos registros ya no se ven en la aplicación: si los necesitas, pídelos por el correo de esta sección.
- Lo borrado sigue en las copias de respaldo hasta que vencen (sección 8).
- Una lista de insumos que ya imprimiste o compartiste no se borra, porque está fuera de MATU.
- No se puede deshacer.

Un abogado revisará, antes de usar MATU con datos reales, cómo confirmar la identidad de quien lo pide por correo sin tener cuenta en MATU, y si quien cuida a la persona sin ser su representante legal puede pedirlo por su cuenta. <!-- PENDIENTE: consulta legal sobre cómo verificar la identidad de la persona sin cuenta que lo pide por correo, y si una cuidadora o un cuidador de hecho puede pedirlo por su cuenta -->

**Quién puede pedirlo:**
- Sobre tus datos, tú.
- Sobre los datos de la persona cuidada, ella misma o su representante legal. Todavía no definimos si quien la cuida sin ser su representante legal puede pedirlo en su nombre. Un abogado lo revisará antes de usar MATU con datos reales. <!-- PENDIENTE: si la cuidadora o el cuidador de hecho puede pedirlo en su nombre. Está en consulta legal -->

**Cómo:** escribe a cuidaconmatu@gmail.com. Si tienes cuenta en MATU, escríbenos desde el correo de tu cuenta. Si lo pides por la persona que cuidas, cuéntanos en qué calidad lo pides. No incluyas en tu correo datos de salud ni el texto de la ficha: no los necesitamos para responderte. Puede que te pidamos confirmar tu identidad. Te avisamos que recibimos tu correo dentro de 2 días hábiles y te respondemos a más tardar en 30 días corridos. Es gratis. <!-- PENDIENTE: CL-48, plazo legal de respuesta antes y después del 01-12-2026 -->

En «Tu cuenta» puedes ver qué versión de esta política aceptaste y cuándo.

Si no te respondemos o no estás de acuerdo con la respuesta, puedes reclamar ante la Agencia de Protección de Datos Personales cuando esté funcionando, o ante los tribunales.

## 11. Si hay una filtración de datos

Si hay una filtración que afecte datos personales, avisaremos sin demora a la Agencia de Protección de Datos Personales y a las personas afectadas. Nuestra meta interna es hacerlo dentro de 72 horas desde que lo sepamos. Tendremos un procedimiento escrito para responder a una filtración antes de usar MATU con datos reales. <!-- PENDIENTE: procedimiento escrito ante una filtración -->

## 12. Cambios a esta política

- Cada versión tiene un número y una fecha, que ves al comienzo de esta página.
- Al crear tu cuenta, te pedimos marcar que leíste y aceptas esta política. Guardamos la versión, la fecha y la hora, y una huella del texto exacto que viste, que permite comprobar después cuál era. No guardamos tu dirección IP ni tu navegador. Ese registro no se puede cambiar ni borrar desde la aplicación.
- Si creaste tu cuenta antes de la versión 0.11, no tenemos registro de qué versión aceptaste, y «Tu cuenta» lo dice así.
- Con cada autorización guardamos el número de la versión vigente cuando la diste.
- Si un cambio agrega usos, datos o personas que reciben datos, te pediremos una autorización nueva.
- La versión 0.12 agrega los pedidos. No te pedimos aceptar de nuevo esta política ni volver a dar las autorizaciones de la ficha y de los insumos: los pedidos tienen su propia autorización, que se pide la primera vez que haces un pedido (sección 5). <!-- D11 de MATU-61. PENDIENTE: CL-24 -->
- La versión 1.0 será la primera revisada por un abogado y la primera que permita usar datos reales.
<!-- PENDIENTE: CL-50, si «acepto» es un consentimiento o solo un acuse de lectura -->

## 13. Lo que todavía no funciona en el piloto

- Borrar el teléfono del relevo 30 días después de que el acceso vence o se corta. Mientras no exista, MATU no trata datos reales.
- Ver o descargar los datos desde la aplicación. Por ahora, en «Tu cuenta» ves tu email, parte de tu celular y qué versión de esta política aceptaste. Para lo demás, escribe a cuidaconmatu@gmail.com (sección 10).
- Borrar los datos de la persona cuando lo pide por correo, sin pasar por su grupo. Mientras no exista, MATU no trata datos reales.
- El recordatorio de los 12 meses.
- Un aviso automático al equipo cuando una de las tareas diarias falla. Mientras no exista, el equipo revisa a mano el historial de corridas.
- Renovar desde la aplicación la autorización cuando vence su revisión de los 12 meses.
- Avisos de insumos por notificación o por correo: en el piloto se prueban sin enviarse (los de la aplicación ya funcionan). Elegir desde la aplicación, en «Tu cuenta», si los recibes por correo o en un teléfono.
- Enviar correos solo a direcciones verificadas.
- Invitaciones y pagos. Los pedidos se arman y se confirman hasta ver el total, pero todavía no se pagan ni se entregan.
- Verificar tu email al crear la cuenta. Mientras no exista, si intentas registrarte con un email que ya tiene cuenta, MATU te lo dirá, y alguien podría registrar un email que no es suyo.
- Eliminar tu cuenta o cambiar tu nombre o tu correo desde la aplicación. Mientras tanto, pídelo a cuidaconmatu@gmail.com desde el correo de tu cuenta.

## 14. Leyes que aplican

<!-- ADR-027 (27-10), aprobado por Jorge. -->

- Ley 19.628 sobre protección de la vida privada, con las modificaciones de la Ley 21.719 de protección de datos personales, que rigen plenamente desde el 1 de diciembre de 2026.
- Ley 19.496 sobre protección de los derechos de los consumidores, para los pedidos y los pagos.
- Decreto 6 de 2021 del Ministerio de Economía (Reglamento de Comercio Electrónico) y Decreto 52 de 2024 (exclusión del derecho a retracto), para los pedidos y los pagos.
- Ley 20.422 sobre igualdad de oportunidades e inclusión de personas con discapacidad. Por eso esta política está escrita para leerse en el teléfono.

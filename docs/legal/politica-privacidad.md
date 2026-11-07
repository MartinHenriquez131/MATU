# Política de privacidad de MATU

**Versión 0.10 · 3 de noviembre de 2026 (03/11/2026)** · agrega el cálculo de insumos (MATU-36) y corrige la sesión y los dispositivos (MATU-38). La versión 0.9 era del 21/10/2026, revisada el 24/10/2026
**Estado:** borrador para el piloto académico. Todavía no sirve para tratar datos reales.
**Aprobación:** aprobada como borrador v0.9 por Jorge Espinoza (Product Owner) el 25/10/2026. La revisión la hizo el orquestador del equipo de agentes, por delegación. Se confirman los tres compromisos del texto: MATU no vende datos, borra de inmediato los datos reales que entren por error, y ejercer los derechos es gratis. Los [PENDIENTE] que quedan (contacto, plazos, proveedores y procedimiento ante filtraciones) se resuelven en la versión 1.0, antes de tratar datos reales.
**Identificador de versión en el sistema:** `0.10`
**Versión 0.10 (03-11):** la redactó el analista normativo con las decisiones de Jorge del 31-10, del 02-11 y del 03-11 (contrato de MATU-32, MATU-36 y MATU-38). Aprobada por Jorge el 05-11 como borrador del piloto, que trabaja solo con datos sintéticos. Antes de tratar datos reales pasa por la consulta legal. `POLITICA_VERSION` pasa a `0.10` en el backend con MATU-36
**ADR-027 (27-10):** las secciones que empiezan con esa nota adaptan el texto a los pedidos y pagos del ADR-027. Aprobado por Jorge el 27-10 como diseño. Las frases sobre lo que el comercio ve o no ve se publican solo cuando la migración del sprint 4 (requisitos R7 a R9, arquitectura 18.1) las haga ciertas. Siguen sin publicarse en la versión 0.10: se publican cuando el sprint 4 las haga ciertas, con una versión nueva.
**MATU-50 (03-11):** se precisan las secciones 4, 6, 8 y 9 con la ficha ampliada ya construida, y se agrega que la ficha no se imprime (ADR-029). No agregan usos, datos ni destinatarios, y no cambian las declaraciones. No cambian la versión: `POLITICA_VERSION` sigue en `0.10`. Aprobado por Jorge el 03-11.

**MATU-09 (27-10):** se ajustan las secciones 4, 6, 8, 9, 10 y 13 con el acceso de relevo. Aprobado por Jorge el 27-10 como diseño. No cambian la versión: `POLITICA_VERSION` sigue en `0.9`.
**MATU-41 (04-11):** se ajustan las secciones 3, 6, 8 y 13 con los avisos por notificación y por correo. No agregan usos ni datos. No cambian la versión: `POLITICA_VERSION` sigue en `0.10`. Aprobado por Jorge el 04-11. Mientras el envío sea simulado no hay destinatarios nuevos. Activar un proveedor real de correo o de notificaciones exige una versión nueva de esta política, con sus nombres y su país.

**MATU-25 (05-11):** se ajustan las secciones 4, 7, 8 y 9 con el ambiente de prueba en Railway y el límite por IP. No cambian la versión: `POLITICA_VERSION` sigue en `0.10`, porque el ambiente de prueba trata solo datos inventados y ninguna persona real dio una autorización en él. Aprobado por Jorge el 05-11. La versión 1.0 nombrará el proveedor y el país donde se alojen los datos reales.

**MATU-60 (06-11):** se ajustan las secciones 3, 5, 6, 8 y 9 con la lista de insumos. La lista se arma con lo que el grupo ya ve, MATU no la guarda ni la envía, y quien la imprime o la comparte lo hace desde su teléfono. El único dato nuevo es cuántas unidades trae cada envase de un insumo, que describe el envase y no a la persona. No agregan usos ni destinatarios de MATU, así que no cambian la versión: `POLITICA_VERSION` sigue en `0.10`. **Criterio desde el 06-11 (decisión de Jorge):** la versión cambia cuando una declaración deja de cubrir lo que se trata. Un dato o una función nueva dentro de la misma finalidad se informa en la política vigente sin cambiar la versión. La consulta legal lo confirma antes de la versión 1.0 (CL-4). Aprobado por Jorge el 06-11.

**MATU-44 (06-11):** se ajustan las secciones 4, 5, 6, 8, 10 y 13 con el retiro de las autorizaciones desde la aplicación, volver a autorizar la ficha y el borrado de la ficha 90 días después del retiro. No agregan usos, datos ni destinatarios, y no cambian las declaraciones, así que no cambian la versión: `POLITICA_VERSION` sigue en `0.10` (criterio del 06-11). Aprobado por Jorge el 06-11.

**MATU-51 (07-11):** se ajustan las secciones 6 y 8 con «Compré» y «Me quedan», que anotan una compra o lo que queda en cualquier insumo, haya aviso o no, y las compras anotadas pasan a guardarse 90 días. No agregan usos, datos ni destinatarios, y un plazo más corto no cambia las declaraciones, así que no cambian la versión: `POLITICA_VERSION` sigue en `0.10` (criterio del 06-11). [PENDIENTE DE JORGE]

---

## En un minuto

- MATU te ayuda a organizar el cuidado de una persona mayor. Su parte principal es una ficha de relevo para quien te reemplaza.
- **Hoy MATU es un piloto académico y no guarda datos reales.** Si lo pruebas, usa nombres y datos inventados.
- MATU **no pide diagnósticos** ni fichas clínicas. Solo pide lo necesario para cuidar. Si quieres, puedes anotar en la ficha qué remedios toma y a qué hora, para que quien te reemplaza no se equivoque.
- La ficha se guarda cifrada. La ven solo las personas de tu grupo que tienen permiso y el relevo al que tú se la compartes, por el tiempo que tú elijas.
- MATU no usa publicidad ni analítica de terceros, y no vende datos.
- MATU nunca ve ni guarda los datos completos de tu tarjeta.
- Puedes pedir ver, corregir o borrar los datos. La sección 10 explica cómo.

---

## 1. Esto es un borrador del piloto académico

- MATU es un proyecto de título. Esta versión es un borrador escrito para su piloto académico, y **todavía no la revisa un abogado**.
- **En los sprints 1 a 3 del piloto, del 16 de octubre al 5 de noviembre de 2026, MATU no trata datos reales.** Todo lo que hay en el sistema son datos inventados para probarlo.
- El resto del semestre también se trabaja solo con datos inventados, en los ambientes de prueba y de demostración.
- Si estás probando MATU, **no escribas datos reales**, ni tuyos ni de otra persona.
- Si alguien ingresa datos reales por error, los borramos apenas lo sepamos.
- Antes de usar MATU con personas reales, publicaremos una versión nueva, revisada por un abogado, y te pediremos aceptarla.
- Algunas funciones que se describen aquí todavía se están construyendo. La sección 13 dice cuáles.

## 2. Quién es responsable de los datos

- **Responsable durante el piloto académico:** el equipo del proyecto, Jorge Espinoza y Martín Henríquez, como personas naturales. MATU todavía no tiene persona jurídica (decisión MATU-27 del 24/10/2026). Eso cambia en la versión 1.0, antes de tratar datos reales.
- **Contacto para temas de privacidad:** [PENDIENTE: correo de contacto]

## 3. Para qué usamos los datos

1. Crear tu cuenta y dejarte entrar.
2. Formar tu grupo de cuidado y dar a cada persona su permiso.
3. Registrar a la persona que cuidas y la autorización para usar sus datos.
4. Guardar la ficha de relevo y compartirla con quien tú elijas.
5. Calcular cuándo se acaba cada insumo de la persona que cuidas, mostrarte cuáles se acaban pronto y avisarte. Con los que se acaban pronto, MATU arma una lista de insumos con una cantidad sugerida, que puedes imprimir o compartir desde tu teléfono. Los avisos dentro de la aplicación ya funcionan. En el piloto, los avisos por notificación y por correo se prueban sin enviarse: no salen de los equipos de MATU (MATU-41).
6. Hacer pedidos y pagos de insumos. *Todavía no disponible.*
7. Cuidar la seguridad: registrar quién abrió la ficha, detectar accesos extraños y responder si hay una filtración.

**Cada uso se autoriza por separado.** MATU pide una autorización para la ficha de relevo y otra para el cálculo de insumos. La del cálculo se pide la primera vez que anotas un insumo. Los avisos de insumos van dentro de esa misma autorización: no se pide otra. Antes de activar los pedidos, te pediremos una autorización aparte.

MATU no usa los datos para publicidad ni los vende. Tampoco toma decisiones automáticas sobre las personas. La fecha en que se acaba un insumo es solo una estimación para avisarte.

## 4. Qué datos guardamos

### De ti

- **Tu nombre, tu email y tu celular.** Para crear tu cuenta no pedimos nada más.
- **Tu celular** lo pedimos para enviarte un código cuando quieras recuperar tu contraseña. Antes de usarlo para eso, te pedimos confirmarlo con un código; mientras no lo confirmes, el código te llega a tu correo. Guardamos si lo confirmaste y si prefieres recibir los códigos por SMS o por WhatsApp. Si cambias el número, tendrás que confirmarlo de nuevo. El mensaje solo trae el código: nunca tu nombre, el de la persona que cuidas ni nada de su cuidado. No lo mostramos a otras personas del grupo ni lo usamos para publicidad. Del código guardamos solo una huella que no permite reconstruirlo, cuándo vence y cuántas veces se intentó, y la borramos al usarlo o a los 10 minutos. Cuando cambias tu contraseña, cerramos tu sesión en todos tus dispositivos (ver «Tu sesión») y te avisamos por el otro canal, o por tu correo si tu celular no está confirmado. **En el piloto, el código se prueba sin enviarse:** no sale de los equipos de MATU, así que no te llega un SMS, un WhatsApp ni un correo (MATU-57).
- **Tu email se guarda legible**, porque lo necesitamos para que entres y para escribirte. Lo protege la separación entre familias de la base de datos. Para iniciar sesión usamos además una huella del email que no permite recuperarlo.
- **Tu contraseña**, guardada transformada de una forma que no se puede revertir. Nadie en MATU puede leerla.
- **Los grupos a los que perteneces** y tu rol en cada uno.
- **Registros técnicos.** Por cada acción guardamos la fecha y hora, el tipo de acción sin su contenido, si resultó o no, cuánto tardó y un número interno que te identifica a ti y a tu grupo. En esos registros no guardamos tu email, tu contraseña, tus códigos de acceso, el nombre del grupo ni tu dirección IP.
- **Tu dirección IP y tu email, para limitar intentos.** Para evitar abusos, MATU limita cuántas veces se puede, desde una misma dirección IP, crear una cuenta, entrar, pedir un código para recuperar el acceso y abrir un enlace de relevo. Si alguien se equivoca varias veces al entrar, MATU hace esperar antes del siguiente intento. Para contarlos guardamos una huella de tu dirección IP y, al entrar o al recuperar el acceso, otra de tu email, que no permiten recuperarlos. La mayoría se borra sola en una hora; las de recuperar el acceso, en 24 horas como máximo (sección 8). No guardamos tu IP en la base de datos ni en los registros de MATU. [PENDIENTE: consulta legal sobre la base de este conteo]
- **Tus dispositivos.** Por cada navegador donde entras guardamos un nombre general, como «Chrome en Android», y cuándo lo usaste por última vez. No guardamos los datos de tu navegador. Si activas los avisos, guardamos además la dirección que tu navegador nos da para enviártelos. Los avisos no dicen el nombre de la persona ni del insumo.
- **Cuando des una autorización** para la persona que cuidas: la fecha y la hora, en qué calidad la diste, qué declaración viste y la versión de esta política. Si eres cuidadora o cuidador de hecho, también qué aviso viste: su identificador, su versión y una huella de su texto. Si registras la decisión de la propia persona, queda anotado que la registraste tú, en su presencia. No guardamos tu dirección IP ni tu navegador.
- **Cuando retires una autorización:** la fecha y la hora, y quién la retiró. No guardamos tu dirección IP ni tu navegador. La autorización retirada no se borra: queda como respaldo de que se dio y de cuándo se retiró (sección 8).

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
- Su dirección, si quieres darla al registrarla. Es opcional y puedes agregarla más adelante, por ejemplo con el primer pedido. No guardamos su ubicación en el mapa.
- La autorización: quién la dio, en qué calidad y cuándo, y la referencia al documento si quien autoriza es su representante legal.
- Si diste la autorización como cuidadora o cuidador de hecho, la fecha en que te pediremos confirmar que sigues a cargo, 12 meses después.
- La ficha de relevo, con sus tres campos: **Su día**, **Si se altera** y **A quién llamar**. También guardamos quién escribió cada campo y cuándo.
- **Su consumo de insumos:** qué insumos usa, en qué unidad, cuánto usa cada cuántos días, cuánto quedaba la última vez que lo anotaste, con cuántos días de anticipación quieres saberlo y, si lo anotas, cuántas unidades trae cada envase. Con eso MATU calcula una fecha estimada. Si el insumo no está en el catálogo, guardamos el nombre que escribas: usa el nombre del envase, sin remedios ni para qué lo usa. Los remedios van en la ficha, no en los insumos.
- **Secciones adicionales de la ficha**, si decides agregarlas: Quién es, Lo que le hace bien, Comer y beber, Moverse y descansar, Cómo hablarle y Sus remedios. Todas son opcionales y se escriben con tus palabras, hasta 500 caracteres cada una (800 en Sus remedios). Se guardan cifradas, como la ficha, y siguen sus mismos plazos. Si quitas una sección, su texto se borra en ese momento y quien tenga un enlace deja de verla. Si la vuelves a agregar, ningún enlace anterior la ve. **Sus remedios** guarda en texto libre qué remedios toma la persona y a qué hora, tal como se los da la familia. No es una receta y no reemplaza la indicación del médico. Al compartir con un relevo, tú marcas qué secciones ve. Sus remedios viene siempre sin marcar. Te recomendamos no escribir diagnósticos ni nombres de enfermedades en ninguna sección. Ya puedes agregarlas, editarlas y quitarlas.

**El nivel de apoyo y la ficha son datos sensibles**, porque hablan de la salud y de la dependencia de la persona. Por eso los protegemos de forma especial.

**El consumo de insumos también lo tratamos como un dato sensible**, porque puede revelar algo de la salud o de la dependencia de la persona. A diferencia de la ficha, no se cifra con una clave propia: lo protege la separación entre familias de la base de datos. [PENDIENTE: consulta legal sobre si el consumo es un dato relativo a la salud y si basta esta protección]

### De otras personas que tú anotas

- **Relevo:** su nombre y su teléfono, qué campos y qué secciones adicionales le compartiste, hasta cuándo, el motivo, cada vez que abrió el enlace, aunque no haya escrito el PIN, cuántas veces abrió la ficha y cada PIN incorrecto. Su teléfono es obligatorio: sirve para que tú le envíes el enlace desde tu teléfono, con la aplicación de mensajes que elijas, y para que quien administra el grupo o lo cuida pueda llamarlo. MATU no le envía mensajes. El PIN no va en el mensaje: se lo dictas por teléfono. Avísale que lo anotaste: cuando abra el enlace, MATU le muestra qué guarda de él, y también tu nombre de pila y el de la persona que cuidas. Tu grupo puede ver ese registro en "Quién la vio" (ver "Quién ve tus datos").
- **"A quién llamar":** los nombres y teléfonos que escribas. Avísales que los anotaste.
- **Invitaciones a tu grupo:** el email o el teléfono de la persona invitada. *Todavía no disponible.*

### De tus pedidos

> ADR-027 (27-10), aprobado por Jorge.

*Todavía no disponible.* Cuando existan los pedidos, guardaremos:

- Los productos que pediste, con su cantidad, su precio, el envío y el total.
- El comercio que preparó cada producto.
- La dirección de entrega.
- El teléfono de contacto para la entrega.
- Qué elegiste hacer si falta un producto.
- Las condiciones del pedido que aceptaste, su versión y cuándo las aceptaste.
- El pago: el monto cobrado y, si hubo, la devolución.

**Tus pedidos y el consumo de insumos de la persona que cuidas se tratan como datos sensibles**, porque pueden revelar algo de su salud o de su dependencia. Tus pedidos los ven las personas de tu grupo y el equipo de MATU para dar soporte. El consumo de insumos lo ven solo las personas de tu grupo. Ningún comercio los ve junto a un nombre. A diferencia de la ficha, no se cifran con una clave propia de cada persona.

**Para los pedidos te pediremos una autorización expresa y aparte**, distinta de la de la ficha. Puedes retirarla igual de fácil que la diste. Si la retiras, ya no podrás pedir desde MATU, pero sí imprimir o compartir la lista. Los pedidos ya pagados se guardan el plazo de la sección 8, para responder reclamos y por obligación tributaria. [PENDIENTE: confirmar en la versión 1.0]

[PENDIENTE: consulta legal sobre si los productos de un pedido son un dato relativo a la salud, y si el art. 16 bis, inciso 1, de la ley limita su tratamiento aunque haya autorización]

### Lo que MATU no pide

- Diagnósticos, nombres de enfermedades, recetas, exámenes ni fichas clínicas. Si quieres, puedes anotar qué remedios toma y a qué hora, para que quien te reemplaza no se equivoque. Esa sección es opcional y solo la ven tu grupo y los relevos a quienes tú se la muestres (decisión de Jorge del 03-11, por la seguridad del cuidado).
- El RUT de nadie.
- Copias de documentos. Si eres representante legal, guardamos solo una referencia al documento.
- Los datos de tu tarjeta.

**Un consejo para la ficha:** escribe qué ayuda, no qué enfermedad tiene. Por ejemplo: "se tranquiliza si bajas las persianas".

## 5. La autorización para usar los datos de la persona que cuidas

Para guardar la ficha necesitamos una autorización. Al dar de alta a la persona, eliges en qué calidad la das. Si después se retira, quien administra el grupo o quien cuida a la persona puede volver a darla desde «Grupo familiar», con la misma declaración y eligiendo de nuevo la calidad (sección 10).

**La propia persona (titular).** La persona que cuidas decide por sí misma y tú registras su decisión. Al registrarla declaras:

> Declaro que la persona que cuido me dijo hoy, en persona, que autoriza a MATU a guardar su ficha de relevo, incluidas las secciones adicionales y sus remedios si se agregan, y a compartirla con el relevo que elija el grupo, según la política de privacidad vigente. Yo solo registro su decisión.

**Su representante legal.** Tienes un nombramiento legal para representarla. Declaras:

> Declaro que soy representante legal de la persona que cuido y que la referencia que indico corresponde al documento que lo acredita. Como su representante, autorizo a MATU a guardar su ficha de relevo, incluidas las secciones adicionales y sus remedios si se agregan, y a compartirla con el relevo que elija el grupo, según la política de privacidad vigente.

**Cuidadora o cuidador de hecho.** La cuidas en el día a día, pero no tienes un nombramiento legal para representarla. Declaras:

> Declaro que cuido a esta persona y que no soy su representante legal. Autorizo a MATU a guardar su ficha de relevo, incluidas las secciones adicionales y sus remedios si se agregan, y a compartirla con el relevo que elija el grupo, según la política de privacidad vigente. Leí el aviso sobre el límite de esta autorización.

### Aviso para quien cuida sin ser representante legal

Este es el texto exacto que MATU muestra al elegir esta calidad. Su identificador en el sistema es `aviso_cuidador_de_hecho`, versión 1.1 (la 1.0 asumía que la persona cuidada es mujer; cambio aprobado por Jorge el 03-11):

> **Aviso: tu autorización tiene un límite**
>
> Declaraste que cuidas a esta persona y que no eres su representante legal. Con esa declaración puedes organizar su cuidado en MATU, pero tu autorización no equivale a la de la propia persona ni a la de su representante legal. MATU no puede comprobar lo que declaras. Por eso deja registrado que la autorización la diste tú, como cuidadora o cuidador de hecho, con la fecha y la versión de la política.
>
> Te pedimos tres cosas: anota solo lo necesario para su cuidado, cuéntale qué guardas en MATU si puede comprenderlo, y respeta lo que esa persona decida. La persona o su representante legal pueden pedir en cualquier momento que se borren sus datos.
>
> En 12 meses te pediremos confirmar que sigues a cargo de su cuidado.

Su huella en el sistema (SHA-256) es `8dfbca33f5c58a2c1f5c43a672b3e0fcd2ed4adcc971dcccd0f8879814b10489`.

Cada declaración también tiene un identificador en el sistema: `declaracion_titular`, `declaracion_representante_legal` y `declaracion_cuidador_de_hecho`. Su versión es la de esta política. Cambiar una sola palabra de una declaración o del aviso es publicar una versión nueva.

Si pasan los 12 meses sin confirmarlo, la ficha queda en pausa: nadie del grupo la puede ver ni cambiar, pero lo escrito sigue guardado. Los enlaces de relevo dejan de abrir mientras tanto, y quien tenga uno ve que por ahora la ficha no se puede ver, sin el motivo. Puedes cortar un enlace igual. Cuando se renueva, vuelven a abrir los enlaces que no hayan vencido. Esto es distinto de retirar la autorización: si la retiras, los enlaces se cortan y no vuelven a abrir (sección 10). [PENDIENTE: qué pasa si nunca se renueva y cuánto tiempo se guarda una ficha en pausa. Está en consulta legal]

### La autorización para calcular insumos

Es aparte de la de la ficha y se da en la misma calidad. Se pide la primera vez que anotas un insumo, y la dan el administrador o el cuidador del grupo. Si eres cuidadora o cuidador de hecho, MATU te vuelve a mostrar el aviso de arriba y a los 12 meses te pedirá confirmar. Las declaraciones son:

**La propia persona (titular):**

> Declaro que la persona que cuido me dijo hoy, en persona, que autoriza a MATU a guardar qué insumos usa, cuánto usa y cuánto queda, y a calcular cuándo se acaban y avisarme cuando se esté por acabar, según la política de privacidad vigente. Yo solo registro su decisión.

**Su representante legal:**

> Declaro que soy representante legal de la persona que cuido y que la referencia que indico corresponde al documento que lo acredita. Como su representante, autorizo a MATU a guardar qué insumos usa, cuánto usa y cuánto queda, y a calcular cuándo se acaban y avisarme cuando se esté por acabar, según la política de privacidad vigente.

**Cuidadora o cuidador de hecho:**

> Declaro que cuido a esta persona y que no soy su representante legal. Autorizo a MATU a guardar qué insumos usa, cuánto usa y cuánto queda, y a calcular cuándo se acaban y avisarme cuando se esté por acabar, según la política de privacidad vigente. Leí el aviso sobre el límite de esta autorización.

Sus identificadores son `declaracion_consumo_titular`, `declaracion_consumo_representante_legal` y `declaracion_consumo_cuidador_de_hecho`. Las aprobó Jorge el 03-11.

## 6. Quién ve los datos

> ADR-027 (27-10), aprobado por Jorge. Cambian los párrafos de comercios, de quien reparte y de Transbank.

**Tu cuenta:** tu email y tu celular los ven solo tú y el equipo que opera MATU. Las personas de tus grupos ven tu nombre. [PENDIENTE: si también ven tu email, se define con la lista de miembros del grupo]

**El nombre del grupo:** lo ven las personas del grupo y el equipo que opera MATU.

**Tu grupo, según el rol de cada persona:**
- **Administrador y cuidador:** ven todo, incluida la calidad en que se dio la autorización, y pueden editar y compartir la ficha. La referencia al documento del representante legal no se muestra en la aplicación: queda guardada solo como respaldo.
- **Pagador:** ve el nombre y la dirección. Ve la ficha solo si le dan ese permiso. Con ese permiso también ve la lista de enlaces de relevo (el nombre del relevo, el motivo, las fechas y quién lo creó), sin su teléfono, y no puede crear ni cortar enlaces.
- **Observador:** ve el nombre. Nunca ve la ficha.

**El estado de las autorizaciones** (MATU-44): todas las personas del grupo ven, en «Grupo familiar», si cada autorización de la persona está vigente, por renovar, retirada o ya borrada, con sus fechas y hasta cuándo se guarda lo escrito. La calidad en que se dio la ven solo el administrador y el cuidador, que son también los únicos que pueden retirarla o volver a darla. Solo la autorización de una cuidadora o un cuidador de hecho se revisa a los 12 meses, así que quien ve esa fecha, o que está por renovar, puede deducir en qué calidad se dio.

**Quién abrió o editó la ficha** (aprobado por Jorge el 28-10, MATU-14): cada vez que un miembro del círculo de cuidado abre o edita la ficha de relevo, MATU registra quién lo hizo, qué acción realizó y cuándo. Si la acción fue agregar, editar o quitar una sección adicional, también queda registrado cuál sección fue, por ejemplo «Sus remedios», aunque después la quites. Nunca su texto. Este registro no guarda el contenido de la ficha ni tu dirección IP. Puede consultarlo la persona administradora del grupo, y cada miembro puede ver sus propios registros. Se guarda 3 años (sección 8).

**Quién abrió el enlace de relevo** (MATU-45, aprobado por Jorge el 03-11): cada vez que un relevo abre el enlace, aunque no escriba el PIN, abre la ficha, escribe mal el PIN o el enlace se bloquea, MATU registra la fecha, la hora y el nombre del relevo. Cuando abre la ficha, también registra qué secciones adicionales vio, sin su texto. Lo ven en "Quién la vio" la persona administradora, quien cuida y quien paga si tiene permiso para ver la ficha. El observador no lo ve. Este registro no muestra el teléfono del relevo, su dirección IP, el enlace ni el PIN. Se guarda 3 años desde que el acceso vence o se corta. [PENDIENTE: consulta legal sobre si 3 años es proporcional para los datos de un tercero, el relevo]

**El consumo de insumos** lo ven todas las personas del grupo, incluido el observador. Solo el administrador y el cuidador lo anotan, lo cambian, dejan de seguir un insumo o lo eliminan. Cada vez que alguien lo hace, MATU registra quién y cuándo, sin el nombre del insumo ni las cantidades. El equipo de MATU no puede leerlo.

**Los avisos de insumos** (MATU-37 y MATU-41). Cuando un insumo está por acabarse, MATU te avisa en la aplicación. MATU también está preparado para avisarte por correo y con una notificación en los teléfonos donde activaste los avisos, pero **en el piloto esos avisos se prueban sin enviarse: no salen de los equipos de MATU** (sección 13). Cuando se activen, saldrán desde las 9:00, hora de Chile. Por defecto avisan al administrador y al cuidador. El pagador y el observador reciben avisos solo si los activan. Tu elección es tuya, no del grupo, y vale para todos tus grupos. El aviso dice solo «MATU: un insumo se está acabando. Abre la app para ver cuál»: no dice qué insumo ni de quién, porque a veces el teléfono está a la vista de otras personas. Su enlace lleva a la aplicación y no dice quién eres. El correo no sabe si lo abriste ni si hiciste clic. Antes de enviar cada aviso, MATU revisa que la autorización de insumos siga vigente y al día, que el aviso siga abierto y que sigas en el grupo. Si algo de eso falla, no lo envía. Cuando se activen los envíos, un servicio de correo recibirá ese texto y tu correo, y el servicio de notificaciones de tu navegador recibirá solo la dirección de avisos de tu navegador, sin ningún texto: el texto lo pone tu teléfono. Nada más. [PENDIENTE: nombres y país, antes de activar los envíos]. Puedes dejar de recibir los avisos por correo o por notificación cuando quieras, en «Tu cuenta» (sección 13), y dejar de recibirlos en un teléfono si cierras la sesión en él o lo sacas de tus dispositivos. Solo el administrador y el cuidador pueden marcar un aviso como resuelto («Ya lo resolví») y anotar, en cualquier momento, que compraron un insumo («Compré») o cuánto queda («Me quedan»), haya aviso o no. Si anotan una compra, MATU guarda la cantidad, la fecha y quién la anotó, y la suma a lo que calculaba que quedaba. Si anotan cuánto queda, MATU reemplaza lo que calculaba y no guarda una compra. Si retiras la autorización de insumos, MATU deja de avisar en ese momento. El aviso nunca hace un pedido.

**La lista de insumos** (MATU-60). Con los insumos que se acaban pronto, MATU arma una lista con el nombre de cada insumo y una cantidad sugerida: lo que falta para cubrir 30 días, descontando lo que MATU calcula que queda, en envases si anotaste cuántas unidades trae cada uno. En la pantalla ves también cuántos días le quedan, pero eso no sale en lo que imprimes o compartes. La ven todas las personas del grupo. Quien administra, cuida o paga puede imprimirla, guardarla como PDF o compartirla como texto desde su teléfono, con la aplicación que elija. El observador la ve, sin esas opciones. Antes de imprimirla o compartirla puedes agregar otros insumos y cambiar las cantidades. Eso queda solo en tu pantalla y MATU no lo guarda. La lista no lleva el nombre de la persona que cuidas, ni nada de su ficha, ni precios, pero el nombre de un insumo puede decir algo de su salud. MATU no envía la lista, no crea un enlace para verla y no sabe si la imprimiste ni a quién se la mandaste. Lo que imprimas o compartas sale de MATU: queda en el papel, en tu teléfono o en la aplicación que usaste, y MATU no puede borrarlo, aunque después elimines el insumo o retires la autorización. Compártela solo con quien la necesita para comprar.

**El relevo**, la persona que te reemplaza:
- Ve solo el nombre con que llaman a la persona, tu nombre de pila, los tres campos de la ficha y las secciones adicionales que marcaste al compartir. Si agregas una sección después, no la ve hasta que le des un acceso nuevo.
- Al abrir el enlace, y antes de escribir el PIN, ve tu nombre de pila y el de la persona que cuidas.
- Entra con un enlace y un PIN de 4 dígitos. El acceso vence en 24 horas, o en el plazo que elijas hasta un máximo de 30 días, y puedes cortarlo cuando quieras.
- Si la autorización de la ficha está en pausa porque no se confirmó a los 12 meses, el enlace deja de abrir mientras tanto. Si la autorización se retira, el enlace se corta y no vuelve a abrir. En los dos casos el relevo no ve el motivo.
- Cada vez que abre la ficha queda registrado, y también cada PIN incorrecto y cada bloqueo. También queda registrado cada vez que abre el enlace, aunque no escriba el PIN.
- Lo que el relevo lea puede anotarlo o fotografiarlo, y MATU no puede impedirlo. Comparte solo lo que necesita y por el tiempo justo.

**Comercios en convenio**, cuando existan los pedidos:
- Para saber si tienen los productos, MATU les pregunta solo por los productos y las cantidades, con una referencia que se crea al azar para cada pedido y no permite saber de quién es. Esa consulta no lleva tus datos, ni los de la persona que cuidas, ni la dirección.
- El comercio que prepara tu pedido ve solo sus productos, la referencia del pedido y el código de retiro. Si falta un producto y otro comercio lo reemplaza, ese comercio ve lo mismo, solo con lo que le toca preparar.
- **Ningún comercio ve un nombre**, ni el tuyo ni el de la persona que cuidas. Tampoco ven la ficha. **La dirección nunca llega al comercio.** MATU vende y emite la boleta, así que el comercio no necesita saber quién paga.
- Aun así, MATU trata a cada comercio como si tratara datos por encargo: su convenio le exige siempre confidencialidad y seguridad.

**Quien reparte**, si en el futuro hay despacho: ve la dirección de entrega y el teléfono de contacto solo mientras lleva el pedido. Lo hace por encargo de MATU y con un contrato que le exige confidencialidad, seguridad y borrar los datos al terminar.

**Transbank**, cuando existan los pagos: el pago se hace en su página. MATU no ve el número de tu tarjeta ni su código. Solo guarda el resultado: el monto, el código de autorización, el tipo de tarjeta y sus últimos 4 dígitos. Puedes pagar con crédito o con débito, y funcionan igual: se cobra una sola vez el total que viste antes de pagar. Si hay una devolución, va a la misma tarjeta, y no te pedimos datos nuevos para hacerla. Durante el piloto los pagos ocurren solo en el ambiente de prueba de Transbank, sin cobros reales. [PENDIENTE: que el débito y la devolución parcial funcionen así se confirma con la prueba en el ambiente de integración de Transbank, antes del sprint 4]

**El equipo de MATU:** para dar soporte ve los pedidos y los pagos. Sus herramientas no permiten leer la ficha ni el consumo de insumos.

**Dictar en vez de escribir:** en la ficha puedes dictar con el botón del micrófono. El reconocimiento de voz lo hace el servicio de tu navegador, no MATU. Por ejemplo, en Chrome el audio se envía a Google para convertirlo en texto, y puede salir de Chile. MATU no guarda el audio, solo el texto que revisas y guardas tú. Si no quieres que el audio salga de tu teléfono, escribe o usa el dictado de tu teclado. [PENDIENTE: consulta legal sobre el envío de audio de un dato sensible a un tercero, y nombrar los servicios y sus países] (decisión de Jorge del 03-11)

**Proveedores de tecnología** que guardan o procesan datos por encargo de MATU: [PENDIENTE: proveedor de nube, de notificaciones push, de WhatsApp, de correo, de SMS y de registro de errores, con qué datos recibe cada uno]

**Autoridades:** solo cuando una ley o un tribunal lo exige.

## 7. Dónde se guardan los datos

- Durante el semestre, MATU corre en los computadores del equipo y en un ambiente de prueba en Railway, un proveedor de servidores, en su región de California, Estados Unidos. Ese ambiente tiene solo datos inventados y se borra al terminar el semestre.
- Aunque los datos sean inventados, cuando usas el ambiente de prueba tu dirección IP pasa por los servidores de Railway en Estados Unidos. MATU no la guarda: solo una huella que no permite recuperarla, por el plazo de la sección 8. Railway puede guardar la dirección IP de cada conexión en sus propios registros técnicos. [PENDIENTE: confirmar qué registra Railway y por cuánto tiempo]
- [PENDIENTE: proveedor y país donde se alojarán los datos reales]
- Si los datos reales se guardan fuera de Chile, lo diremos aquí y aplicaremos lo que la ley exige para ese caso.

## 8. Cuánto tiempo guardamos los datos

- **Ficha de relevo:** mientras la autorización esté vigente y hasta 90 días después de que termine. Pasado ese plazo, MATU la borra destruyendo su clave y borrando el texto cifrado. En el piloto esa tarea se corre a mano (sección 13). Mientras no corre, la ficha ya no se puede ver ni recuperar, aunque su clave todavía exista. Si después se vuelve a autorizar, la ficha empieza en blanco y lo de antes no vuelve. Si pides borrarla, la dejamos ilegible de inmediato destruyendo su clave. [PENDIENTE: confirmar que una solicitud de borrado no espera los 90 días] Una sección adicional que quitas se borra en ese momento. Hasta que vence la última copia de respaldo que la contiene, sigue en esa copia, cifrada.
- **Consumo de insumos:** mientras la autorización para calcular insumos esté vigente y hasta 90 días después de que termine, también los insumos que dejaste de seguir. Un insumo que eliminas se borra en ese momento. Si pides borrar todo el consumo, lo borramos de la base de datos: no se deja ilegible, se borra.
- **Lista de insumos:** MATU no la guarda. Se arma cada vez que la abres, con lo que ya está anotado. Lo que agregas o cambias a mano se pierde al salir de la pantalla. Las copias que imprimas, guardes como PDF o compartas quedan fuera de MATU y no siguen estos plazos.
- **Tu sesión:** cada sesión se borra 30 días después de vencer o de cerrarse.
- **Tus dispositivos:** se borran 90 días después de su último uso. La dirección para enviarte avisos se borra cuando cierras la sesión, sacas el dispositivo o desactivas los avisos en él, o cuando el servicio de notificaciones informa que ya no existe.
- **Huellas para limitar intentos** al crear una cuenta, al entrar y al abrir un enlace de relevo: 1 hora desde el primer intento.
- **Avisos de insumos:** los avisos cerrados, 90 días. El registro de avisos, que dice a quién, por qué canal y si salió o por qué no salió, sin el texto ni tu correo: 90 días desde que se crea. Los eventos internos ya procesados, y los que no se pudieron procesar, 30 días. Las compras anotadas, 90 días desde que se anotan.
- **Código para recuperar el acceso** (MATU-57): hasta que se usa o 10 minutos. Los contadores de envíos, 24 horas como máximo.
- **Copias de respaldo:** [PENDIENTE: plazo]. El borrado queda completo cuando vence la última copia que contiene la clave.
- **Registro de quién abrió la ficha:** 3 años.
- **Pedidos y comprobantes de entrega**, cuando existan: 2 años.
- **Pagos y boletas**, cuando existan: 6 años, por obligación tributaria.
- **Tu cuenta:** [PENDIENTE]
- **Registro de autorizaciones:** cada autorización, también las retiradas, con su fecha de retiro. [PENDIENTE: plazo, en consulta legal]
- **Accesos de relevo:** el nombre del relevo, el motivo y las fechas, 3 años desde que vence o se corta el acceso, igual que el registro de quién abrió la ficha. El teléfono del relevo se borra 30 días después de que el acceso vence o se corta.
- **Registros técnicos del sistema:** [PENDIENTE]

## 9. Cómo protegemos los datos

- La conexión con MATU va cifrada.
- Cada campo y cada sección adicional de la ficha se cifra por separado con una clave propia de cada persona cuidada. Esa clave está protegida por una clave maestra. Durante el piloto, que usa solo datos inventados, la clave maestra está en el mismo servidor que la aplicación. Antes de usar MATU con personas reales, pasará a un servicio de custodia separado del servidor. [PENDIENTE: confirmar el servicio de custodia de claves]
- MATU no imprime ni exporta la ficha. Solo se comparte con el enlace con PIN (ADR-029).
- La lista de insumos sí se puede imprimir o compartir, porque no lleva la ficha ni el nombre de la persona. MATU no la guarda, no la envía y no crea un enlace para verla (ADR-031). Tampoco la guarda en tu teléfono ni en tu navegador: si cierras la pantalla, se pierde.
- La base de datos separa a cada familia: una familia no puede ver los datos de otra, aunque la aplicación tenga un error.
- El registro de quién abrió la ficha no se puede modificar ni borrar.
- Los registros técnicos de MATU no guardan el texto de la ficha, ni tu email, ni contraseñas, ni códigos de acceso, ni enlaces de relevo, ni PIN, ni el nombre del grupo, ni tu dirección IP. El proveedor de servidores puede registrar la dirección IP de cada conexión (sección 7).
- El enlace de relevo se bloquea después de 5 PIN incorrectos. Cada PIN incorrecto y cada bloqueo quedan registrados. Además, desde una misma dirección IP se admite un número limitado de intentos por hora para crear una cuenta, entrar y abrir un enlace de relevo: para contarlos se guarda una huella de la IP que no permite recuperarla y que se borra sola en el plazo de la sección 8. La IP no se guarda en la base de datos ni en los registros de MATU.
- La aplicación no guarda en tu teléfono ni en tu navegador la ficha, el consumo de insumos ni tu código de acceso, que vive solo en la memoria de la página. No usa analítica ni programas de terceros.
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
- La autorización de los insumos no cambia.

**Si retiras la autorización de los insumos:**
- MATU deja de calcular cuándo se acaban y de avisar, desde ese momento. Un aviso que estaba por salir ya no sale, y los avisos abiertos se descartan.
- Nadie del grupo puede ver los insumos anotados.
- Lo anotado se guarda hasta 90 días. Si en ese plazo das una autorización nueva, vuelve a verse tal como estaba. Si no, se borra (sección 8). Si autorizas después de ese plazo, hay que anotar los insumos de nuevo.
- Una lista de insumos que ya imprimiste o compartiste no se borra, porque está fuera de MATU.
- La ficha y los enlaces de relevo no cambian.

[PENDIENTE: consulta legal sobre si se pueden guardar esos 90 días después del retiro]

**Quién puede pedirlo:**
- Sobre tus datos, tú.
- Sobre los datos de la persona cuidada, ella misma o su representante legal. [PENDIENTE: si la cuidadora o el cuidador de hecho puede pedirlo en su nombre. Está en consulta legal]

**Cómo:** escribe a [PENDIENTE: correo de contacto]. Puede que te pidamos confirmar tu identidad. Respondemos dentro de [PENDIENTE: plazo legal de respuesta]. Es gratis.

Si no te respondemos o no estás de acuerdo con la respuesta, puedes reclamar ante la Agencia de Protección de Datos Personales cuando esté funcionando, o ante los tribunales.

## 11. Si hay una filtración de datos

Si hay una filtración que afecte datos personales, avisaremos sin demora a la Agencia de Protección de Datos Personales y a las personas afectadas. Nuestra meta interna es hacerlo dentro de 72 horas desde que lo sepamos. [PENDIENTE: procedimiento escrito ante una filtración]

## 12. Cambios a esta política

- Cada versión tiene un número. Con cada autorización guardamos el número de la versión que aceptaste.
- [PENDIENTE: guardar también qué versión aceptaste al crear tu cuenta y cuándo. Historia por decidir para el sprint 2]
- Si un cambio agrega usos, datos o personas que reciben datos, te pediremos una autorización nueva.
- La versión 1.0 será la primera revisada por un abogado y la primera que permita usar datos reales.

## 13. Lo que todavía no funciona en el piloto

- Borrar el teléfono del relevo 30 días después de que el acceso vence o se corta (MATU-46). Mientras no exista, MATU no trata datos reales.
- Ver, descargar o borrar los datos desde la aplicación. Mientras tanto, por el correo de la sección 10.
- El recordatorio de los 12 meses.
- Las tareas que borran la ficha y los insumos 90 días después de retirar su autorización existen, pero se corren a mano: todavía no hay un programador de tareas. Desde el día 90, la aplicación muestra lo guardado como borrado y nadie lo puede ver ni recuperar, aunque la tarea todavía no haya corrido. Mientras no exista el programador, MATU no trata datos reales.
- Renovar desde la aplicación la autorización cuando vence su revisión de los 12 meses.
- Avisos de insumos por notificación o por correo: en el piloto se prueban sin enviarse (los de la aplicación ya funcionan). Elegir desde la aplicación, en «Tu cuenta», si los recibes por correo o en un teléfono (MATU-55).
- Enviar correos solo a direcciones verificadas.
- Invitaciones, pedidos y pagos.
- Verificar tu email al crear la cuenta. Mientras no exista, si intentas registrarte con un email que ya tiene cuenta, MATU te lo dirá, y alguien podría registrar un email que no es suyo.
- Eliminar tu cuenta desde la aplicación. Mientras tanto, pídelo por el correo de la sección 10.

## 14. Leyes que aplican

> ADR-027 (27-10), aprobado por Jorge.

- Ley 19.628 sobre protección de la vida privada, con las modificaciones de la Ley 21.719 de protección de datos personales, que rigen plenamente desde el 1 de diciembre de 2026.
- Ley 19.496 sobre protección de los derechos de los consumidores, para pedidos y pagos cuando existan.
- Decreto 6 de 2021 del Ministerio de Economía (Reglamento de Comercio Electrónico) y Decreto 52 de 2024 (exclusión del derecho a retracto), para pedidos y pagos cuando existan.
- Ley 20.422 sobre igualdad de oportunidades e inclusión de personas con discapacidad. Por eso esta política está escrita para leerse en el teléfono.

# Política de privacidad de MATU

**Versión 0.9 · 21 de octubre de 2026 (21/10/2026) · revisada el 24/10/2026 con lo que hacen la cuenta, la sesión y el grupo**
**Estado:** borrador para el piloto académico. Todavía no sirve para tratar datos reales.
**Aprobación:** aprobada como borrador v0.9 por Jorge Espinoza (Product Owner) el 25/10/2026. La revisión la hizo el orquestador del equipo de agentes, por delegación. Se confirman los tres compromisos del texto: MATU no vende datos, borra de inmediato los datos reales que entren por error, y ejercer los derechos es gratis. Los [PENDIENTE] que quedan (contacto, plazos, proveedores y procedimiento ante filtraciones) se resuelven en la versión 1.0, antes de tratar datos reales.
**Identificador de versión en el sistema:** `0.9`
**Borrador ADR-027 (27-10):** las secciones que empiezan con esa nota adaptan el texto a los pedidos y pagos del ADR-027. No están aprobadas y no cambian la versión: `POLITICA_VERSION` sigue en `0.9` hasta que Jorge decida si se publican como una versión nueva (la revisión previa del analista normativo propone 0.10).

---

## En un minuto

- MATU te ayuda a organizar el cuidado de una persona mayor. Su parte principal es una ficha de relevo para quien te reemplaza.
- **Hoy MATU es un piloto académico y no guarda datos reales.** Si lo pruebas, usa nombres y datos inventados.
- MATU **no pide diagnósticos** ni datos médicos. Solo pide lo necesario para cuidar.
- La ficha se guarda cifrada. La ven solo las personas de tu grupo que tienen permiso y el relevo al que tú se la compartes, por el tiempo que tú elijas.
- MATU no usa publicidad ni analítica de terceros, y no vende datos.
- MATU nunca ve ni guarda los datos completos de tu tarjeta.
- Puedes pedir ver, corregir o borrar los datos. La sección 10 explica cómo.

---

## 1. Esto es un borrador del piloto académico

- MATU es un proyecto de título. Esta versión 0.9 es un borrador escrito para su piloto académico, y **todavía no la revisa un abogado**.
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
5. Calcular cuándo se acaba cada insumo y avisarte antes. *Todavía no disponible.*
6. Hacer pedidos y pagos de insumos. *Todavía no disponible.*
7. Cuidar la seguridad: registrar quién abrió la ficha, detectar accesos extraños y responder si hay una filtración.

**Cada uso se autoriza por separado.** Hoy MATU pide solo la autorización para la ficha de relevo. Antes de activar el cálculo de insumos, los pedidos o los avisos, te pediremos una autorización para cada uno.

MATU no usa los datos para publicidad ni los vende. Tampoco toma decisiones automáticas sobre las personas. La fecha en que se acaba un insumo es solo una estimación para avisarte.

## 4. Qué datos guardamos

### De ti

- **Tu nombre y tu email.** Para crear tu cuenta no pedimos nada más.
- **Tu email se guarda legible**, porque lo necesitamos para que entres y para escribirte. Lo protege la separación entre familias de la base de datos. Para iniciar sesión usamos además una huella del email que no permite recuperarlo.
- **Tu contraseña**, guardada transformada de una forma que no se puede revertir. Nadie en MATU puede leerla.
- **Los grupos a los que perteneces** y tu rol en cada uno.
- **Registros técnicos.** Por cada acción guardamos la fecha y hora, el tipo de acción sin su contenido, si resultó o no, cuánto tardó y un número interno que te identifica a ti y a tu grupo. En esos registros no guardamos tu email, tu contraseña, tus códigos de acceso, el nombre del grupo ni tu dirección IP.
- **Más adelante,** para frenar los intentos de entrar a la fuerza, usaremos tu dirección IP solo como un contador temporal de intentos por hora. *Todavía no disponible.*
- **Cuando des una autorización** para la persona que cuidas: la fecha y la hora, en qué calidad la diste, qué declaración viste y la versión de esta política. Si eres cuidadora o cuidador de hecho, también qué aviso viste: su identificador, su versión y una huella de su texto. Si registras la decisión de la propia persona, queda anotado que la registraste tú, en su presencia. No guardamos tu dirección IP ni tu navegador.

### Tu sesión

- Cuando entras, tu sesión dura 15 minutos.
- Si se bloquea tu cuenta o cambias tu contraseña, una sesión que ya estaba abierta en otro teléfono puede seguir activa hasta 15 minutos.
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
- Más adelante: qué insumos usa, cuánto usa y cuánto queda.

**El nivel de apoyo y la ficha son datos sensibles**, porque hablan de la salud y de la dependencia de la persona. Por eso los protegemos de forma especial.

### De otras personas que tú anotas

- **Relevo:** su nombre y su teléfono, qué campos le compartiste, hasta cuándo, el motivo y cuántas veces abrió la ficha.
- **"A quién llamar":** los nombres y teléfonos que escribas. Avísales que los anotaste.
- **Invitaciones a tu grupo:** el email o el teléfono de la persona invitada. *Todavía no disponible.*

### De tus pedidos

> Borrador ADR-027 (27-10), por aprobar por Jorge.

*Todavía no disponible.* Cuando existan los pedidos, guardaremos:

- Los productos que pediste, con su cantidad, su precio, el envío y el total.
- El comercio que preparó cada producto.
- La dirección de entrega.
- El pago: el monto cobrado y, si hubo, la devolución.

**Tus pedidos y el consumo de insumos de la persona que cuidas se tratan como datos sensibles**, con la misma protección que la ficha, porque pueden revelar algo de su salud o de su dependencia.

**Para los pedidos te pediremos una autorización expresa y aparte**, distinta de la de la ficha. Puedes retirarla igual de fácil que la diste.

[PENDIENTE: consulta legal sobre si los productos de un pedido son un dato relativo a la salud, y si el art. 16 bis, inciso 1, de la ley limita su tratamiento aunque haya autorización]

### Lo que MATU no pide

- Diagnósticos, nombres de enfermedades, medicamentos, recetas, exámenes ni fichas clínicas.
- El RUT de nadie.
- Copias de documentos. Si eres representante legal, guardamos solo una referencia al documento.
- Los datos de tu tarjeta.

**Un consejo para la ficha:** escribe qué ayuda, no qué enfermedad tiene. Por ejemplo: "se tranquiliza si bajas las persianas".

## 5. La autorización para usar los datos de la persona que cuidas

Para guardar la ficha necesitamos una autorización. Al dar de alta a la persona, eliges en qué calidad la das.

**La propia persona (titular).** La persona que cuidas decide por sí misma y tú registras su decisión. Al registrarla declaras:

> Declaro que la persona que cuido me dijo hoy, en persona, que autoriza a MATU a guardar su ficha de relevo y a compartirla con el relevo que elija el grupo, según la política de privacidad vigente. Yo solo registro su decisión.

**Su representante legal.** Tienes un nombramiento legal para representarla. Declaras:

> Declaro que soy representante legal de la persona que cuido y que la referencia que indico corresponde al documento que lo acredita. Como su representante, autorizo a MATU a guardar su ficha de relevo y a compartirla con el relevo que elija el grupo, según la política de privacidad vigente.

**Cuidadora o cuidador de hecho.** La cuidas en el día a día, pero no tienes un nombramiento legal para representarla. Declaras:

> Declaro que cuido a esta persona y que no soy su representante legal. Autorizo a MATU a guardar su ficha de relevo y a compartirla con el relevo que elija el grupo, según la política de privacidad vigente. Leí el aviso sobre el límite de esta autorización.

### Aviso para quien cuida sin ser representante legal

Este es el texto exacto que MATU muestra al elegir esta calidad. Su identificador en el sistema es `aviso_cuidador_de_hecho`, versión 1.0:

> **Aviso: tu autorización tiene un límite**
>
> Declaraste que cuidas a esta persona y que no eres su representante legal. Con esa declaración puedes organizar su cuidado en MATU, pero tu autorización no equivale a la de la propia persona ni a la de su representante legal. MATU no puede comprobar lo que declaras. Por eso deja registrado que la autorización la diste tú, como cuidadora o cuidador de hecho, con la fecha y la versión de la política.
>
> Te pedimos tres cosas: anota solo lo necesario para su cuidado, cuéntale qué guardas en MATU si puede comprenderlo, y respeta lo que ella decida. Ella o su representante legal pueden pedir en cualquier momento que se borren sus datos.
>
> En 12 meses te pediremos confirmar que sigues a cargo de su cuidado.

Su huella en el sistema (SHA-256) es `9b33205fd93e18b3eaac569071b794d21071a414ccc0d8bb5b89f9c96af3dfc9`.

Cada declaración también tiene un identificador en el sistema: `declaracion_titular`, `declaracion_representante_legal` y `declaracion_cuidador_de_hecho`. Su versión es la de esta política. Cambiar una sola palabra de una declaración o del aviso es publicar una versión nueva.

[PENDIENTE: qué pasa si no se confirma a los 12 meses. Está en consulta legal]

## 6. Quién ve los datos

> Borrador ADR-027 (27-10), por aprobar por Jorge. Cambian los párrafos de comercios, de quien reparte y de Transbank.

**Tu cuenta:** tu email lo ven solo tú y el equipo que opera MATU. Las personas de tus grupos ven tu nombre. [PENDIENTE: si también ven tu email, se define con la lista de miembros del grupo]

**El nombre del grupo:** lo ven las personas del grupo y el equipo que opera MATU.

**Tu grupo, según el rol de cada persona:**
- **Administrador y cuidador:** ven todo, incluida la calidad en que se dio la autorización, y pueden editar y compartir la ficha. La referencia al documento del representante legal no se muestra en la aplicación: queda guardada solo como respaldo.
- **Pagador:** ve el nombre y la dirección. Ve la ficha solo si le dan ese permiso.
- **Observador:** ve el nombre. Nunca ve la ficha.

**El relevo**, la persona que te reemplaza:
- Ve solo el nombre con que llaman a la persona y los campos que tú elegiste.
- Entra con un enlace y un PIN de 4 dígitos. El acceso vence en 24 horas, o en el plazo que elijas hasta un máximo de 30 días, y puedes cortarlo cuando quieras.
- Cada vez que abre la ficha queda registrado.
- Lo que el relevo lea puede anotarlo o fotografiarlo, y MATU no puede impedirlo. Comparte solo lo que necesita y por el tiempo justo.

**Comercios en convenio**, cuando existan los pedidos:
- Para saber si tienen los productos, MATU les pregunta solo por los productos y las cantidades, con una referencia que se crea al azar para cada pedido y no permite saber de quién es. Esa consulta no lleva tus datos, ni los de la persona que cuidas, ni la dirección.
- El comercio que prepara tu pedido ve solo sus productos, la referencia del pedido y el código de retiro. Si falta un producto y otro comercio lo reemplaza, ese comercio ve lo mismo, solo con lo que le toca preparar.
- **Ningún comercio ve un nombre**, ni el tuyo ni el de la persona que cuidas. Tampoco ven la ficha. **La dirección nunca llega al comercio.** MATU vende y emite la boleta, así que el comercio no necesita saber quién paga.
- Aun así, el convenio con cada comercio le exige confidencialidad y seguridad, como a quien trata datos por encargo.
- [PENDIENTE: consulta legal sobre si la referencia del pedido es un dato personal para el comercio]

**Quien reparte**, si en el futuro hay despacho: ve la dirección de entrega solo mientras lleva el pedido. Lo hace por encargo de MATU y con un contrato que le exige confidencialidad, seguridad y borrar los datos al terminar.

**Transbank**, cuando existan los pagos: el pago se hace en su página. MATU no ve el número de tu tarjeta ni su código. Solo guarda el resultado: el monto, el código de autorización, el tipo de tarjeta y sus últimos 4 dígitos. Puedes pagar con crédito o con débito, y funcionan igual: se cobra una sola vez el total que viste antes de pagar. Si hay una devolución, va a la misma tarjeta, y no te pedimos datos nuevos para hacerla. Durante el piloto los pagos ocurren solo en el ambiente de prueba de Transbank, sin cobros reales.

**El equipo de MATU:** para dar soporte ve los pedidos y los pagos. Sus herramientas no permiten leer la ficha ni el consumo de insumos.

**Proveedores de tecnología** que guardan o procesan datos por encargo de MATU: [PENDIENTE: proveedor de nube, de correo, de SMS y de registro de errores, con qué datos recibe cada uno]

**Autoridades:** solo cuando una ley o un tribunal lo exige.

## 7. Dónde se guardan los datos

- En los sprints 1 a 3, el sistema corre en los computadores del equipo y en un ambiente de prueba, siempre con datos inventados.
- [PENDIENTE: proveedor y país donde se alojarán los datos]
- Si los datos se guardan fuera de Chile, lo diremos aquí y aplicaremos lo que la ley exige para ese caso.

## 8. Cuánto tiempo guardamos los datos

- **Ficha de relevo y consumo de insumos:** mientras la autorización esté vigente y hasta 90 días después de que termine. Si pides borrarlos, los dejamos ilegibles de inmediato destruyendo su clave. [PENDIENTE: confirmar que una solicitud de borrado no espera los 90 días]
- **Copias de respaldo:** [PENDIENTE: plazo]. El borrado queda completo cuando vence la última copia que contiene la clave.
- **Registro de quién abrió la ficha:** 3 años.
- **Pedidos y comprobantes de entrega**, cuando existan: 2 años.
- **Pagos y boletas**, cuando existan: 6 años, por obligación tributaria.
- **Tu cuenta:** [PENDIENTE]
- **Registro de autorizaciones:** [PENDIENTE]
- **Accesos de relevo**, con el nombre y el teléfono del relevo: [PENDIENTE]
- **Registros técnicos del sistema:** [PENDIENTE]

## 9. Cómo protegemos los datos

- La conexión con MATU va cifrada.
- Cada campo de la ficha se cifra con una clave propia de cada persona cuidada. Esa clave está protegida por una clave maestra que se guarda fuera del servidor. [PENDIENTE: confirmar el servicio de custodia de claves]
- La base de datos separa a cada familia: una familia no puede ver los datos de otra, aunque la aplicación tenga un error.
- El registro de quién abrió la ficha no se puede modificar ni borrar.
- Los registros técnicos no guardan el texto de la ficha, ni tu email, ni contraseñas, ni códigos de acceso, ni enlaces de relevo, ni PIN, ni el nombre del grupo, ni tu dirección IP.
- El enlace de relevo se bloquea después de 5 PIN incorrectos.
- La aplicación no guarda la ficha en tu teléfono ni en tu navegador, y no usa analítica ni programas de terceros.

Ningún sistema es completamente seguro. Si algo falla, la sección 11 dice qué hacemos.

## 10. Tus derechos y cómo ejercerlos

Puedes pedir:
- **Ver** qué datos tenemos.
- **Corregir** un dato equivocado.
- **Borrar** los datos.
- **Oponerte** a un uso de los datos.
- **Recibir una copia** de los datos para llevarla a otro lugar.
- **Retirar una autorización.** Al retirarla, se cortan los accesos de relevo vigentes.

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

- Ficha cifrada y relevo con enlace y PIN: se están construyendo.
- Retirar una autorización desde la aplicación.
- Ver, descargar o borrar los datos desde la aplicación. Mientras tanto, por el correo de la sección 10.
- El recordatorio de los 12 meses.
- Cálculo de insumos, avisos, invitaciones, pedidos y pagos.
- Verificar tu email al crear la cuenta. Mientras no exista, si intentas registrarte con un email que ya tiene cuenta, MATU te lo dirá, y alguien podría registrar un email que no es suyo.
- Eliminar tu cuenta desde la aplicación. Mientras tanto, pídelo por el correo de la sección 10.

## 14. Leyes que aplican

- Ley 19.628 sobre protección de la vida privada, con las modificaciones de la Ley 21.719 de protección de datos personales, que rigen plenamente desde el 1 de diciembre de 2026.
- Ley 19.496 sobre protección de los derechos de los consumidores, para pedidos y pagos cuando existan.
- Ley 20.422 sobre igualdad de oportunidades e inclusión de personas con discapacidad. Por eso esta política está escrita para leerse en el teléfono.

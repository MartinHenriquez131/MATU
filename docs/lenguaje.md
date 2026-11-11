# MATU · Lenguaje y textos al usuario

**Versión 1.0 · 26 de octubre de 2026 (26/10/2026)** · historia MATU-30
**Estado:** borrador. Lo revisa Martín en MATU-31 y lo aprueba Jorge. Los textos marcados **[PENDIENTE DE JORGE]** no se usan hasta que él los apruebe.
**Decisiones de Jorge del 27-10 (MATU-09 y MATU-30):** aprobó el aviso al relevo (7.5), los dos nombres antes del PIN (7.1 y 7.4), la ayuda del teléfono (9) y las preguntas guía con el nombre de la persona (5.1 y 5.2). La sección 10 marca qué diferencias quedan resueltas.
**MATU-68 (08-11):** entran los textos que la app ya mostraba sin estar aquí: las secciones nuevas 25 (alta) y 26 (marco de la app), la 6.6 y filas en 5.4, 7.1, 7.3, 7.4, 7.5, 8, 9.1, 13.3, 15 y 18. Los del alta los revisó el analista normativo, y donde propuso un cambio va el texto propuesto. El alta ya no pide la dirección. Aprobados por Jorge el 08-11. La sección 24 queda para MATU-72.
**MATU-72 (08-11):** entra la sección 24, borrar los datos de la persona, con los ajustes A1, A2 y A3 del diseñador (A3: textos sin pronombre, porque MATU no guarda el género). La 22 precisa que después de un borrado no vuelve nada. Aprobados por Jorge el 08-11.
**MATU-59 (08-11):** entra la sección 27, el catálogo, y dos filas en 3.2 («escara» y «ostomía»). Los revisó el analista normativo. Aprobados por Jorge el 08-11.
**MATU-67 (09-11):** entra la sección 28, el aviso de versión nueva. Aprobados por Jorge el 09-11.
**MATU-75 (09-11):** entra la sección 29, la política de privacidad en la app y su aceptación al crear la cuenta. La 7.5 activa la frase del correo de contacto con cuidaconmatu@gmail.com, retira el párrafo «En la demo» y ya muestra el enlace a la política. La 3.1 permite «cookie» y «sesión» en la política. Aprobados por Jorge el 09-11.
**MATU-61 (11-11):** entra la sección 31, el pedido, con los textos de la especificación de pantallas v1.1 (sección 15). Con la decisión D10 de Jorge cambian la 21 (la lista nunca compra sola), la 23 («Compré» nunca hace un pedido) y la 27 («Agregar al pedido» en el catálogo). La 17 mantiene «El aviso nunca ofrece comprar.». La sección 30 es de MATU-84, en otra rama, y la 31 se renumera al fusionar si hace falta. Por aprobar por Jorge al fusionar.
**Fuentes:** resultados de las entrevistas (`docs/resultados-entrevistas.md`), arquitectura sección 10, política de privacidad v0.9, la demo aprobada (`Demo/src/`, rama `demo-web-viernes-30`) y el contrato de MATU-09 (`docs/api/`, rama `matu-09-contrato-api`).

---

## 1. Para qué sirve y quién lo usa

Este documento es la fuente de **todo texto que ve una persona en MATU**: etiquetas, preguntas, ejemplos, botones, avisos y mensajes de error. Si un texto no está aquí, se agrega aquí primero y después va a la pantalla.

| Quién | Para qué |
|---|---|
| Frontend (CLAUDE.md, agente 3) | Copia los textos tal cual. No inventa uno nuevo: si falta, lo pide al orquestador |
| MATU-12 · Completar la ficha | Etiqueta, pregunta guía y ejemplo de cada campo (sección 5) |
| MATU-13 · Conflicto de edición | Mensajes del 412 y del 428 (sección 6) |
| MATU-23 · Página del relevo | Un texto por estado del relevo (sección 7) |
| MATU-31 · Revisión cruzada | Contrasta los textos de la ficha con este documento |
| Analista normativo | Revisa que los avisos digan lo que exige la política de privacidad |
| Backend | El `detail` de un error RFC 7807 es para quien depura. La pantalla nunca lo muestra: se guía por `type` y muestra el texto de la sección 8 |

**Cómo se lee.** Las llaves marcan lo que se reemplaza al mostrar el texto: `{nombre_pila}` es el nombre con que llaman a la persona cuidada, `{nombre_comparte}` es el nombre de pila de quien compartió la ficha con el relevo (`nombre_pila_comparte` en la API), `{autor}` es quien guardó un campo, `{n}` es un número, `{fecha}` va en `DD/MM/AAAA` y `{hora}` en 24 horas (`HH:MM`). Las comillas latinas «» van tal cual en pantalla.

---

## 2. Tono

Una cuidadora cansada, con poco tiempo y desde un teléfono. Un relevo que abre la ficha por primera vez, con apuro, en una casa ajena. El texto tiene que servirles a las dos en una sola lectura.

1. **Español de Chile, neutro y en tú.** "Escribe el PIN", no "Escriba" ni "Ingrese". Sin chilenismos que no entienda alguien de otra región.
2. **Frases cortas.** Una idea por frase. Párrafos de dos o tres frases como máximo.
3. **Instructivo, no expediente.** La ficha cuenta cómo cuidar a alguien. No describe lo que le pasa a su cuerpo ni lo clasifica. Se pregunta por **apoyos**, no por funciones (arquitectura 10.3, "Lenguaje sobre el cuerpo"). Una ficha sirve como instrucciones para cuidar, no como un expediente.
4. **Sin términos clínicos ni jerga técnica.** "Se acaban en 6 días", no "stock proyectado". "Cortar el enlace", no "revocar el acceso". La sección 3 tiene la lista.
5. **Sin culpar a la persona.** Un error dice qué pasó y cómo seguir. "Ese PIN no es", no "PIN inválido". "Este enlace venció", no "Acceso denegado".
6. **El mismo verbo en el botón y en su confirmación.** "Cortar el enlace" y "Enlace cortado". "Guardar" y "«Su día» guardado" (demo, `DISENO.md` principio 6).
7. **Sin punto y coma**, igual que el resto de la documentación del proyecto. Se usa punto seguido.
8. **Formato de Chile.** Fechas `30/10/2026`, hora `18:05`, dinero en pesos enteros con punto de miles: `$69.000`.
9. **La persona cuidada se nombra por su nombre** (`{nombre_pila}`), no por una categoría.

---

## 3. Términos prohibidos

Ninguna pantalla, aviso, correo, mensaje de error ni ejemplo usa estos términos. Tampoco una pregunta guía de la ficha. **Esta sección es el único lugar del documento donde aparecen.**

### 3.1 Los cinco del backlog (MATU-30)

| Término prohibido | Por qué | Qué se dice en su lugar |
|---|---|---|
| diagnóstico | MATU no pide diagnósticos (política v0.9, "En un minuto"). Nombrarlo en la interfaz invita a escribir un dato de salud, que no se necesita para cuidar y aumenta lo que hay que proteger | "Lo que necesita", "los apoyos que necesita". En la ficha, nada: las preguntas guía no lo piden |
| conducta | Mira a la persona como un caso que se observa. La ficha la escribe alguien que la quiere | "Cómo está", "si se altera", "lo que le gusta", "lo que la calma" |
| incidente | Suena a informe de turno y a culpa. El relevo tiene que saber a quién llamar, no llenar un formulario | "Si algo pasa", "lo que pasó" |
| deterioro | Describe a la persona por lo que perdió. Además es una inferencia de salud | "Cambios", "necesita más apoyo que antes" |
| incontinencia | Nombrarla afecta la dignidad de la persona cuidada (arquitectura 10.3, "Lenguaje sobre el cuerpo") | Se pregunta por el apoyo: "apoyo para ir al baño", "cambio de pañal". En insumos, el nombre del producto: "pañal adulto", "protectores", "toallitas húmedas" |

**Excepción en los textos legales.** La política de privacidad dice que MATU **no pide** diagnósticos. Ese uso informa un límite y no invita a escribir el dato, así que se mantiene en los textos legales que apruebe Jorge. Ninguna otra pantalla lo copia.

**Excepción en la ayuda de la ficha (sección 14).** La ayuda que va bajo cada sección dice «No hace falta escribir diagnósticos ni enfermedades.» Igual que la política, nombra el diagnóstico solo para decir que MATU **no** lo pide, y está aprobada por Jorge. Es el único texto de la app que lo usa. Ningún otro lo copia, y ninguno lo usa para preguntar.

La política de privacidad también puede usar «cookie» y «sesión», porque tiene que informarlas. En la app se siguen evitando (3.2).

### 3.2 Otros que se evitan

Salen del análisis de las entrevistas, de la arquitectura y del contrato de MATU-09.

| Evitar | Por qué | Qué se dice |
|---|---|---|
| paciente | La persona no está en un hospital. La familia no es personal de salud | Su nombre, `{nombre_pila}`. En textos generales, "la persona que cuidas" |
| usuario, beneficiario | Jerga de sistema | "Tú". Para la persona cuidada, su nombre |
| adulto mayor (en la ficha y en avisos) | Es una categoría. La ficha habla de una persona concreta | Su nombre. En textos institucionales, "persona mayor", como la política |
| postrado, postrada | Reduce a la persona a su condición física | "Necesita apoyo en todo" (texto del alta en la demo) |
| demencia, Alzheimer y cualquier nombre de enfermedad | Dato de salud. MATU no lo pide ni lo sugiere en un ejemplo | Nada. La ficha pregunta qué hacer, no qué tiene |
| crisis, episodio, descompensación | Lenguaje clínico | "Si se altera", "cuando se angustia" |
| manejo de situaciones difíciles | Era el nombre técnico del campo 2. Las entrevistadas usaron otra expresión (arquitectura 10.4) | "Si se altera" |
| escara, úlcera, antiescaras | Lenguaje clínico, y describe una lesión de la persona | "Crema protectora de la piel" |
| ostomía, ostomizado | Lenguaje clínico, y revela una condición de salud | "Bolsa colectora" |
| stock, quiebre, stock proyectado | Jerga del equipo (arquitectura 10.3) | "Se acaban en 6 días", "Pronto se acaba" |
| revocar, revocado | Jerga legal y técnica | "Cortar el enlace", "Enlace cortado", "Cortado" |
| token, cookie, sesión, autenticar, credenciales, canje | Jerga técnica | "Enlace", "PIN", "entrar" |
| consentimiento (en botones y mensajes) | La política lo llama "autorización", y es la palabra que se entiende | "Autorización", "permiso" |
| auditoría, registro de accesos, log | Suena a vigilancia. Cinco de diez entrevistadas no mirarían esa pantalla (arquitectura 10.4) | "Quién la vio", "quién se está informando" |
| error 404, 410, 412 y cualquier código | El código no le dice nada a la persona | El texto de la sección 8 |
| inválido, denegado, rechazado, fallido | Culpan o suenan a máquina | "Ese PIN no es", "ya no está disponible" |

---

## 4. Palabras de las familias

Cómo nombraron las cosas las diez entrevistadas, y el término que usa MATU. Solo vocabulario cotidiano. No incluye condiciones de salud, citas textuales ni códigos de entrevista.

| Lo que dicen las familias | Dónde apareció | Lo que dice MATU |
|---|---|---|
| La hoja, el cuaderno, la pizarra, la planilla, la bitácora, las notas en el WhatsApp | Siete de diez tienen algo escrito, en uno de esos formatos (resultados, sección 2) | **Ficha** de relevo. La versión impresa es "la hoja" ("La ficha en una hoja, para pegar en el refrigerador") |
| La que llegue, la que me reemplaza, quien me cubre | Varias entrevistadas, y el bloque 3 del protocolo | En la app de la familia: "quien te reemplaza". En botones: "relevo" ("Compartir con un relevo"). Al relevo nunca se le dice "relevo": lee "ficha de cuidado" |
| Entrega de turno | La cuidadora remunerada entrevistada (arquitectura 10.6) | Ficha de relevo. "Entrega de turno" se entiende, pero viene del vocabulario clínico y no se usa en pantalla |
| Qué la calma, qué hacer cuando se angustia | Tres de diez entrevistadas, cada una por su cuenta | Campo **"Si se altera"**, pregunta "¿Qué calma a `{nombre_pila}`…?" |
| Un día bueno, un día malo | Una entrevistada se trabó al contar "un día normal" | La pregunta de **"Su día"** admite contar un día bueno o uno difícil |
| A quién llamo, la vecina que tiene llave | Bloque 3 del protocolo | Campo **"A quién llamar"** |
| Salir, no poder salir, salir unas horas | Nueve de diez dejaron de salir por falta de relevo | Motivos del enlace: "Salgo unas horas", "Fin de semana fuera", "Turno de noche" |
| Quién está mirando, quién se está informando | Cinco de diez entrevistadas valoran esa pantalla | "Quién la vio" (pestaña) y "Últimas aperturas" |
| Pañales, toallitas, cremas, protectores, suplemento | Pregunta 24 del protocolo | El nombre del producto tal como se vende: "Pañal adulto M", "Toallitas húmedas" |
| Que me avise antes, cuántos días quedan | Varias entrevistadas | "Se acaban en 6 días", "Pronto" |
| El súper, la farmacia, la app | Resultados, sección 2 | El nombre del comercio. En general, "comercio" solo en textos legales |
| La boleta | Una entrevistada | "Boleta" |
| Lo del consultorio, el beneficio, lo que entrega el municipio | Pregunta 27, padrón público | "Lo que recibes del consultorio" (capa 2, fuera de este sprint) |
| Poner la plata, el que aporta | La familiar aportante entrevistada | "Familiar que aporta" (arquitectura 10.1) |
| De quién es esto, de la familia o mío | Una entrevistada, sobre la propiedad del registro | Sin texto todavía: consulta legal abierta (arquitectura 18) |

---

## 5. Ficha de relevo

La ficha tiene tres campos. Cada uno acepta **hasta 500 caracteres** y se guarda por separado y cifrado (MATU-12, contrato decisión 2). Los textos vienen de `Demo/src/demo/datos.ts`, que los tomó del prototipo v1.1.

| Clave técnica (contrato) | Clave en la demo | Etiqueta visible |
|---|---|---|
| `rutina` | `su_dia` | **Su día** |
| `manejo_situaciones` | `si_se_altera` | **Si se altera** |
| `red_apoyo` | `a_quien_llamar` | **A quién llamar** |

### 5.1 Su día (`rutina`)

- **Pregunta guía:** ¿Cómo es un día normal para `{nombre_pila}`? Puedes contar un día bueno o uno difícil.
- **Ejemplo:** Por ejemplo: «08:00 Despierta. Le gusta que abran la cortina primero». Si empiezas con la hora, lo mostramos como línea de tiempo.

### 5.2 Si se altera (`manejo_situaciones`)

- **Pregunta guía:** ¿Qué calma a `{nombre_pila}` cuando se angustia?
- **Ejemplo:** Por ejemplo: «Le hace bien que le tomen la mano y le hablen de su pueblo».

### 5.3 A quién llamar (`red_apoyo`)

- **Pregunta guía:** ¿A quién llamar si algo pasa y no te ubican?
- **En el relevo:** ¿A quién llamar si algo pasa? Quien reemplaza no es quien escribió la ficha, así que la pregunta no le habla con «te» (decisión de Jorge del 09-11). En el editor de la familia queda la pregunta de arriba.
- **Ejemplo:** Por ejemplo: «Rodrigo, su hijo: +56 9 5555 0102».

Las preguntas guía nombran a la persona por su nombre y no usan femenino ni masculino, porque el modelo no guarda su género (aprobado por Jorge el 27-10). La demo del viernes 30 no cambia.

**Los ejemplos solo los ve quien escribe la ficha.** La página del relevo muestra la pregunta guía y nunca el ejemplo (decisión de Jorge del 09-11, que cambia la D2 del 28-10). En la demo, el «+56 9 5555 0102» aparecía justo debajo del teléfono real de «A quién llamar», y en un apuro el relevo podría llamar al número de ejemplo.

Los ejemplos son sintéticos: Carmen cuida a María, Rosa la reemplaza y Rodrigo es su hijo. Los teléfonos usan la serie `5555`, que no se asigna. Un ejemplo nunca nombra una enfermedad, un remedio ni una dosis.

### 5.4 Textos de la pantalla de la ficha

| Dónde | Texto |
|---|---|
| Título de la sección | Ficha de relevo |
| Bajada de la lista de campos · Cambiada por Jorge el 03-11 (ADR-028: los tres campos van siempre) | Tres campos cortos para que quien te reemplace sepa qué hacer. Cada campo se guarda por separado. |
| Avance | `{n}` de 3 campos listos |
| Estado de un campo con texto / sin texto | Listo / Falta |
| Botón de un campo sin texto / con texto | Completar «`{campo}`» / Editar «`{campo}`» |
| Quién lo escribió | Lo escribió `{autor}`: `{cuándo}` |
| Nota de seguridad **[desde MATU-11]** | Cada campo se guarda cifrado, por separado. No se muestra hasta que el cifrado exista (política v0.9, sección 13) |
| Encabezado del editor | Campo `{n}` de 3 |
| Contador | `{n}` de 500 caracteres |
| Botones del editor | Guardar · Dictar en vez de escribir · Seguir después |
| Mientras se dicta | Escuchando… |
| Botón para dejar de dictar (MATU-68) | Detener |
| Sin micrófono (MATU-68) | No pudimos usar el micrófono. Puedes escribir el texto. |
| Mientras se guarda | Guardando… |
| Vista previa | Así la ve quien te reemplaza · La hoja, mientras escribes |
| **Campo vacío** (en la hoja, para el relevo y en la vista previa) | **Sin completar** |

**Sin hoja impresa (ADR-029, 03-11):** la ficha no se imprime ni se exporta. Salieron de esta tabla los textos de la hoja impresa (la bajada, el botón «Imprimir», el pie y el campo vacío impreso). La hoja del refrigerador queda solo como el aspecto de la ficha en pantalla.

"Guardar" con un campo vacío que nunca se escribió no hace nada y no muestra mensaje (contrato, decisión 6). Vaciar un campo que ya tenía texto sí se guarda, y el campo vuelve a "Sin completar".

---

## 6. Mensajes de la ficha

### 6.1 Guardado

| Situación | Texto |
|---|---|
| Campo guardado (título) | «`{campo}`» guardado |
| Faltan campos | Vas en `{n}` de 3. Puedes seguir cuando quieras, no se pierde nada. |
| Ficha completa | La ficha está completa. |
| Botones después de guardar | Seguir con «`{campo siguiente}`» · Ver los campos · Compartir con un relevo · Volver al inicio |

### 6.2 Otra persona guardó el mismo campo (412, `version-desactualizada`)

La pantalla muestra el conflicto, nunca lo esconde (CLAUDE.md, agente 3). `{autor}` es `actual.actualizado_por.nombre` del 412. Si viene vacío, se dice "Otra persona".

| Parte | Texto |
|---|---|
| Título | `{autor}` guardó «`{campo}`» mientras escribías |
| Explicación | No guardamos lo tuyo encima de lo suyo. Elige qué versión dejar: la otra se descarta. |
| Versión guardada | La de `{autor}` · Guardada a las `{hora}` |
| Versión propia | La tuya · Lo que escribiste recién, sin guardar |
| Versión sin texto | Vacía |
| Botones | Dejar la de `{autor}` · Dejar la mía |
| Nota al pie | MATU no mezcla los textos solo. Si quieres, copia una parte antes de elegir. |
| Confirmación | Dejaste tu versión. / Dejaste la versión de `{autor}`. |

### 6.3 Falta la versión (428, `falta-version`)

No debería ocurrir: la pantalla siempre manda `If-Match` o `If-None-Match`. Si ocurre, es un defecto del cliente.

> **No pudimos guardar este campo.** Vuelve a abrirlo y guarda de nuevo. Lo que escribiste sigue aquí.

El texto escrito no se borra: la persona lo puede copiar antes de reabrir.

### 6.4 Sin autorización (403, `sin-consentimiento`)

> **Falta la autorización para usar la ficha de `{nombre_pila}`.** Sin ella no podemos guardar ni mostrar la ficha. La puede registrar quien administra el grupo o quien la cuida en MATU, desde Grupo familiar, en "Permiso para guardar su ficha".

Para admin y cuidador, la última oración («La puede registrar quien administra…») se reemplaza por "La puedes volver a autorizar desde Grupo familiar.", con el botón secundario **Volver a autorizar** (MATU-44, sección 22). Si quien lo ve tiene otro rol (pagador u observador), el texto termina en: "Pídele a quien administra el grupo que la registre."

Junto con 6.4b, son las dos causas de un 403 en la capa 1 (contrato, decisiones 4 y 33).

### 6.4b Autorización por renovar (403, `revision-vencida`) · Aprobado por Jorge el 28-10

Aparece cuando la autorización la registró quien la cuida sin ser su representante legal, y ya pasó un año sin renovarla. No es un error: es un aviso que ayuda a volver.

> **Hay que renovar la autorización de la ficha de `{nombre_pila}`.** Se renueva una vez al año. Mientras tanto, la ficha no se puede ver ni cambiar, pero lo que escribiste sigue guardado.
>
> Pídele a quien administra el grupo que la renueve.
>
> [Apoyos del Estado para quienes cuidan](https://www.chileatiende.gob.cl/fichas/112779-persona-cuidadora) (se abre en ChileAtiende)

- **El enlace** es la ficha oficial "Persona cuidadora" de ChileAtiende: explica cómo acreditarse como persona cuidadora y obtener la credencial. Se eligió por ser lo más útil para quien cuida (decisión de Jorge del 28-10).
- **El texto no dice que la credencial renueva la autorización**, porque no la renueva: la credencial da acceso preferente en instituciones públicas, pero no convierte a nadie en representante legal. Qué trámite equivale a ser representante legal está en la consulta legal.
- **[PENDIENTE]** Todavía no existe la pantalla para renovar la autorización. Cuando exista, para admin y cuidador la frase "Pídele a quien administra el grupo que la renueve" se cambia por el botón **Renovar la autorización**.
- **Vale igual en el relevo** (decisión de Jorge del 28-10): mientras no se renueve, no se crean accesos nuevos y un relevo con un enlace anterior tampoco abre la ficha. Cortar un acceso y ver la lista siguen permitidos.

### 6.5 Texto demasiado largo (422, `validacion`, `tipo: string_too_long`)

> Cada campo admite hasta 500 caracteres. Acorta un poco el texto para guardarlo.

### 6.6 Salir sin guardar y entrada vencida (MATU-68) · Aprobados por Jorge el 08-11

| Situación | Texto |
|---|---|
| Salir del editor con texto sin guardar | Lo que escribiste en «`{campo}`» no se guardó. ¿Salir igual? |
| Botones | Salir sin guardar · Seguir escribiendo |
| Bajo un error, con texto escrito | Lo que escribiste sigue aquí. Cópialo si lo quieres guardar en otra parte. |
| Entrada vencida con texto sin guardar | Tienes que volver a entrar. Copia lo que escribiste antes de seguir: no se guardó. |

---

## 7. El relevo (MATU-23)

La página pública `/r#<token>`, sin cuenta. Antes de escribir el PIN, la página muestra el nombre de pila de quien compartió y el de la persona cuidada, como en la demo (aprobado por Jorge el 27-10). Quien envía el enlace lo hace a su nombre, y un enlace que pide un PIN sin decir qué es no da confianza. Jorge acepta el riesgo: quien reciba un enlace reenviado ve los dos nombres de pila. El nombre de quien comparte se guarda en el acceso con una migración de MATU-18. La pantalla del PIN pide los dos nombres a `POST /v1/relevo/presentacion` con solo el token, que devuelve `nombre_pila_comparte` y `nombre_pila`. Esa ruta no cuenta como intento de PIN. Queda registrada, y la familia la ve en "Quién la vio" como "abrió el enlace" (contrato, decisión 30). Responde los mismos 410 y 423 de la sección 7.3. Después del canje, `GET /v1/relevo/ficha` trae `nombre_pila` y `nombre_pila_comparte` (contrato de MATU-09, decisión 28).

### 7.1 Encabezado y pantalla del PIN

| Parte | Texto |
|---|---|
| Encabezado | MATU · Ficha de cuidado compartida |
| Título | `{nombre_comparte}` te compartió la ficha de `{nombre_pila}` |
| Bajada | Escribe el PIN de cuatro números que te dictaron por teléfono. |
| Etiqueta del campo | PIN |
| Botón | Ver la ficha |
| Pie | No necesitas cuenta ni instalar nada. Al entrar, el enlace se borra de la barra de direcciones. |
| Título de la pestaña del navegador (MATU-68) | Ficha de cuidado compartida · MATU · En un estado que no abre: `{título del estado}` · MATU, sin el punto final del título |
| Mientras abre (MATU-68) | Abriendo el enlace… · Abriendo la ficha… (también en el botón, mientras revisa el PIN) |

### 7.2 La acción común

Todos los estados en que el enlace ya no abre terminan con la misma acción, en una nota con el título "¿Qué hago?":

> **Pídele a quien te envió el enlace uno nuevo.**

### 7.3 Un texto por estado

| Estado | `type` y status | Título | Texto | Acción |
|---|---|---|---|---|
| PIN de menos de 4 números | `/errores/validacion` 422 (no cuenta como intento) | — (mensaje bajo el campo) | El PIN tiene 4 números. Revisa que estén todos. | — |
| PIN incorrecto, quedan 2 o más | `/errores/pin-incorrecto` 401 | — (mensaje bajo el campo) | **Ese PIN no es.** Revisa los cuatro números que te dictaron. Te quedan `{intentos_restantes}` intentos. Después, el enlace se bloquea. | — |
| PIN incorrecto, queda 1 | `/errores/pin-incorrecto` 401 | — (mensaje bajo el campo) | **Ese PIN no es.** Revisa los cuatro números que te dictaron. Te queda 1 intento. Después, el enlace se bloquea. | — |
| Bloqueado | `/errores/relevo-bloqueado` 423 | Este enlace se bloqueó | El PIN se escribió mal cinco veces. Por seguridad, el enlace ya no abre. | Pídele a quien te envió el enlace uno nuevo. |
| Vencido | `/errores/relevo-vencido` 410 | Este enlace venció | Los enlaces de MATU duran un tiempo fijo, y el de esta ficha ya terminó. | Pídele a quien te envió el enlace uno nuevo. |
| Cortado | `/errores/relevo-revocado` 410 | Este enlace se cortó | Quien te compartió la ficha cortó el enlace, y ya no abre. | Pídele a quien te envió el enlace uno nuevo. |
| No disponible | `/errores/relevo-no-disponible` 410 | Este enlace no está disponible | Puede que se haya copiado incompleto o que ya no exista. Revisa que lo abriste completo desde el mensaje. | Pídele a quien te envió el enlace uno nuevo. |
| En pausa · Aprobado por Jorge el 04-11 (decisión 33) | `/errores/relevo-pausado` 410 | Por ahora esta ficha no se puede ver. | — (no dice el motivo a un tercero) | Pídele a quien te envió el enlace que lo revise. |
| Sin sesión | `/errores/sin-sesion-relevo` 401 | Vuelve a abrir el enlace | Por seguridad, la ficha se cierra después de un rato. Abre de nuevo el enlace que te enviaron y escribe el PIN. | — (el enlace sigue sirviendo) |
| Demasiados intentos desde la conexión | `/errores/demasiadas-peticiones` 429 | Espera un momento | Hubo muchos intentos de entrar desde esta conexión. Vuelve a intentarlo en `{minutos}` minutos. | — |

**Los minutos del 429 (MATU-68):** con 1 se escribe «Vuelve a intentarlo en 1 minuto.». Si la respuesta no trae `Retry-After`: «Vuelve a intentarlo en unos minutos.».

El mensaje del PIN se anuncia con `role="alert"` y deja el foco en el campo. Los títulos de los estados que no abren se anuncian al cargar. Un estado nunca se distingue solo por color: lleva ícono y título.

### 7.4 La ficha abierta

| Parte | Texto |
|---|---|
| Encabezado de la hoja | Ficha de cuidado de · `{nombre_pila}` |
| Vigencia | Puedes verla hasta el `{fecha}` a las `{hora}`. |
| Botón | Actualizar |
| Nota | Solo `{nombre_comparte}` puede cambiar esta ficha. |
| Campo compartido sin texto | Sin completar |
| Mientras actualiza (MATU-68) | Actualizando… |
| Después de actualizar (MATU-68) | Ficha actualizada a las `{hora}`. |
| Nombre accesible de la columna lateral (MATU-68) | Sobre esta ficha |

### 7.5 Aviso al relevo · Aprobado por Jorge el 27-10, ajustado el 03-11 (MATU-45: la familia ve el registro)

Aviso para el relevo como titular de su nombre y su teléfono. Va en la pantalla del PIN, antes del canje, bajo el botón, en texto secundario, con el enlace a la política. Es el texto final: se copia tal cual.

> MATU guarda tu nombre y tu teléfono, que anotó quien te compartió la ficha, para enviarte el enlace y poder contactarte. Tu teléfono se borra 30 días después de que el enlace vence o se corta. También registra cada vez que abres el enlace o la ficha y cada PIN incorrecto, con la fecha y la hora. La familia que te compartió la ficha puede ver ese registro con tu nombre. Lo guardamos 3 años. Responsables de tus datos: Jorge Espinoza y Martín Henríquez. Puedes pedir ver, corregir o borrar tus datos escribiendo a cuidaconmatu@gmail.com. [Política de privacidad]

El correo de contacto es el mismo de la política, sección 2, y se completa con la versión 0.11.

**Título y enlace (MATU-68, aprobados por Jorge el 08-11).** Sobre el aviso va el título «Tus datos en MATU», y el enlace a la política dice «Política de privacidad (se abre en otra pestaña)». La página parte el aviso en tres párrafos sin cambiar una palabra: el texto del aviso se sigue copiando tal cual. Desde MATU-75 la política tiene su página en la app, en /privacidad, y el enlace se muestra.

Fuentes: decisiones de Jorge del 27-10 (contrato de MATU-09), política v0.9, secciones 2, 4, 8 y 10, y figura legal del piloto, secciones 4.1 y 4.4.

---

## 8. Correspondencia `type` → texto al usuario

La pantalla elige el texto por `type` (y, en un 422, por `errores[].campo` y `errores[].tipo`). Nunca muestra `title`, `detail` ni `mensaje` de la API: el `mensaje` de un 422 hoy viene de Pydantic, en inglés (contrato, decisión 20).

| `type` | Status | Dónde | Texto al usuario |
|---|---|---|---|
| `/errores/no-autenticado` | 401 | App de la familia | Hace tiempo que no entrabas. Vuelve a entrar con tu correo y tu contraseña. |
| `/errores/token-invalido` | 401 | App de la familia | Hace tiempo que no entrabas. Vuelve a entrar con tu correo y tu contraseña. |
| `/errores/sin-consentimiento` | 403 | Ficha | Sección 6.4 |
| `/errores/revision-vencida` | 403 | Ficha | Sección 6.4b |
| `/errores/no-encontrado` | 404 | App de la familia | No encontramos lo que buscas. Puede que ya no tengas acceso. Vuelve al inicio. |
| `/errores/version-desactualizada` | 412 | Ficha | Sección 6.2 |
| `/errores/validacion` | 422 | Ficha, `string_too_long` | Sección 6.5 |
| `/errores/validacion` | 422 | Ficha, `vacio_sin_crear` | Sin texto: la pantalla no envía un campo vacío que nunca se escribió |
| `/errores/validacion` | 422 | Canje, `pin` | El PIN tiene 4 números. Revisa que estén todos. |
| `/errores/validacion` | 422 | Compartir, `expira_en`, `vigencia_maxima` | El enlace puede durar como máximo 30 días. |
| `/errores/validacion` | 422 | Compartir, `telefono_relevo` | Escribe un celular de Chile, por ejemplo +56 9 5555 0137. |
| `/errores/validacion` | 422 | Compartir, `nombre_relevo` | Escribe el nombre de quien te reemplaza. |
| `/errores/validacion` | 422 | Compartir, `relevo_informado` | Marca que le avisaste a `{nombre}` para crear el enlace. |
| `/errores/validacion` | 422 | Compartir, `seccion_no_agregada` | Otra persona quitó una sección mientras compartías. Revisa qué más puede ver y vuelve a crear el enlace. |
| `/errores/falta-version` | 428 | Ficha | Sección 6.3 |
| `/errores/pin-incorrecto` | 401 | Relevo | Sección 7.3 |
| `/errores/sin-sesion-relevo` | 401 | Relevo | Sección 7.3 |
| `/errores/relevo-vencido` | 410 | Relevo | Sección 7.3 |
| `/errores/relevo-revocado` | 410 | Relevo | Sección 7.3 |
| `/errores/relevo-no-disponible` | 410 | Relevo | Sección 7.3 |
| `/errores/relevo-pausado` | 410 | Relevo | Sección 7.3 |
| `/errores/relevo-bloqueado` | 423 | Relevo | Sección 7.3 |
| `/errores/demasiadas-peticiones` | 429 | Relevo | Sección 7.3 |
| `/errores/demasiadas-peticiones` | 429 | Entrar | Sección 13.3, «Varios intentos fallidos» |
| `/errores/demasiadas-peticiones` | 429 | Crear cuenta | Sección 13.3, «Muchos intentos desde la conexión» |
| `/errores/demasiadas-peticiones` | 429 | Recuperar el acceso y verificar el celular (demora por intentos con el código y límites de envío, no el límite por IP) | Sección 19 |
| `/errores/validacion` | 422 | Crear cuenta, `email`, `dominio_no_permitido` (solo staging) | Sección 13.3 |
| Cualquier otro, o sin respuesta | 5xx o red | Toda la app | No pudimos completar esto. Revisa tu conexión y vuelve a intentarlo. Lo que escribiste sigue aquí. |

El 404 de la familia no dice si el recurso existe en otro grupo: un recurso de otro grupo responde 404, nunca 403 (CLAUDE.md, agente 2).

**En la página del relevo (MATU-68).** El texto de «Cualquier otro» se parte en título, «No pudimos completar esto.», y texto, «Revisa tu conexión y vuelve a intentarlo.». Va sin «Lo que escribiste sigue aquí.», porque quien abre el enlace no escribió nada. El botón dice «Volver a intentar» (sección 26).

**Sin acceso a la ficha, en la app de la familia (MATU-68):** No tienes acceso a la ficha de `{nombre}`. Si la necesitas, pídeselo a quien administra el grupo.

---

## 9. Compartir y enlaces (MATU-18 y MATU-20)

Textos de la demo, con los cambios que pide el contrato de MATU-09.

| Dónde | Texto |
|---|---|
| Bajada de Compartir · Aprobada por Jorge el 04-11 (el envío ya no es solo por WhatsApp) | Quien te reemplaza recibe un enlace en un mensaje y el PIN se lo dictas tú. El enlace vence solo y lo puedes cortar antes. |
| Preguntas del formulario | ¿Quién te va a reemplazar? · Su teléfono · ¿Hasta cuándo? · ¿Cuántos días? (Hasta 30 días.) Qué ve se elige con el selector de la sección 14.2 (desde MATU-50, «¿Qué puede ver?» se retira) |
| Ayuda del teléfono · Aprobado por Jorge el 27-10 | Para enviarle el enlace y poder contactarle. |
| Recordatorio bajo el selector de secciones · Versión neutra aprobada por Jorge el 04-11 | Comparte solo lo que necesita para cuidar a `{nombre_pila}`. Quien recibe el enlace puede anotar o fotografiar lo que lee, y MATU no puede impedirlo. |
| Recordatorio al crear el enlace | Cuéntale a `{nombre}` que anotaste su nombre y su teléfono en MATU, y que cada vez que abra el enlace o la ficha queda registrado. |
| Motivo (obligatorio, uno elegido de partida) | ¿Para qué lo compartes? · Salgo unas horas · Fin de semana fuera · Turno de noche · Otro motivo |
| PIN recién creado | **Díctaselo a `{nombre}` por teléfono.** No lo mandes junto con el enlace. Solo lo verás ahora. |
| PIN que ya no se ve | El PIN ya no se puede ver. Por seguridad se muestra una sola vez. Si se perdió, crea un enlace nuevo y corta el anterior. |
| Estados de un enlace (`vigente`, `vencido`, `revocado`, `bloqueado`) | Activo · Vencido · Cortado · Bloqueado |
| Detalle de bloqueado | Se bloqueó porque el PIN se escribió mal cinco veces. |
| Botón y confirmación | Cortar el enlace de `{nombre}` · Enlace cortado. Ya no abre para `{nombre}`. |
| Bajada de Enlaces · Aprobada por Jorge el 04-11 | Al cortar un enlace deja de abrir de inmediato. Si quien lo tenía estaba mirando la ficha, se cierra cuando vuelva a mirarla. Quien lo tenía no recibe aviso. En la tarjeta de un enlace: «Si `{nombre}` tenía la ficha abierta, se cierra cuando vuelva a mirarla.» |
| Sin enlaces | No hay enlaces todavía. Crea uno desde Compartir. |
| Bajada de Quién la vio · Aprobado por Jorge el 27-10 | Una línea por cada vez que alguien abre el enlace o la ficha, o escribe mal el PIN. Es un respaldo para ti, no una vigilancia. |
| Aperturas (`presentacion`, `apertura`, `pin_incorrecto`, `bloqueo`) | `{nombre}` abrió el enlace · `{nombre}` abrió la ficha · `{nombre}` escribió mal el PIN · El enlace de `{nombre}` se bloqueó por PIN incorrecto |
| Sin aperturas | Todavía nadie ha abierto la ficha. Cuando alguien la abra, aparece aquí. |


### 9.1 Compartir y enlaces en la app de la familia (MATU-48) · Aprobados por Jorge el 04-11

Salen de la revisión previa del analista normativo y de la especificación `docs/diseno/matu-48-compartir.md` (MATU_PROYECTO). El enlace se envía con la hoja de compartir del teléfono o copiándolo, nunca con el token en la dirección de un servicio de terceros, y nunca con el PIN.

| Dónde | Texto |
|---|---|
| Pestañas | Compartir · Enlaces |
| Vigencias | 24 horas · Fin de semana · Otra cantidad de días |
| Ayuda del nombre | Basta con su nombre de pila. |
| Casilla obligatoria (decisión 34 del contrato) | Le avisé a `{nombre}` que MATU guarda su nombre y su teléfono para enviarle la ficha. |
| Casilla sin marcar | Marca que le avisaste a `{nombre}` para crear el enlace. |
| Vigencia antes de crear | Vence el `{DD/MM/AAAA}` a las `{HH:MM}`. |
| Fecha que ya pasó | Esa fecha ya pasó. Elige de nuevo hasta cuándo. |
| Botón y espera | Crear enlace · Creando el enlace… |
| Vista previa | Lo que verá `{nombre}` · sin nombre escrito: Lo que verá quien te reemplaza |
| Enlace creado | Enlace creado para `{nombre}` · PIN para abrir la ficha |
| Envío | Enviar el enlace · Copiar el enlace |
| Mensaje que acompaña el enlace (sin el PIN) | Hola, `{nombre}`. Te comparto la ficha de cuidado en MATU: `{url}`. El PIN te lo digo por teléfono. |
| Copiado | Enlace copiado. Pégalo en tu mensaje a `{nombre}`. |
| No se pudo copiar | No pudimos copiar el enlace. Usa «Enviar el enlace». |
| Después de crear | Ver los enlaces · Crear un enlace nuevo |
| Grupos de la lista | Abren ahora · Ya no abren |
| Ningún enlace activo | Ningún enlace abre ahora. |
| Estado de un enlace | Activo, vence en `{restante}` («45 min», «23 h», «3 días») · Lo creó `{nombre}`. Vence el `{fecha}` a las `{hora}`. · Venció el `{fecha}` a las `{hora}`. · Lo cortaron el `{fecha}` a las `{hora}`. |
| Cortando | Cortando… |
| Error al cortar | No pudimos cortar el enlace. Revisa tu conexión y vuelve a intentarlo. El enlace todavía abre. |
| Error al listar | No pudimos traer los enlaces. Revisa tu conexión e inténtalo de nuevo. |
| Paginación | Ver enlaces anteriores |
| Llamar al relevo (admin y cuidador) | Llamar a `{nombre}` |
| Teléfono ya borrado (después de 30 días) | Ya no guardamos su teléfono. |
| Autorización por renovar, en Enlaces (decisión 33) | Aviso: Mientras no se renueve la autorización, ningún enlace abre. Cuando se renueve, vuelven a abrir los que no hayan vencido. · En cada enlace vigente: En pausa (con ícono, en vez de «Activo») · La autorización retirada está en la sección 22 |
| Ver las aperturas de un enlace | Ver cuándo la abrió |
| Nombre accesible del enlace creado | Enlace para `{nombre}` |
| Al cargar más enlaces | Se agregó 1 enlace. · Se agregaron `{n}` enlaces. |
| Servicio no disponible (503) | MATU no está disponible en este momento. Vuelve a intentarlo en unos minutos. |
| Nombre accesible de las pestañas | Vistas de Compartir |
| Campos vacíos al compartir (MATU-68) | `{campo}` está vacío: `{nombre}` verá «Sin completar». · Con más de uno: `{campo}`, `{campo}` y `{campo}` están vacíos: `{nombre}` verá «Sin completar». |
| Junto al campo de «¿Cuántos días?» (MATU-68) | días |
| En Quién la vio, bloque «Quién puede verla ahora» (MATU-68) | vence en `{restante}` |
| En Quién la vio | Nadie tiene un enlace activo ahora. · Si te preocupa, puedes cortarlo desde Enlaces. · Ver todo en Quién la vio |

---

## 10. Diferencias entre la demo y el contrato que resuelve el equipo

La demo del viernes 30 no se modifica. Al conectarla a la API, o al construir MATU-12 y MATU-23, se resuelve esto:

| # | Demo | Contrato o este documento | Quién decide |
|---|---|---|---|
| 1 | La pantalla del PIN dice "Carmen te compartió la ficha de María", y la ficha abierta dice "Carmen te la compartió" y "Solo Carmen puede cambiar esta ficha" | `POST /v1/relevo/presentacion` devuelve los dos nombres con solo el token, y `GET /v1/relevo/ficha` trae `nombre_pila_comparte` (contrato, decisión 28) | **Resuelto por Jorge el 27-10:** se muestran los dos nombres antes del PIN y "Solo `{nombre_comparte}` puede cambiar esta ficha" después (secciones 7.1 y 7.4). La demo coincide. La migración va en MATU-18 |
| 2 | Un solo estado "Este enlace ya no está disponible" para vencido, cortado y bloqueado | Cuatro textos (sección 7.3), como pide MATU-23 | Ya resuelto aquí |
| 3 | Mensaje del PIN con un punto y coma antes de "después el enlace se bloquea" | "Te quedan `{n}` intentos. Después, el enlace se bloquea." | Ya resuelto aquí |
| 4 | El `detail` del 410 revocado en el contrato dice "Pídele uno nuevo si lo necesitas" | La acción del backlog es "Pídele a quien te envió el enlace uno nuevo". La pantalla no muestra `detail`, pero conviene alinear el ejemplo del contrato | Martín, en el contrato |
| 5 | Ayuda del teléfono: "Para enviarle el enlace." | La API no envía nada (contrato, decisión 21). Texto propuesto en la sección 9, pendiente de la finalidad del teléfono | **Resuelto por Jorge el 27-10:** el teléfono es obligatorio, para enviarle el enlace desde el teléfono de quien comparte y poder contactarlo. MATU no envía mensajes. Ayuda aprobada en la sección 9 |
| 6 | "Motivo, si quieres", tres chips que se pueden desmarcar | Motivo obligatorio con "Otro motivo" y sin texto libre | Ya resuelto aquí |
| 7 | Estado "Activo" calculado en el cliente | `estado = vigente` de la API, que se muestra como "Activo" | Ya resuelto aquí |
| 8 | Las preguntas guía hablan en femenino ("para ella", "qué la calma") | La persona cuidada no tiene género en el modelo. Alternativa neutra: "¿Cómo es un día normal para `{nombre_pila}`?" y "¿Qué calma a `{nombre_pila}` cuando se angustia?" | **Resuelto por Jorge el 27-10:** las preguntas guía usan `{nombre_pila}` (secciones 5.1 y 5.2). La demo del viernes no cambia |
| 9 | El texto que la demo dicta en "Si se altera" insinúa una condición de salud de María | Los ejemplos de este documento no lo hacen (sección 5). El dictado de la demo no se copia a la app | Jorge, si quiere cambiar el dictado después del viernes |
| 10 | Los documentos de las entrevistas no seguían los códigos del protocolo, sección 6 | Este documento no usa códigos de entrevista | **Resuelto por Jorge el 27-10:** los documentos de las entrevistas usan los códigos E01 a E10 del protocolo, sin iniciales ni edades exactas |
| 11 | Demo: "Cada campo se guarda cifrado" y "se guarda protegido" | No se dice "cifrado" hasta que MATU-11 exista (política v0.9, sección 13). Marcado **[desde MATU-11]** en la sección 5.4 | Ya resuelto aquí |
| 12 | Demo: "Sirve sin conexión y sin aplicación" en la hoja impresa | La ficha no se imprime ([ADR-029](adr/ADR-029-ficha-no-se-imprime.md)). La demo no se copia a la app | **Resuelto por Jorge el 03-11** |

**Para la tarjeta de consulta legal en Trello:**

- **Resuelto:** el motivo del enlace es obligatorio y se elige de una lista cerrada, sin texto libre (contrato, decisión 16). Así no puede guardar un dato de salud.
- **Resuelto:** la política v0.9 ya dice que se registran los PIN incorrectos y los bloqueos (secciones 4, 6 y 9, ajustadas el 27-10). El aviso al relevo (7.5) también lo dice.

---

## 11. Textos del piloto académico

La figura legal del piloto (sección 4.1) pide un aviso visible en todas las pantallas y toma su texto exacto de aquí. Coinciden con la demo (`DISENO.md` y `Demo/src/`).

| Dónde | Texto | Regla |
|---|---|---|
| Distintivo, en todas las pantallas de las tres apps y en la página del relevo | **Piloto académico con datos de prueba** | Visible siempre, también en modo presentación y con texto al 200%. No se abrevia. En pantallas angostas se parte en dos líneas: "Piloto académico / con datos de prueba" |
| Lista de insumos, pedido y boleta | **Precios de ejemplo.** MATU todavía no tiene convenio con comercios, y en esta demo no se cobra dinero real. | Una vez por pantalla, nunca junto al botón principal |
| Pasarela de pago simulada | Pasarela de pago simulada · Transbank, ambiente de prueba. **Pago de prueba. No se cobra dinero real.** | En la pasarela, que no usa la marca de MATU |
| Primera mención de un comercio en una pantalla | `{nombre}` (comercio ficticio) | Por ejemplo, "Farmacia Los Aromos (comercio ficticio)" |

Al pasar a datos reales, con la política 1.0, estos textos se retiran o se cambian, y se actualiza esta sección.

---

## 12. Cómo se cambia este documento

- Un texto nuevo o cambiado entra aquí en el mismo pull request que la pantalla que lo usa.
- Un término nuevo en la lista prohibida lo propone cualquiera y lo aprueba Jorge.
- Un aviso legal o un texto que informa sobre datos personales pasa antes por el analista normativo.
- Si este documento contradice la política de privacidad, manda la política y se corrige este documento.

---

## 13. Insumos, entrada y dispositivos (MATU-32, MATU-36 y MATU-38) · Aprobados por Jorge el 02-11 y el 03-11

En la app se dice "entrar", nunca "sesión" (decisión de Jorge del 02-11). Los textos marcados [PROPUESTO] están en `docs/diseno/matu-36-insumos.md` (MATU_PROYECTO) y se aprueban con la pantalla.

### 13.1 Cuánto alcanza

| Caso | Texto |
|---|---|
| Quedan varios días | Alcanza para {n} días |
| Queda un día | Alcanza para 1 día |
| Cero días | Se acaba hoy |
| El cálculo da negativo | Puede que ya no quede |
| Nota bajo la fecha | Es un cálculo con lo que anotaste. Si compraste o te quedan menos, anótalo con «Compré» o «Me quedan». (MATU-51) |
| Ayuda del nombre del insumo | Por ejemplo: «Toallitas húmedas». Sin remedios ni para qué se usa |
| Botón de descartar un aviso (MATU-37) | Ya lo resolví |

### 13.2 La autorización para calcular insumos

Son las tres declaraciones de la política de privacidad, en la sección 5, "La autorización para calcular insumos", con sus identificadores `declaracion_consumo_<calidad>`. Se copian sin cambiar una palabra: cambiarlas es publicar una versión nueva de la política.

Si no se elige quién da el permiso, el error dice: «Elige quién da el permiso.» (08-11, igual que en el alta, 25.4).

### 13.3 Entrar y dispositivos

| Dónde | Texto |
|---|---|
| Entrada vencida (`sesion-expirada`, `no-autenticado`, `token-invalido`) | Hace tiempo que no entrabas. Vuelve a entrar con tu correo y tu contraseña. |
| Varios intentos fallidos (429) | Hubo varios intentos de entrar. Espera {minutos} minutos. · enlace: Recupera tu cuenta (MATU-57, aprobado por Jorge el 03-11) |
| Muchos intentos desde la conexión (429 del límite por IP de MATU-25), solo al crear la cuenta. Recuperar el acceso y verificar el celular conservan sus textos de la sección 19 (corregido el 05-11) | Título: Espera un momento · Texto: Hubo muchos intentos desde esta conexión. Vuelve a intentarlo en {minutos} minutos. Con 1: «en 1 minuto». Los minutos salen de `Retry-After` redondeados hacia arriba (aprobado por Jorge el 05-11, P2-1 de la prueba en el teléfono) |
| Correo de un dominio no permitido, solo en staging (`errores[].tipo = dominio_no_permitido`, decisión 105) | Bajo el campo del correo: En este ambiente de prueba usa un correo terminado en @example.com. (aprobado por Jorge el 05-11, P3-1 de la prueba en el teléfono) |
| Entrar sin correo o sin contraseña (MATU-68) | Escribe tu correo y tu contraseña. |
| Después de salir (MATU-68) | Saliste de MATU. Para volver, entra con tu correo y tu contraseña. |
| El correo o la contraseña no coinciden (MATU-68) | El correo o la contraseña no coinciden. Revísalos y vuelve a intentarlo. |
| Título de la pantalla de dispositivos | Dónde entraste |
| El dispositivo actual | Este teléfono |
| Último uso | Última vez: {fecha} a las {hora} |
| Botón | Cerrar en ese teléfono |
| Aviso push (MATU-41) | MATU: un insumo se está acabando. Abre la app para ver cuál |

---

## 14. Ficha ampliada (MATU-49, ADR-028) · Aprobados por Jorge el 03-11

Los textos de 14.3 están en `docs/diseno/matu-49-ficha-ampliada.md` (MATU_PROYECTO) y se aprueban en este PR.

### 14.1 Las seis secciones

| Sección | Título | Pregunta guía | Ejemplo |
|---|---|---|---|
| `quien_es` | Quién es | ¿Qué le gustaría que supiera de esta persona alguien que recién la conoce? | Por ejemplo: «Le dicen Tito. Fue profesor de música en Talca. Su nieta Sofía le visita los domingos y tiene un gato, el Pelusa.» |
| `preferencias` | Lo que le hace bien | ¿Qué le alegra, le entretiene o le calma? | Por ejemplo: «Le gustan los boleros y conversar de fútbol. Ve las noticias a las 9 de la noche.» |
| `alimentacion` | Comer y beber | ¿Qué le gusta comer y cómo se le sirve? | Por ejemplo: «Toma té con poca azúcar. Prefiere la comida picada en trozos chicos y el pan blando.» |
| `movilidad` | Moverse y descansar | ¿Cómo se le ayuda a moverse, levantarse y descansar? | Por ejemplo: «Camina con bastón dentro de la casa. Para levantarse, ofrécele el brazo derecho. Duerme siesta después de almuerzo.» |
| `comunicacion` | Cómo hablarle | ¿Qué ayuda a que se entiendan? | Por ejemplo: «Usa audífono en el oído izquierdo. Háblale de frente y despacio. Si algo le molesta, se toca la frente.» |
| `remedios` | Sus remedios | ¿Qué remedios toma y a qué hora, tal como se los da la familia? | Por ejemplo: «8:00 con el desayuno: 1 pastilla blanca de la caja azul. 20:00: 1 pastilla de la caja verde.» |

La pregunta guía y el ejemplo no se muestran en la página del relevo.

### 14.2 Ayudas, avisos y compartir

| Dónde | Texto |
|---|---|
| Bajo cada sección | No hace falta escribir diagnósticos ni enfermedades. Escribe lo que ayuda a cuidar. |
| Comer y beber, y Sus remedios | Si tiene alergia a algún remedio o alimento, anótalo aquí. |
| Sus remedios, siempre visible (también al relevo) | Esto lo escribe la familia. No reemplaza la indicación del médico. |
| Contador | {n} de 500 caracteres · {n} de 800 caracteres |
| Compartir, casilla (siempre sin marcar) | Incluir Sus remedios |
| Compartir, ayuda de la casilla | Quien te reemplaza verá qué remedios toma y a qué hora. Márcalo solo si va a dárselos o a estar a cargo de ellos. |
| Compartir, confirmación | Vas a compartir sus remedios con {nombre} hasta el {DD/MM/AAAA}. Puedes cortar el acceso cuando quieras. |

### 14.3 Textos de la pantalla · Aprobados por Jorge el 03-11

| Dónde | Texto |
|---|---|
| Ficha, título del bloque | «Más sobre `{nombre_pila}`» |
| Ficha, bajada | «Si quieres, cuenta más para que quien te reemplace conozca a `{nombre_pila}`. Agrega solo lo que te sirva, cuando tengas tiempo.» |
| Ficha, lo agregado | «Agregaste 1 sección.» · «Agregaste `{n}` secciones.» |
| Ficha, encabezado de las no agregadas | «Puedes agregar» |
| Ficha, botones | «Agregar «`{título}`»» (nombre accesible) · «Editar «`{título}`»» |
| Ficha, vista previa | «Cada relevo ve solo las secciones que eliges al compartir.» |
| Editor, sobre el título | «Más sobre `{nombre_pila}`» |
| Guardado, primera vez | «Agregaste «`{título}`».» |
| Guardado, cambio | «Guardamos «`{título}`».» |
| Guardado, con accesos vigentes | «Quien ya tiene un enlace no la verá. Para que la vea, crea un enlace nuevo.» |
| Quitar, botón | «Quitar «`{título}`»» |
| Quitar, pregunta | «¿Quitar «`{título}`»?» |
| Quitar, texto | «Se borra lo que escribiste en esta sección. Quien tenga un enlace dejará de verla. No se puede deshacer.» |
| Quitar, botones | «Quitar y borrar» · «Dejarla como está» |
| Quitar, en curso | «Quitando…» |
| Quitar, hecho | «Quitaste «`{título}`».» |
| Quitar, 404 | ««`{título}`» ya no estaba en la ficha.» |
| Quitar, 412 | «`{autor}` cambió «`{título}`» mientras la ibas a quitar» · «Esta es la versión que guardó `{autor}`:» · «Quitarla igual» · «Dejarla como está» |
| Compartir, base | «Siempre ve» · «Su día, Si se altera y A quién llamar.» |
| Compartir, secciones | «¿Qué más puede ver?» · «Elige las secciones que le sirven.» |
| Compartir, confirmación | «Sí, crear el enlace» · «No incluir sus remedios» |
| PIN y Enlaces | «Ve su día, si se altera, a quién llamar, `{secciones en minúscula}`.» · «Si agregas una sección después, `{nombre}` no la verá. Para que la vea, crea un enlace nuevo.» |

Revisados contra los términos prohibidos (diagnóstico, conducta, incidente, deterioro, incontinencia): «diagnósticos» aparece solo en la ayuda aprobada, como lo que **no** se pide. Ningún texto asume el género de la persona cuidada ni de quien usa la app.

---

### 14.4 Conflictos y errores de las secciones (MATU-50) · Aprobados por Jorge el 03-11

| Dónde | Texto |
|---|---|
| Guardar cuando otra persona quitó la sección, título | Otra persona quitó «`{sección}`» mientras escribías |
| Ídem, texto | Lo que escribiste no se guardó. Puedes agregarla de nuevo con tu texto. |
| Ídem, botones | Agregarla de nuevo · Dejarla quitada |
| Ídem, al pie | Si quieres, copia lo que escribiste antes de elegir. |
| Ídem, al confirmar | Agregaste «`{sección}`». · Dejaste «`{sección}`» quitada. |
| Texto demasiado largo (422) | Esta sección admite hasta `{tope}` caracteres. Acorta un poco el texto para guardarlo. |
| «Dejarla como está» en el conflicto al quitar | Dejaste «`{sección}`» como la guardó `{autor}`. |

## 15. Quién la vio (MATU-45) · Aprobados por Jorge el 03-11

| Dónde | Texto |
|---|---|
| Bajada | Una línea por cada vez que alguien abre el enlace o la ficha, o escribe mal el PIN. Es un respaldo para ti. |
| Volver | Volver a la ficha |
| Enlace abierto sin abrir la ficha (solo si después no hubo otro evento de ese enlace) | Todavía no abre la ficha. Puede que no haya escrito el PIN aún, o que el enlace le haya llegado a otra persona. (Con MATU-48 se agrega: Si te preocupa, puedes cortarlo desde Enlaces.) |
| Enlace bloqueado | Ya no abre con ese enlace. Si fue un error al escribir, crea uno nuevo y díctale el PIN de nuevo. |
| Error | No pudimos traer quién la vio. Revisa tu conexión e inténtalo de nuevo. |
| Paginación | Ver aperturas anteriores · Se agregaron {n} líneas. · No hay más. |
| Nota final | La ficha se guarda cifrada. |
| Fechas | Hoy · Ayer · El {día} (hasta 6 días) · El DD/MM/AAAA, con hora de 24 h de Chile |
| En la ficha, bloque de aperturas (MATU-68) | Últimas aperturas · Ver todo en Quién la vio (de la sección 9.1) |

## 16. Insumos para quien solo lee (MATU-36) · Aprobado por Jorge el 03-11

| Dónde | Texto |
|---|---|
| Cómo calculamos, observador y pagador | Dividimos lo que quedaba por lo que se usa, y contamos los días desde que la familia lo anotó. Si compraron y no lo anotaron, no lo sabe. Tampoco sabe si cambió lo que usa {pila}. (MATU-51) |
| Nota corta, observador y pagador | Es un cálculo con lo que anotó la familia. |

## 17. Avisos de insumos (MATU-37) · Aprobados por Jorge el 03-11

En la app se dice «se acaba», nunca «quiebre». La fecha es una estimación. El aviso nunca ofrece comprar.

| Dónde | Texto |
|---|---|
| Bloque | Se acaban pronto · Se acaban pronto ({n}) (con más de 3) |
| Nota del bloque | Admin y cuidador: Es una estimación con lo que anotaste. · Pagador y observador (MATU-51, aprobado por Jorge el 07-11): Es una estimación con lo que anotó la familia. |
| Marca en la lista | Te estamos avisando |
| Botón (solo admin y cuidador) | Ya lo resolví |
| Panel | Con envase conocido (MATU-51): ¿Compraste? ¿Cuántos envases? · Si no compraste, déjalo en 0 y solo dejamos de avisarte. · Junto al campo: envase de {u} unidades / envases de {u} unidades (sección 21). Sin envase: ¿Compraste? ¿Cuántos? / ¿Cuántos sobres? / ¿Cuántos ml? / ¿Cuántos gramos? · Si no compraste, déjalo en blanco y solo dejamos de avisarte. En los dos: Guardando… · Volver |
| Con cantidad | Anotamos tu compra de {nombre}: {cantidad}. Ahora alcanza para {n} días. (1 día en singular). Desde MATU-51, {cantidad} se arma como en la sección 21: «2 envases de 20 unidades», «24 unidades», «1 sobre», «500 ml» |
| Con cantidad, si sigue en 0 o menos | Anotamos tu compra de {nombre}: {cantidad}. Si te quedan menos, cámbialo en la lista. |
| Sin cantidad | Listo. No te avisaremos de nuevo por {nombre} hasta que cambie la fecha estimada. |
| Otra persona cambió el insumo antes de resolver (412) | {autor} cambió «{nombre}» mientras lo resolvías. Revisa cómo quedó y vuelve a intentarlo. · Ver cómo quedó |
| Ya resuelto por otra persona (409) | Alguien de tu familia ya resolvió este aviso. · Ver cómo quedó |
| Aviso que ya no existe (404) | Este aviso ya no está. Puede que el insumo se haya cambiado o eliminado. |
| Sin permiso | Solo quien administra o cuida puede resolver un aviso. |
| Cantidad inválida | Con envase: Escribe un número de 0 a 99. Si no compraste, déjalo en 0. · Sin envase: Escribe un número de 1 a 10.000, o déjalo en blanco. (MATU-51) |
| Más de 100.000 o más de 10 años (MATU-51) | Con esa compra quedarían más de 100.000 {unidades / sobres / ml / g}. Revisa cuántos compraste. · Con esa compra alcanzaría para más de 10 años. Revisa cuántos compraste. |
| Error al guardar | No pudimos guardar. Revisa tu conexión y vuelve a intentarlo. |
| Error al cargar | No pudimos ver qué se acaba pronto. |
| Lista, singular | Queda 1 hoy · Quedan {n} hoy |

## 18. Pantalla de Insumos (MATU-36) · Aprobados por Jorge el 03-11

Complementa la sección 13 (lo central ya aprobado: «Alcanza para {n} días», «Se acaba hoy», «Puede que ya no quede», la ayuda del nombre y las declaraciones). El texto completo vive en `web/src/familia/textosInsumos.ts` (MATU_PROYECTO) y en `docs/diseno/matu-36-insumos.md`.

| Parte | Textos |
|---|---|
| Permiso | Antes de calcular, un permiso · Es un permiso aparte del de su ficha. · Permiso guardado. Ahora anota el primer insumo. · No pudimos guardar el permiso. Revisa lo que elegiste y vuelve a intentarlo. · Falta el permiso para calcular los insumos de {nombre}. · Sin él no podemos mostrar cuándo se acaban. Pídele a quien administra el grupo o a quien cuida a {nombre} que lo registre. · Hay que renovar la autorización de los insumos de {nombre}. · Se renueva una vez al año. Mientras tanto, no podemos calcular ni mostrar sus insumos, pero lo que anotaste sigue guardado. |
| Lista | Cargando los insumos… · Ver más · Anotar un insumo · Cambiar · Cómo calculamos · Dividimos lo que quedaba por lo que se usa, y contamos los días desde que lo anotaste. Si compraste o cambió lo que queda, anótalo con «Compré» o «Me quedan». No sabe si cambió lo que usa {nombre}. (MATU-51) · hasta el {fecha} · Según lo anotado, se acababa el {fecha} · Usa {n} al día. · Usa {n} cada {d} días. · Quedaban {n} el {fecha} · Queda 1 hoy. / Quedan {n} hoy. · Todavía no hay insumos anotados · Cuando alguien de tu grupo anote uno, aparece aquí. |
| Títulos y vacío (MATU-68, aprobados por Jorge el 08-11) | Títulos de los formularios: Anotar un insumo · Cambiar un insumo · Sin insumos, para admin y cuidador: Aún no sabemos qué usa {pila} · Cuéntanos de un solo producto, el que más te preocupa. Con eso ya te podemos avisar antes de que se acabe. |
| Formulario | Cambiar lo anotado · Volver a los insumos · ¿Qué insumo es? · ¿Cómo se cuenta? · Se cuenta por unidad. / por sobre. · ¿Cada cuánto se usa? · ¿Cada cuántos días? · ¿Cuántos usa {nombre} al día? / cada {d} días? · ¿Cuántos quedan hoy, más o menos? · El {fecha} anotaste {n}. Escribe cuántos quedan hoy, o déjalo en blanco si no lo sabes. · ¿Con cuántos días de anticipación te avisamos? · Si pones 0, te avisamos el mismo día. · Así, alcanza para {n} días, hasta el… · Así, se acaba hoy. · No había cambios. · Guardamos «{nombre}». |
| Validación y errores | Escribe el nombre del insumo. · Escribe cuántos usa, al menos 1. · Escribe un número hasta 10.000. · Escribe un número de 2 a 90. · Escribe cuántos quedan. Si no queda nada, escribe 0. · Escribe un número hasta 100.000. · Escribe un número de 0 a 60. · El nombre admite hasta 60 caracteres. Acórtalo un poco. · Escribe el nombre en una sola línea. · Con esos números alcanzaría para más de 10 años. Revisa cuánto queda y cuánto se usa. · Ese producto no se puede seguir en MATU. · Ese producto ya está anotado. Búscalo en la lista y cámbialo ahí. · No pudimos guardar. Revisa los datos y vuelve a intentarlo. · Ya no se está siguiendo este insumo. · Alguien desmarcó «Seguir» mientras lo cambiabas. Para cambiarlo, vuelve a marcar «Seguir» en la lista. · No pudimos guardar este insumo. · Vuelve a abrirlo y guarda de nuevo. Lo que escribiste sigue aquí. |
| Conflicto | {autor} cambió «{nombre}» mientras lo cambiabas · No guardamos lo tuyo encima de lo suyo. Elige qué dejar. · Lo que guardó · Lo tuyo, sin guardar · (cambió) · Guardar lo mío · Dejar lo que guardó · Dejaste lo que guardó {autor}. |
| Seguir y eliminar | Seguir · Sin seguir · No calculamos ni avisamos mientras no lo sigues. · Dejaste de seguir «{nombre}». Lo anotado sigue guardado. · Volviste a seguir «{nombre}». Si cambió cuánto queda, anótalo. · ¿Eliminar «{nombre}»? · Se borra todo lo anotado de este insumo y no se puede recuperar. · Si solo quieres dejar de calcularlo por un tiempo, desmarca «Seguir». · Eliminar · Eliminando… · Eliminaste «{nombre}». |

---

## 19. Recuperar el acceso y confirmar el celular (MATU-57) · Aprobados por Jorge el 03-11

En la app se dice «correo» y «entrar», nunca «email» ni «sesión». La respuesta al pedir un código es siempre la misma, exista o no la cuenta. Con `{minutos}` igual a 1 se escribe en singular: «1 minuto».

| Pantalla | Textos |
|---|---|
| Entrar | ¿Olvidaste tu contraseña? · Hubo varios intentos de entrar. Espera {minutos} minutos. · Recupera tu cuenta · Listo. Cambiamos tu contraseña. Por seguridad, tendrás que volver a entrar en tus otros teléfonos y computadores. |
| Recuperar | Volver a entrar · Recupera tu cuenta · Escribe tu correo y te enviaremos un código para crear una contraseña nueva. · Enviar código · Enviando… |
| Código | Si hay una cuenta con ese correo, te enviamos un código. Puede tardar un minuto. · Volver · Escribe el código · Te lo enviamos por mensaje al celular o al correo. Tiene 6 números. · Código · Nueva contraseña · Cambiar contraseña · Cambiando… · El código tiene 6 números. |
| Reenvío y errores | ¿No te llegó? · Pide que te lo enviemos a tu correo · Si hay una cuenta con ese correo, te enviamos un código nuevo al correo. Puede tardar un minuto. · Puedes pedir otro en un minuto. · El código no es correcto o ya venció. Pide uno nuevo. · Hubo varios intentos con ese código. Pide uno nuevo en {minutos} minutos. |
| Tu cuenta | Tu cuenta · Tus datos para entrar a MATU. · Tu correo · Tu celular · Confirmado · Sin confirmar · Confirmar celular · Tu cuenta todavía no tiene un celular. · Volver a tu cuenta |
| Confirmar el celular | Confirma tu celular · Si algún día olvidas la contraseña, te enviaremos un código a este número para que puedas volver a entrar. · ¿Cómo prefieres recibir los códigos? · Mensaje de texto (SMS) · WhatsApp · Enviar código · Enviando… · Ahora no · Te enviamos un código al {celular oculto}. · Confirmar · Confirmando… · ¿No te llegó? Enviar otro código · Listo. Tu celular quedó confirmado. · Ir a la ficha · Ya pediste varios códigos. Espera {minutos} minutos y vuelve a intentarlo. · No pudimos enviar el mensaje ahora. Vuelve a intentarlo en unos minutos. |
| Mensajes (simulados en el semestre) | MATU: tu código es {código}. Vence en 10 minutos. No lo compartas con nadie; MATU nunca te lo pedirá por teléfono. · MATU: se cambió la contraseña de tu cuenta. Si no fuiste tú, pide un código para recuperar tu acceso. |

---

## 20. Avisos por correo y push (MATU-41) · Aprobados por Jorge el 04-11

El correo y el push nunca dicen qué insumo ni de quién, no ofrecen comprar y su enlace no lleva identificadores ni token. En el piloto se prueban sin enviarse.

| Dónde | Texto |
|---|---|
| Correo, remitente | MATU |
| Correo, asunto | MATU: un insumo se está acabando |
| Correo, cuerpo | Un insumo se está acabando. Abre la app para ver cuál. |
| Correo, botón o enlace (sin identificadores) | Abrir MATU |
| Correo, pie | Te llega este correo porque eres parte de un grupo de cuidado en MATU. Para dejar de recibir estos avisos por correo, entra a MATU y desactívalos en Tu cuenta. |
| Push, título y cuerpo | MATU · Un insumo se está acabando. Abre la app para ver cuál. |
| Preferencias en «Tu cuenta» (pantalla en MATU-55) | Avisos cuando un insumo se está acabando · Por correo · En este teléfono |

---

## 21. Lista de insumos (MATU-60) · Aprobados por Jorge el 06-11

En la app se dice «lista de insumos», nunca «lista de reposición» ni «quiebre». La cantidad es una sugerencia: lo que falta para cubrir 30 días, descontando lo que MATU calcula que queda. La lista nunca compra sola. Solo quien tiene la autorización de pedidos puede tocar "Pedir estos productos". El texto que se imprime o se comparte no lleva los días que quedan ni el nombre de la persona (ADR-031).

| Dónde | Texto |
|---|---|
| Título de la pantalla | Lista de insumos |
| Pestañas de la sección Insumos | Insumos · Lista de insumos |
| Nombre de las pestañas, para el lector | Vistas de Insumos |
| Título de la pestaña del navegador | Lista de insumos · MATU (al imprimir: Lista de insumos) |
| Título impreso y primera línea del texto compartido | Lista de insumos · {DD/MM/AAAA} |
| Bajada | Lo que se acaba pronto, con una cantidad sugerida para 30 días. Puedes cambiarla antes de imprimir o compartir. |
| Bajada, observador | Lo que se acaba pronto, con una cantidad sugerida para 30 días. |
| Línea, en pantalla | {nombre} · {cantidad} · Alcanza para {n} días / Alcanza para 1 día / Se acaba hoy / Puede que ya no quede |
| Línea agregada a mano, en pantalla | Solo en esta pantalla |
| Cantidad, con envase conocido | {n} envases de {u} unidades / 1 envase de {u} unidades (con sobres, ml o g: «de {u} sobres», «de {u} ml», «de {u} g». Con {u} igual a 1: «de 1 unidad», «de 1 sobre») |
| Cantidad, sin envase | {n} unidades / {n} sobres / {n} ml / {n} g (con 1: «1 unidad», «1 sobre») |
| Cantidad, agregado a mano | {n} unidades / {n} sobres / {n} envases (con 1: «1 unidad», «1 sobre», «1 envase») |
| Etiqueta del campo | Cantidad |
| Botones del campo, para el lector | Menos: Cantidad de {nombre} · Más: Cantidad de {nombre} |
| Cantidad fuera de rango | Escribe una cantidad de 1 a 100.000. |
| Nota del cálculo | Es una sugerencia con lo que anotaste, y ya descuenta lo que queda. Cambia la cantidad si necesitas otra. |
| Nota del cálculo, pagador | Es una sugerencia con lo que anotó la familia, y ya descuenta lo que queda. Cambia la cantidad si necesitas otra. |
| Nota del cálculo, observador | Es una sugerencia con lo que anotó la familia, y ya descuenta lo que queda. |
| Agregar a mano | Agregar otro insumo · Por ejemplo: «Toallitas húmedas». Sin remedios ni para qué se usa · Esto queda solo en esta pantalla. No lo guardamos. |
| Agregar a mano, cómo se cuenta | ¿Cómo se cuenta? (de la sección 18) · Unidades · Sobres · Envases |
| Agregar a mano, botón | Agregar |
| Agregar a mano, anuncio | Agregamos «{nombre}» a la lista. |
| Quitar una línea | Quitar de la lista · Para el lector: Quitar de la lista: {nombre} |
| Quitar, anuncio, línea de MATU | Quitamos «{nombre}» de la lista. Sigue en Insumos. |
| Quitar, anuncio, línea agregada a mano | Quitamos «{nombre}» de la lista. |
| Después de quitar una línea de MATU | Lo que quitaste sigue en Insumos. Vuelve a esta lista cuando entras de nuevo. |
| Sin líneas, después de quitarlas todas | Quitaste todo de la lista. Si quieres, agrega uno a mano. |
| Aviso, siempre visible sobre los botones | La lista no lleva el nombre de {pila}, pero sí lo que usa. Lo que imprimas o compartas sale de MATU y no podemos borrarlo. Compártela solo con quien va a comprar. |
| Botones | Imprimir o guardar en PDF · Compartir la lista · Copiar la lista |
| Copiada | Copiamos la lista. Pégala donde quieras. |
| No se pudo copiar | No pudimos copiar la lista. Usa «Compartir la lista». |
| No se pudo copiar, sin Compartir en el navegador | No pudimos copiar la lista. Usa «Imprimir o guardar en PDF». |
| No se pudo compartir | No pudimos abrir Compartir. Usa «Copiar la lista». |
| Sin insumos | No hay insumos que se acaben pronto. Si quieres, agrega uno a mano. |
| Sin insumos, observador | No hay insumos que se acaben pronto. |
| Observador | Quien administra, cuida o paga puede imprimirla o compartirla. |
| Error al cargar | No pudimos traer la lista. Revisa tu conexión e inténtalo de nuevo. |
| Sin autorización o revisión vencida | Los textos de «Permiso» de la sección 18 |
| Pie del texto compartido y de la impresión | Piloto académico con datos de prueba |
| Al imprimir cualquier otra pantalla de la app | Esta pantalla no se imprime. |
| Campo nuevo en el formulario del insumo (opcional) | ¿Cuántas unidades trae cada envase? · Ayuda: Si lo anotas, la lista sugiere envases enteros. Puedes dejarlo en blanco. |
| Campo del envase, fuera de rango | Escribe un número de 1 a 10.000, o déjalo en blanco. |
| Campo del envase, en el conflicto (412) | Cada envase trae {u} {unidades / sobres / ml / g} (con 1: «1 unidad», «1 sobre»). · Sin unidades por envase. |

Formato exacto del texto compartido (sin enlace, sin los días y sin el nombre de la persona ni del grupo):

```
Lista de insumos · 06/11/2026
- Pañal adulto talla M: 6 envases de 20 unidades
- Toallitas húmedas: 120 unidades
- Toallitas para el baño: 2 envases
Piloto académico con datos de prueba
```

## 22. Retirar una autorización (MATU-44) · Aprobados por Jorge el 06-11

En la app se dice «autorización» y «retirar», nunca «consentimiento» ni «revocar». El botón y la confirmación usan el mismo verbo. Los números de enlaces y las fechas los da la API, la pantalla no los calcula.

| Dónde | Texto |
|---|---|
| Barra de secciones | Grupo familiar · corto: Grupo |
| Grupo familiar, título y bajada | Grupo familiar · A quién cuidan en `{nombre del grupo}` y qué permisos dieron. |
| Grupo familiar, bloque de la ficha | Permiso para guardar su ficha · Autorizada el `{fecha}`. · Retirar la autorización |
| Grupo familiar, bloque de los insumos | Permiso para calcular sus insumos · Autorizado el `{fecha}`. · Retirar la autorización |
| Bloque, por renovar | Autorizada el `{fecha}`. Hay que renovarla desde el `{fecha_revision}`. · Insumos: Autorizado el `{fecha}`. Hay que renovarlo desde el `{fecha_revision}`. |
| Insumos sin autorización todavía | Sin permiso todavía. Se pide al anotar el primer insumo. |
| Nombre accesible de los botones | Retirar la autorización de la ficha de `{nombre_pila}` · Retirar la autorización de los insumos de `{nombre_pila}` · Volver a autorizar la ficha de `{nombre_pila}` · Volver a autorizar los insumos de `{nombre_pila}` |
| Error al cargar Grupo familiar | No pudimos traer los permisos. Revisa tu conexión e inténtalo de nuevo. · Intentar de nuevo |
| Confirmación de la ficha, título | ¿Retirar la autorización de la ficha de `{nombre_pila}`? |
| Confirmación de la ficha, texto | Nadie del grupo podrá ver ni cambiar su ficha. · Se cortan ahora todos sus enlaces de relevo. Hoy abren `{n}`. (Con 1: «Hoy abre 1.» Con 0: «Hoy ningún enlace abre.») Si alguien tiene la ficha abierta, se le cierra cuando vuelva a mirarla. No recibe aviso. · Un enlace cortado no vuelve a abrir, aunque autorices de nuevo. · Lo escrito queda guardado sin que nadie lo vea. Si no vuelves a autorizar en 90 días, se borra. · La autorización de los insumos no cambia. |
| Confirmación de la ficha, autorización por renovar | En lugar de «Hoy abren `{n}`.»: Hoy están en pausa `{n}`. (Con 1: «Hoy está en pausa 1.» Con 0: «Hoy ningún enlace abre.») |
| Confirmación de los insumos, título | ¿Retirar la autorización de los insumos de `{nombre_pila}`? |
| Confirmación de los insumos, texto | Dejamos de calcular cuándo se acaban y de avisar, desde ahora. Tampoco avisamos al resto del grupo. · Nadie del grupo podrá ver los insumos anotados. · Lo anotado queda guardado sin que nadie lo vea. Si no vuelves a autorizar en 90 días, se borra. · Una lista que ya imprimiste o compartiste no se borra: quedó fuera de MATU. · Su ficha y los enlaces de relevo no cambian. |
| Botones | Retirar la autorización · No retirar |
| En curso | Retirando… |
| Hecho, ficha | Autorización retirada. Cortamos `{n}` enlaces. (Con 1: «Autorización retirada. Cortamos 1 enlace.» Con 0: «Autorización retirada. No había enlaces que abrieran.») |
| Hecho, insumos | Autorización retirada. Ya no calculamos ni avisamos por los insumos de `{nombre_pila}`. |
| Error de conexión | No pudimos retirar la autorización. Revisa tu conexión y vuelve a intentarlo. Todo sigue como estaba. |
| Ya la retiró otra persona | Otra persona de tu grupo ya retiró esta autorización. |
| Grupo familiar, después del retiro | Autorización retirada el `{fecha}`. Si no vuelves a autorizar, lo guardado se borra el `{fecha_borrado}`. · Volver a autorizar |
| Grupo familiar, ya borrado | Autorización retirada el `{fecha}`. Lo guardado se borró el `{fecha_borrado}`. · Volver a autorizar |
| Pagador y observador, debajo del estado | Vigente o por renovar: Puede retirarla quien administra el grupo o quien cuida a `{nombre_pila}`. · Retirada o borrada: Puede volver a autorizarla quien administra el grupo o quien cuida a `{nombre_pila}`. |
| Pagador y observador, después del retiro | Autorización retirada el `{fecha}`. Si nadie vuelve a autorizar, lo guardado se borra el `{fecha_borrado}`. |
| Ficha sin autorización (6.4), admin y cuidador | Termina en: La puedes volver a autorizar desde Grupo familiar. · Volver a autorizar |
| Volver a autorizar, enlace de vuelta | Volver a Grupo familiar |
| Volver a autorizar la ficha, frase de estado | Dentro de los 90 días: Al autorizar de nuevo, vuelve lo que estaba escrito. Los enlaces que se cortaron no vuelven a abrir. · Después: Lo escrito antes se borró el `{fecha_borrado}`. La ficha empieza en blanco. |
| Volver a autorizar la ficha, botón | Acepto y vuelvo a autorizar · Autorizando… |
| Volver a autorizar los insumos, frase de estado | Dentro de los 90 días: Si vuelves a dar el permiso antes del `{fecha_borrado}`, vuelve lo que estaba anotado. · Después: Lo anotado antes se borró el `{fecha_borrado}`. Hay que anotar los insumos de nuevo. |
| Volver a autorizar, errores | No pudimos guardar la autorización. Revisa lo que elegiste y vuelve a intentarlo. · Otra persona de tu grupo ya volvió a autorizar. |
| Volver a autorizar, hecho | Ficha: Autorización registrada. Ya puedes ver y cambiar la ficha de `{nombre_pila}`. · Ficha después de los 90 días: Autorización registrada. La ficha de `{nombre_pila}` empieza en blanco. · Insumos: Permiso guardado. Volvió lo que estaba anotado. · Insumos después de los 90 días: Permiso guardado. Ahora anota el primer insumo. |
| Enlaces, autorización retirada | Título: Se retiró la autorización de la ficha. · Cuerpo: Los enlaces se cortaron y no vuelven a abrir. · Ver los permisos en Grupo familiar |

**Reglas de armado:** si no se pudieron contar los enlaces, se omite «Hoy abren `{n}`.». Si la persona no tiene autorización de insumos, se omite «La autorización de los insumos no cambia.». El caso de la autorización retirada en Enlaces sale de la sección 9.1 y queda en esta tabla.

**Después de un borrado (MATU-72):** lo que dice «vuelve lo que estaba escrito» o «vuelve lo que estaba anotado» vale solo para un retiro. Si se borraron los datos de la persona (sección 24), no vuelve nada: la persona sale de MATU y no hay autorización que volver a dar. Para cuidarla con MATU de nuevo hay que registrarla otra vez, y todo empieza en blanco.

## 23. Anotar una compra o lo que queda (MATU-51) · Aprobados por Jorge el 07-11

En la app se dice «Compré» y «Me quedan», nunca «reposición», «reponer» ni «stock». Lo que se anota con «Compré» se llama **«compras anotadas»** en los textos, en las tarjetas y en el código. «Compré» habla de lo que la familia ya hizo: "Compré" anota lo que la familia ya compró, y nunca hace un pedido. La fecha la pone MATU (hoy) y la familia no la elige. Los días y la fecha de la confirmación los da la API.

| Dónde | Texto |
|---|---|
| Botones de cada insumo (solo admin y cuidador) | Compré · Me quedan |
| Nombre accesible de los botones | Compré: {nombre} · Me quedan: {nombre} |
| Compré, pregunta | Con envase conocido: ¿Cuántos envases compraste? · Sin envase: ¿Cuántos compraste? / ¿Cuántos sobres compraste? / ¿Cuántos ml compraste? / ¿Cuántos gramos compraste? |
| Compré, ayuda | Lo sumamos a lo que calculamos que queda hoy. |
| Compré, cantidad junto al campo | La de la sección 21 («envase de {u} unidades», «envases de {u} unidades»), y sin envase la de la sección 18 («unidades», «sobres», «ml», «g») |
| Compré, botón | Anotar la compra |
| Me quedan, pregunta | ¿Cuántos quedan hoy, más o menos? (de la sección 18) |
| Me quedan, ayuda | Reemplaza lo que calculábamos. Si no queda nada, escribe 0. |
| Me quedan, botón | Anotar lo que queda |
| En curso y cerrar | Guardando… · Volver (de la sección 17) |
| Compra anotada | Compra anotada para «{nombre}»: {cantidad}. Ahora alcanza para {n} días, hasta el {fecha}. (Con 1: «1 día». Con 0: «Compra anotada para «{nombre}»: {cantidad}. Así, se acaba hoy.» Negativo: «… Según lo anotado, puede que ya no quede.») |
| Lo que queda, anotado | Anotamos lo que queda de «{nombre}»: {cantidad}. Alcanza para {n} días, hasta el {fecha}. (Con 1: «1 día». Si se acaba hoy: «Anotamos lo que queda de «{nombre}»: {cantidad}. Así, se acaba hoy.») |
| Lo que queda, con 0 | Anotamos que no queda «{nombre}». Cuando compres, anótalo con «Compré». |
| Compré, falta la cantidad | Escribe cuántos envases compraste, al menos 1. · Escribe cuántos compraste, al menos 1. |
| Compré, sobre el tope | Con envase: Escribe un número de 1 a 99 envases. · Sin envase: Escribe un número hasta 10.000. (de la sección 18) |
| Compré, lo que queda pasaría de 100.000 | Con esa compra quedarían más de 100.000 {unidades / sobres / ml / g}. Revisa cuántos compraste. |
| Me quedan, falta o sobre el tope | Escribe cuántos quedan. Si no queda nada, escribe 0. · Escribe un número hasta 100.000. (de la sección 18) |
| Más de 10 años | Compré: Con esa compra alcanzaría para más de 10 años. Revisa cuántos compraste. · Me quedan: Con esa cantidad alcanzaría para más de 10 años. Revisa cuántos quedan. |
| El insumo ya no está (404) | Este insumo ya no está. Puede que alguien de tu familia lo haya eliminado. |
| Dejaron de seguirlo (409) | Alguien de tu familia dejó de seguir «{nombre}» mientras lo anotabas. No anotamos nada. Si quieres anotarlo, vuelve a marcar «Seguir». · Ver cómo quedó |
| Otra persona lo cambió (412) | {autor} cambió «{nombre}» mientras lo anotabas. Revisa cómo quedó y vuelve a intentarlo. · Ver cómo quedó |
| Errores generales | No pudimos guardar. Revisa tu conexión y vuelve a intentarlo. (sección 17) · No pudimos guardar. Revisa los datos y vuelve a intentarlo. (sección 18) |


## 24. Borrar los datos de la persona (MATU-72) · Aprobados por Jorge el 08-11

En la app se dice «borrar», nunca «suprimir» ni «eliminar». El número de enlaces lo da la API, la pantalla no lo calcula.

| Dónde | Texto |
|---|---|
| Grupo familiar, bloque al final, separado de los permisos | Borrar sus datos · Si {nombre_pila} o su representante legal lo pide, o si ya no usan MATU para cuidar a {nombre_pila}, puedes borrar todo lo guardado. No se puede deshacer. · [botón] Borrar los datos de {nombre_pila} |
| Confirmación, título | ¿Borrar todo lo guardado de {nombre_pila}? |
| Confirmación, texto | Esto no se puede deshacer. · Borramos ahora su ficha, con todas sus secciones, y los insumos y las compras anotadas. Nadie los podrá recuperar, tampoco el equipo de MATU. · Se cortan ahora todos sus enlaces de relevo. Hoy abren {n}. (1: «Hoy abre 1.» 0: «Hoy ningún enlace abre.») Quien tenga la ficha abierta deja de verla cuando vuelva a mirarla. No recibe aviso. · {nombre_pila} sale de MATU. Si después quieren volver a usar MATU, hay que registrar a {nombre_pila} de nuevo, y todo empieza en blanco. · Guardamos, sin nada de lo escrito, el registro de las autorizaciones, de los enlaces y de quién abrió la ficha, por los plazos de la política de privacidad. · Lo borrado sigue en las copias de respaldo hasta que vencen, y nadie las usa para ver datos. · Una lista que ya imprimiste o compartiste no se borra: quedó fuera de MATU. |
| Casilla obligatoria | Entiendo que esto no se puede deshacer. |
| Botones | Borrar todo · No borrar |
| En curso | Borrando… |
| Hecho | Borramos los datos de {nombre_pila}. Cortamos {n} enlaces. (1: «Cortamos 1 enlace.» 0: «No había enlaces que abrieran.») |
| Error de conexión | No pudimos borrar los datos. Revisa tu conexión y vuelve a intentarlo. Todo sigue como estaba. |
| 409 | Otra persona de tu grupo ya borró los datos de {nombre_pila}. |
| Pagador y observador, en lugar del botón | Puede borrarlos quien administra el grupo o quien cuida a {nombre_pila}. |
| Relevo | Sin texto nuevo: el 410 `relevo-revocado` de siempre. |

**Ajustes del diseñador, aprobados el 08-11:** A1, el botón no lleva `aria-label`: su nombre accesible es el texto visible. A2, al pagador y al observador el bloque les muestra solo el título y la línea de quién puede borrar.

**Reglas de armado:** si no se pudieron contar los enlaces, se omite «Hoy abren {n}.».

## 25. Alta: la cuenta, el grupo, la persona y la autorización (MATU-68) · Aprobados por Jorge el 08-11

Esta sección es de **MATU-68**, que construyó la pantalla del alta. MATU-39 la originó, pero no la mantiene.

En la app se dice «autorización» y «permiso», nunca «consentimiento». Estos textos informan sobre datos personales: los revisó el analista normativo el 08-11 (sección 12) y, donde propuso un cambio, aquí va el texto aprobado. La pantalla se ajusta a esta sección.

| Dónde | Texto |
|---|---|
| Pasos del alta | Tu cuenta · Tu grupo · A quién cuidas · La autorización |
| Avance | Paso `{n}` de 4 |
| Frase de marca, en las pantallas del alta | Que el cuidado no dependa de una sola persona. |

### 25.1 Tu cuenta (`/crear-cuenta`)

| Dónde | Texto |
|---|---|
| Título y bajada | Crea tu cuenta · Para empezar te pedimos solo esto. |
| Nombre | Tu nombre · Ayuda: Así te verán en tu grupo. Quien te reemplace verá tu nombre de pila. |
| Correo y celular | Tu correo · Tu celular (de la sección 19) · Ayuda del celular: Para ayudarte a recuperar tu cuenta si olvidas la contraseña. |
| Contraseña | Una contraseña · Ayuda: Al menos 10 caracteres. (también en Recuperar) |
| Ver la contraseña | Mostrar · Ocultar |
| En curso y hecho | Creando la cuenta… · Cuenta creada. |
| Validación en la pantalla | Escribe tu nombre. · Revisa cómo escribiste tu correo. · La contraseña necesita al menos 10 caracteres. (también en Recuperar) |
| Validación de la API (422, por `errores[].campo`) | Escribe tu nombre, de hasta 100 caracteres. · La contraseña necesita entre 10 y 128 caracteres. (también en Recuperar) |
| Correo ya registrado | Título: Ese correo ya tiene una cuenta · Texto: Entra con tu contraseña, o usa otro correo. · Botón: Entrar con ese correo |

### 25.2 Tu grupo (`/empezar/grupo`)

| Dónde | Texto |
|---|---|
| Título y bajada | Ponle nombre a tu grupo · Es el grupo de las personas que cuidan contigo. |
| Campo | Nombre del grupo |
| Ayuda del campo (de la política de privacidad, sección 4, «De tu grupo», tal cual) | Usa un nombre corto, como «Familia Soto». No incluyas el nombre completo de la persona que cuidas ni datos de salud. |
| Botón y espera | Crear el grupo · Creando el grupo… |
| Sin nombre | Escribe un nombre para el grupo. |

### 25.3 A quién cuidas (`/empezar/persona`)

| Dónde | Texto |
|---|---|
| Título | ¿A quién cuidas? |
| Nombre | ¿Cómo se llama? |
| Cómo le dicen | ¿Cómo le dicen? · Ayuda: Es el nombre que verá quien te reemplace. |
| Apoyo | ¿Cuánto apoyo necesita en el día a día? · Las tres respuestas están en la sección 25.4 |
| Lo que no se pide | No te preguntamos qué enfermedad tiene, porque para cuidar no hace falta. |
| Validación | Escribe su nombre y cómo le dicen para seguir. · Elige cuánto apoyo necesita. |
| Grupo sin persona registrada | Todavía no hay nadie registrado en `{grupo}`. Quien administra el grupo puede registrar a la persona que cuidan. |

**Sin dirección (decisión de Jorge del 08-11, opción A del analista).** El alta no pide dónde vive la persona: la dirección se pide con el primer pedido (MATU-61). Salen de esta pantalla la pregunta, su ayuda, los campos y su mensaje de validación.

«Enfermedad» informa lo que MATU no pide, como la ayuda de la sección 14.2. No nombra ninguna (sección 3.2).

### 25.4 La autorización (`/empezar/autorizacion`)

| Dónde | Texto |
|---|---|
| Título | Permiso para guardar su ficha (el mismo nombre de la sección 22) |
| Bajada | Lo que anotes sobre el cuidado de `{nombre_pila}` puede decir algo de su salud. Por eso lo protegemos de forma especial y necesitamos una autorización. Puedes retirarla cuando quieras, desde Grupo familiar. |
| Pregunta | ¿Quién da la autorización? |
| Representante legal, referencia | Referencia del documento · Ayuda: Por ejemplo: número de resolución y fecha. Sin el RUT. |
| Cuidadora o cuidador de hecho, casilla del aviso | Leí el aviso y lo acepto |
| Sobre la declaración | Lo que declaras |
| Botón y espera | Acepto y registro a `{nombre_pila}` · Registrando a `{nombre_pila}`… |
| Hecho | Listo. Registramos a `{nombre_pila}` y la autorización. Ahora puedes completar su ficha. |
| Para volver a la persona después de un error | Volver a corregir los datos de `{nombre_pila}` |
| Validación | Elige quién da la autorización. · Escribe la referencia del documento que te nombra representante. · Marca que leíste el aviso para seguir. |

**Las tres calidades.** Sus nombres y detalles no son declaraciones y se aprueban aquí.

| Calidad | Nombre en pantalla | Detalle | Declaración que se muestra |
|---|---|---|---|
| `titular` | `{nombre_pila}` lo autoriza y yo lo registro | `{nombre_pila}` decide por su cuenta y tú registras su decisión. | `declaracion_titular` |
| `representante_legal` | Soy su representante legal | Tienes un nombramiento legal para representar a esta persona. | `declaracion_representante_legal` |
| `cuidador_de_hecho` | Cuido a esta persona, pero no soy su representante legal | Cuidas a esta persona en el día a día, sin un nombramiento legal. | `declaracion_cuidador_de_hecho`, con el aviso `aviso_cuidador_de_hecho` |

**Las declaraciones y el aviso.** Son los de la política de privacidad, sección 5: las tres declaraciones (`declaracion_titular`, `declaracion_representante_legal` y `declaracion_cuidador_de_hecho`) y el aviso `aviso_cuidador_de_hecho`, versión 1.1, con su título «Aviso: tu autorización tiene un límite». Van bajo «Lo que declaras» y se copian sin cambiar una palabra: cambiarlas es publicar una versión nueva de la política. Este documento no las repite, igual que la sección 13.2 con las de insumos.

**Los niveles de apoyo** (respuestas a «¿Cuánto apoyo necesita en el día a día?»):

| Valor | Texto |
|---|---|
| `autovalente_con_supervision` | Se maneja con autonomía, con supervisión |
| `apoyo_parcial` | Necesita apoyo en varias cosas |
| `apoyo_total` | Necesita apoyo en todo |

## 26. Marco de la app y esperas (MATU-68) · Aprobados por Jorge el 08-11

| Dónde | Texto |
|---|---|
| Botón para reintentar después de un error | Volver a intentar |
| Mientras carga una pantalla | Cargando… |
| Al abrir la app | Abriendo MATU… |
| Cabecera, sobre el nombre de la persona cuidada | Cuidas a |
| Cabecera, bajo el nombre | Le dicen `{nombre_pila}` |

## 27. Catálogo (MATU-59) · Aprobados por Jorge el 08-11

Es la tercera pestaña de Insumos, para todos los roles del grupo. "Agregar al pedido" está en cada comercio que tiene el producto, para quien administra o cuida (MATU-61, sección 31). La pantalla no dice «stock» (sección 3.2): dice «Hay en» y «No hay en».

| Dónde | Texto |
|---|---|
| Título de la pantalla | Catálogo |
| Bajada | Productos que usan las familias que cuidan. Mirar no te compromete a nada. |
| Aviso del piloto, una vez arriba | **Precios de ejemplo.** MATU todavía no tiene convenio con comercios, y en esta demo no se cobra dinero real. |
| Junto a cada precio | Precio de ejemplo |
| Bajo el precio | IVA incluido |
| Comercio, una vez por tarjeta de producto | `{nombre}` (comercio ficticio) |
| Hay en ese comercio | Hay en `{nombre}` |
| No hay en ese comercio | No hay en `{nombre}` por ahora |
| Ningún comercio lo tiene | Por ahora no está disponible |
| Nota de lo que hay | Lo que hay se confirma antes de pagar. |
| Envío | El envío se suma al pedido, una sola vez por pedido. |
| Retracto, si se pierde al abrir el sello (letra no menor que el precio) | Derecho a retracto: tienes 10 días desde que lo recibes. No aplica si abres el sello del producto. |
| Retracto, el resto (letra no menor que el precio) | Derecho a retracto: tienes 10 días desde que lo recibes. |
| Catálogo vacío | Todavía no hay productos en el catálogo. |
| Error al cargar | No pudimos traer el catálogo. Revisa tu conexión e inténtalo de nuevo. |
| El catálogo está apagado (capa 3 sin activar, la API responde 404) | El catálogo no está disponible por ahora. |
| Mientras carga y para reintentar | Los de la sección 26 |

**Categorías:** Higiene y cuidado personal · Cuidado de la piel · Alimentación.

**La bolsa colectora va en «Higiene y cuidado personal»** (decisión D3 de Jorge, 08-11). No se crea una categoría propia, porque nombraría una condición de salud (sección 3.1, «ostomía»).

**Nombres de los productos de ejemplo:** Pañal adulto M x30 · Toallitas húmedas x80 · Protectores diarios x20 · Crema protectora de la piel 100 g · Suplemento nutricional en polvo 400 g · Bolsa colectora x10. Sin marcas reales ni afirmaciones de salud («previene», «cura», «para diabéticos»).

**Pendiente de la consulta legal:** si el suplemento y las bolsas colectoras pierden el retracto al abrir el sello. Mientras no responda, usan el texto sin la exclusión.

## 28. Aviso de versión nueva (MATU-67) · Aprobados por Jorge el 09-11

Aparece cuando hay una versión nueva de MATU y la pestaña estaba abierta. Nunca recarga sola. Va en la app de familia y en la página del relevo. No aparece mientras se escribe en un campo, en el alta, en recuperar acceso ni en la pantalla que muestra el PIN del relevo.

| Dónde | Texto |
|---|---|
| Título | Hay una versión nueva de MATU. |
| Bajada, app de familia | Recarga cuando termines lo que estás haciendo. |
| Bajada, página del relevo | Recarga cuando termines de leer. |
| Botón | Recargar |
| Mientras recarga | Recargando… |
| Para cerrarlo | Más tarde |
| Si hay algo sin guardar, título | Lo que escribiste en «`{donde}`» no se guardó. |
| Si hay algo sin guardar en Insumos, título | Lo que anotaste de «`{nombre}`» no se guardó. |
| Si hay algo sin guardar y no se sabe dónde, título | Hay algo que escribiste y no se guardó. |
| Si hay algo sin guardar, bajada | Si recargas ahora, se pierde. |
| Si hay algo sin guardar, botones | Seguir escribiendo · Recargar igual |

`{donde}` es el nombre de la sección de la ficha. En Insumos (Compré, Me quedan, Ya lo resolví y el editor) va el título con `{nombre}`, el nombre del insumo. El título sin lugar va cuando no se sabe dónde, por ejemplo en «Anotar un insumo» antes de escribir el nombre o en Compartir.

El aviso tampoco aparece en la pantalla «Lo que escribiste no se guardó».

En el relevo se mantiene «Actualizar» (sección 7.4), que es otra acción: trae la ficha de nuevo sin cambiar de versión.

---

## 29. Política de privacidad (MATU-75) · Aprobados por Jorge el 09-11

La política se muestra en la app, en /privacidad, desde «En un minuto» hasta el final. `{version}` es el número de versión de la política y `{DD/MM/AAAA}` su fecha. El correo de contacto es cuidaconmatu@gmail.com, el de la política, sección 2. Lo que va entre corchetes es el enlace a la política.

| Dónde | Texto |
|---|---|
| Título de la página | Política de privacidad |
| Título del documento | Política de privacidad · MATU |
| Bajo el título | Versión {version} · actualizada el {DD/MM/AAAA} |
| Crear cuenta, casilla | Leí y acepto la [política de privacidad]. |
| Crear cuenta, error | Para crear tu cuenta, marca que leíste la política de privacidad. |
| Autorizaciones, bajo la declaración | Lee la [política de privacidad] antes de autorizar. |
| Tu cuenta, fila | Política de privacidad |
| Tu cuenta, dato | Aceptaste la versión {version} el {DD/MM/AAAA}. |
| Tu cuenta, sin registro | No tenemos registro de qué versión aceptaste. |
| Tu cuenta, cómo pedir | Para cambiar tu nombre o tu correo, pedir una copia de tus datos o eliminar tu cuenta, escribe a cuidaconmatu@gmail.com desde el correo de tu cuenta. |
| Enlace a otra pestaña | {texto} (se abre en otra pestaña) |
| Rótulo del índice | Índice |
| Al final de cada sección, en el teléfono | Volver al índice |
| Crear cuenta, la política cambió mientras se creaba, título | Actualizamos la política de privacidad. |
| Crear cuenta, la política cambió mientras se creaba, bajada | Cambió mientras creabas tu cuenta. Léela de nuevo y vuelve a marcar la casilla. |
| Tu cuenta, enlace | Política de privacidad (se abre en otra pestaña) |

«(se abre en otra pestaña)» se muestra en pantalla, no solo para el lector de pantalla. Cuando la política cambia mientras se crea la cuenta, la casilla se desmarca. El enlace de «Tu cuenta» usa el mismo texto de 7.5.

---

## 31. Pedido (MATU-61) · Por aprobar por Jorge al fusionar

> La sección 30 es de MATU-84, en otra rama. Si al fusionar el número ya está tomado, esta sección se renumera.

Los textos salen de la especificación de pantallas de MATU-61, v1.1 del 11-11 (`docs/diseno/matu-61-pedido.md`, sección 15), que marca el origen de cada uno: los propuestos por el analista normativo (`legal/revision-previa-matu-61.md`, sección 4), los que fijó Jorge en sus decisiones D8 a D10 y los nuevos del diseñador. Las llaves son datos de la API: `{producto}` es el nombre del producto, `{comercio}` el nombre de fantasía del comercio, `{pila}` el nombre de pila de la persona cuidada, `{precio}` en pesos enteros con punto de miles (`$12.990`) y `{HH:MM}` en 24 horas, hora de Chile.

**Regla de la sección.** En la app se dice «tu pedido», nunca «carro» ni «carrito». Se dice «lo que hay» y «que haya», nunca «stock». La cantidad es en envases del catálogo. **Todos los precios llevan el IVA incluido:** el total se llama «Total», nunca «Total con IVA», y ningún texto presenta el IVA como algo que se suma o que aparece después. «IVA» solo va en «Precio de ejemplo · IVA incluido» (sección 27). «Pedir» lo hace solo quien tiene la autorización de pedidos. La lista nunca compra sola, el aviso nunca ofrece comprar y «Compré» nunca hace un pedido (D10).

| Dónde | Texto |
|---|---|
| Pestaña de Insumos | Pedido |
| `<title>` | Tu pedido · MATU · ¿Dónde lo entregamos? · MATU · Antes de pagar · MATU · Condiciones del pedido · MATU |
| **Autorización** | |
| Título | Antes de pedir, un permiso |
| Explicación | Para pedir desde MATU, primero autoriza los pedidos. Sin esta autorización igual puedes imprimir o compartir la lista. · Es un permiso aparte del de su ficha y del de sus insumos. |
| Volver | Volver al catálogo · Volver a la lista de insumos |
| Botón | Autorizar los pedidos · Autorizando… |
| Hecho | Pedidos autorizados. Agregamos «{producto}» a tu pedido. · Pedidos autorizados. Agrega productos desde el catálogo o desde tu lista de insumos. |
| Error | No pudimos guardar la autorización. Revisa lo que elegiste y vuelve a intentarlo. |
| Pagador, sin autorización | Falta la autorización de pedidos para {pila}. Sin ella no se pueden hacer pedidos desde MATU. Pídele a quien administra el grupo o a quien cuida a {pila} que la dé. |
| Por renovar | Hay que renovar la autorización de los pedidos de {pila}. Se renueva una vez al año. Mientras tanto no se pueden hacer pedidos, pero tu pedido sigue guardado. · Renovar la autorización · Pídele a quien administra el grupo o a quien cuida a {pila} que la renueve. |
| Declaraciones | Las tres `declaracion_pedidos_<calidad>` de la política de privacidad 0.12, sección 5, tal cual |
| **Catálogo** | |
| Botón | Agregar al pedido · Agregando… · Para el lector: Agregar al pedido: {producto}, de {comercio} |
| Ya agregado | En tu pedido · Ver tu pedido |
| Anuncio | Agregamos «{producto}» a tu pedido. |
| Error | No pudimos agregarlo. Revisa tu conexión y vuelve a intentarlo. |
| **Lista de insumos** | |
| Frase y botón | Los productos de esta lista que están en el catálogo se pueden pedir con MATU. Antes de pagar ves el total. · Pedir estos productos · Agregando a tu pedido… |
| Al llegar al pedido | Agregamos {n} productos de tu lista a tu pedido. (con 1: «Agregamos 1 producto de tu lista a tu pedido.») · {producto} ya estaba en tu pedido: dejamos la cantidad de la lista. · No están en el catálogo y no van en el pedido: {nombres}. (con 1: «{nombre} no está en el catálogo y no va en el pedido.») |
| **Tu pedido** | |
| Título y bajada | Tu pedido · Revisa los productos y cuántos quieres. Antes de pagar confirmamos que haya. |
| Comercio | De {comercio} (comercio ficticio) |
| Precio | {precio} cada uno · Precio de ejemplo · IVA incluido |
| Cantidad | Cantidad · el sufijo de la sección 21 · Para el lector: Quitar uno: {producto} · Agregar uno: {producto} |
| De la lista | En tu lista: {cantidad} |
| Cantidad fuera de rango | Escribe una cantidad de 1 a 99. |
| Cantidad, error al guardar | No pudimos guardar la cantidad. Revisa tu conexión y vuelve a intentarlo. |
| Subtotal | Subtotal: {precio} |
| Si falta | Si falta este producto · Buscarlo en otro comercio · El mismo producto. Pagas lo mismo. · Sacarlo del pedido y devolverme su precio · Nunca lo cambiamos por otra marca ni por otro producto. (una vez, sobre las líneas) |
| Si falta, error | No pudimos guardar qué hacer si falta. Revisa tu conexión y vuelve a intentarlo. |
| Si falta, pagador y resumen | Si falta: lo buscamos en otro comercio. · Si falta: lo sacamos y te devolvemos su precio. |
| Sacar | Sacar del pedido · Para el lector: Sacar del pedido: {producto} · Sacamos «{producto}» del pedido. · No pudimos sacarlo. Revisa tu conexión y vuelve a intentarlo. |
| Entrega | Entrega · Dirección · Todavía no hay una dirección de entrega. · Agregar la dirección · Cambiar dirección · Teléfono de contacto · (tu celular) · Cambiar teléfono · Llega entre 24 y 48 horas hábiles. |
| Teléfono | Para que quien entrega pueda avisarte. Si es el de otra persona, avísale. · Guardar el teléfono · Guardamos el teléfono. · Escribe un celular de Chile, por ejemplo +56 9 5555 0137. |
| Pie | Productos: {precio} · El envío y el total los ves al confirmar que haya cada producto. · Ver el total · Confirmando… · Estamos confirmando que haya cada producto… |
| Sin dirección | Agrega la dirección de entrega para ver el total. |
| Total ya confirmado | Ya confirmaste el total. Para cambiar algo, toca «Cambiar el pedido». |
| Vacío | Tu pedido está vacío. Agrega productos desde el catálogo o desde tu lista de insumos. · Ir al catálogo · Ir a la lista de insumos · Pagador y observador: Todavía no hay un pedido para {pila}. |
| Pagador y observador | Quien administra el grupo o quien cuida a {pila} puede cambiar el pedido y ver el total. · Ver el resumen (solo el pagador) · Pasaron 15 minutos y el total venció. Pídele a quien armó el pedido que lo vuelva a confirmar. |
| **Dirección** | |
| Título y ayuda | ¿Dónde lo entregamos? · La usamos solo para entregar tus pedidos. Ningún comercio la ve. · La guardamos para los próximos pedidos de {pila}. |
| Campos | Calle · Número · Depto (opcional) · Comuna · Referencia (opcional) · Por ejemplo: portón verde. No escribas datos de salud. |
| Botón y hecho | Guardar la dirección · Guardando… · Guardamos la dirección. |
| Vaciar | Si no quieres que MATU la guarde, puedes vaciarla. Para el próximo pedido habrá que escribirla de nuevo. · Vaciar la dirección · Para el lector: Vaciar la dirección de entrega de {pila} · ¿Vaciar la dirección de entrega de {pila}? · La borramos de MATU. Para el próximo pedido habrá que escribirla de nuevo. · Dejarla como está · Vaciando… · Vaciamos la dirección. · No pudimos vaciar la dirección. Revisa tu conexión y vuelve a intentarlo. Todo sigue como estaba. · Otra persona de tu grupo cambió la dirección mientras la revisabas. Revisa cómo quedó antes de vaciarla. |
| Validación | Escribe la calle. · Escribe el número. Si no tiene, escribe S/N. · Escribe la comuna. · La referencia admite hasta 200 caracteres. Acórtala un poco. · No pudimos guardar la dirección. Revisa los datos y vuelve a intentarlo. |
| Volver | Volver a tu pedido · Volver a antes de pagar |
| Conflicto (412) | Otra persona de tu grupo cambió la dirección mientras la cambiabas. · No guardamos la tuya encima de la suya. Elige cuál dejar. · La que guardó · La tuya, sin guardar · Guardar la mía · Dejar la que guardó · Dejaste la dirección que guardó otra persona de tu grupo. |
| **Antes de pagar** | |
| Título y bajada | Antes de pagar · Confirmamos que hay cada producto. El total es {total}. |
| Cambiar el pedido | Si cambias algo, antes de pagar confirmamos el total de nuevo. · Cambiar el pedido · Abriendo tu pedido… · Ya puedes cambiar tu pedido. Cuando termines, toca «Ver el total» para confirmarlo de nuevo. · No pudimos abrir tu pedido para cambiarlo. Revisa tu conexión y vuelve a intentarlo. El total sigue confirmado. |
| Cambios | Cambió desde tu pedido · Ya no hay {producto}. Salió del pedido. · Ahora {producto} lo prepara {comercio} (comercio ficticio). · Cambió el precio de {producto}: antes {precio}, ahora {precio}. · Cambió el precio · Otro comercio |
| Productos | Productos · {cantidad} × {precio} · Subtotal: {precio} |
| Retracto | Los dos de la sección 27, en cada línea, con letra no menor que el precio |
| Boleta | Tu pedido · Productos ({n}) · Envío (uno por pedido) · Total · Este total vale hasta las {HH:MM}. · Se cobra una sola vez este total, con crédito o con débito. No hay reserva ni cobros después. |
| Plazo | Quedan 2 minutos para pagar este total. · Volver a confirmar · Confirmamos de nuevo. Este total vale hasta las {HH:MM}. · Revisa lo que cambió antes de pagar. |
| Vencido | Venció · Este total venció a las {HH:MM}. · Pasaron 15 minutos y el total venció. Vuelve a confirmar para ver lo que hay y su precio. · Volver a confirmar |
| Entrega | Entrega: {ventana} · Teléfono de contacto: {telefono} |
| Si falta | Si falta un producto · Si al retirar falta un producto, lo buscamos en otro comercio y pagas lo mismo. Si nadie lo tiene, o elegiste sacarlo, anulamos su cobro el mismo día, a la misma tarjeta. Cuándo lo ves en tu cuenta depende de tu banco. |
| Vendedor y reclamos | Quién vende · Vende: MATU, piloto académico, sin persona jurídica. En este piloto no se emite boleta. · Reclamos: escríbenos a {correo}. |
| Condiciones | Condiciones del pedido (se abre en otra pestaña) · Leí y acepto las condiciones del pedido. · Marca que leíste y aceptas las condiciones para pagar. |
| Pagar (MATU-62) | Pagar {total} · Pagando… |
| Salida | No pagar no tiene costo. · Cancelar pedido |
| **Cancelar** | ¿Cancelar este pedido? · No tiene costo. · Cancelar pedido · Seguir con el pedido · Cancelando… · Cancelamos el pedido. No se cobró nada. · No pudimos cancelar el pedido. Revisa tu conexión y vuelve a intentarlo. Todo sigue como estaba. · Otra persona de tu grupo ya canceló este pedido. |
| **Errores** | No pudimos traer tu pedido. Revisa tu conexión e inténtalo de nuevo. · No pudimos confirmar el total. Revisa tu conexión y vuelve a intentarlo. Tu pedido sigue aquí. · Ahora ningún comercio tiene estos productos. No hay nada que pagar. Tu pedido sigue aquí para intentarlo más tarde. · Este pedido cambió mientras lo revisabas. Te mostramos cómo quedó. · No encontramos este pedido. · Ir a tu pedido · El pedido no está disponible por ahora. |
| **Grupo familiar** | Permiso para pedir sus insumos · Autorizado el {fecha}. · Autorizado el {fecha}. Hay que renovarlo desde el {fecha}. · Autorización retirada el {fecha}. · Sin permiso todavía. Se pide la primera vez que haces un pedido. · Para el lector: Retirar la autorización de los pedidos de {pila} · Volver a autorizar los pedidos de {pila} |
| Ver la dirección (propuesta O12 del diseñador) | Ver la dirección de entrega · Para el lector: Ver la dirección de entrega de {pila} |
| Retirar | ¿Retirar la autorización de los pedidos de {pila}? · Ya no se pueden hacer pedidos para {pila} desde MATU, desde ahora. · Cancelamos sin costo los pedidos sin pagar y borramos la dirección y el teléfono que se copiaron en ellos. · Los pedidos ya pagados siguen hasta que se entreguen. · La dirección de entrega de {pila} queda guardada para cuando vuelvas a autorizar. Puedes vaciarla cuando quieras. · La lista de insumos se puede seguir imprimiendo y compartiendo. · Su ficha, sus insumos y los enlaces de relevo no cambian. · Autorización retirada. Ya no se pueden hacer pedidos para {pila}. |
| Volver a autorizar, hecho | Pedidos autorizados. Ya puedes hacer pedidos para {pila}. |
| Aviso del piloto | El de la sección 11, una vez por pantalla con precios: tu pedido y antes de pagar |

`{correo}` es el canal de reclamo de las condiciones del pedido, cuidaconmatu@gmail.com (D8). `{ventana}` es la ventana fija del piloto, «Entre 24 y 48 horas hábiles» (D8). «Pagar {total}» es de MATU-62: aquí solo se fija el texto.

**Ninguno usa** los términos de la sección 3, «stock», «carro», «carrito», «reserva» (salvo en «No hay reserva ni cobros después.», que la niega), «tope», «estimado», «aprox.» ni «monto real». «Boleta» aparece solo en «En este piloto no se emite boleta».

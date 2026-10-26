# MATU · Lenguaje y textos al usuario

**Versión 1.0 · 26 de octubre de 2026 (26/10/2026)** · historia MATU-30
**Estado:** borrador. Lo revisa Martín en MATU-31 y lo aprueba Jorge. Los textos marcados **[PENDIENTE DE JORGE]** no se usan hasta que él los apruebe.
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

**Cómo se lee.** Las llaves marcan lo que se reemplaza al mostrar el texto: `{nombre_pila}` es el nombre con que llaman a la persona cuidada, `{autor}` es quien guardó un campo, `{n}` es un número, `{fecha}` va en `DD/MM/AAAA` y `{hora}` en 24 horas (`HH:MM`). Las comillas latinas «» van tal cual en pantalla.

---

## 2. Tono

Una cuidadora cansada, con poco tiempo y desde un teléfono. Un relevo que abre la ficha por primera vez, con apuro, en una casa ajena. El texto tiene que servirles a las dos en una sola lectura.

1. **Español de Chile, neutro y en tú.** "Escribe el PIN", no "Escriba" ni "Ingrese". Sin chilenismos que no entienda alguien de otra región.
2. **Frases cortas.** Una idea por frase. Párrafos de dos o tres frases como máximo.
3. **Instructivo, no expediente.** La ficha cuenta cómo cuidar a alguien. No describe lo que le pasa a su cuerpo ni lo clasifica. Se pregunta por **apoyos**, no por funciones (arquitectura 10.3, "Lenguaje sobre el cuerpo"). Una entrevistada lo dijo así: es distinto un instructivo que un expediente (Y.40).
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
| incontinencia | Tres de diez entrevistadas pidieron no nombrarla, por dignidad de la persona cuidada (J.54, F.52, C.57, resultados sección 5, y arquitectura 10.3) | Se pregunta por el apoyo: "apoyo para ir al baño", "cambio de pañal". En insumos, el nombre del producto: "pañal adulto", "protectores", "toallitas húmedas" |

**Excepción, solo en textos legales.** La política de privacidad dice que MATU **no pide** diagnósticos. Ese uso informa un límite y no invita a escribir el dato, así que se mantiene en los textos legales que apruebe Jorge. Ninguna otra pantalla lo copia.

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
| stock, quiebre, stock proyectado | Jerga del equipo (arquitectura 10.3) | "Se acaban en 6 días", "Pronto se acaba" |
| revocar, revocado | Jerga legal y técnica | "Cortar el enlace", "Enlace cortado", "Cortado" |
| token, cookie, sesión, autenticar, credenciales, canje | Jerga técnica | "Enlace", "PIN", "entrar" |
| consentimiento (en botones y mensajes) | La política lo llama "autorización", y es la palabra que se entiende | "Autorización", "permiso" |
| auditoría, registro de accesos, log | Suena a vigilancia. Cinco de diez entrevistadas no mirarían esa pantalla (arquitectura 10.4) | "Quién la vio", "quién se está informando" |
| error 404, 410, 412 y cualquier código | El código no le dice nada a la persona | El texto de la sección 8 |
| inválido, denegado, rechazado, fallido | Culpan o suenan a máquina | "Ese PIN no es", "ya no está disponible" |

---

## 4. Palabras de las familias

Cómo nombraron las cosas las diez entrevistadas, y el término que usa MATU. Solo vocabulario cotidiano. No incluye condiciones de salud ni citas que identifiquen a nadie. Las entrevistas se citan por código.

| Lo que dicen las familias | Dónde apareció | Lo que dice MATU |
|---|---|---|
| La hoja, el cuaderno, la pizarra, la planilla, la bitácora, las notas en el WhatsApp | Siete de diez tienen algo escrito, en uno de esos formatos (resultados, sección 2) | **Ficha** de relevo. La versión impresa es "la hoja" ("La ficha en una hoja, para pegar en el refrigerador") |
| La que llegue, la que me reemplaza, quien me cubre | A.38, y el bloque 3 del protocolo | En la app de la familia: "quien te reemplaza". En botones: "relevo" ("Compartir con un relevo"). Al relevo nunca se le dice "relevo": lee "ficha de cuidado" |
| Entrega de turno | A.38, cuidadora remunerada (arquitectura 10.6) | Ficha de relevo. "Entrega de turno" se entiende, pero viene del vocabulario clínico y no se usa en pantalla |
| Qué la calma, qué hacer cuando se angustia | Y.40, C.57 y A.38, cada una por su cuenta | Campo **"Si se altera"**, pregunta "¿Qué la calma…?" |
| Un día bueno, un día malo | C.57 se trabó al contar "un día normal" | La pregunta de **"Su día"** admite contar un día bueno o uno difícil |
| A quién llamo, la vecina que tiene llave | Bloque 3 del protocolo | Campo **"A quién llamar"** |
| Salir, no poder salir, salir unas horas | Nueve de diez dejaron de salir por falta de relevo | Motivos del enlace: "Salgo unas horas", "Fin de semana fuera", "Turno de noche" |
| Quién está mirando, quién se está informando | P.55, I.63, N.71, A.38 y A.55 la valoran | "Quién la vio" (pestaña) y "Últimas aperturas" |
| Pañales, toallitas, cremas, protectores, suplemento | Pregunta 24 del protocolo | El nombre del producto tal como se vende: "Pañal adulto M", "Toallitas húmedas" |
| Que me avise antes, cuántos días quedan | C.57, Y.40 | "Se acaban en 6 días", "Pronto" |
| El súper, la farmacia, la app | Resultados, sección 2 | El nombre del comercio. En general, "comercio" solo en textos legales |
| La boleta | A.38 | "Boleta" |
| Lo del consultorio, el beneficio, lo que entrega el municipio | Pregunta 27, padrón público | "Lo que recibes del consultorio" (capa 2, fuera de este sprint) |
| Poner la plata, el que aporta | E.64 | "Familiar que aporta" (arquitectura 10.1) |
| De quién es esto, de la familia o mío | A.38, propiedad del registro | Sin texto todavía: consulta legal abierta (arquitectura 18) |

---

## 5. Ficha de relevo

La ficha tiene tres campos. Cada uno acepta **hasta 500 caracteres** y se guarda por separado y cifrado (MATU-12, contrato decisión 2). Los textos vienen de `Demo/src/demo/datos.ts`, que los tomó del prototipo v1.1.

| Clave técnica (contrato) | Clave en la demo | Etiqueta visible |
|---|---|---|
| `rutina` | `su_dia` | **Su día** |
| `manejo_situaciones` | `si_se_altera` | **Si se altera** |
| `red_apoyo` | `a_quien_llamar` | **A quién llamar** |

### 5.1 Su día (`rutina`)

- **Pregunta guía:** ¿Cómo es un día normal para ella? Puedes contar un día bueno o uno difícil.
- **Ejemplo:** Por ejemplo: «08:00 Despierta. Le gusta que abran la cortina primero». Si empiezas con la hora, lo mostramos como línea de tiempo.

### 5.2 Si se altera (`manejo_situaciones`)

- **Pregunta guía:** ¿Qué la calma cuando se angustia o se desorienta?
- **Ejemplo:** Por ejemplo: «Le hace bien que le tomen la mano y le hablen de su pueblo».

### 5.3 A quién llamar (`red_apoyo`)

- **Pregunta guía:** ¿A quién llamar si algo pasa y no te ubican?
- **Ejemplo:** Por ejemplo: «Rodrigo, su hijo: +56 9 5555 0102».

Los ejemplos son sintéticos: Carmen cuida a María, Rosa la reemplaza y Rodrigo es su hijo. Los teléfonos usan la serie `5555`, que no se asigna. Un ejemplo nunca nombra una enfermedad, un remedio ni una dosis.

### 5.4 Textos de la pantalla de la ficha

| Dónde | Texto |
|---|---|
| Título de la sección | Ficha de relevo |
| Bajada de la lista de campos | Tres campos cortos para que quien te reemplace sepa qué hacer. Cada campo se guarda protegido y puedes compartir solo algunos. |
| Avance | `{n}` de 3 campos listos |
| Estado de un campo con texto / sin texto | Listo / Falta |
| Botón de un campo sin texto / con texto | Completar «`{campo}`» / Editar «`{campo}`» |
| Quién lo escribió | Lo escribió `{autor}`: `{cuándo}` |
| Nota de seguridad | Cada campo se guarda cifrado, por separado. |
| Encabezado del editor | Campo `{n}` de 3 |
| Contador | `{n}` de 500 caracteres |
| Botones del editor | Guardar · Dictar en vez de escribir · Seguir después |
| Mientras se dicta | Escuchando… |
| Mientras se guarda | Guardando… |
| Vista previa | Así la ve quien te reemplaza · La hoja, mientras escribes |
| **Campo vacío** (en la hoja, para el relevo y en la vista previa) | **Sin completar** |
| Campo vacío en la hoja impresa | Sin completar. Pregúntale a `{nombre de quien imprime}`. |
| Pie de la hoja impresa | Para quien la cuide hoy. Gracias por estar. |
| Bajada de la hoja impresa | La ficha en una hoja, para pegar en el refrigerador. Sirve sin conexión y sin aplicación. |

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

> **Falta la autorización para usar la ficha de `{nombre_pila}`.** Sin ella no podemos guardar ni mostrar la ficha.

Es la única causa de un 403 en la capa 1 (contrato, decisión 4).

### 6.5 Texto demasiado largo (422, `validacion`, `tipo: string_too_long`)

> Cada campo admite hasta 500 caracteres. Acorta un poco el texto para guardarlo.

---

## 7. El relevo (MATU-23)

La página pública `/r#<token>`, sin cuenta. Antes de escribir el PIN la página **no sabe** de quién es la ficha: con el token solo no se revela ningún nombre (contrato, diferencias con la demo). Después del canje la ficha trae `nombre_pila`, pero nunca quién la compartió.

### 7.1 Encabezado y pantalla del PIN

| Parte | Texto |
|---|---|
| Encabezado | MATU · Ficha de cuidado compartida |
| Título | Te compartieron una ficha de cuidado |
| Bajada | Escribe el PIN de cuatro números que te dictaron por teléfono. |
| Etiqueta del campo | PIN |
| Botón | Ver la ficha |
| Pie | No necesitas cuenta ni instalar nada. Al entrar, el enlace se borra de la barra de direcciones. |

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
| Sin sesión | `/errores/sin-sesion-relevo` 401 | Vuelve a abrir el enlace | Por seguridad, la ficha se cierra después de un rato. Abre de nuevo el enlace que te enviaron y escribe el PIN. | — (el enlace sigue sirviendo) |
| Demasiados intentos desde la conexión | `/errores/demasiadas-peticiones` 429 | Espera un momento | Hubo muchos intentos de entrar desde esta conexión. Vuelve a intentarlo en `{minutos}` minutos. | — |

El mensaje del PIN se anuncia con `role="alert"` y deja el foco en el campo. Los títulos de los estados que no abren se anuncian al cargar. Un estado nunca se distingue solo por color: lleva ícono y título.

### 7.4 La ficha abierta

| Parte | Texto |
|---|---|
| Encabezado de la hoja | Ficha de cuidado de · `{nombre_pila}` |
| Vigencia | Puedes verla hasta el `{fecha}` a las `{hora}`. |
| Botón | Actualizar |
| Nota | Solo la familia puede cambiar esta ficha. |
| Campo compartido sin texto | Sin completar |

### 7.5 Aviso al relevo · [PENDIENTE DE JORGE]

Propuesta del analista normativo para el relevo como titular de su nombre y su teléfono (contrato MATU-09, "Decisiones de Jorge", punto 5). Va en la pantalla del PIN, bajo el botón, en texto secundario. **No se publica hasta que Jorge lo apruebe.** El plazo de conservación del teléfono sigue pendiente (punto 2 del mismo apartado), por eso el aviso no lo nombra.

> **Antes de entrar.** Esta ficha te la compartió una familia para que cuides a una persona mientras la reemplazas. Úsala solo para eso y no la reenvíes. Cada vez que la abres queda registrado, y la familia puede verlo. MATU guarda tu nombre y tu teléfono porque te los pidió quien te compartió la ficha. Responsable de los datos: el equipo del proyecto MATU, durante el piloto académico. [Política de privacidad]

---

## 8. Correspondencia `type` → texto al usuario

La pantalla elige el texto por `type` (y, en un 422, por `errores[].campo` y `errores[].tipo`). Nunca muestra `title`, `detail` ni `mensaje` de la API: el `mensaje` de un 422 hoy viene de Pydantic, en inglés (contrato, decisión 20).

| `type` | Status | Dónde | Texto al usuario |
|---|---|---|---|
| `/errores/no-autenticado` | 401 | App de la familia | Tu sesión terminó. Vuelve a entrar con tu email y tu contraseña. |
| `/errores/token-invalido` | 401 | App de la familia | Tu sesión terminó. Vuelve a entrar con tu email y tu contraseña. |
| `/errores/sin-consentimiento` | 403 | Ficha | Sección 6.4 |
| `/errores/no-encontrado` | 404 | App de la familia | No encontramos lo que buscas. Puede que ya no tengas acceso. Vuelve al inicio. |
| `/errores/version-desactualizada` | 412 | Ficha | Sección 6.2 |
| `/errores/validacion` | 422 | Ficha, `string_too_long` | Sección 6.5 |
| `/errores/validacion` | 422 | Ficha, `vacio_sin_crear` | Sin texto: la pantalla no envía un campo vacío que nunca se escribió |
| `/errores/validacion` | 422 | Canje, `pin` | El PIN tiene 4 números. Revisa que estén todos. |
| `/errores/validacion` | 422 | Compartir, `expira_en`, `vigencia_maxima` | El enlace puede durar como máximo 30 días. |
| `/errores/validacion` | 422 | Compartir, `telefono_relevo` | Escribe un celular de Chile, por ejemplo +56 9 5555 0137. |
| `/errores/validacion` | 422 | Compartir, `nombre_relevo` | Escribe el nombre de quien te reemplaza. |
| `/errores/validacion` | 422 | Compartir, `campos` | Elige al menos un campo. |
| `/errores/falta-version` | 428 | Ficha | Sección 6.3 |
| `/errores/pin-incorrecto` | 401 | Relevo | Sección 7.3 |
| `/errores/sin-sesion-relevo` | 401 | Relevo | Sección 7.3 |
| `/errores/relevo-vencido` | 410 | Relevo | Sección 7.3 |
| `/errores/relevo-revocado` | 410 | Relevo | Sección 7.3 |
| `/errores/relevo-no-disponible` | 410 | Relevo | Sección 7.3 |
| `/errores/relevo-bloqueado` | 423 | Relevo | Sección 7.3 |
| `/errores/demasiadas-peticiones` | 429 | Relevo | Sección 7.3 |
| Cualquier otro, o sin respuesta | 5xx o red | Toda la app | No pudimos completar esto. Revisa tu conexión y vuelve a intentarlo. Lo que escribiste sigue aquí. |

El 404 de la familia no dice si el recurso existe en otro grupo: un recurso de otro grupo responde 404, nunca 403 (CLAUDE.md, agente 2).

---

## 9. Compartir y enlaces (MATU-18 y MATU-20)

Textos de la demo, con los cambios que pide el contrato de MATU-09.

| Dónde | Texto |
|---|---|
| Bajada de Compartir | Quien te reemplaza recibe un enlace por WhatsApp y el PIN se lo dictas tú. El enlace vence solo y lo puedes cortar antes. |
| Preguntas del formulario | ¿Quién te va a reemplazar? · Su teléfono · ¿Qué puede ver? · ¿Hasta cuándo? · ¿Cuántos días? (Hasta 30 días.) |
| Ayuda del teléfono · [PENDIENTE DE JORGE] | Queda anotado junto al enlace. MATU no le envía nada: el enlace se lo mandas tú. |
| Motivo (obligatorio, uno elegido de partida) | ¿Para qué lo compartes? · Salgo unas horas · Fin de semana fuera · Turno de noche · Otro motivo |
| PIN recién creado | **Díctaselo a `{nombre}` por teléfono.** No lo mandes junto con el enlace. Solo lo verás ahora. |
| PIN que ya no se ve | El PIN ya no se puede ver. Por seguridad se muestra una sola vez. Si se perdió, crea un enlace nuevo y corta el anterior. |
| Estados de un enlace (`vigente`, `vencido`, `revocado`, `bloqueado`) | Activo · Vencido · Cortado · Bloqueado |
| Detalle de bloqueado | Se bloqueó porque el PIN se escribió mal cinco veces. |
| Botón y confirmación | Cortar el enlace de `{nombre}` · Enlace cortado. Ya no abre para `{nombre}`. |
| Bajada de Enlaces | Al cortar un enlace deja de abrir de inmediato. Quien lo tenía no recibe aviso. |
| Sin enlaces | No hay enlaces todavía. Crea uno desde Compartir. |
| Bajada de Quién la vio | Una línea por cada vez que alguien abre la ficha o escribe mal el PIN. Es un respaldo para ti, no una vigilancia. |
| Aperturas (`apertura`, `pin_incorrecto`, `bloqueo`) | `{nombre}` abrió la ficha · `{nombre}` escribió mal el PIN · El enlace de `{nombre}` se bloqueó por PIN incorrecto |
| Sin aperturas | Todavía nadie ha abierto la ficha. Cuando alguien la abra, aparece aquí. |

---

## 10. Diferencias entre la demo y el contrato que resuelve el equipo

La demo del viernes 30 no se modifica. Al conectarla a la API, o al construir MATU-12 y MATU-23, se resuelve esto:

| # | Demo | Contrato o este documento | Quién decide |
|---|---|---|---|
| 1 | La pantalla del PIN dice "Carmen te compartió la ficha de María", y la ficha abierta dice "Carmen te la compartió" y "Solo Carmen puede cambiar esta ficha" | Antes del canje no hay nombres, y la API nunca dice quién compartió. Este documento usa "Te compartieron una ficha de cuidado" y "Solo la familia puede cambiar esta ficha" | Jorge, si quiere mostrar quién compartió (requiere migración) |
| 2 | Un solo estado "Este enlace ya no está disponible" para vencido, cortado y bloqueado | Cuatro textos (sección 7.3), como pide MATU-23 | Ya resuelto aquí |
| 3 | Mensaje del PIN con un punto y coma antes de "después el enlace se bloquea" | "Te quedan `{n}` intentos. Después, el enlace se bloquea." | Ya resuelto aquí |
| 4 | El `detail` del 410 revocado en el contrato dice "Pídele uno nuevo si lo necesitas" | La acción del backlog es "Pídele a quien te envió el enlace uno nuevo". La pantalla no muestra `detail`, pero conviene alinear el ejemplo del contrato | Martín, en el contrato |
| 5 | Ayuda del teléfono: "Para enviarle el enlace." | La API no envía nada (contrato, decisión 21). Texto propuesto en la sección 9, pendiente de la finalidad del teléfono | Jorge (contrato, "Decisiones de Jorge", punto 1) |
| 6 | "Motivo, si quieres", tres chips que se pueden desmarcar | Motivo obligatorio con "Otro motivo" y sin texto libre | Ya resuelto aquí |
| 7 | Estado "Activo" calculado en el cliente | `estado = vigente` de la API, que se muestra como "Activo" | Ya resuelto aquí |
| 8 | Las preguntas guía hablan en femenino ("para ella", "qué la calma") | La persona cuidada no tiene género en el modelo. Alternativa neutra: "¿Cómo es un día normal para `{nombre_pila}`?" y "¿Qué le ayuda a calmarse cuando se angustia o se desorienta?" | Jorge, antes de MATU-12 |
| 9 | El texto que la demo dicta en "Si se altera" insinúa una condición de salud de María | Los ejemplos de este documento no lo hacen (sección 5). El dictado de la demo no se copia a la app | Jorge, si quiere cambiar el dictado después del viernes |

---

## 11. Cómo se cambia este documento

- Un texto nuevo o cambiado entra aquí en el mismo pull request que la pantalla que lo usa.
- Un término nuevo en la lista prohibida lo propone cualquiera y lo aprueba Jorge.
- Un aviso legal o un texto que informa sobre datos personales pasa antes por el analista normativo.
- Si este documento contradice la política de privacidad, manda la política y se corrige este documento.

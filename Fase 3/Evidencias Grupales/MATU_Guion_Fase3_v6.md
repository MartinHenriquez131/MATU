# MATU · Presentación final · Guion hablado

**23/11/2026** · Lo escribe el guionista para la presentación final (MATU-104). Lo revisan Jorge y Martín, y se ensaya con cronómetro (MATU-111).
**Incluye:** el anexo A, con las respuestas preparadas para las preguntas de la comisión, y el anexo B, con las capturas del plan B.
**Reparto:** ocho bloques, el de Jorge:
- **Martín:** bloques 1, 4, 5 y 8, y las capas 2 y 3 de la demo;
- **Jorge:** bloques 2, 3 y 7, y la capa 1 de la demo.

---

## 0. Cómo se lee este guion

- **Lo que va en cita se dice palabra por palabra.** Lo que va entre corchetes es una indicación (un cambio de lámina, una pausa o un clic) y no se lee.
- **MATU está terminado, y el guion lo muestra así.** Cumple lo que el equipo se propuso, y cada ajuste de alcance o de meta fue una decisión del equipo, aprobada por el Product Owner y registrada con su fecha en un ADR o en `docs/arquitectura.md`.
- **Sin nombres propios.** Se habla de roles: la cuidadora, la persona cuidada («su mamá»), el relevo, la familia, el hijo que paga y el comercio. Jorge y Martín se nombran solo en el bloque 1, con la portada y el equipo en pantalla.
- **Los cambios de hablante son preguntas.** Quien termina hace una pregunta, y el otro parte respondiéndola (sección 2.1).
- **El tiempo se midió con un script** que cuenta las palabras como se dicen («96,4 %» son siete) y suma las pausas y las esperas de la demo. **A 130 palabras por minuto dura 8:34, y a 140, 8:01.** El tope es 9:00, y el margen es de 26 s al ritmo lento.
- **Las esperas de la demo son estimaciones,** y la de Webpay incluye el formulario de la tarjeta y el paso del banco de prueba. Todas se confirman en el ensayo. Si una escena se alarga, se corta su última frase: nunca se habla más rápido.

---

## 1. Los tiempos

**Total: 8:34 a 130 palabras por minuto y 8:01 a 140.** Las tablas salen del mismo script que cuenta el texto de la sección 2, así que coinciden con él.

### 1.1 Por bloque

| Bloque | Láminas | Habla | Inicio | Término | Palabras | Pausas y esperas | A 130 | A 140 | Referencia de Jorge |
|---|---|---|---|---|---|---|---|---|---|
| 1 · Portada y equipo | 1 y 2 | Martín | 0:00 | 0:20 | 42 | 1 s | **0:20** | 0:19 | 0:25 |
| 2 · Contexto, diagnóstico y propuesta | 3, 4 y 5 | Jorge | 0:20 | 1:52 | 190 | 4 s | **1:32** | 1:25 | 1:20 |
| 3 · Objetivos, alcance y requerimientos | 6, 7 y 8 | Jorge | 1:52 | 2:35 | 86 | 3 s | **0:43** | 0:40 | 1:00 |
| 4 · Metodología, cronograma y tecnologías | 9, 10 y 11 | Martín | 2:35 | 3:22 | 99 | 2 s | **0:48** | 0:44 | 0:50 |
| 5 · Arquitectura y modelo de datos | 12 y 13 | Martín | 3:22 | 4:24 | 129 | 2 s | **1:02** | 0:57 | 1:05 |
| 6 · Demo, capa 1 | 14 y la app | Jorge | 4:24 | 5:29 | 113 | 13 s | **1:05** | 1:01 | 1:10 |
| 6 · Demo, capas 2 y 3 | la app | Martín | 5:29 | 7:11 | 184 | 17 s | **1:42** | 1:36 | 1:20 |
| 7 · Modelo de negocios y próximos pasos | 15 y 16 | Jorge | 7:11 | 7:56 | 92 | 2 s | **0:44** | 0:41 | 0:45 |
| 8 · Reflexión y cierre | 17 | Martín | 7:56 | 8:34 | 75 | 4 s | **0:39** | 0:36 | 0:30 |
| **Total** | **17** | | **0:00** | **8:34** | **1010** | **48 s** | **8:34** | **8:01** | 8:25 |

### 1.2 Por persona

| Persona | Bloques | Palabras | A 130 | A 140 |
|---|---|---|---|---|
| **Jorge** | 2, 3, capa 1 de la demo y 7 | 481 | **4:04** | 3:48 |
| **Martín** | 1, 4, 5, capas 2 y 3 de la demo y 8 | 529 | **4:30** | 4:13 |

El margen hasta 9:00 es de 26 s al ritmo lento y de 59 s al rápido.

### 1.3 Por qué el reparto se aleja de la referencia

- **La escena de Webpay dura unos 45 s,** porque el formulario de la tarjeta y el paso del banco de prueba no se pueden apurar. Martín los llena con la razón del cobro único, que es evidencia del objetivo 6, y por eso las capas 2 y 3 suben a 1:42. Por eso Martín habla 26 s más que Jorge: esa escena es de las capas que Jorge le asignó.
- **El bloque 5 dice en voz alta lo técnico que muestran las láminas 12 y 13:** el monolito modular y su prueba de arquitectura, la capa 3 que se apaga, la meta de carga, Row Level Security forzado, el 404 en vez del 403 y el cifrado AES-256-GCM con una clave por persona.
- **Para compensar, el bloque 1 queda en 0:20 y el bloque 3 en 0:43:** el objetivo general está entero en la lámina 6, con la nota de que su núcleo es el plan de cuidado, y los diez requisitos no funcionales se leen en la lámina 8.
- **El bloque 2 queda en 1:32.** Es de los tres de mayor impacto, con las cifras de ENDIDE, los dos problemas que son uno, los relevos que fallaron, la cita, las tres capas y el criterio escrito antes de entrevistar.

---

## 2. El guion, bloque por bloque

### Bloque 1 · Portada y equipo · Martín · 0:00 a 0:20

**En pantalla:** lámina 1 y lámina 2.

> [Lámina 1]
> Buenas tardes. Somos Jorge Espinoza y Martín Henríquez. Les presentamos MATU, una app para que el cuidado de una persona mayor no se corte cuando quien la cuida sale.
> [Pausa de 1 s · lámina 2]
> Jorge es Product Owner, y yo, Scrum Master. **Jorge les cuenta por qué.**

- **42 palabras · 0:20.** Es el único bloque con nombres, porque están en las láminas 1 y 2. Lo que hace cada rol lo muestra la lámina 2.
- **Fuentes:** los roles, en `docs/adr/ADR-030-roles-del-equipo.md`. La app móvil que en el semestre corre en el navegador, en ADR-026.

### Bloque 2 · Contexto, diagnóstico y propuesta · Jorge · 0:20 a 1:52

**En pantalla:** lámina 3 (contexto), lámina 4 (diagnóstico del problema) y lámina 5 (propuesta de solución).

> [Lámina 3]
> Una cuidadora atiende a su mamá, y este sábado tiene que salir. Pero su rutina, qué la calma y a quién llamar, lo sabe solo ella.
> [Pausa de 1 s]
> En Chile, casi un millón y medio de personas adultas viven con dependencia. El 96,4 % de quienes las cuidan en casa no recibe pago, y el 41,3 % de las personas dependientes no tiene un cuidador formal.
> [Pausa de 1 s · lámina 4]
> En diez entrevistas, nueve dejaron de salir y seis se quedaron sin un insumo. Parecen dos problemas, y son uno: todo depende de una sola persona. De nueve relevos, seis fallaron por algo que solo sabía quien cuida. Una lo dijo así: «Eso no estaba en la hoja porque yo lo sé y se me olvidó que los demás no.»
> [Pausa de 2 s, en silencio · lámina 5]
> Por eso MATU tiene tres capas: la ficha de relevo, que es el producto, el aviso antes de que se acabe un insumo, y el despacho, que se puede quitar. La ficha es corta porque lo medimos: con un plan de ocho secciones, la meta era siete de diez en cinco minutos, y lo lograron tres.

- **Cómo se dice:**
  - La primera frase va lenta, como quien cuenta algo, y nombra sin decirlo los tres campos de la ficha: su rutina, qué la calma y a quién llamar.
  - «Son uno: todo depende de una sola persona» se dice con peso, señalando el óvalo de la lámina 4. «De nueve relevos, seis fallaron» señala la tarjeta de la derecha.
  - La cita se lee más despacio que el resto, y después viene la pausa más larga del guion.
- **190 palabras · 1:32.**
- **Fuentes:**
  - ENDIDE 2022, en `docs/arquitectura.md` §1.1:
    - 1.498.977 personas adultas con dependencia;
    - el 96,4 % de quienes cuidan en el hogar no recibe remuneración;
    - el 41,3 % de las personas adultas dependientes no cuenta con un cuidador formal.

    La lámina 3 agrega que son el 9,8 % de la población de 18 años y más (la misma sección).
  - De las 10 entrevistas: 9 de 10 dejaron de salir por falta de relevo o por el costo de explicar, y 6 de 10 se quedaron sin un insumo en los últimos tres meses (`docs/arquitectura.md` §1.1 y `docs/resultados-entrevistas.md` §3, H2 y H3).
  - De los nueve relevos relatados con detalle, seis fallaron por conocimiento que solo tenía la cuidadora: `docs/arquitectura.md` §1.1, tabla «Lo que se midió».
  - La cita: `docs/resultados-entrevistas.md` §6 (E06), sin código ni edad.
  - Las tres capas: `docs/arquitectura.md` §1, decisiones 1 y 2.
  - El plan de ocho secciones y H1: se pedía que 7 de 10 completaran el mínimo (las tres preguntas) en menos de 5 minutos, y lo lograron 3. Está en `docs/protocolo-entrevistas.md` §7, `docs/resultados-entrevistas.md` §3 y `docs/adr/ADR-023-cierre.md`.

### Bloque 3 · Objetivos, alcance y requerimientos · Jorge · 1:52 a 2:35

**En pantalla:** lámina 6 (objetivos), lámina 7 (alcance) y lámina 8 (requerimientos).

> [Pausa de 1 s · lámina 6]
> Nuestro objetivo general: una plataforma que convierta el plan de cuidado en una predicción de cuándo se acaban los insumos, y coordine su reposición y pago, operativa en un entorno de demostración. Los siete objetivos específicos están cumplidos, cada uno con su evidencia en Git, y cinco los verán en vivo.
> [Pausa de 1 s · lámina 7]
> MATU es para tres actores: la familia, que es quien cuida y quien aporta, quien la reemplaza y el comercio.
> [Pausa de 1 s · lámina 8]
> Y cada requisito se verifica, con pruebas automáticas, mediciones o personas. **¿Y cómo llegamos aquí?**

- **Cómo se dice:**
  - El objetivo general está entero en la lámina, con la nota de que su núcleo es el plan de cuidado, y se dice en una frase.
  - Al decir «cada uno con su evidencia en Git», Jorge señala las líneas en turquesa de la lámina 6. Al decir «cinco los verán en vivo», señala los objetivos 3 a 7.
  - En la lámina 7, nombra a cada actor señalando su tarjeta.
  - En la lámina 8, los diez RNF, con su evidencia al lado, quedan para que se lean.
- **Paso a Martín:** «¿Y cómo llegamos aquí?». Martín responde: «Con Scrum…».
- **86 palabras · 0:43.**
- **Fuentes:**
  - El objetivo general: la presentación de la Fase 2, lámina 4, y la de la Fase 1, lámina 10.
  - El plan de cuidado como núcleo: `docs/arquitectura.md` §1 («El plan de cuidado pasó a ser el núcleo») y §3.1, «Capa 1 · Plan de cuidado», con la ficha de relevo como su versión mínima (RF-02).
  - Los objetivos y su evidencia: la sección 4 de este guion y `TESTER/2026-11-20-MATU-80-recorridos.md`. Los objetivos 5, 6 y 7, en su redacción vigente: `docs/arquitectura.md` §15.4.
  - Los tres actores, con quien cuida y quien aporta dentro de la familia:
    - `docs/arquitectura.md` §15.1;
    - `docs/lenguaje.md` §7.1 y §36;
    - la decisión de Jorge del 11/11 de hablarle a los dos destinatarios (`docs/resultados-entrevistas.md` §8).
  - Los diez RNF y cómo se verifica cada uno: `docs/arquitectura.md` §2.2. La evidencia de la lámina 8:
    - RNF-01, los 9 casos de pago (§12.4); RNF-02, «Quién la vio»; RNF-03, la ronda 2 de usabilidad, 3 de 3 bajo 3:00 sin ayuda;
    - RNF-04, la prueba de dependencias; RNF-05, la carga con k6 del 22/11; RNF-06, la línea de tiempo del pedido en el recorrido 6 (`TESTER/2026-11-20-MATU-80-recorridos.md`);
    - RNF-07, las 308 pruebas; RNF-08, el cifrado AES-256-GCM; RNF-09, la demo al 200 %; RNF-10, las 6 pruebas de `test_salud.py` en `origin/main`.
  - La trazabilidad en el CI: el paso «Trazabilidad (RF y RNF Debe con prueba)» de `.github/workflows/ci.yml`.

### Bloque 4 · Metodología, cronograma y tecnologías · Martín · 2:35 a 3:22

**En pantalla:** lámina 9 (metodología), lámina 10 (cronograma) y lámina 11 (tecnologías).

> [Lámina 9]
> Con Scrum, en sprints de una semana, y validando en terreno: catorce entrevistas y dos rondas de usabilidad. La ronda 1, con un prototipo, dejó dos tareas bajo la meta: llenar la ficha y compartirla. Las rediseñamos, y en la ronda 2, con la app y tres personas nuevas, las tres cumplieron. Cada cambio pasa por la revisión de la otra persona y por diecisiete controles automáticos.
> [Pausa de 1 s · lámina 10]
> Así llegaron los siete objetivos, sprint a sprint.
> [Pausa de 1 s · lámina 11]
> MATU es una app móvil: en el semestre, una aplicación web progresiva que se abre en el navegador y se instala en el inicio.

- **Cómo se dice:** al decir «las tres cumplieron», Martín señala el recuadro «Rediseñado tras la ronda 1» de la lámina 9. En la lámina 11 señala el ícono de MATU en el teléfono y después la tarjeta de GitHub Actions. No se dice quién construye ni quién prueba.
- **99 palabras · 0:48.**
- **Fuentes:**
  - Los sprints de una semana: `docs/sprints/calendario-sprints.md` §3.
  - Las 14 entrevistas: `docs/resultados-entrevistas.md` §1 y §8.
  - Las dos rondas de usabilidad: `docs/usabilidad/ronda-1-informe.md` y `docs/usabilidad/ronda-2-informe.md`.
  - Las metas de cada tarea: `docs/estrategia-pruebas.md` §11. Las dos tareas bajo la meta en la ronda 1 y resueltas en la ronda 2: la tabla «Ronda 1» y la sección de comparación de `docs/usabilidad/ronda-2-informe.md`.
  - La revisión y las pruebas en cada cambio: `docs/sprints/sprint-5-planificacion.md` §8. Los 17 controles: los pasos de `.github/workflows/ci.yml` en `main` del repositorio del código (11 del backend, la imagen y 5 de la app web).
  - El stack: `CLAUDE.md` §2. La app en el navegador: ADR-026.
  - La instalación en la pantalla de inicio:
    - el manifiesto de `web/index.html` (MATU-55) y `web/public/sw.js`, en `main` del repositorio del código;
    - el texto «Agregar a inicio» de `docs/lenguaje.md` §33.

### Bloque 5 · Arquitectura y modelo de datos · Martín · 3:22 a 4:24

**En pantalla:** lámina 12 (la vista de contenedores) y lámina 13 (modelo de datos). Al final, la lámina 14.

> [Pausa de 1 s · lámina 12]
> La app habla con un monolito modular en FastAPI: con dos personas, los microservicios no se justifican, y una prueba de arquitectura impide que los módulos se crucen. La capa 3 se apaga, y 27 pruebas verifican que las capas 1 y 2 siguen funcionando. Y la meta de carga del piloto se cumplió: 10 usuarios a la vez, 0 % de fallos y mediana bajo 800 milisegundos en cada paso.
> [Pausa de 1 s · lámina 13]
> PostgreSQL aísla a cada familia con Row Level Security forzado. Si una familia pide un dato de otra, recibe 404, no 403: ni siquiera sabe que existe. Lo verifican 308 pruebas. La ficha va cifrada con AES-256-GCM y una clave por persona: destruirla la deja ilegible.
> [Lámina 14]
> **Veámoslo en vivo.**

- **Cómo se dice:**
  - Las dos primeras frases recorren la lámina 12 de arriba abajo: el navegador, la API con sus tres capas, y los servicios y las tareas.
  - Al decir «la capa 3 se apaga», Martín señala la capa punteada.
  - La carga se dice como lo que es: la meta del piloto de RNF-05, cumplida. La lámina agrega cómo se midió y el percentil 95, como pide el mismo RNF.
  - Al decir «404, no 403», señala la columna «Otra familia» de la lámina 13.
  - Las preguntas de arquitectura y seguridad las responde Jorge (anexo A).
- **Paso a Jorge:** «Veámoslo en vivo». Jorge parte en la escena 1.
- **129 palabras · 1:02.**
- **Fuentes:**
  - Los contenedores y las tareas:
    - `docs/arquitectura.md` §6;
    - §7.7, «Cómo quedó en el semestre», con las tareas de Railway de MATU-74 para los borrados, el cálculo de cuándo se acaban los insumos, los avisos, la conciliación de pagos y el despacho;
    - `docs/entorno-demo.md` §1.
  - Redis, para las sesiones del relevo y los límites: `docs/arquitectura.md` §11.6 y `docs/api/README.md` del repositorio del código.
  - El monolito modular y por qué: `docs/arquitectura.md` §1, decisión 4, y §2.1. Las dependencias: `CLAUDE.md` §2 (`test_arquitectura.py`).
  - Las 27 y las 308 pruebas son funciones de `test_capa3_desacoplable.py` y de `test_aislamiento.py` en `origin/main` del repositorio del código. El commit es el 6038105, del 22/11/2026, contado con `git grep -c -E "^\s*(async )?def test_"`.
  - La carga del piloto: `TESTER/2026-11-22-MATU-80-carga-meta.md`, anexo, con la base local recién preparada: 0,00 % de fallos, la mediana de cada paso bajo 800 ms y un percentil 95 total de 814 ms. La meta, en `docs/arquitectura.md` §2.2, RNF-05, que pide medirla «sobre una base recién preparada» e informar el percentil 95.
  - El aislamiento, el 404 en vez del 403 y RLS forzado: RNF-07. El cifrado AES-256-GCM y la clave destruida: RNF-08 y `docs/arquitectura.md` §11.4.

### Bloque 6 · Demo · Jorge (capa 1) y Martín (capas 2 y 3) · 4:24 a 7:11

**En pantalla:** la lámina 14 unos segundos, y después la app en vivo. Los clics y el plan B de cada escena están en la sección 3.

> **Escena 1 · Jorge** · [Espera de 2 s: se pasa a la app de la cuidadora]
> Esta es la app de la cuidadora, y esta, la ficha de su mamá: su día, si se altera y a quién llamar.
>
> **Escena 2 · Jorge**
> Antes de salir, la compartió con su relevo: un enlace que vence solo y un PIN dictado por teléfono.
> [Espera de 1 s]
>
> **Escena 3 · Jorge** · [Espera de 2 s: se pasa al teléfono del relevo]
> Este es el teléfono del relevo: sin cuenta y sin instalar nada. Escribe el PIN, que tiene cinco intentos…
> [Espera de 3 s]
> y ahí está. Arriba, a quién llamar. Después, su día, hora a hora. Y si se angustia en la tarde, boleros a volumen bajo.
>
> **Escena 4 · Jorge** · [Espera de 2 s: se vuelve a la app de la cuidadora]
> La cuidadora ve que el relevo abrió la ficha. Al volver, corta el enlace…
> [Espera de 3 s: «Cortar el enlace», se pasa a la ventana del relevo y se recarga]
> y ya no abre. **¿Y lo que nadie alcanza a vigilar?**
>
> **Escena 5 · Martín** · [Espera de 1 s]
> **Eso es la capa 2.** La cuidadora anotó que su mamá usa cuatro pañales al día, y MATU avisa antes de que se acaben: le quedan dos días.
>
> **Escena 6 · Martín**
> La lista sugiere cuánto comprar para un mes, y se copia o se imprime: sirve sin despacho.
> [Espera de 1 s: «Copiar la lista»]
> O se pide con MATU, a precio exacto.
> [Espera de 3 s: MATU confirma que haya cada producto y muestra el total]
>
> **Escena 7 · Martín** · [Espera de 3 s: se pasa al teléfono del hijo y se abre Webpay]
> Paga el hijo, desde su teléfono, en Webpay, la página de Transbank: MATU nunca ve la tarjeta. Es el ambiente de prueba, con su tarjeta de prueba y sin dinero real.
> [Mientras habla: el número, la fecha y el código de la tarjeta]
> Elegimos un solo cobro del total exacto porque la captura diferida no funciona con débito, el medio más usado por estas familias. Así lo probamos contra Transbank, con crédito y con débito.
> [Mientras habla: el paso del banco de prueba. Espera de 6 s: se aprueba y vuelve a MATU]
> Pagado, una sola vez, y es el total que vio. Un retorno repetido no cobra de nuevo.
>
> **Escena 8 · Martín** · [Espera de 1 s: se pasa a la consola del comercio]
> Este pedido lo pagamos antes: el pago y su aviso van juntos a un outbox, que se despacha cada cinco minutos. El comercio no ve de quién es ni a dónde va: solo escribe el código de retiro, que sirve una vez…
> [Espera de 2 s]
> y entrega. **¿Y esto se sostiene?**

- **Capa 1:** 113 palabras y 13 s de espera, 1:05.
- **Capas 2 y 3:** 184 palabras y 17 s de espera, 1:42.
- **La demo completa dura 2:47.** En la escena 7, la narración va encima de los clics de Webpay, que toman unos 40 s.
- **Fuentes de lo nuevo en la v6:**
  - Los cinco intentos del PIN: `docs/lenguaje.md` §7.3, estado «Bloqueado».
  - Cortar el enlace y lo que ve el relevo: `docs/lenguaje.md` §9 («Cortar el enlace de…», «Enlace cortado. Ya no abre…») y §7.3 («Este enlace se cortó»).
  - Copiar la lista: `docs/lenguaje.md` §21 («Copiar la lista», «Copiamos la lista. Pégala donde quieras.») y ADR-031.
  - Un retorno repetido no cobra de nuevo: `docs/arquitectura.md` §12.4, caso 5 («Retorno de pasarela recibido dos veces»), y el anexo A, pregunta 5.
  - El pago y su aviso en la misma transacción, por el outbox: `docs/arquitectura.md` §8.4, el diagrama del retorno («transacción aprobada + cargo pagado + pedido pagado + evento outbox»). La tarea de despacho, cada 5 minutos: `TESTER/2026-11-16-sprint-5-cola.md`, H8.

### Bloque 7 · Modelo de negocios y próximos pasos · Jorge · 7:11 a 7:56

**En pantalla:** lámina 15 (modelo de negocios) y lámina 16 (próximos pasos).

> [Pausa de 1 s: se vuelve de la app a la presentación · lámina 15]
> **Con suscripción, sí.** La familia paga $5.990 al mes y el comercio, el 10 % de cada pedido: así bastan 84 familias. Cobrando solo el despacho, harían falta 429. Y hay quién pague: seis de diez ya pagan hoy por algún servicio de cuidado, y los familiares que aportan también lo pagarían.
> [Pausa de 1 s · lámina 16]
> Vienen tres pasos: el pago dividido entre familiares, el retiro de medicamentos en farmacias y centros de salud pública, y lo que más esperamos, pilotos con municipios. **¿Para quién es todo esto?**

- **Cómo se dice:**
  - «Con suscripción, sí» responde la pregunta de Martín y repite el título de la lámina 15.
  - «$5.990» se dice «cinco mil novecientos noventa pesos». Al decir quién paga cada cosa, Jorge señala las dos etiquetas de la lámina.
  - «Seis de diez ya pagan hoy» es un hecho, no una intención.
  - «Ejercicio de viabilidad, no una proyección» queda escrito al pie de la lámina.
  - Los pilotos con municipios llevan el énfasis del bloque.
- **Paso a Martín:** «¿Para quién es todo esto?». Martín responde: «Para tres personas».
- **92 palabras · 0:44.**
- **Fuentes:**
  - 84 y 429 familias, $5.990 y el 10 %: `docs/arquitectura.md` §16.2 y §16.4. Que el 10 % lo paga el comercio: la liquidación con cada comercio, `neto = bruto − comisión` (`docs/modelo-datos.md`, tabla `liquidacion`).
  - 6 de 10 ya pagan hoy por algún servicio de cuidado, con las mismas palabras de `docs/arquitectura.md` §16.1 y §16.6, punto 1, y `docs/resultados-entrevistas.md` §3 (H4) y §4.
  - Los cuatro familiares que aportan lo pagarían: `docs/resultados-entrevistas.md` §8.
  - «Ejercicio de viabilidad»: `docs/arquitectura.md` §16.6.
  - Los tres pasos:
    - el pago dividido: `docs/resultados-entrevistas.md` §8;
    - los medicamentos: `docs/arquitectura.md` §15.1 y `docs/modelo-datos.md` §11;
    - el canal municipal: `docs/resultados-entrevistas.md` §8 (H7).

### Bloque 8 · Reflexión y cierre · Martín · 7:56 a 8:34

**En pantalla:** lámina 17.

> [Pausa de 1 s · lámina 17]
> **Para tres personas.** Para la cuidadora, que puede delegar sin explicarlo todo. Para la persona cuidada, que recibe el mismo cuidado, la cuide quien la cuide. Y para la familia, que no se queda sin insumos.
> [Pausa de 1 s]
> **Aprendimos** que fijar el criterio antes de medir cambia el producto, y que probar en cada cambio evita sorpresas.
> [Pausa de 1 s]
> Casi todas las que cuidan en casa lo hacen sin pago. Queremos que puedan salir, y volver tranquilas.
> [Pausa de 1 s]
> Gracias. ¿Preguntas?

- **Cómo se dice:** «Para tres personas» responde la pregunta de Jorge. Martín mira a la comisión y señala una tarjeta de la lámina con cada persona que nombra. Lo que aprendimos está escrito bajo las tarjetas. «Y volver tranquilas» repite el título de la lámina. Jorge se pone a su lado para las preguntas.
- **75 palabras · 0:39.**
- **Fuentes:** las tres personas son las tarjetas de la lámina 17. «Casi todas sin pago» es el 96,4 % de ENDIDE 2022 (`docs/arquitectura.md` §1.1).

### 2.1 Los cambios de hablante

| Minuto | De | A | Quien termina dice | Quien sigue parte con |
|---|---|---|---|---|
| 0:20 | Martín | Jorge | «Jorge les cuenta por qué.» (en la lámina 2, donde los nombres sí van) | «Una cuidadora atiende a su mamá…» |
| 2:35 | Jorge | Martín | «¿Y cómo llegamos aquí?» | «Con Scrum, en sprints de una semana…» |
| 4:24 | Martín | Jorge | «Veámoslo en vivo.» | «Esta es la app de la cuidadora…» |
| 5:29 | Jorge | Martín | «¿Y lo que nadie alcanza a vigilar?» | «Eso es la capa 2.» |
| 7:11 | Martín | Jorge | «¿Y esto se sostiene?» | «Con suscripción, sí.» |
| 7:56 | Jorge | Martín | «¿Para quién es todo esto?» | «Para tres personas.» |

La pregunta se dice mirando al compañero, y la respuesta parte sin pausa.

---

## 3. La demo, escena por escena

### 3.1 Qué está preparado y qué se hace en vivo

| | Preparado antes | En vivo |
|---|---|---|
| Capa 1 | La ficha completa. El enlace del relevo ya creado, con el PIN anotado en papel. El teléfono del relevo abierto en la pantalla del PIN | El relevo escribe el PIN y abre la ficha. La cuidadora ve que la abrió y corta el enlace. Al recargar, el relevo ve «Este enlace se cortó» |
| Capa 2 | Los insumos, con el pañal a punto de acabarse | El aviso, y la lista copiada con «Copiar la lista» |
| Capa 3 | Un pedido pagado antes, preparado por el comercio, con su código de retiro generado en la consola de operación y anotado en papel | La cuidadora arma el pedido y confirma el total. El hijo paga en Webpay. El comercio valida el código del pedido preparado y entrega |

**El retiro se hace con un pedido preparado,** porque el pago llega al comercio con la tarea de despacho, que corre cada 5 minutos (`TESTER/2026-11-16-sprint-5-cola.md`, hallazgo H8). Martín lo dice en la escena 8, como pidió ese hallazgo.

### 3.2 La preparación, el día de la presentación

La hace Martín, dueño del entorno de demostración (ADR-030). **Ningún PIN, código de retiro, contraseña ni enlace del relevo se escribe en un chat, un documento o un commit** (`docs/entorno-demo.md` §5). Van solo en papel. Las cuentas son las de `docs/entorno-demo.md` §2, por su rol: admin, pagador y comercio.

1. **En la mañana, restablecer la demo** (`docs/entorno-demo.md` §3). Así el pañal dice «Alcanza para 2 días» ese mismo día. Si dice otra cosa, la escena 5 dice lo que muestre la pantalla.
2. **Resolver los nombres en pantalla** según el punto 1 de «Para decidir». Va antes de todo lo demás, porque cambia lo que hay que preparar.
3. **Crear el enlace del relevo** desde la cuenta de administración:
   - «Compartir con un relevo», con un nombre de rol y un celular de la serie sintética `+56 9 0000 00xx`;
   - vigencia de «24 horas» y la casilla de aviso marcada;
   - **el PIN, anotado en papel.**
4. **Abrir el enlace en la ventana del relevo,** en pantalla completa (F11), para que la barra de direcciones no se proyecte. Tiene que quedar en la pantalla del PIN.
5. **Preparar el pedido del retiro, entre 75 y 60 minutos antes de la presentación.** El código vence a los 90 minutos (`docs/legal/registro-tratamientos.md`).
   - Un paquete de pañales del comercio de la cuenta `comercio@example.com`. Se confirma el total, y la cuenta pagador paga con la tarjeta de prueba.
   - Se espera la tarea de despacho, como máximo 5 minutos.
   - En el comercio: «Empezar a preparar», «Lo tengo» y «Listo para retirar».
   - En la consola de operación, con la contraseña y el código del teléfono: «Generar el código». **Se anota en papel.** Si la presentación se atrasa más de una hora, «Generar un código nuevo».
6. **Cuatro ventanas,** cada una en su perfil del navegador y con el zoom al 200 %, que la app admite sin desplazamiento horizontal (RNF-09):
   - la cuidadora, en la ficha;
   - el relevo, en pantalla completa, en la pantalla del PIN;
   - el hijo que paga, en su inicio;
   - el comercio, en el pedido preparado, con el campo «Código de retiro» a la vista.
7. **La tarjeta de prueba** es la AMEX de crédito o la Redcompra de débito del ambiente de integración (`TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`, H2). Los datos de la tarjeta y del banco de prueba van en el papel.
8. **La red de la sala,** con el teléfono de Martín como punto de acceso de respaldo. Las notificaciones del computador, apagadas. Las capturas y el video del plan B, a un clic.

### 3.3 Las escenas

Esto supone la propuesta del punto 2 de «Para decidir»: **Martín maneja toda la demo, y Jorge solo habla en la capa 1.**

| Escena | Minuto | Habla | Ventana | Clic exacto | Lo que se ve | Fuente | Plan B |
|---|---|---|---|---|---|---|---|
| **1 · La ficha** | 4:24 a 4:37 | Jorge | Cuidadora | Pasar a su ventana, que ya está en la ficha | «Ficha de relevo», «3 de 3 campos listos» | `docs/lenguaje.md` §5 | PB1 |
| **2 · El enlace con PIN** | 4:37 a 4:47 | Jorge | Cuidadora | Pestaña «Enlaces» | El enlace del relevo, «Activo» | `docs/lenguaje.md` §9 y §9.1 | PB2 |
| **3 · El relevo abre la ficha** | 4:47 a 5:12 | Jorge | Relevo | Escribir el PIN del papel y tocar «Ver la ficha» | La ficha abierta: «A quién llamar» arriba, «Su día» como línea de tiempo y «Si se altera» | `docs/lenguaje.md` §7.1 y §7.4. MATU-95 (`parte-tecnica-jorge.md` §2.3). Ficha de la semilla | PB3 |
| **4 · Quién la vio, y el corte** | 5:12 a 5:29 | Jorge | Cuidadora, y después el relevo | Pestaña «Quién la vio», o el bloque «Últimas aperturas». Después, en «Enlaces», «Cortar el enlace de…». Se pasa a la ventana del relevo y se recarga | La apertura del enlace y la de la ficha. «Enlace cortado. Ya no abre para…». En el relevo, «Este enlace se cortó» | `docs/lenguaje.md` §9, §15 y §7.3 | PB4 y PB4b |
| **5 · Cuándo se acaba** | 5:29 a 5:44 | Martín | Cuidadora | Sección «Insumos» | «Se acaban pronto», con el pañal: «Alcanza para 2 días» y «Te estamos avisando» | Semilla: 4 al día, 8 en casa y aviso con 7 días (`infra/semillas/demo.py`). `docs/lenguaje.md` §13.1 y §17 | PB5 |
| **6 · La lista y el pedido** | 5:44 a 5:59 | Martín | Cuidadora | Pestaña «Lista de insumos», «Copiar la lista», después «Pedir estos productos» y «Ver el total» | La cantidad sugerida, «Copiamos la lista. Pégala donde quieras.», y después «Antes de pagar · Confirmamos que hay cada producto. El total es…» | `docs/lenguaje.md` §21 y §31. ADR-031 y ADR-027 | PB6 y PB7 |
| **7 · Un solo cobro** | 5:59 a 6:45 | Martín | Hijo que paga | «Ver el resumen», la casilla de las condiciones y «Pagar $…». En Webpay, la tarjeta de prueba (número, fecha y código) y el paso del banco de prueba, hasta aprobar | Al volver, «Pagaste tu pedido · Pagaste $… una sola vez. Es el total que viste antes de pagar.», con el sello «Pago de prueba» | `docs/lenguaje.md` §32. `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`. R5: `TESTER/2026-11-21-MATU-80-k6-cierre.md` | PB8 y PB9 |
| **8 · El retiro con código** | 6:45 a 7:11 | Martín | Comercio | Escribir el código del papel y tocar «Revisar código» | «Aquí ves solo los productos.» y, al validar, «Código correcto. Entrega el pedido…» | `docs/lenguaje.md` §36. R6: `TESTER/2026-11-20-MATU-80-recorridos.md` | PB10 |

### 3.4 El plan B, con la frase exacta para pasar a él

**La regla:** quien habla dice la frase, y quien maneja abre las capturas o el video (anexo B). El texto de cada escena sirve igual sobre la captura.

| Si falla | Lo dice | Frase exacta | Qué se muestra |
|---|---|---|---|
| La app o la red, en la capa 1 | Jorge | «La conexión nos está fallando. Les muestro lo mismo en las capturas de esta mañana.» | PB1 a PB4b |
| El relevo no muestra el corte al recargar | Jorge | «Así lo ve el relevo cuando vuelve a mirarla.» | PB4b |
| La red, en la capa 2 | Martín | «Sigo con las capturas, que muestran lo mismo.» | PB5, PB6 y PB7 |
| Webpay no responde | Martín | «Webpay, el ambiente de prueba de Transbank, no responde ahora. No se cobró nada. Esto es lo que vieron en el ensayo.» | PB8 y PB9 |
| El código venció o se bloqueó | Martín | «Venció: el código sirve noventa minutos y una sola vez. Así se ve cuando es el correcto.» | PB10 |
| Se cae todo, o quedan menos de 2 minutos | Quien habla | «Les mostramos el mismo recorrido en el video del ensayo.» | El video, sin audio, narrado con el texto de las escenas que falten |

La frase de Webpay es el texto de la app para ese caso (`docs/lenguaje.md` §32). Así, el plan B también muestra cómo MATU le habla a una familia cuando algo falla.

### 3.5 Después de la demo

- **El enlace del relevo ya quedó cortado en la escena 4.** Si se pasó al plan B, se corta igual, porque el PIN se escribió frente a la sala.
- **El código de retiro ya se usó.** Si no se usó, por el plan B, se genera uno nuevo antes de volver a mostrarlo.
- Si se proyectó un dato que no debía, se restablece la demo (`docs/entorno-demo.md` §5).

### 3.6 Lo que se revisa en el ensayo (MATU-111)

- [ ] El cronómetro de cada bloque, y en especial el de la escena 7, de punta a punta. Si pasa de 50 s, ver el punto 3 de «Para decidir».
- [ ] Si la demo pasa de 2:55, la escena 5 se acorta a «Eso es la capa 2: al pañal le quedan dos días, y MATU avisa antes».
- [ ] Al cortar el enlace y recargar la ventana del relevo, aparece «Este enlace se cortó» antes de 3 s.
- [ ] «Copiar la lista» muestra «Copiamos la lista. Pégala donde quieras.» en el navegador de la demo.
- [ ] No queda ningún nombre propio en pantalla, o se aplica lo que se decida en el punto 1.
- [ ] La lista muestra solo el pañal, y «Pedir estos productos» lo agrega.
- [ ] Con el pedido preparado ya pagado, se puede armar uno nuevo desde la lista.
- [ ] La tarjeta de prueba y el paso del banco de prueba funcionan ese día.
- [ ] La ventana del relevo no muestra la barra de direcciones.
- [ ] Desde el fondo de la sala, la app con el zoom al 200 % se lee bien.
- [ ] Se graban el video y las capturas del plan B, sin nombres.

---

## 4. Mapa de evidencia por objetivo

Es el criterio 2 de la planilla, el de más peso (25). La columna «En la lámina 6» repite lo que dice la pantalla.

| # | Objetivo | En la lámina 6 | Evidencia en Git | Dónde aparece |
|---|---|---|---|---|
| 1 | Validar el problema con criterios fijados antes | 10 entrevistas; la ficha quedó en 3 campos | `docs/protocolo-entrevistas.md` §7. `docs/resultados-entrevistas.md` §3 y §8. `docs/adr/ADR-023-cierre.md` | Bloque 2 (el criterio y la ficha) y bloque 4 (las entrevistas y la usabilidad) |
| 2 | Aislar los datos de cada familia | 308 pruebas de aislamiento en cada cambio | 31 pruebas al cierre del sprint 0 (`docs/arquitectura.md` §15.4). 308 funciones en `test_aislamiento.py` en `origin/main` (6038105, 22/11). El CI las corre en cada push | Bloque 5 y lámina 13 |
| 3 | Compartir la ficha de forma segura y revocable | Recorrido 2 en el teléfono · «Quién la vio» | Cumplido el 29/10 (`docs/arquitectura.md` §15.4). R2 en el teléfono (`TESTER/2026-11-09-MATU-64-demo.md` y `TESTER/2026-11-20-MATU-80-recorridos.md`). `test_recorrido_2_relevo.py` (`parte-tecnica-jorge.md` §3.3) | Demo, escenas 1 a 4, con el corte del enlace en vivo. Bloque 5 (la clave por persona) |
| 4 | Anticipar cuándo se acaba cada insumo | 8 pruebas de dominio · recorrido 3 | Cumplido el 05/11 (`parte-tecnica-jorge.md` §3). Las ocho pruebas de dominio son el criterio de aceptación (`docs/arquitectura.md` §7, perfil de consumo). PASS en el teléfono (`TESTER/2026-11-05-pruebas-telefono.md`). `test_recorrido_3_insumos_y_aviso.py` | Demo, escena 5 |
| 5 | La lista de reposición, operativa sin convenio comercial y compartible como texto (redacción vigente, §15.4) | Recorrido 4 · se imprime, copia o comparte | #57 y `TESTER/2026-11-07-MATU-60-lista-insumos.md`. `test_recorrido_4_lista_y_compra.py`. Con la capa 3 apagada: 27 pruebas en `test_capa3_desacoplable.py` (6038105, 22/11) | Demo, escena 6, con «Copiar la lista». Bloque 5 |
| 6 | Pagar el pedido con un solo cobro del total exacto | 9 casos de pago probados · recorrido 5 | Los nueve casos en `backend/tests/modules/payments/test_casos_pago.py` (`docs/arquitectura.md` §12.4). Los cuatro casos contra Transbank con PASS: `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`. `TESTER/2026-11-12-MATU-62-pago.md` | Demo, escenas 6 y 7 |
| 7 | Desplegar el sistema con seis recorridos críticos | Recorridos 1 a 6 aprobados en el teléfono | Despliegue de `main` y R1 a R6 en OK en el teléfono, el 20/11: `TESTER/2026-11-20-MATU-80-recorridos.md`. Los seis recorridos como pruebas de punta a punta en cada push: `backend/tests/e2e/` (#106) | Bloque 3, y toda la demo, que corre en ese entorno. Escena 8, R6 |

---

## 5. Cobertura de la planilla

| Criterio | Puntos | Dónde se cumple | Riesgo |
|---|---|---|---|
| 1 · Relevancia, objetivos, metodología y desarrollo | 15 | Relevancia, bloque 2. Objetivos, bloque 3. Metodología, bloque 4. Desarrollo, bloques 5 y 6 | Bajo |
| 2 · Evidencias del cumplimiento de los objetivos | 25 | La lámina 6, con la evidencia de cada objetivo y los objetivos 5 a 7 en su redacción vigente. La lámina 8, con los diez RNF y su evidencia. Los bloques 4 y 5 en voz alta (la usabilidad rediseñada, los 17 controles del CI, las 27 y 308 pruebas y la carga con su condición). La demo, con cinco objetivos en vivo, el corte del enlace y la lista copiada. El mapa de la sección 4 | Bajo. Se refuerza mostrando GitHub en las preguntas (punto 4 de «Para decidir») |
| 3 · Respuestas a las preguntas | 20 | El anexo A, con 20 respuestas. Las de arquitectura y seguridad las responde Jorge | Depende del ensayo |
| 4 · Formato y tiempo | 5 | 8:34 a ritmo lento, con 26 s de margen. 17 láminas en el orden de Jorge, con el texto de 30 px o más | Bajo, si se cronometra la escena 7 |
| 5 · Fluidez, claridad, precisión y lenguaje técnico | 5 | Cifras al día y con su condición (la carga en una base recién preparada, las personas adultas de 18 años y más, quién paga el 10 %), el mismo dato en lámina y voz, y seis cambios de hablante con pregunta | Bajo |
| 6 · Documentación y evidencias en Git | 20 | La lámina 6, con «Todo en Git». El bloque 3, en voz alta. Cada dato del guion tiene su ruta (sección 6). La rama `fase3-presentacion-final` va en un PR a `main` | Bajo, con el PR fusionado antes de presentar |
| 7 · Lenguaje técnico y manejo de la información | 10 | El bloque 5 en voz alta: el monolito modular y su prueba de arquitectura, Row Level Security forzado, el 404 en vez del 403, la mediana en milisegundos y AES-256-GCM con una clave por persona. La demo: los cinco intentos del PIN, el corte del enlace, el retorno idempotente y el outbox. El anexo A lo profundiza con el pool de conexiones y el borrado criptográfico | Bajo |

---

## 6. Las afirmaciones y su fuente

| # | Bloque | Lo que se dice | Fuente |
|---|---|---|---|
| 1 | 1 | Los roles de Product Owner y Scrum Master | ADR-030 |
| 2 | 2 | Casi un millón y medio de personas adultas con dependencia | ENDIDE 2022, en `docs/arquitectura.md` §1.1 |
| 3 | 2 | El 96,4 % de quienes cuidan en casa no recibe pago | Ídem |
| 4 | 2 | El 41,3 % de las personas dependientes no tiene un cuidador formal | Ídem |
| 5 | 2 | De nueve relevos, seis fallaron por algo que solo sabía quien cuida | `docs/arquitectura.md` §1.1, tabla «Lo que se midió» |
| 6 | 2 | En diez entrevistas a quienes cuidan y a sus familias, nueve dejaron de salir (por falta de relevo o por lo que cuesta explicar) | `docs/resultados-entrevistas.md` §1. `docs/arquitectura.md` §1.1 |
| 7 | 2 | Seis se quedaron sin un insumo | Ídem, y `docs/resultados-entrevistas.md` §3 (H3) |
| 8 | 2 | La cita «Eso no estaba en la hoja…» | `docs/resultados-entrevistas.md` §6 (E06) |
| 9 | 2 | Las tres capas, en ese orden | `docs/arquitectura.md` §1 |
| 10 | 2 | Con un plan de ocho secciones, la meta era 7 de 10 en 5 minutos, y lo lograron 3 | `docs/protocolo-entrevistas.md` §7. `docs/resultados-entrevistas.md` §3. ADR-023 |
| 11 | 3 | El objetivo general, en una frase, con su núcleo en el plan de cuidado (en la lámina) | Presentaciones de la Fase 2 (lámina 4) y de la Fase 1 (lámina 10). `docs/arquitectura.md` §1 y §3.1 |
| 12 | 3 | Siete objetivos cumplidos, cada uno con su evidencia en Git | Sección 4. `TESTER/2026-11-20-MATU-80-recorridos.md`. Redacción vigente de los objetivos 5 a 7: `docs/arquitectura.md` §15.4 |
| 13 | 3 | Tres actores, y la familia es quien cuida y quien aporta | `docs/arquitectura.md` §15.1. `docs/resultados-entrevistas.md` §8 |
| 14 | 3 | Cada requisito se verifica, con pruebas automáticas, mediciones o personas | `docs/arquitectura.md` §2.2, columna «Cómo se verifica» de RNF-01 a RNF-10, y §3 |
| 15 | 4 | Sprints de una semana y catorce entrevistas | `docs/sprints/calendario-sprints.md`. `docs/resultados-entrevistas.md` §1 y §8 |
| 16 | 4 | La ronda 1 dejó dos tareas bajo la meta; rediseñadas, en la ronda 2 las tres personas cumplieron | `docs/usabilidad/ronda-1-informe.md` y `docs/usabilidad/ronda-2-informe.md` («U1 y U2, que no cumplían en la ronda 1, ahora cumplen en 3 de 3») |
| 17 | 4 | Cada cambio, revisado por la otra persona y con diecisiete controles automáticos | `docs/sprints/sprint-5-planificacion.md` §8. `.github/workflows/ci.yml` |
| 18 | 4 | Los siete objetivos, sprint a sprint | `docs/sprints/calendario-sprints.md`. El objetivo 7, el 20/11: `TESTER/2026-11-20-MATU-80-recorridos.md` |
| 19 | 4 | Aplicación web progresiva, que se instala en la pantalla de inicio | ADR-026. `web/index.html` (manifiesto) y `web/public/sw.js` en `main`. `docs/lenguaje.md` §33 |
| 20 | 5 | La app habla con un monolito modular en FastAPI | `docs/arquitectura.md` §6 y §7.7. `docs/entorno-demo.md` §1 |
| 21 | 5 | Con dos personas, los microservicios no se justifican, y una prueba de arquitectura impide que los módulos se crucen | `docs/arquitectura.md` §1, decisión 4, y §2.1. `test_arquitectura.py` (CLAUDE.md §2) |
| 22 | 5 | 27 pruebas: sin la capa 3, las capas 1 y 2 siguen funcionando | `test_capa3_desacoplable.py`, `origin/main` 6038105 (22/11) |
| 23 | 5 | La meta de carga del piloto, cumplida: 10 usuarios a la vez, 0 % de fallos y mediana bajo 800 ms en cada paso | `TESTER/2026-11-22-MATU-80-carga-meta.md`, anexo (base recién preparada, p95 total de 814 ms). RNF-05 |
| 24 | 5 | Row Level Security forzado, 404 y no 403, y 308 pruebas | RNF-07. `test_aislamiento.py`, `origin/main` 6038105 (22/11) |
| 25 | 5 | AES-256-GCM y una clave por persona: destruirla deja la ficha ilegible | RNF-08. `docs/arquitectura.md` §11.4 |
| 26 | 6 | Tres campos. Un enlace que vence solo, con un PIN dictado | `docs/lenguaje.md` §5 y §9 |
| 27 | 6 | El relevo, sin cuenta ni instalar nada | `docs/lenguaje.md` §7.1 |
| 28 | 6 | «A quién llamar» arriba, y «Su día» hora a hora | MATU-95. `docs/lenguaje.md` §5.1 |
| 29 | 6 | Boleros a volumen bajo | Ficha de la semilla (`infra/semillas/demo.py`) |
| 30 | 6 | El PIN tiene cinco intentos. La cuidadora ve quién la abrió, corta el enlace en vivo y ya no abre | `docs/lenguaje.md` §7.3, §9 y §15 |
| 31 | 6 | Cuatro pañales al día, y le quedan dos días | `infra/semillas/demo.py`, con la demo restablecida ese día |
| 32 | 6 | La lista sugiere para un mes, se copia o se imprime y sirve sin despacho. Precio exacto | `docs/lenguaje.md` §21. ADR-031. ADR-027 |
| 33 | 6 | MATU nunca ve la tarjeta | `docs/lenguaje.md` §32 |
| 34 | 6 | La captura diferida no funciona con débito, el medio más usado por estas familias | ADR-027. `parte-tecnica-jorge.md` §3.2 |
| 35 | 6 | Probado contra Transbank con crédito y con débito | `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md` |
| 36 | 6 | Un retorno repetido no cobra de nuevo. El pago y su aviso van juntos a un outbox, que se despacha cada cinco minutos | `docs/arquitectura.md` §8.4 y §12.4, caso 5. `TESTER/2026-11-16-sprint-5-cola.md`, H8 |
| 37 | 6 | El comercio no ve de quién es el pedido ni a dónde va, y el código sirve una vez | `docs/lenguaje.md` §36. `TESTER/2026-11-16-sprint-5-cola.md` (MATU-63) |
| 38 | 7 | La familia paga $5.990 al mes y el comercio el 10 %: bastan 84 familias. Solo con despacho, 429 | `docs/arquitectura.md` §16.2 y §16.4. `docs/modelo-datos.md`, `liquidacion` |
| 39 | 7 | 6 de 10 ya pagan hoy por algún servicio de cuidado | `docs/arquitectura.md` §16.1. `docs/resultados-entrevistas.md` §3 (H4) y §4 |
| 40 | 7 | Los familiares que aportan también lo pagarían | `docs/resultados-entrevistas.md` §8 |
| 41 | 7 | Ejercicio de viabilidad, no una proyección (al pie de la lámina 15) | `docs/arquitectura.md` §16.6 |
| 42 | 7 | Tres pasos: el pago dividido, los medicamentos y los pilotos municipales | `docs/resultados-entrevistas.md` §8. `docs/arquitectura.md` §15.1. `docs/modelo-datos.md` §11 |
| 43 | 8 | Tres personas que se benefician | Lámina 17 |
| 44 | 8 | Casi todas las que cuidan en casa lo hacen sin pago | ENDIDE 2022 (96,4 %) |
| 45 | 8 | Aprendimos que fijar el criterio antes de medir cambia el producto, y que probar en cada cambio evita sorpresas | ADR-023 (H1 y la ficha de tres campos). El CI de `main` |

---

## 7. Para decidir (Jorge y Martín)

1. **Los nombres en pantalla durante la demo.** La semilla los trae, en las cuentas, la persona cuidada, la ficha, la página del relevo y los comercios. Propongo una semilla de presentación con nombres de rol, que es código de Jorge con la revisión de Martín. Si no alcanza, una familia creada a mano en la demo, en unos 20 minutos de Martín. El relevo se crea con un nombre de rol, como «Relevo».
2. **La demo en el computador,** con cuatro ventanas y el zoom al 200 %, y Martín manejando todo. Jorge vigila el tiempo y dice la frase del plan B en la capa 1.
3. **Si la escena 7 pasa de 50 s en el ensayo:**
   - Jorge escribe la tarjeta mientras Martín narra;
   - o se guarda la tarjeta de prueba en el autocompletado del navegador;
   - o se pasa a las capturas PB8 y PB9.
4. **GitHub abierto en las preguntas,** con `TESTER/`, la última corrida verde de Actions y `backend/tests/e2e/`. Las capturas del plan B, como láminas ocultas al final.
5. **Las cifras 27, 308 y los 17 controles son de `main` al 22/11.** Se recuentan si entra otro cambio antes de presentar. Si la presentación es después del 1/12, la Ley 21.719 ya se dice «vigente».

---

## 8. Lo que va solo en el anexo A, y lo que no se dice

**Va en el anexo A, si la comisión lo pregunta:**
- lo que pasa con la carga cuando hay más volumen de datos (pregunta 1);
- el trabajo con agentes de IA y los commits (pregunta 11);
- las fechas del calendario y el factor de cada sprint (pregunta 13);
- la conciliación con el comercio (pregunta 15);
- la app nativa (pregunta 17).

**No se dice, porque no está en `docs/`:**
- el total y el envío del pedido de la demo, que se leen en la pantalla;
- los datos de la tarjeta y del banco de prueba de Webpay, que son públicos de Transbank y van solo en el papel.

---

## Anexo A · Respuestas preparadas para la comisión

**Es el criterio 3 de la planilla** (20 puntos). Son 20 preguntas, con respuestas de dos o tres frases, de unos 30 segundos. Jorge responde las de arquitectura y seguridad, aunque Martín presente el bloque 5.

### Cómo se responde

- **Responde quien está asignado.** El otro agrega una frase solo si suma un dato.
- **Primero la respuesta, después la evidencia:** «Sí, y está en…».
- **Cada ajuste de alcance o de meta es una decisión del equipo,** con su razón, aprobada por el Product Owner y registrada con su fecha. Se dice con seguridad.
- **Si un hecho no tiene más encuadre que el hecho,** se dice breve y con su dato, sin dramatizar.
- **Si no se sabe:** «Eso no lo medimos. Lo que sí medimos es…». Nunca se inventa una cifra.
- **Sin nombres propios.** Se habla de la cuidadora, la persona cuidada, el relevo, la familia y el comercio.

| # | Pregunta | Responde |
|---|---|---|
| 1 | ¿Escala? ¿Cómo se fijó la meta de carga? | Jorge |
| 2 | ¿Cómo protegen los datos de salud? | Jorge |
| 3 | ¿Qué datos guardan de la persona, y quién los ve? | Jorge |
| 4 | ¿Qué impide probar los 10.000 PIN, y qué pasa si el enlace se reenvía? | Jorge |
| 5 | ¿Qué pasa si el retorno de Webpay llega dos veces, o nunca llega? | Jorge |
| 6 | ¿Cómo evitan que una conexión del pool arrastre la familia de otra petición? | Jorge |
| 7 | Si hay respaldos, ¿cuándo queda ilegible de verdad la ficha? | Jorge |
| 8 | ¿Qué pasa si se quita la capa 3? | Jorge |
| 9 | ¿Quién autoriza por la persona cuidada, si ella no puede? | Jorge |
| 10 | ¿Se sostiene el negocio? | Jorge |
| 11 | ¿Cómo trabajaron con agentes de IA, y por qué hay commits de «Claude»? | Jorge |
| 12 | ¿En qué se diferencia de WhatsApp, un delivery o una app de cuidado? | Martín |
| 13 | ¿Cómo cupo el alcance en cinco sprints, y cómo lo controlaron? | Martín |
| 14 | ¿Cambiaron los objetivos en el camino? | Martín |
| 15 | ¿Por qué no se ve la conciliación con el comercio? | Martín |
| 16 | ¿Por qué un solo cobro y no una reserva? | Martín |
| 17 | ¿Por qué una app en el navegador y no una nativa? | Martín |
| 18 | ¿Cómo saben que el relevo entiende la ficha, y qué pasa si se bloquea el PIN? | Martín |
| 19 | ¿Cómo hicieron la usabilidad, y qué cambió entre rondas? | Martín |
| 20 | ¿Cómo se repartieron los roles de Scrum? | Martín |

---

### 1. ¿Escala? ¿Cómo se fijó la meta de carga?

- **Responde:** Jorge
- **Respuesta:** Para el piloto, sí. La meta la fijó el Product Owner el 20 de noviembre y está registrada en la arquitectura, en RNF-05: con 10 usuarios a la vez, 0 % de fallos y la mediana de cada paso bajo 800 milisegundos, porque el piloto atiende a pocas familias. Se cumplió el 21 y el 22 de noviembre, y la meta de producción, el percentil 95 bajo 800 ms con 50 usuarios, se mide en un equipo representativo antes de salir a producción, porque el computador de prueba, de 2 núcleos y un solo proceso, se satura con 50.
- **El percentil 95, que la lámina 12 informa:** con 10 usuarios, 814 ms en total y 1,8 s en el retorno del pago.
- **Si preguntan qué pasa con más datos:** con mucho volumen acumulado, el pago se vuelve más lento. Está identificado en la arquitectura con su causa probable, las políticas de seguridad por fila de las tablas del pago, y con su forma de confirmarlo (`EXPLAIN (ANALYZE, BUFFERS)`) y de corregirlo antes de producción, con un índice o una migración revisada.
- **Fuente:**
  - `docs/arquitectura.md` §2.2, RNF-05, en los párrafos «La meta de RNF-05 para el piloto (20-11)» y «El pago se encarece con el volumen (22-11)».
  - `TESTER/2026-11-21-MATU-80-k6-cierre.md` y `TESTER/2026-11-22-MATU-80-carga-meta.md`, anexo.
  - `TESTER/2026-11-20-MATU-80-k6-tercera.md`.

### 2. ¿Cómo protegen los datos de salud?

- **Responde:** Jorge
- **Respuesta:** Cada familia está aislada en PostgreSQL con Row Level Security forzado, la app entra con un rol sin privilegios de dueño, y un recurso de otra familia responde 404: lo verifican 308 pruebas en cada cambio. La ficha va cifrada con AES-256-GCM y una clave por persona, y nunca aparece en registros, direcciones ni en el almacenamiento del navegador. La Ley 21.719, en plena vigencia desde el 1 de diciembre de 2026, trata los datos de salud como sensibles, y la tomamos como requisito de diseño: MATU no pide datos clínicos, tiene su política de privacidad y su registro de tratamientos, y cada historia con datos personales se revisó contra la normativa antes y al cierre.
- **Fuente:** `docs/arquitectura.md` §2.2 (RNF-07 y RNF-08), §11.4 y §11.6. `test_aislamiento.py` en `origin/main` 6038105. `docs/legal/politica-privacidad.md` y `docs/legal/registro-tratamientos.md`.

### 3. ¿Qué datos guardan de la persona, y quién los ve?

- **Responde:** Jorge
- **Respuesta:** De la persona guardamos su nombre, el nivel de apoyo, la ficha que escribe la familia, cifrada, y lo que usa, sin datos clínicos. Cada uno ve lo suyo:
  - quien solo se informa no ve montos;
  - el relevo ve solo las secciones que se eligieron al compartir, y hasta que vence el enlace;
  - el comercio ve solo los productos, sin la persona ni la dirección;
  - el equipo de operación nunca ve la ficha.

  La familia puede descargar una copia de sus datos desde la app, o borrar los de la persona en el acto.
- **Fuente:** `docs/arquitectura.md` §3.1 (RF-01), §7.7 y §11.6. `docs/lenguaje.md` §14.3, §31, §36 y §40. `TESTER/2026-11-12-MATU-54-mis-datos.md` y `TESTER/2026-11-09-MATU-72-borrar-al-tiro.md`.

### 4. ¿Qué impide probar los 10.000 PIN, y qué pasa si el enlace se reenvía?

- **Responde:** Jorge
- **Respuesta:** El token del enlace tiene 256 bits y se guarda solo su SHA-256, y el PIN se guarda como un HMAC con un secreto del servidor, ligado a ese acceso, así que quien leyera la tabla no lo recupera. Probar los 10.000 PIN no sirve: el quinto incorrecto bloquea el enlace, y el canje tiene además un límite de 10 intentos por hora por conexión, contado en Redis sin guardar la IP. Si el enlace se reenvía, sin el PIN que se dicta por teléfono no abre, cada apertura y cada PIN incorrecto aparecen en «Quién la vio», donde la cuidadora lo corta al instante, y como el token va en el fragmento de la dirección y se canjea por una cookie de sesión efímera, no queda en el historial de un teléfono prestado.
- **Fuente:**
  - `docs/api/README.md` del repositorio del código: las huellas del token y del PIN, `token_hash` con SHA-256 y `pin_hash` con HMAC-SHA-256 y `PEPPER_PIN`.
  - `docs/modelo-datos.md`, tabla `acceso_relevo`, con un máximo de 5 intentos fallidos.
  - `docs/backlog-sprints-1-3.md`, MATU-25, con `/v1/relevo/canje` a 10 por hora por IP en Redis.
  - `docs/arquitectura.md` §11.6, en «Acceso de relevo» y «API», y §7.7, con `indice_token.revocado_en`.
  - `docs/lenguaje.md` §7.3, §9 y §15.

### 5. ¿Qué pasa si el retorno de Webpay llega dos veces, o nunca llega?

- **Responde:** Jorge
- **Respuesta:** La idempotencia es de MATU y no de la pasarela: cada pago lleva su clave de idempotencia y el token de la venta queda registrado, así que un retorno repetido no crea otro cargo ni paga el pedido dos veces, y lo probamos contra Transbank el 10 de noviembre. Si el retorno nunca llega, porque la familia cerró el navegador, la tarea de conciliación consulta cada 5 minutos el estado de toda venta iniciada hace más de 10 y la cierra en menos de 15 minutos, con el resultado escrito en una sola transacción junto con su evento en el outbox. Elegimos tareas programadas en Railway, y no un proceso en escucha, porque la arquitectura excluye todo componente que exija operación continua para un equipo de dos.
- **Fuente:**
  - `docs/arquitectura.md`:
    - §8.2, «Cuatro defensas» y la conciliación cada 5 minutos (D-62-17);
    - §12.4, casos 5 y 6;
    - §8.6, el contrato del outbox;
    - §7.7, «Cómo quedó en el semestre» (MATU-74);
    - §2.1, las restricciones.
  - `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`, caso 4.

### 6. ¿Cómo evitan que una conexión del pool arrastre la familia de otra petición?

- **Responde:** Jorge
- **Respuesta:** Toda petición pasa por un solo helper, `sesion_tenant`, que abre una transacción y fija primero el usuario y después la familia con `set_config(…, true)`: ese `true` deja el ajuste local a la transacción, así que la conexión vuelve al pool sin la familia anterior, y una consulta sin `app.grupo_id` devuelve cero filas. Saltarse la seguridad por fila tampoco se puede sin querer, porque la API entra como `matu_app`, que no es dueño de las tablas ni superusuario, y toda tabla de negocio tiene `FORCE ROW LEVEL SECURITY`. Lo verifican `test_conexion_app.py`, que revisa con qué rol se conecta la API, y las 308 pruebas de aislamiento.
- **Fuente:** `docs/arquitectura.md` §7.7 («Contexto de sesión», el código de `sesion_tenant` y el párrafo sobre `set_config`) y §2.2 (RNF-07). `CLAUDE.md` §5, punto 2.

### 7. Si hay respaldos, ¿cuándo queda ilegible de verdad la ficha?

- **Responde:** Jorge
- **Respuesta:** Al borrar a la persona, MATU destruye su clave de datos, y la ficha queda ilegible en la base en ese momento, sin que la clave se pueda volver a llenar. El borrado se completa cuando vence el último respaldo que todavía contiene esa clave, y por eso la retención de los respaldos se fija antes de tratar datos reales. El sobre-cifrado protege sobre todo contra el robo de respaldos y de disco, porque sin la clave maestra, que en producción vive en un servicio de custodia, lo robado no se lee, y frente a una API comprometida va el registro de uso de la clave maestra, con alerta por volumen.
- **Si preguntan dónde está hoy la clave maestra:** en una variable de entorno, porque solo hay datos de prueba. Es un desvío declarado y aprobado por el Product Owner el 28 de octubre, y se reemplaza sin tocar el cifrado, porque está detrás de un puerto.
- **Fuente:** `docs/arquitectura.md`:
  - §11.4;
  - §7, la tabla `clave_datos` (migración 0003);
  - §11.8, la retención;
  - §14, el ADR-016 y su desvío aprobado;
  - §17, el borrado criptográfico y el último respaldo.

### 8. ¿Qué pasa si se quita la capa 3?

- **Responde:** Jorge
- **Respuesta:** Se apaga con un interruptor, `CAPA3_HABILITADA`, y la API arranca sin los módulos del despacho, con un contrato que muestra solo las capas 1 y 2. Hay 27 pruebas que verifican que nada de las capas 1 y 2 depende de la capa 3, y que las dos siguen funcionando con ella bloqueada: la ficha, compartir, el relevo con PIN, el consumo y los avisos. La familia sigue con su lista de insumos, que se imprime o se comparte y sirve en cualquier tienda.
- **Si preguntan por qué se diseñó así:** ningún convenio con comercios estaba garantizado, y el despacho desacoplable elimina el único punto de falla externo del proyecto.
- **Fuente:** `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md`. `test_capa3_desacoplable.py` en `origin/main` 6038105. `docs/arquitectura.md` §1, decisión 2. ADR-031.

### 9. ¿Quién autoriza por la persona cuidada, si ella no puede?

- **Responde:** Jorge
- **Respuesta:** Sin una autorización vigente, MATU no guarda ni muestra la ficha. Al registrar a la persona, MATU anota quién autoriza y en qué calidad: la propia persona, su representante legal o quien la cuida de hecho, que hace una declaración, ve un aviso de su límite y la renueva cada año. La ficha, los insumos y los pedidos tienen cada uno su propia autorización, y cada una se puede retirar.
- **Si preguntan si eso basta ante la ley:** el diseño no trata la declaración de quien cuida de hecho como si fuera la del titular. Por eso el piloto opera con datos de prueba, y esa figura se valida con asesoría legal como paso previo a tratar datos reales.
- **Fuente:** `docs/arquitectura.md` §11.5. `docs/lenguaje.md` §6.4, §6.4b y §22.

### 10. ¿Se sostiene el negocio?

- **Responde:** Jorge
- **Respuesta:** Con suscripción, sí. Sobre 200 familias, con la canasta medida (una mediana de $70.000 y una compra al mes), una comisión del 10 %, una última milla supuesta de $3.500 y unos $600.000 al mes de costos fijos, cada familia deja $7.210 al mes y bastan 84, contra 429 cobrando solo el despacho. La capa 2 es el diferenciador, aunque H3 se validó justo en el umbral, 6 de 10, porque cuatro de las ocho que pagarían $5.990 lo condicionaron a que resuelva los insumos, y un delivery no puede calcular cuándo se acaba algo sin conocer a la persona.
- **Si preguntan qué incluyen los $600.000:** la arquitectura los fija como un total de costos fijos austeros, sin desglose. La pasarela y la última milla van aparte, como costos variables.
- **Si preguntan cómo se valida la comisión del 10 %:** con el primer convenio. El primer comercio a contactar es la farmacia de barrio que ya trabaja con cuenta corriente y boleta para una familia entrevistada, con una carta de intención de una página, y el municipio es el canal para llegar a las familias.
- **Fuente:**
  - `docs/arquitectura.md` §16.1, §16.2, §16.4 y §16.6, y §18.1, «Convenio comercial».
  - `docs/resultados-entrevistas.md` §3 (H3 y H4), §5 (la farmacia de E07 para la carta de intención) y §8 (H7).
  - `docs/protocolo-entrevistas.md`, anexo A.
  - `README.md`, capa 2.

### 11. ¿Cómo trabajaron con agentes de IA, y por qué hay commits de «Claude»?

- **Responde:** Jorge
- **Respuesta:** Los agentes de IA escribieron buena parte del código, las pruebas y los borradores de documentos a partir de nuestras instrucciones, y por eso hay commits con Claude como autor o como coautor, como lo declara el calendario de sprints desde el 13 de octubre. Las decisiones son de las personas: el Product Owner decide el alcance, las prioridades y los criterios, y aprueba cada ADR y cada texto de la app, y el Scrum Master revisa, prueba en el teléfono y fusiona cada pull request, con su informe en `TESTER/`. Ningún cambio entra a la rama principal sin el CI en verde y sin esa revisión, las pruebas de las reglas críticas las define una persona, y nunca se usan datos reales.
- **Si preguntan cuántos commits:** en `main` del repositorio del código hay 1569 commits. 46 tienen a Claude como autor, y la gran mayoría lo lleva como coautor. Todos entraron por un pull request revisado.
- **Si preguntan cuánto aceleró:** las horas estimadas sin IA contra las reales dieron un factor de 1,86 en el semestre (154,5 h contra 83,11 h), contando solo las horas de la persona.
- **Fuente:**
  - `docs/sprints/calendario-sprints.md` §2, que declara el desarrollo asistido, las pruebas críticas definidas por una persona y el uso exclusivo de datos sintéticos.
  - `docs/adr/ADR-030-roles-del-equipo.md`. `CLAUDE.md` §5.
  - `docs/sprints/sprint-5-planificacion.md` §8, «Con vibecoding no hay excepciones».
  - `parte-tecnica-jorge.md` §4.3.
  - `git log origin/main` del repositorio del código, en 6038105.

### 12. ¿En qué se diferencia de WhatsApp, un delivery o una app de cuidado?

- **Responde:** Martín
- **Respuesta:** Cada uno resuelve una parte:
  - un delivery trae pañales, pero no sabe qué necesita la persona ni cuándo se acaba;
  - un chat guarda la rutina, pero no vence, no se corta cuando la cuidadora vuelve y no avisa nada;
  - la teleasistencia, como Mis Tatas, cobra entre $10.000 y $39.000 al mes y acompaña a la persona, no el traspaso entre quienes la cuidan.

  MATU junta lo que falta: la ficha que se comparte y se corta, el aviso antes de que se acabe un insumo y, si se quiere, el pedido. Por eso el despacho no es el diferenciador: tres de diez entrevistadas ya compran por aplicación, y están conformes.
- **Fuente:** `docs/arquitectura.md` §16.3 (Mis Tatas) y §16.5 (los tres sustitutos). `README.md`, «MATU no es una aplicación de delivery». Las notas en el WhatsApp como registro propio: `docs/lenguaje.md` §4.

### 13. ¿Cómo cupo el alcance en cinco sprints, y cómo lo controlaron?

- **Responde:** Martín
- **Respuesta:** Cupo porque el alcance se decidió por escrito antes del primer sprint: dos decisiones de alcance, de 41 y de 160 horas, dejaron 213 horas comprometidas contra 270 de capacidad, y el 13 de octubre el calendario agrupó en cinco sprints semanales, con dos de reserva, lo que la arquitectura repartía en ocho. Cada sprint tuvo su planificación, su revisión y su retrospectiva, y medimos el factor entre horas estimadas y reales, que fue de 1,80, 2,77, 1,48, 2,20 y 1,09, con 1,86 en el semestre, sobre el umbral de 1,4 que fijó el calendario. Y la revisión del sprint 3 cambió el equipo: ese día dejamos fijo, en el ADR-030, el reparto por rol que habíamos probado esa semana, con 15 historias cerradas.
- **Si preguntan por las fechas:** los siete objetivos llegaron dentro del calendario, el último el 20 de noviembre, el primer día de la reserva.
- **Si preguntan cómo se usó la IA:** ver la pregunta 11. El calendario de sprints agrupó el alcance en cinco sprints contando con ese factor, y lo midió en cada retrospectiva.
- **Fuente:**
  - `docs/sprints/calendario-sprints.md` §1 a §3.
  - `docs/arquitectura.md` §15.2 (414 contra 270 horas), §15.3 (las dos decisiones de alcance y el resultado de 213 horas) y §15.4.
  - `parte-tecnica-jorge.md` §4.3.
  - `docs/adr/ADR-030-roles-del-equipo.md`.
  - `TESTER/2026-11-20-MATU-80-recorridos.md`.

### 14. ¿Cambiaron los objetivos en el camino?

- **Responde:** Martín
- **Respuesta:** Tres cambiaron su redacción, y cada cambio fue una decisión del Product Owner registrada con su fecha:
  - **el 6, el pago,** pasó a un solo cobro del total exacto con el ADR-027, del 26 de octubre, porque la prueba de concepto mostró que la captura diferida no funciona con débito;
  - **el 5, la lista,** pasó a texto sin enlace con el ADR-031, del 6 de noviembre, porque un enlace expondría el consumo, que tratamos como dato de salud;
  - **el 7** fijó sus seis recorridos críticos el 8 de noviembre.

  La meta de carga del piloto se decidió igual, el 20 de noviembre, y está en la arquitectura (pregunta 1).
- **Fuente:** `parte-tecnica-jorge.md` §3.1, §3.2 y §3.3, con la redacción original y la vigente. `docs/adr/ADR-027-precios-exactos.md` y `docs/adr/ADR-031-lista-insumos-solo-texto.md`. `docs/arquitectura.md` §15.4 y §2.2.

### 15. ¿Por qué no se ve la conciliación con el comercio?

- **Responde:** Martín
- **Respuesta:** Es una decisión de alcance del 17 de noviembre: con comercios ficticios no hay boletas reales que conciliar, así que la conciliación automática se dejó para el primer convenio. Mientras tanto, la consola de operación muestra en solo lectura lo que MATU le debe a cada comercio, y el cierre se hace en planilla, como define la arquitectura desde la primera decisión de alcance. Está registrada, con su razón, en la arquitectura y en la parte técnica.
- **Fuente:** `parte-tecnica-jorge.md` §2.3, «Requisitos *Debe*». `docs/arquitectura.md` §15.3, primer recorte («Liquidación automática»). `docs/legal/revision-previa-matu-81.md` (D-81-11).

### 16. ¿Por qué un solo cobro y no una reserva?

- **Responde:** Martín
- **Respuesta:** La captura diferida de Transbank solo funciona con crédito, el débito es el medio más usado por estas familias, y una retención mayor que el pedido es difícil de explicar, como observó el análisis de la Ley 19.496. Con precios exactos, la familia ve el total antes de pagar, se cobra una sola vez en venta normal de Webpay Plus, y si un producto falta se anula su parte a la misma tarjeta. El 10 de noviembre lo probé contra el ambiente de integración, y dieron PASS los cuatro casos: crédito, débito, una anulación parcial de $8.990 con los dos medios y un retorno duplicado que dejó un solo cobro.
- **Fuente:** `docs/adr/ADR-027-precios-exactos.md`. `parte-tecnica-jorge.md` §3.2. `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`.

### 17. ¿Por qué una app en el navegador y no una nativa?

- **Responde:** Martín
- **Respuesta:** MATU es una app móvil que en el semestre es una aplicación web progresiva: corre en el navegador del teléfono y se instala en la pantalla de inicio, sin pasar por una tienda, por una decisión del 14 de octubre que sugirió el profesor guía. Nos dio un solo lenguaje para la familia, el relevo y el comercio, la accesibilidad del navegador, y lo clave para el relevo: abrir la ficha con un enlace. Una participante de la usabilidad lo dijo así: «Me gusta que sea rápido de usar en el celular, sin tener que descargar aplicaciones pesadas».
- **Si preguntan por los avisos en iPhone:** llegan cuando se agrega MATU a la pantalla de inicio, y el correo es el canal garantizado. La app nativa se decide con los datos del piloto.
- **Fuente:**
  - `docs/adr/ADR-026-aplicacion-web.md`.
  - El manifiesto en `web/index.html` (MATU-55) y `web/public/sw.js`, en `main`.
  - `docs/lenguaje.md` §33.
  - `docs/usabilidad/ronda-2-informe.md`, citas (P1).

### 18. ¿Cómo saben que el relevo entiende la ficha, y qué pasa si se bloquea el PIN?

- **Responde:** Martín
- **Respuesta:** La ficha está hecha para leerse con apuro: tres campos con las palabras de las cuidadoras, «A quién llamar» arriba, «Su día» hora a hora y sin los ejemplos, para que nadie llame a un número de ejemplo, y en la usabilidad las tres participantes la abrieron como relevo con el PIN en poco más de un minuto. En el piloto, que la entiende se medirá preguntando después de cada relevo si necesitó algo que no estaba escrito, contra la línea base de las entrevistas, donde 6 de 9 relevos fallaron por algo que solo sabía la cuidadora. Si el PIN se escribe mal cinco veces, el enlace se bloquea por seguridad, la página le dice al relevo que pida uno nuevo, y la cuidadora ve el bloqueo en «Quién la vio» y crea otro enlace en menos de dos minutos.
- **Si preguntan qué pasa si la cuidadora no contesta:** el enlace no abre sin el PIN. Es la misma regla que impide que un enlace reenviado abra la ficha.
- **Fuente:**
  - `docs/lenguaje.md` §4, §5.3 (los ejemplos solo para quien escribe), §7.3 y §15.
  - MATU-95, «A quién llamar» a primera vista (`parte-tecnica-jorge.md` §2.3).
  - `docs/usabilidad/ronda-1-informe.md`, tarea 5, con 1:20, 1:10 y 1:20.
  - `docs/usabilidad/ronda-2-informe.md`, U2, compartir con PIN bajo 2 minutos.
  - `docs/arquitectura.md` §1.1, con los 6 de 9 relevos.
  - La forma de medirlo en el piloto es la propuesta del equipo, y no tiene datos todavía.

### 19. ¿Cómo hicieron la usabilidad, y qué cambió entre rondas?

- **Responde:** Martín
- **Respuesta:** Fueron dos rondas de tres personas, con las mismas metas: la ficha en menos de 3 minutos sin ayuda, compartir con PIN en menos de 2 y el pedido en menos de 6. La ronda 1, con un prototipo, llevó a la app la pregunta guía con un ejemplo en la pantalla de quien escribe y el envío del enlace desde el teléfono con el PIN aparte, y en la ronda 2, ya con la app, la ficha y el compartir pasaron de 1 de 3 a 3 de 3. Los sesgos están declarados en los informes: tres sesiones por ronda, dos de tres participantes de la segunda con el mismo perfil y llegadas por familiares del moderador, y el mismo moderador en las dos rondas.
- **Si preguntan qué costó en la ronda 2:** declarar el consumo con envases cerrados y unidades sueltas. Se resolvió después en «Me quedan» (MATU-109).
- **Fuente:**
  - `docs/usabilidad/ronda-1-informe.md`, hallazgos U1 y U2.
  - `docs/usabilidad/ronda-2-informe.md`, tiempos y «Limitaciones».
  - `docs/lenguaje.md` §5.
  - `parte-tecnica-jorge.md` §2.3 (MATU-109).

### 20. ¿Cómo se repartieron los roles de Scrum?

- **Responde:** Martín
- **Respuesta:** Por rol, con el ADR-030:
  - el Product Owner lleva dos sombreros, porque decide el producto y también lo desarrolla;
  - el Scrum Master cuida el proceso, la calidad, el despliegue y las pruebas con usuarios, y revisa cada cambio antes de que entre.

  Lo probamos una semana y lo dejamos fijo el 5 de noviembre, en la revisión del sprint 3, después de que ese sprint cerrara 15 historias, y las entrevistas las hicimos cinco cada uno. Como cada rol depende de una persona, el estado vive en los repositorios, los cambios son chicos y el orden de prioridades está escrito.
- **Fuente:**
  - `docs/adr/ADR-030-roles-del-equipo.md`.
  - `docs/arquitectura.md` §15.5 y §17.
  - `docs/resultados-entrevistas.md` §1, columna «Entrevistador».

---

### Si preguntan algo que no está aquí

- **Una cifra que no tenemos:** «Eso no lo medimos. Lo que sí medimos es…», y se pasa al dato más cercano que tenga fuente.
- **Una decisión:** se nombra su ADR, en `docs/adr/`:
  - el 023: la ficha de tres campos;
  - el 026: la app en el navegador;
  - el 027: un solo cobro;
  - el 028: la ficha ampliada;
  - el 029: la ficha no se imprime;
  - el 030: los roles;
  - el 031: la lista como texto.
- **Cuánto se construyó:**
  - en `main` hay 36 migraciones reversibles (`docs/arquitectura.md` §7.8);
  - al 18/11/2026 había 2371 funciones de prueba en el backend y 103 archivos de prueba en la web (`parte-tecnica-jorge.md` §1).

---

## Anexo B · Capturas del plan B

Se toman con la demo recién restablecida (`docs/entorno-demo.md` §3). **Ninguna muestra nombres** (punto 1 de «Para decidir»), ni la barra de direcciones con el enlace del relevo, el PIN, el código de retiro o los datos de la tarjeta.

| Código | Pantalla | Dónde se usa |
|---|---|---|
| PB1 | La ficha, «3 de 3 campos listos» | Plan B, escena 1 |
| PB2 | «Enlaces», con el del relevo «Activo» | Plan B, escena 2 |
| PB3 | La ficha abierta por el relevo: «A quién llamar» arriba y «Su día» como línea de tiempo | Plan B, escena 3 |
| PB4 | «Quién la vio», con la apertura del relevo | Plan B, escena 4 |
| PB4b | La ventana del relevo con «Este enlace se cortó» | Plan B, escena 4 |
| PB5 | «Insumos», con el bloque «Se acaban pronto» | Plan B, escena 5 |
| PB6 | «Lista de insumos», con «Copiamos la lista» | Plan B, escena 6 |
| PB7 | «Antes de pagar», con el total | Plan B, escena 6 |
| PB8 | Webpay en integración, sin los datos de la tarjeta | Plan B, escena 7 |
| PB9 | «Pagaste tu pedido», con el sello «Pago de prueba» | Plan B, escena 7 |
| PB10 | Consola del comercio: «Código correcto. Entrega el pedido…» | Plan B, escena 8 |
| PB-video | El recorrido completo de la demo, de 60 a 90 s, grabado en el ensayo | Plan B de cualquier escena |

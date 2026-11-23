# MATU · Presentación final · Guion hablado

**23/11/2026** · Lo escribe el guionista para la tarjeta de la presentación final (MATU-104). Lo revisan Jorge y Martín, y se ensaya con cronómetro (MATU-111).
**Incluye:** el anexo A, con las preguntas probables de la comisión, y el anexo B, con las capturas del plan B.
**Reparto:** el de Jorge, en ocho bloques. Cuatro son de Jorge (2, 3, 7 y la capa 1 de la demo) y cuatro de Martín (1, 4, 5, 8 y las capas 2 y 3 de la demo).

---

## 0. Cómo se lee este guion

- **El texto entre comillas angulares o en cita es lo que se dice, palabra por palabra.** Lo que va entre corchetes es una indicación: un cambio de lámina, una pausa o un clic. No se lee.
- **El tiempo se midió con un script** que cuenta las palabras tal como se dicen. Por ejemplo, «96,4 %» son siete palabras: «noventa y seis coma cuatro por ciento». A eso suma las pausas y las esperas de la demo, que son los segundos en que la pantalla carga y nadie habla.
- **Se dan dos ritmos:** 130 palabras por minuto, que es el lento, y 140, el rápido. El guion está hecho para el lento: **a 130 dura 8:30, y a 140 dura 7:57.** El tope es 9:00, así que quedan entre 30 segundos y un minuto de margen.
- **Las esperas de la demo son estimaciones.** Se confirman en el ensayo con la demo restablecida. Si una escena se alarga, se corta su última frase, nunca se habla más rápido.
- **Las personas son ficticias:** Carmen, María, Luisa y Rodrigo son las de la semilla de la demo (`infra/semillas/demo.py`). Nadie de las entrevistas aparece con nombre.

---

## 1. Los tiempos

### 1.1 Por bloque

| Bloque | Láminas | Habla | Inicio | Término | Palabras | Pausas y esperas | Duración a 130 | A 140 | Referencia de Jorge |
|---|---|---|---|---|---|---|---|---|---|
| 1 · Portada y equipo | 1 y 2 | Martín | 0:00 | 0:26 | 53 | 1 s | **0:26** | 0:24 | 0:25 |
| 2 · Contexto, el problema y la propuesta | 3, 4 y 5 | Jorge | 0:26 | 2:07 | 213 | 3 s | **1:41** | 1:34 | 1:20 |
| 3 · Objetivos, alcance y requerimientos | 6, 7 y 8 | Jorge | 2:07 | 2:56 | 100 | 3 s | **0:49** | 0:46 | 1:00 |
| 4 · Metodología, cronograma y tecnologías | 9, 10 y 11 | Martín | 2:56 | 3:44 | 100 | 2 s | **0:48** | 0:45 | 0:50 |
| 5 · Arquitectura y modelo de datos | 12 y 13 | Martín | 3:44 | 4:45 | 127 | 2 s | **1:01** | 0:56 | 1:05 |
| 6 · Demo, capa 1 | 14 y la app | Jorge | 4:45 | 5:47 | 112 | 10 s | **1:02** | 0:58 | 1:10 |
| 6 · Demo, capas 2 y 3 | la app | Martín | 5:47 | 7:14 | 161 | 13 s | **1:27** | 1:22 | 1:20 |
| 7 · Modelo de negocios y próximos pasos | 15 y 16 | Jorge | 7:14 | 7:58 | 92 | 2 s | **0:45** | 0:41 | 0:45 |
| 8 · Reflexión y cierre | 17 | Martín | 7:58 | 8:30 | 61 | 4 s | **0:32** | 0:30 | 0:30 |
| **Total** | **17** | | **0:00** | **8:30** | **1019** | **40 s** | **8:30** | **7:57** | 8:25 |

### 1.2 Por persona

| Persona | Bloques | Palabras | A 130 | A 140 |
|---|---|---|---|---|
| **Jorge** | 2, 3, capa 1 de la demo y 7 | 517 | **4:17** | 4:00 |
| **Martín** | 1, 4, 5, capas 2 y 3 de la demo y 8 | 502 | **4:14** | 3:57 |
| Diferencia | | | 3 s | 3 s |

### 1.3 Por qué cambia el reparto de referencia

- **El bloque 2 sube de 1:20 a 1:41.** Es uno de los tres de mayor impacto, y Jorge pidió recoger en él la solidez de la Fase 1: las cifras de ENDIDE, los dos problemas que son uno, la cita, las tres capas y la hipótesis refutada. No cabía en 1:20 sin perder la validación, que es lo que distingue a MATU de una idea.
- **El bloque 3 baja de 1:00 a 0:49** para compensar. El detalle de cada objetivo queda en la lámina 6 y en el mapa de evidencia (sección 4), y la mitad de los objetivos se ve en vivo en la demo.
- **En la demo, Martín sube a 1:27 y Jorge baja a 1:02.** El pago en Webpay obliga a esperar pantallas que la capa 1 no tiene. Aun así, la demo completa dura 2:29, un segundo menos que la referencia.
- **Los dos quedan casi iguales:** 4:17 y 4:14.

---

## 2. El guion, bloque por bloque

### Bloque 1 · Portada y equipo · Martín · 0:00 a 0:26

**En pantalla:** lámina 1 (portada) y lámina 2 (equipo).

> [Lámina 1]
> Buenas tardes. Somos Jorge Espinoza y Martín Henríquez. Les presentamos MATU, una app para que el cuidado de una persona mayor no se corte cuando quien la cuida sale.
> [Pausa de 1 s · lámina 2]
> Jorge es Product Owner y desarrolla con seis agentes de IA. Yo soy Scrum Master: despliego, pruebo y fusiono. **Jorge les cuenta por qué.**

- **Paso a Jorge:** «Jorge les cuenta por qué». Martín mira a Jorge al decirlo.
- **53 palabras · 0:26.**
- **Fuentes:** roles, `docs/adr/ADR-030-roles-del-equipo.md`. App móvil que en el semestre corre en el navegador, `docs/adr/ADR-026-aplicacion-web.md`.

### Bloque 2 · Contexto, el problema y la propuesta · Jorge · 0:26 a 2:07

**En pantalla:** lámina 3 (contexto), lámina 4 (los dos problemas que son uno) y lámina 5 (las tres capas).

> [Lámina 3]
> Carmen cuida a su mamá, María, y este sábado tiene que salir. Pero el día de María, qué la calma, a quién llamar, lo sabe solo ella.
> Carmen es inventada. El problema, no. En Chile, casi un millón y medio de personas adultas viven con dependencia. El 96,4 % de quienes las cuidan en casa no recibe pago, y el 41,3 % no tiene un cuidador formal. No falta gente: falta poder traspasar el cuidado.
> [Pausa de 1 s · lámina 4]
> Entrevistamos a diez cuidadoras. Nueve dejaron de salir por falta de relevo o por lo que cuesta explicar. Seis se quedaron sin un insumo. Parecen dos problemas. Son el mismo: todo depende de una sola persona. Una lo dijo así: «Eso no estaba en la hoja porque yo lo sé y se me olvidó que los demás no.»
> [Pausa de 2 s, en silencio. Es la pausa más importante del guion · lámina 5]
> Por eso MATU tiene tres capas, y el orden importa. La ficha de relevo es el producto. El aviso de cuándo se acaba un insumo, el diferenciador. El despacho, un servicio que se puede quitar.
> La ficha tiene tres campos porque escribimos los criterios antes de entrevistar. Pedíamos que siete de diez llenaran el plan en cinco minutos, y lo lograron tres. La hipótesis se refutó y el producto cambió.

- **Cómo se dice:** la primera frase va lenta, como quien cuenta algo. «Carmen es inventada. El problema, no.» marca el paso del relato a las cifras. La cita se lee más despacio que el resto, y después se calla.
- **213 palabras · 1:41.**
- **Fuentes:**
  - 1.498.977 personas adultas con dependencia, 96,4 % de quienes cuidan en el hogar sin remuneración y 41,3 % sin cuidador formal: ENDIDE 2022, citado en `docs/arquitectura.md` §1.1.
  - Diez entrevistas, 9 de 10 dejaron de salir por falta de relevo o por el costo de explicar, y 6 de 10 con un insumo que se acabó en los últimos tres meses: `docs/arquitectura.md` §1.1 y `docs/resultados-entrevistas.md` §3 (H2 y H3).
  - La cita: `docs/resultados-entrevistas.md` §6, entrevista E06. Va sin código ni edad, como se anonimizó en la Fase 1.
  - Las tres capas y su orden: `docs/arquitectura.md` §1, decisiones 1 y 2, y `CLAUDE.md` §1.
  - Criterios escritos antes de entrevistar: `docs/protocolo-entrevistas.md` §7. H1 pedía 7 de 10 bajo cinco minutos y la lograron 3: `docs/resultados-entrevistas.md` §3. La ficha de tres campos: `docs/adr/ADR-023-cierre.md`.

### Bloque 3 · Objetivos, alcance y requerimientos · Jorge · 2:07 a 2:56

**En pantalla:** lámina 6 (los siete objetivos), lámina 7 (alcance) y lámina 8 (requerimientos).

> [Pausa de 1 s · lámina 6]
> Nos comprometimos a una plataforma que parte del plan de cuidado, avisa cuándo se acaba cada insumo y coordina su reposición y pago, en un entorno de demostración. Los siete objetivos están cumplidos, con su evidencia en Git, y cinco los verán en vivo. Uno llegó un día tarde: el despliegue final fue el 20 de noviembre.
> [Pausa de 1 s · lámina 7]
> El alcance puso primero lo que nunca se sacrifica: la ficha, el enlace con PIN, el aviso y la lista.
> [Pausa de 1 s · lámina 8]
> De 25 requisitos obligatorios, cumplimos 24. Falta conciliar la boleta del comercio, que sin comercios reales no existe. **Martín les cuenta cómo trabajamos.**

- **Cómo se dice:** «Uno llegó un día tarde» va en el mismo tono que el resto, sin disculparse. Al decir «cinco los verán en vivo», Jorge señala los sellos 3 a 7 de la lámina.
- **Paso a Martín:** «Martín les cuenta cómo trabajamos».
- **100 palabras · 0:49.**
- **Fuentes:**
  - El objetivo general, dicho en corto: el de la presentación de la Fase 2, lámina 4, y de la Fase 1, lámina 10 (`Fase 2/Evidencias Grupales/` y `Fase 1/`, que no se tocan).
  - Siete objetivos cumplidos: `Fase 3/Evidencias Grupales/parte-tecnica-jorge.md` §3 para los seis primeros. El 7, con el despliegue final de `main` (e8c468b) el 20/11/2026 a las 13:23 y los recorridos R1 a R6 en OK en el teléfono entre las 16:45 y las 16:57: `TESTER/2026-11-20-MATU-80-recorridos.md`. Ese informe dice por qué fue el 20 y no el 19.
  - Lo que nunca se sacrifica: `docs/arquitectura.md` §15.3.
  - 24 de 25 requisitos *Debe*, con RF-31 pendiente: `parte-tecnica-jorge.md` §2.3. RF-31 sigue como *Debe* en `docs/arquitectura.md` §3.3.

### Bloque 4 · Metodología, cronograma y tecnologías · Martín · 2:56 a 3:44

**En pantalla:** lámina 9 (metodología), lámina 10 (cronograma) y lámina 11 (tecnologías).

> [Lámina 9]
> Trabajamos con Scrum, en sprints de una semana. Jorge construye cada cambio con los agentes y abre un pull request con el CI en verde. Yo lo pruebo en el teléfono, y recién ahí lo fusiono: son 45 informes en el repositorio. Con personas: tres de tres llenaron la ficha en menos de tres minutos.
> [Pausa de 1 s · lámina 10]
> Los objetivos llegaron en el orden prometido, y medimos la IA: lo estimado en casi dos horas tomó una.
> [Pausa de 1 s · lámina 11]
> MATU es una app móvil, con tecnología conocida: React, FastAPI, PostgreSQL y Webpay. Hoy se abre desde el navegador del teléfono, sin instalar nada.

- **Cómo se dice:** al decir «45 informes», Martín señala la miniatura del informe de GitHub en la lámina 9. «Lo estimado en casi dos horas tomó una» es el factor 1,86 de la lámina 10, dicho para el oído.
- **100 palabras · 0:48.**
- **Fuentes:**
  - Sprints de viernes a jueves: `docs/sprints/calendario-sprints.md`. El camino de cada cambio: ADR-030 y `docs/sprints/sprint-5-planificacion.md` §8 (definición de terminado, punto 5).
  - 45 informes en `TESTER/`, del 05/11/2026 al 22/11/2026, sin contar el README (listado de la carpeta, 23/11/2026). **Si llegan más antes de la presentación, se actualiza la cifra en la lámina 2, en la 9 y aquí.**
  - Tres de tres completaron la ficha bajo tres minutos y sin ayuda: `docs/usabilidad/ronda-2-informe.md`, tarea U1.
  - Factor de 1,86, sobre 154,5 h estimadas y 83,11 h reales: `parte-tecnica-jorge.md` §4.3.
  - El stack: `CLAUDE.md` §2. La app en el navegador, sin instalar nada: ADR-026.

### Bloque 5 · Arquitectura y modelo de datos · Martín · 3:44 a 4:45

**En pantalla:** lámina 12 (arquitectura) y lámina 13 (modelo de datos). Al final, la lámina 14.

> [Pausa de 1 s · lámina 12]
> La arquitectura es un monolito modular: con dos personas, no se justifican microservicios. Las dependencias van solo hacia abajo: la ficha no sabe que existe el despacho. Por eso la capa 3 se apaga, y 21 pruebas verifican que lo demás sigue funcionando.
> Y medimos la carga del pago. Con diez compras a la vez, no hubo fallos, y la mediana de cada paso quedó bajo 800 milisegundos. Pero el pago se encarece cuando la base acumula pedidos. Está escrito, con su plan, para antes de producción.
> [Pausa de 1 s · lámina 13]
> Para otra familia, María no existe: PostgreSQL aísla cada familia con Row Level Security, y lo verifican 270 pruebas. La ficha va cifrada con una clave por persona. Destruir esa clave la borra.
> [Lámina 14]
> **El sábado de Carmen, en vivo.**

- **Cómo se dice:** «Pero el pago se encarece…» va en el mismo tono que «no hubo fallos». Es una limitación con su plan, no una confesión. Al decir «se apaga», Martín señala el interruptor de la lámina 12.
- **Paso a Jorge:** «El sábado de Carmen, en vivo». Jorge toma la palabra en la escena 1 de la demo.
- **127 palabras · 1:01.**
- **Fuentes:**
  - Monolito modular, y por qué no microservicios: `docs/arquitectura.md` §1, decisión 4, y §2.1.
  - Dependencias hacia abajo: `CLAUDE.md` §2, verificadas por `test_arquitectura.py`.
  - La capa 3 se apaga con `CAPA3_HABILITADA`, con 21 pruebas en `test_capa3_desacoplable.py`: `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md`.
  - La carga del piloto: con 10 compras simultáneas en k6, sobre una base recién preparada, 0 % de fallos y medianas de 453 ms al confirmar y de 421 ms en el retorno: `TESTER/2026-11-22-MATU-80-carga-meta.md`, anexo. La meta del piloto y el párrafo «El pago se encarece con el volumen»: `docs/arquitectura.md` §2.2, RNF-05.
  - El aislamiento por familia y el 404 ante un recurso ajeno: `docs/arquitectura.md` §2.2, RNF-07. Las 270 pruebas son las funciones de `test_aislamiento.py` al 18/11/2026: `parte-tecnica-jorge.md` §3, objetivo 2.
  - El cifrado con una clave por persona y el borrado al destruirla: `docs/arquitectura.md` §11.4 y RNF-08.

### Bloque 6 · Demo · Jorge (capa 1) y Martín (capas 2 y 3) · 4:45 a 7:14

**En pantalla:** la lámina 14 unos segundos, y después la app en vivo. El detalle de cada escena, con sus clics y su plan B, está en la sección 3.

> **Escena 1 · Jorge** · [Espera de 2 s: se pasa de la lámina 14 a la app de Carmen]
> Esta es la app de Carmen, y esta, la ficha de María: su día, si se altera y a quién llamar.
>
> **Escena 2 · Jorge**
> Antes de salir, la compartió con Luisa: un enlace que vence solo y un PIN que le dictó por teléfono.
> [Espera de 1 s]
>
> **Escena 3 · Jorge** · [Espera de 2 s: se pasa al teléfono de Luisa]
> Este es el teléfono de Luisa: sin cuenta y sin instalar nada. Escribe el PIN…
> [Espera de 3 s: se escribe el PIN y abre la ficha]
> y ahí está. Arriba, a quién llamar. Después, su día, hora por hora. Y si se angustia en la tarde, boleros a volumen bajo.
>
> **Escena 4 · Jorge** · [Espera de 2 s: se vuelve a la app de Carmen]
> Carmen ve que Luisa abrió la ficha. Al volver, corta el enlace, y deja de abrir al instante.
> Luisa ya sabe qué hacer. **Lo que nadie alcanza a vigilar, lo muestra Martín.**
>
> **Escena 5 · Martín** · [Espera de 1 s]
> Carmen anotó una vez lo que usa María: cuatro pañales al día. Con eso, MATU calcula cuándo se acaba cada insumo, y avisa antes. Al pañal le quedan dos días.
>
> **Escena 6 · Martín**
> La lista sugiere cuánto comprar para un mes, sin el nombre de María. Se imprime o se comparte, y sirve aunque no haya despacho.
>
> **Escena 7 · Martín**
> O se pide con MATU, a precio exacto, y el total se confirma antes de pagar.
> [Espera de 3 s: MATU confirma que haya cada producto]
>
> **Escena 8 · Martín**
> Paga Rodrigo, el hijo, desde su teléfono, en Webpay. MATU nunca ve la tarjeta. Se cobra una sola vez el total que vio, con crédito o débito: así lo probamos contra Transbank. Es el ambiente de prueba, sin dinero real.
> [Espera de 6 s: Webpay autoriza y vuelve a MATU]
> Pagado, una sola vez.
>
> **Escena 9 · Martín** · [Espera de 1 s: se pasa a la consola del comercio]
> El pago de Rodrigo llega al comercio en unos minutos, así que este lo pagamos antes. El comercio, de prueba, no ve de quién es ni a dónde va. Solo escribe el código de retiro, que sirve una vez…
> [Espera de 2 s: «Código correcto»]
> y entrega. **Jorge les cuenta cómo se sostiene.**

- **Paso de Jorge a Martín:** «Lo que nadie alcanza a vigilar, lo muestra Martín».
- **Paso de Martín a Jorge:** «Jorge les cuenta cómo se sostiene». En ese momento se vuelve a la presentación, a la lámina 15.
- **Capa 1: 112 palabras y 10 s de espera · 1:02. Capas 2 y 3: 161 palabras y 13 s de espera · 1:27. Total de la demo: 2:29.**
- **Fuentes:** en la sección 3, escena por escena.

### Bloque 7 · Modelo de negocios y próximos pasos · Jorge · 7:14 a 7:58

**En pantalla:** lámina 15 (modelo de negocios) y lámina 16 (próximos pasos).

> [Pausa de 1 s: se vuelve de la app a la presentación · lámina 15]
> ¿Se sostiene? Solo con despacho, harían falta 429 familias. Con una suscripción de $5.990 al mes, además del despacho, bastan 84. Ocho de diez entrevistadas la pagarían, y la mitad, si resuelve los insumos. Es un cálculo de viabilidad, no una proyección.
> [Pausa de 1 s · lámina 16]
> Lo que viene, en orden. Primero, lo que exige operar con datos reales: la consulta legal y la clave maestra fuera del servidor. Después, el pago entre familiares. Y lo que más esperamos: un piloto con un municipio, con familias reales. **Martín cierra.**

- **Cómo se dice:** «$5.990» se dice «cinco mil novecientos noventa pesos». La última frase, la del piloto, es la de mayor énfasis del bloque: es lo que esperamos para MATU.
- **Paso a Martín:** «Martín cierra».
- **92 palabras · 0:45.**
- **Fuentes:**
  - 429 y 84 familias, la suscripción de $5.990 y la comisión del 10 % por pedido, sobre 200 familias: `docs/arquitectura.md` §16.2 y §16.4.
  - 8 de 10 dijeron que sí a $5.990, y 4 lo condicionaron a que resuelva los insumos: `docs/resultados-entrevistas.md` §3 (H4). Es una pregunta hipotética (`docs/arquitectura.md` §16.1).
  - «Ejercicio de viabilidad, no compromiso de alcance»: `docs/arquitectura.md` §3, «Cobertura», y §16.6.
  - Lo que falta antes de datos reales, con la consulta legal: `parte-tecnica-jorge.md` §5.2. La clave maestra en un servicio de custodia: `docs/arquitectura.md` §11.4.
  - El pago entre familiares como fase 2, prioridad 1: `docs/resultados-entrevistas.md` §8, decisiones de Jorge del 11/11.
  - El municipio como canal: `docs/resultados-entrevistas.md` §8 (H7 validada, con las cuatro entrevistas por los grupos de personas mayores del municipio). El piloto con un municipio es lo que esperamos, no un compromiso.

### Bloque 8 · Reflexión y cierre · Martín · 7:58 a 8:30

**En pantalla:** lámina 17. La franja del sábado de María vuelve, ahora con las 22:00 completas.

> [Pausa de 1 s · lámina 17]
> Antes, lo que Carmen sabía se iba con ella. Esta vez, a las diez de la noche, Luisa dejó encendida la luz del pasillo, porque estaba en la ficha.
> [Pausa de 2 s]
> Ese es el impacto que buscamos. Para quien cuida, casi siempre sin pago, poder salir unas horas. Para la persona cuidada, que su día siga igual.
> [Pausa de 1 s]
> Gracias. Quedamos atentos a sus preguntas.

- **Cómo se dice:** Martín mira a la comisión, no a la pantalla. «Porque estaba en la ficha» responde a la cita del bloque 2, «eso no estaba en la hoja». Jorge se pone a su lado para las preguntas.
- **61 palabras · 0:32.**
- **Fuentes:** «se acuesta a las 22:00 con la luz del pasillo encendida», en «Su día» de María (`infra/semillas/demo.py`, `FICHA_MARIA`). «Casi siempre sin pago»: el 96,4 % de ENDIDE 2022 (`docs/arquitectura.md` §1.1).

### 2.1 Las frases de paso, juntas

| De | A | Frase exacta | Momento |
|---|---|---|---|
| Martín | Jorge | «Jorge les cuenta por qué.» | 0:26, de la lámina 2 a la 3 |
| Jorge | Martín | «Martín les cuenta cómo trabajamos.» | 2:56, de la lámina 8 a la 9 |
| Martín | Jorge | «El sábado de Carmen, en vivo.» | 4:45, en la lámina 14 |
| Jorge | Martín | «Lo que nadie alcanza a vigilar, lo muestra Martín.» | 5:47, dentro de la demo |
| Martín | Jorge | «Jorge les cuenta cómo se sostiene.» | 7:14, de la app a la lámina 15 |
| Jorge | Martín | «Martín cierra.» | 7:58, de la lámina 16 a la 17 |

---

## 3. La demo, escena por escena

### 3.1 Qué está preparado y qué se hace en vivo

| | Preparado antes | En vivo |
|---|---|---|
| Capa 1 | La ficha de María completa (la siembra la semilla). El enlace de Luisa ya creado, con su PIN anotado en papel. El teléfono de Luisa abierto en la pantalla del PIN | Luisa escribe el PIN y abre la ficha. Carmen ve «Luisa abrió la ficha» |
| Capa 2 | Los insumos de María, con el pañal a punto de acabarse (la semilla) | Se muestran el aviso y la lista |
| Capa 3 | Un pedido pagado antes, ya preparado por el comercio y con su código de retiro generado en la consola de operación, anotado en papel | Carmen arma el pedido desde la lista y confirma el total. Rodrigo paga en Webpay. El comercio valida el código del pedido preparado y entrega |

**Por qué el retiro se hace con un pedido preparado:** el pago llega al comercio con la tarea de despacho, que corre cada 5 minutos (`TESTER/2026-11-16-sprint-5-cola.md`, hallazgo H8). En 1:27 no se puede esperar. Martín lo dice en voz alta, como pidió ese hallazgo.

### 3.2 La preparación, el día de la presentación

Lo hace Martín, dueño del entorno de demostración (ADR-030). **Ningún PIN, código de retiro, contraseña ni enlace del relevo se escribe en un chat, un documento o un commit** (`docs/entorno-demo.md` §5). Van solo en un papel.

1. **En la mañana, restablecer la demo** desde cero (`docs/entorno-demo.md` §3, unos 2 segundos). Así el pañal dice «Alcanza para 2 días» el mismo día. Si se restableció el día anterior, dirá 1 día, y la frase de la escena 5 se ajusta a lo que diga la pantalla.
2. **Crear el enlace de Luisa** desde la app de Carmen: «Compartir con un relevo», nombre «Luisa», su celular sintético de la serie `+56 9 0000 00xx`, vigencia «24 horas», motivo «Fin de semana fuera» y la casilla «Le avisé a Luisa…». **Anotar el PIN en papel.**
3. **Abrir el enlace en la ventana de Luisa,** en pantalla completa (F11), para que la barra de direcciones con el enlace no se proyecte. Debe quedar en «Carmen te compartió la ficha de María», con el campo del PIN vacío.
4. **Preparar el pedido del retiro, entre 75 y 60 minutos antes de la presentación.** El código vence a los 90 minutos (`docs/legal/registro-tratamientos.md`, código de retiro).
   - Carmen agrega un paquete de «Pañal adulto M x30» de Almacén El Ejemplo, que es el comercio de la cuenta `comercio@example.com`, y confirma el total.
   - Rodrigo paga con la tarjeta de prueba.
   - Se espera la tarea de despacho, como máximo 5 minutos.
   - En la consola del comercio: «Empezar a preparar», «Lo tengo» y «Listo para retirar».
   - En la consola de operación, que pide la contraseña y el código del teléfono: el pedido, la parte, «Generar el código». **Se anota en papel.**
   - Si la presentación se atrasa más de una hora, se genera uno nuevo con «Generar un código nuevo», y el anterior deja de servir.
5. **Dejar abiertas cuatro ventanas,** cada una en su propio perfil del navegador, porque cada cuenta entra por separado. Todas con el zoom al 200 %, que la app admite sin desplazamiento horizontal (RNF-09):
   - **Carmen,** en la ficha de María;
   - **Luisa,** en pantalla completa, en la pantalla del PIN;
   - **Rodrigo,** en su inicio;
   - **el comercio,** en el pedido preparado, con el campo «Código de retiro» a la vista.
6. **La tarjeta de prueba** es la AMEX de crédito o la Redcompra de débito del ambiente de integración. La VISA y la Mastercard de crédito de prueba no pasan en venta normal (`TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`, hallazgo H2).
7. **Internet:** la red de la sala, y el teléfono de Martín como punto de acceso de respaldo.
8. **Las notificaciones del computador, apagadas.** Las capturas y el video del plan B, abiertos y a un clic (sección 3.4).

### 3.3 Las escenas

Quién maneja el equipo es una decisión pendiente (sección 7, punto 2). Lo que sigue supone la propuesta: **Martín maneja toda la demo, y Jorge solo habla en la capa 1.**

| Escena | Minuto | Habla | Ventana | Clic exacto | Lo que se ve y se dice | Fuente | Plan B |
|---|---|---|---|---|---|---|---|
| **1 · La ficha** | 4:45 a 4:57 | Jorge | Carmen | Pasar de la presentación a la ventana de Carmen. Ya está en la ficha | «Ficha de relevo», «3 de 3 campos listos». Jorge nombra los tres campos | `docs/lenguaje.md` §5 y §5.4. La ficha de María en `infra/semillas/demo.py` | PB1 |
| **2 · El enlace con PIN** | 4:57 a 5:07 | Jorge | Carmen | Pestaña «Enlaces» | El enlace de Luisa, «Activo». Jorge dice que vence solo y que el PIN se dictó por teléfono | `docs/lenguaje.md` §9 y §9.1 | PB2 |
| **3 · Luisa abre la ficha** | 5:07 a 5:30 | Jorge | Luisa | Escribir el PIN del papel y tocar «Ver la ficha» | «Carmen te compartió la ficha de María». Abre la ficha: «A quién llamar» arriba, «Su día» como línea de tiempo y «Si se altera» con los boleros | `docs/lenguaje.md` §7.1 y §7.4. MATU-95, «A quién llamar» a primera vista (`parte-tecnica-jorge.md` §2.3). Semilla | PB3 |
| **4 · Quién la vio** | 5:30 a 5:47 | Jorge | Carmen | Pestaña «Quién la vio», o el bloque «Últimas aperturas» de la ficha | «Luisa abrió el enlace» y «Luisa abrió la ficha». Jorge dice que, al volver, Carmen corta el enlace, pero **no se corta en vivo** | `docs/lenguaje.md` §9 y §15. Cortar el enlace: §9, «deja de abrir de inmediato» | PB4 |
| **5 · Cuándo se acaba** | 5:47 a 6:01 | Martín | Carmen | Sección «Insumos» | El bloque «Se acaban pronto», con el pañal: «Alcanza para 2 días» y «Te estamos avisando» | Semilla: 4 al día y 8 en casa, con aviso desde 7 días (`infra/semillas/demo.py`). `docs/lenguaje.md` §13.1 y §17 | PB5 |
| **6 · La lista** | 6:01 a 6:12 | Martín | Carmen | Pestaña «Lista de insumos» | La cantidad sugerida en envases y los botones «Imprimir o guardar en PDF», «Compartir la lista» y «Copiar la lista». No se toca ninguno | `docs/lenguaje.md` §21. ADR-031. Objetivo 5 | PB6 |
| **7 · El pedido** | 6:12 a 6:23 | Martín | Carmen | «Pedir estos productos», después «Ver el total» | «Antes de pagar · Confirmamos que hay cada producto. El total es…» y «Este total vale hasta las…» | `docs/lenguaje.md` §31. ADR-027 | PB7 |
| **8 · Un solo cobro** | 6:23 a 6:49 | Martín | Rodrigo | «Ver el resumen», la casilla de las condiciones, «Pagar $…», y en Webpay la tarjeta de prueba hasta aprobar | Webpay de integración. Al volver: «Pagaste tu pedido · Pagaste $… una sola vez. Es el total que viste antes de pagar.», con el sello «Pago de prueba» | `docs/lenguaje.md` §32. `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`. R5 en el teléfono: `TESTER/2026-11-21-MATU-80-k6-cierre.md` | PB8 y PB9 |
| **9 · El retiro con código** | 6:49 a 7:14 | Martín | Comercio | Escribir el código del papel en «Código de retiro (6 números)» y tocar «Revisar código» | «Pedidos de hoy · Aquí ves solo los productos.» y, al validar, «Código correcto. Entrega el pedido…» | `docs/lenguaje.md` §36. R6 en el teléfono: `TESTER/2026-11-20-MATU-80-recorridos.md`. El código de un solo uso: `TESTER/2026-11-16-sprint-5-cola.md` (MATU-63) | PB10 |

**Al volver a la presentación** (7:14), Martín pasa a la lámina 15 mientras dice «Jorge les cuenta cómo se sostiene».

### 3.4 El plan B, con la frase exacta para pasar a él

**La regla:** quien está hablando dice la frase, y quien maneja abre las capturas o el video. Las capturas PB1 a PB10 y el video están listados en el anexo B, en «Capturas que hay que tomar». El texto de cada escena sirve igual sobre la captura: no se cambia.

| Si falla | Quién lo dice | Frase exacta | Qué se muestra |
|---|---|---|---|
| La app no carga o la red se cae, en la capa 1 | Jorge | «La conexión nos está fallando. Les muestro lo mismo en las capturas de esta mañana.» | PB1 a PB4, una por escena |
| La red se cae en la capa 2 | Martín | «Sigo con las capturas, que muestran lo mismo.» | PB5 y PB6 |
| Webpay no responde | Martín | «Webpay, el ambiente de prueba de Transbank, no responde ahora. No se cobró nada. Esto es lo que vieron en el ensayo.» | PB7, PB8 y PB9 |
| El código de retiro venció o se bloqueó | Martín | «Venció: el código sirve noventa minutos y una sola vez. Así se ve cuando es el correcto.» | PB10 |
| Se cae todo, o quedan menos de 2 minutos para la demo | Quien esté hablando | «Les mostramos el mismo recorrido en el video que grabamos en el ensayo.» | El video, de 60 a 90 s, sin audio. Se narra con el texto de las escenas que falten |

**La frase de Webpay sale de la app:** es el texto «Webpay no responde ahora. No se cobró nada.» de `docs/lenguaje.md` §32. Así el plan B también muestra cómo MATU le habla a una familia cuando algo falla.

### 3.5 Después de la demo

- **Cortar el enlace de Luisa** desde la app de Carmen, al terminar la presentación: el PIN se escribió frente a la sala.
- **El código de retiro ya se usó** y no sirve de nuevo. Si hubo plan B y el código quedó sin usar, se genera uno nuevo antes de volver a mostrarlo.
- Si se proyectó un dato que no debía, se restablece la demo (`docs/entorno-demo.md` §5: «si se pega uno por error, se rota»).

### 3.6 Lo que se revisa en el ensayo (MATU-111)

- [ ] El cronómetro de cada bloque. Si la demo pasa de 2:40, se corta la escena 6 (la lista) y se dice en la 7: «la lista también se imprime o se comparte».
- [ ] La lista de insumos muestra solo el pañal, y «Pedir estos productos» lo agrega.
- [ ] Con el pedido preparado ya pagado, Carmen puede armar uno nuevo desde la lista.
- [ ] La tarjeta de prueba que se va a usar pasa en Webpay ese día.
- [ ] La ventana de Luisa no muestra la barra de direcciones en el proyector.
- [ ] «Quién la vio» muestra «Luisa abrió la ficha» después de la escena 3.
- [ ] Desde el fondo de la sala, la app con el zoom al 200 % se lee bien.
- [ ] Se graba el video del plan B y se toman las capturas PB1 a PB10.

---

## 4. Mapa de evidencia por objetivo

Es el criterio 2 de la planilla, el de más peso (25). Cada objetivo tiene su evidencia en Git y un momento del guion donde se dice o se ve.

| # | Objetivo (redacción corta) | Evidencia en Git | Dónde aparece |
|---|---|---|---|
| 1 | Validar las siete hipótesis con criterios escritos antes de entrevistar | `docs/protocolo-entrevistas.md` §7. `docs/resultados-entrevistas.md` §3 y §8. `docs/adr/ADR-023-cierre.md` | Bloque 2 (H1 refutada y la ficha de tres campos) y láminas 4 y 5 |
| 2 | Modelo de datos con aislamiento entre familias, probado contra una base real | 31 pruebas al cierre del sprint 0 (`docs/arquitectura.md` §15.4). 270 funciones en `test_aislamiento.py` al 18/11 (`parte-tecnica-jorge.md` §3). El CI las corre en cada push, en verde en la corrida 44439817400 del 18/11 (`parte-tecnica-jorge.md` §1) | Bloque 5 y lámina 13 |
| 3 | Ficha con acceso de relevo que vence y se corta, «Quién la vio» y borrado criptográfico | Cumplido el 29/10/2026 (`docs/arquitectura.md` §15.4). R1 y R2 en el teléfono (`TESTER/2026-11-09-MATU-64-demo.md` y `TESTER/2026-11-20-MATU-80-recorridos.md`). Pruebas de punta a punta `test_recorrido_1_alta_y_ficha.py` y `test_recorrido_2_relevo.py` (`parte-tecnica-jorge.md` §3.3) | Demo, escenas 1 a 4. Bloque 5 (la clave por persona) |
| 4 | Fecha en que se acaba cada insumo y aviso anticipado, con ocho pruebas de dominio | Cumplido el 05/11/2026 (`parte-tecnica-jorge.md` §3). Las ocho pruebas son el criterio de aceptación (`docs/arquitectura.md` §7, perfil de consumo). MATU-37 en PASS en el teléfono (`TESTER/2026-11-05-pruebas-telefono.md`). R3 | Demo, escena 5 |
| 5 | La lista de insumos, operativa sin convenio comercial | #57 y `TESTER/2026-11-07-MATU-60-lista-insumos.md`. R4 y `test_recorrido_4_lista_y_compra.py`. La capa 3 apagada: `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md` | Demo, escena 6. Bloque 5 (la capa 3 se apaga) |
| 6 | El pedido con un solo cobro del total exacto, con los nueve casos de pago | `backend/tests/modules/payments/test_casos_pago.py`. Los cuatro casos contra Transbank el 10/11, con PASS: `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`. `TESTER/2026-11-12-MATU-62-pago.md` | Demo, escenas 7 y 8 |
| 7 | Desplegado en un entorno de demostración, con los seis recorridos y el pipeline en verde | Despliegue final de `main` el 20/11, y R1 a R6 en OK en el teléfono: `TESTER/2026-11-20-MATU-80-recorridos.md`. Los seis recorridos como pruebas de punta a punta en cada push: `backend/tests/e2e/` (#106) | Bloque 3 (el día de atraso) y toda la demo, que corre sobre ese entorno. Escena 9, R6 |

---

## 5. Cobertura de la planilla

| Criterio | Puntos | Dónde se cumple | Riesgo |
|---|---|---|---|
| 1 · Relevancia, objetivos, metodología y desarrollo | 15 | Relevancia: bloque 2. Objetivos: bloque 3. Metodología: bloque 4. Desarrollo: bloques 5 y 6 | Bajo |
| 2 · Evidencias del cumplimiento de los objetivos | 25 | Bloque 3 (7 de 7, con su fecha, y 24 de 25), bloque 4 (45 informes y la usabilidad), bloque 5 (21 pruebas, 270 pruebas y la carga) y la demo (cinco objetivos en vivo). El mapa de la sección 4 da la evidencia de cada uno para las preguntas | **Medio.** La evidencia de los objetivos 1, 2 y 4 se dice en una frase. Si la comisión la pide, se responde con el mapa y se muestra en GitHub (sección 7, punto 6) |
| 3 · Respuestas a las preguntas de la comisión | 20 | el anexo A: 12 preguntas, con quién responde y su fuente | Depende del ensayo de las respuestas |
| 4 · Formato y tiempo | 5 | 8:30 a ritmo lento, con 30 s de margen. 17 láminas en el orden de Jorge, con una idea por lámina | Bajo, si la demo se cronometra en el ensayo |
| 5 · Fluidez, claridad, precisión y lenguaje técnico | 5 | Frases cortas, seis frases de paso (sección 2.1) y un relato, el sábado de María, que une el inicio, la demo y el cierre | Bajo |
| 6 · Documentación y evidencias en Git | 20 | Bloque 3 («con su evidencia en Git»), bloque 4 («45 informes en el repositorio») y la línea de evidencia de la lámina 6. Cada dato del guion tiene su ruta en Git (sección 6) | **Medio.** Se dice, pero no se muestra el repositorio en vivo. Ver la sección 7, punto 6 |
| 7 · Lenguaje técnico disciplinar y manejo de la información | 10 | Bloque 4 (Scrum, pull request, CI) y bloque 5 (monolito modular, dependencias, mediana en milisegundos, Row Level Security, cifrado con una clave por persona). Las preguntas lo profundizan | Bajo |

---

## 6. Las afirmaciones y su fuente

Cada dato que se dice en voz alta, en el orden en que aparece.

| # | Bloque | Lo que se dice | Fuente |
|---|---|---|---|
| 1 | 1 | Jorge es PO y desarrolla con seis agentes. Martín es Scrum Master: despliega, prueba y fusiona | ADR-030 |
| 2 | 2 | Casi un millón y medio de personas adultas con dependencia (1.498.977) | ENDIDE 2022, en `docs/arquitectura.md` §1.1 |
| 3 | 2 | 96,4 % de quienes cuidan en casa no recibe pago | Ídem |
| 4 | 2 | 41,3 % no tiene un cuidador formal | Ídem |
| 5 | 2 | Diez cuidadoras entrevistadas | `docs/resultados-entrevistas.md` §1 |
| 6 | 2 | Nueve dejaron de salir por falta de relevo o por el costo de explicar | `docs/arquitectura.md` §1.1 |
| 7 | 2 | Seis se quedaron sin un insumo (en los últimos tres meses) | Ídem, y `docs/resultados-entrevistas.md` §3 (H3) |
| 8 | 2 | La cita «Eso no estaba en la hoja…» | `docs/resultados-entrevistas.md` §6, E06 |
| 9 | 2 | Tres capas, en ese orden: producto, diferenciador y servicio que se quita | `docs/arquitectura.md` §1. `CLAUDE.md` §1 |
| 10 | 2 | Criterios escritos antes de entrevistar. Se pedían 7 de 10 en cinco minutos, y lo lograron 3. H1 refutada | `docs/protocolo-entrevistas.md` §7. `docs/resultados-entrevistas.md` §3. ADR-023 |
| 11 | 3 | El objetivo general, en corto | Presentación de la Fase 2, lámina 4, y de la Fase 1, lámina 10 |
| 12 | 3 | Siete objetivos cumplidos, con evidencia en Git | `parte-tecnica-jorge.md` §3. `TESTER/2026-11-20-MATU-80-recorridos.md` |
| 13 | 3 | El 7, un día tarde: despliegue final el 20 de noviembre | `TESTER/2026-11-20-MATU-80-recorridos.md`, «Despliegue» |
| 14 | 3 | Lo que nunca se sacrifica: ficha, enlace con PIN, aviso y lista | `docs/arquitectura.md` §15.3 |
| 15 | 3 | 24 de 25 requisitos obligatorios. Falta RF-31, la conciliación de la boleta | `parte-tecnica-jorge.md` §2.3. `docs/arquitectura.md` §3.3 |
| 16 | 4 | Scrum en sprints de una semana | `docs/sprints/calendario-sprints.md` |
| 17 | 4 | El camino de cada cambio: agentes, PR con CI en verde, prueba en el teléfono y fusión | ADR-030. `docs/sprints/sprint-5-planificacion.md` §8 |
| 18 | 4 | 45 informes de revisión en el repositorio | Listado de `TESTER/` al 23/11/2026 |
| 19 | 4 | Tres de tres llenaron la ficha en menos de tres minutos | `docs/usabilidad/ronda-2-informe.md`, U1 |
| 20 | 4 | Los objetivos, en el orden del cronograma | `docs/arquitectura.md` §15.4 |
| 21 | 4 | Lo estimado en casi dos horas tomó una (factor 1,86) | `parte-tecnica-jorge.md` §4.3 |
| 22 | 4 | React, FastAPI, PostgreSQL y Webpay. App móvil que se abre desde el navegador, sin instalar nada | `CLAUDE.md` §2. ADR-026 |
| 23 | 5 | Monolito modular. Con dos personas, no se justifican microservicios | `docs/arquitectura.md` §1, decisión 4, y §2.1 |
| 24 | 5 | Dependencias solo hacia abajo | `CLAUDE.md` §2 (`test_arquitectura.py`) |
| 25 | 5 | La capa 3 se apaga, y 21 pruebas lo verifican | `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md` |
| 26 | 5 | Con diez compras a la vez, 0 fallos y medianas bajo 800 ms | `TESTER/2026-11-22-MATU-80-carga-meta.md`, anexo. RNF-05 en `docs/arquitectura.md` §2.2 |
| 27 | 5 | El pago se encarece cuando la base acumula pedidos, con su plan para antes de producción | `docs/arquitectura.md` §2.2, «El pago se encarece con el volumen» (K6) |
| 28 | 5 | Cada familia aislada con Row Level Security, y 270 pruebas | `docs/arquitectura.md` §2.2, RNF-07. `parte-tecnica-jorge.md` §3 |
| 29 | 5 | La ficha cifrada con una clave por persona, y destruirla la borra | `docs/arquitectura.md` §11.4 y RNF-08 |
| 30 | 6 | Ficha de tres campos. Enlace que vence solo, con un PIN dictado por teléfono | `docs/lenguaje.md` §5 y §9 |
| 31 | 6 | El relevo entra sin cuenta y sin instalar nada | `docs/lenguaje.md` §7.1 |
| 32 | 6 | «A quién llamar» arriba, y «Su día» hora por hora | MATU-95 (`parte-tecnica-jorge.md` §2.3). `docs/lenguaje.md` §5.1 |
| 33 | 6 | Si se angustia en la tarde, boleros a volumen bajo | Ficha de María, `infra/semillas/demo.py` |
| 34 | 6 | Carmen ve quién abrió la ficha. Al cortar, el enlace deja de abrir de inmediato | `docs/lenguaje.md` §9 y §15 |
| 35 | 6 | Cuatro pañales al día, y le quedan dos días | `infra/semillas/demo.py` (4 al día, 8 en casa), con la demo restablecida ese día |
| 36 | 6 | La lista sugiere para un mes, sin el nombre de María, y sirve sin despacho | `docs/lenguaje.md` §21. ADR-031. MATU-40 |
| 37 | 6 | Precio exacto y total confirmado antes de pagar | ADR-027. `docs/lenguaje.md` §31 |
| 38 | 6 | MATU nunca ve la tarjeta | `docs/lenguaje.md` §32 |
| 39 | 6 | Un solo cobro, con crédito o débito, probado contra Transbank | `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md` |
| 40 | 6 | Ambiente de prueba, sin dinero real | `docs/lenguaje.md` §11 |
| 41 | 6 | El pago llega al comercio en unos minutos | `TESTER/2026-11-16-sprint-5-cola.md`, H8 |
| 42 | 6 | El comercio no ve de quién es el pedido ni a dónde va | `docs/lenguaje.md` §36 |
| 43 | 6 | El código de retiro sirve una vez | `TESTER/2026-11-16-sprint-5-cola.md` (MATU-63). `docs/legal/registro-tratamientos.md` |
| 44 | 7 | 429 familias solo con despacho, y 84 con la suscripción de $5.990 | `docs/arquitectura.md` §16.4 |
| 45 | 7 | 8 de 10 la pagarían, y la mitad, si resuelve los insumos | `docs/resultados-entrevistas.md` §3 (H4) |
| 46 | 7 | Es un cálculo de viabilidad, no una proyección | `docs/arquitectura.md` §3 y §16.6 |
| 47 | 7 | Primero, la consulta legal y la clave maestra fuera del servidor | `parte-tecnica-jorge.md` §5.2. `docs/arquitectura.md` §11.4 |
| 48 | 7 | Después, el pago entre familiares | `docs/resultados-entrevistas.md` §8 |
| 49 | 7 | Un piloto con un municipio | `docs/resultados-entrevistas.md` §8 (H7, el canal municipal). Es una aspiración y se dice como tal |
| 50 | 8 | La luz del pasillo a las 22:00 está en la ficha | `infra/semillas/demo.py` |
| 51 | 8 | Quien cuida lo hace casi siempre sin pago | ENDIDE 2022 (96,4 %) |

---

## 7. Para decidir (Jorge y Martín)

1. **¿La demo va en el computador o en el teléfono con duplicación de pantalla?**
   - **Propuesta: en el computador,** con cuatro ventanas en perfiles separados y el zoom al 200 %. La duplicación suma un punto de falla (la red o el cable), y la demo necesita cuatro cuentas a la vez: Carmen, Luisa, Rodrigo y el comercio. En R2, Martín ya usó el computador como segundo dispositivo (`TESTER/2026-11-20-MATU-80-recorridos.md`).
   - **Si se elige el teléfono,** la escena 3 sale más natural. Entonces Luisa va en el teléfono duplicado y lo demás en el computador.
   - **Si queda el computador,** la frase «Este es el teléfono de Luisa» pasa a «Esta ventana es el teléfono de Luisa», con una palabra más.
2. **¿Quién maneja el equipo?**
   - **Propuesta: Martín maneja toda la demo.** Es el dueño del entorno de demostración (ADR-030) y el que hizo R1 a R6. En la capa 1 maneja mientras Jorge habla, y en las capas 2 y 3 habla y maneja él. Jorge vigila el tiempo y, si algo falla en la capa 1, dice la frase del plan B.
   - **La otra opción** es que siempre maneje el que no habla. Suma un cambio de manos en el minuto 5:47.
3. **Luisa.** En la semilla, Luisa es miembro del grupo con el rol de cuidadora. En la demo entra por enlace, como relevo, que es lo que pidió el encargo. Si la comisión pregunta, la respuesta es que el relevo no necesita cuenta, así que puede ser cualquiera. **La otra opción** es usar a «Rosa», el relevo que ya siembra la semilla con su PIN fijo, y ahorrar el paso 2 de la preparación. Pero entonces el bloque 2 y la lámina 14 dirían Rosa.
4. **El pie «En Git» de las láminas.** Lo saqué de 15 de las 17 láminas, porque sumaba texto chico que nadie lee desde el fondo. Queda como una sola línea en la lámina 6, la de los objetivos: «Evidencia en Git: `TESTER/` · `parte-tecnica-jorge.md` · `docs/`». En las láminas 3 y 4 queda la fuente del dato, sin ruta, porque una cifra sin fuente no se proyecta. La evidencia en Git se dice en voz alta en los bloques 3 y 4. Si prefieren el pie en todas, está en la versión anterior del archivo de láminas.
5. **El objetivo general en la lámina 6** va abreviado: «Del plan de cuidado al aviso y al pago». Confirmen que la abreviatura les sirve. La redacción completa está en la presentación de la Fase 2, y Jorge la dice en corto en el bloque 3.
6. **¿Se muestra GitHub en las preguntas?** Propongo dejar abierta una pestaña con `TESTER/`, la última corrida verde de Actions y `backend/tests/e2e/`. Si la comisión pregunta por la evidencia, se muestra en 10 segundos. Es lo que más ayuda a los criterios 2 y 6.
7. **El bloque 2 dura 1:41,** no 1:20. Si quieren volver a 1:20, lo primero que sale es «Carmen es inventada. El problema, no.» (2 s). Después, la frase de las tres capas, que la lámina 5 ya muestra (9 s). Lo último sería la hipótesis refutada, pero es lo que Jorge pidió destacar.
8. **Las capturas del plan B:** ¿van como láminas ocultas al final de la presentación (de la 18 en adelante) o en una carpeta aparte? Propongo las láminas ocultas: se llega con un clic y no hay que cambiar de programa.
9. **El video del plan B** lo graba Martín en el ensayo, con la demo restablecida. Ese día se decide si va sin audio, narrado en vivo, que es la propuesta, o con la voz grabada.
10. **Las cifras que cambian con el tiempo:** los 45 informes de `TESTER/` y las 270 pruebas de aislamiento, contadas al 18/11. Si Jorge quiere la cifra del día, se recuenta antes de la presentación con el comando de `parte-tecnica-jorge.md` §6. Si no, se dice «al 18 de noviembre».
11. **La fecha de la presentación.** Si es después del 1 de diciembre, la Ley 21.719 ya está en plena vigencia, y la respuesta de la pregunta 2 cambia «en vigencia plena desde el 1 de diciembre» por «vigente desde el 1 de diciembre».

---

## 8. Lo que no entró, y los datos sin respaldo

**Datos que no se dicen porque no encontré su fuente, o porque cambian:**
- **El total del pedido y el precio del envío de la demo.** Dependen de la cantidad que sugiere la lista ese día. Se leen de la pantalla, y el guion no los dice.
- **El total de PR del semestre.** Solo está documentado el de los sprints 3 a 5 (93 PR, `parte-tecnica-jorge.md` §1). Va en las preguntas con esa precisión, no en el guion.
- **El total de pruebas al día de hoy.** El último conteo con fuente es del 18/11: 2371 funciones de prueba en el backend y 103 archivos de prueba en la web (`parte-tecnica-jorge.md` §1).

**Lo que se dejó fuera para cumplir el tiempo,** y queda para las preguntas:
- los 6 de 9 relevos que fallaron por algo que solo sabía la cuidadora (`docs/arquitectura.md` §1.1);
- por qué el objetivo 7 se atrasó un día (la fila de PR con migraciones, `TESTER/2026-11-20-MATU-80-recorridos.md`);
- el PIN que se muestra una sola vez, y el enlace que se borra de la barra de direcciones;
- el detalle de la carga: las medianas por paso y la base acumulada;
- la app nativa, que está en la lámina 16 y en la pregunta 4.

**Términos.** El guion no usa ninguno de los términos prohibidos de `docs/lenguaje.md` §3. El punto 4 de la estructura de Jorge se nombra aquí «el problema», y la lámina lleva su título-afirmación. Para la persona cuidada se dice «persona mayor» o su nombre. Lo que se acaba es un «insumo» que «se acaba», y lo que hace la familia es «cortar el enlace».

---

## Anexo A · Preguntas probables de la comisión

**Es el criterio 3 de la planilla** (20 puntos). Son 12 preguntas, seis para cada uno, y cada respuesta tiene entre dos y tres frases, unos 30 segundos.

---

### Cómo se responde

- **Responde quien está asignado,** y el otro solo agrega una frase si suma un dato. No se responde a dos voces.
- **Primero la respuesta, después la evidencia.** «Sí, y está en…» convence más que una explicación larga.
- **Si no se sabe, se dice:** «Eso no lo medimos. Lo que sí medimos es…». Nunca se inventa una cifra.
- **La evidencia está en Git.** Si la comisión la pide, se muestra la pestaña de GitHub preparada (guion, sección 7, punto 6).
- **Mismo lenguaje que la app** (`docs/lenguaje.md` §3): «autorización», «cortar el enlace», «Quién la vio», «cuándo se acaba».

| # | Pregunta | Responde |
|---|---|---|
| 1 | ¿Escala? ¿Qué pasó con la carga? | Martín |
| 2 | ¿Cómo protegen los datos de salud? | Jorge |
| 3 | ¿Quién autoriza por la persona cuidada, si ella no puede? | Jorge |
| 4 | ¿Por qué una app en el navegador y no una nativa? | Martín |
| 5 | ¿Cómo controlaron la calidad con agentes de IA? | Jorge |
| 6 | ¿Qué pasa si se quita la capa 3? | Martín |
| 7 | ¿Se sostiene el negocio? | Jorge |
| 8 | ¿Qué faltó? | Martín |
| 9 | ¿Por qué un solo cobro y no una reserva? | Martín |
| 10 | ¿Cómo saben que el problema existe? | Jorge |
| 11 | ¿Por qué el objetivo 7 llegó un día tarde? | Martín |
| 12 | ¿Qué datos guardan de la persona, y quién los ve? | Jorge |

---

### 1. ¿Escala? ¿Qué pasó con la carga?

- **Responde:** Martín
- **Respuesta:** Para el piloto, sí: con diez compras simultáneas sobre una base recién preparada, no hubo fallos y las medianas fueron de 453 ms al confirmar y de 421 ms en el retorno del pago. Encontramos una limitación: con los pedidos de cinco corridas acumulados en la base, esas dos medianas se duplicaron, porque el pago se encarece con el volumen. No se corrige en el semestre, porque la demo se restablece desde cero, pero antes de producción se mide con volumen creciente, se confirma qué consulta crece y se corrige con una migración revisada.
- **Si repreguntan por la causa:** la más probable es el costo de las políticas de seguridad por fila de las tablas del pago (`transaccion_pasarela`, `cargo` y `participacion`) o un índice que falta. No está confirmada.
- **Si repreguntan por 50 compras simultáneas:** esa es la meta de producción (percentil 95 bajo 800 ms), y se mide en un equipo representativo. En el computador de prueba, de 2 núcleos y con un solo proceso de la API, todos los pasos subían juntos con 50: eso apunta a la máquina, no a un paso del código.
- **Fuente:** `TESTER/2026-11-22-MATU-80-carga-meta.md`, anexo. `TESTER/2026-11-20-MATU-80-k6-tercera.md`. `docs/arquitectura.md` §2.2, RNF-05, con los párrafos «La meta de RNF-05 para el piloto» y «El pago se encarece con el volumen».

### 2. ¿Cómo protegen los datos de salud?

- **Responde:** Jorge
- **Respuesta:** Cada familia está aislada en PostgreSQL con Row Level Security forzado, la app entra con un rol sin privilegios de dueño y un recurso de otra familia responde 404, lo que verifican 270 pruebas en cada push. La ficha va cifrada con AES-256-GCM y una clave por persona, nunca aparece en registros, direcciones ni en el almacenamiento del navegador, y destruir la clave la deja ilegible. La Ley 21.719, en plena vigencia desde el 1 de diciembre de 2026, trata los datos de salud como sensibles, y la tomamos como requisito de diseño: MATU no pide datos clínicos, tiene su política de privacidad y su registro de tratamientos, y el analista normativo revisó antes y al cierre cada historia con datos personales.
- **Si repreguntan por la clave maestra:** hoy está en una variable de entorno, porque solo hay datos sintéticos. Antes de tratar datos reales pasa a un servicio de custodia, sin tocar el cifrado, porque está detrás de un puerto.
- **Fuente:** `docs/arquitectura.md` §2.2 (RNF-07 y RNF-08), §11.4 y §11.6. `parte-tecnica-jorge.md` §3 (270 pruebas). `docs/legal/politica-privacidad.md` y `docs/legal/registro-tratamientos.md`. `CLAUDE.md` §3 (analista normativo) y §5.

### 3. ¿Quién autoriza por la persona cuidada, si ella no puede?

- **Responde:** Jorge
- **Respuesta:** Sin una autorización vigente, MATU no guarda ni muestra la ficha. Al registrar a la persona, MATU anota quién autoriza y en qué calidad: la propia persona, su representante legal o quien la cuida de hecho, que hace una declaración, ve un aviso de su límite y la renueva cada año. La ficha, los insumos y los pedidos tienen cada uno su propia autorización, y cada una se puede retirar.
- **Si repreguntan si eso basta ante la ley:** no lo sabemos, y lo decimos. Si basta la declaración de quien cuida de hecho es la pregunta central de la consulta legal, que tiene 75 preguntas abiertas. Por eso MATU trata solo datos sintéticos hasta tener la respuesta. En la demo, María está autorizada por Carmen como cuidadora de hecho.
- **Fuente:** `docs/arquitectura.md` §11.5. `docs/lenguaje.md` §6.4, §6.4b y §22. `parte-tecnica-jorge.md` §5.2. `docs/legal/consulta-legal.md`. La calidad de la autorización de María: `infra/semillas/demo.py`.

### 4. ¿Por qué una app en el navegador y no una nativa?

- **Responde:** Martín
- **Respuesta:** MATU es una app móvil que en el semestre corre en el navegador del teléfono, sin instalar nada, por una decisión del 14 de octubre que sugirió el profesor guía. Nos dio un solo lenguaje para la familia, el relevo, el comercio y la operación, la accesibilidad que trae el navegador, y algo clave para el relevo: abrir la ficha con un enlace, sin descargar nada. Una participante de la usabilidad lo dijo así: «Me gusta que sea rápido de usar en el celular, sin tener que descargar aplicaciones pesadas».
- **Si repreguntan por los límites:** en iPhone, los avisos push solo llegan si se agrega MATU a la pantalla de inicio, así que el correo es el canal garantizado. La app nativa se decide con los datos del piloto, y con lo que ya está en React, React Native sería el camino más corto.
- **Fuente:** `docs/adr/ADR-026-aplicacion-web.md`. `docs/usabilidad/ronda-2-informe.md`, citas (P1). `docs/arquitectura.md` §17, riesgo del push en iPhone.

### 5. ¿Cómo controlaron la calidad con agentes de IA?

- **Responde:** Jorge
- **Respuesta:** Cada agente tiene un perímetro: el orquestador no programa, el backend no toca la interfaz, el QA solo prueba y reporta, el analista normativo revisa antes y al cierre lo que toca datos o dinero, y el diseñador especifica y revisa cada pantalla. El código generado cumple la misma definición de terminado que el escrito a mano: el CI corre en cada push el análisis estático, la detección de secretos, las migraciones que suben y bajan, y las pruebas de aislamiento, de arquitectura y de trazabilidad, y nada entra a `main` sin la revisión de Martín, que dejó 45 informes. Y medimos el efecto en vez de suponerlo: un factor de 1,86 en 40 tarjetas, contando solo las horas de Jorge, no las de los agentes.
- **Si repreguntan por el factor:** son las horas estimadas sin IA divididas por las horas reales. En el semestre, 154,5 h estimadas contra 83,11 h reales. El sprint 5 dio 1,09, porque sus tarjetas fueron correcciones chicas, y está informado así.
- **Fuente:** `CLAUDE.md` §3 y §5. `docs/sprints/sprint-5-planificacion.md` §8 («Con vibecoding no hay excepciones»). `parte-tecnica-jorge.md` §2.3 (trazabilidad) y §4. ADR-030. `TESTER/`.

### 6. ¿Qué pasa si se quita la capa 3?

- **Responde:** Martín
- **Respuesta:** Se apaga con un interruptor, `CAPA3_HABILITADA`, y la API arranca sin los módulos del despacho: el contrato de la API muestra solo las capas 1 y 2. Hay 21 pruebas que verifican que nada de las capas 1 y 2 depende de la capa 3, y que la ficha, compartir, el relevo con PIN, el consumo y los avisos funcionan con ella bloqueada. La familia sigue con su lista de insumos, que se imprime o se comparte y sirve en cualquier tienda: es el objetivo 5, operativo sin convenio comercial.
- **Si repreguntan por qué se diseñó así:** porque ningún convenio con comercios estaba garantizado. El despacho desacoplable elimina el único punto de falla externo del proyecto.
- **Fuente:** `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md` (`test_capa3_desacoplable.py`). `docs/arquitectura.md` §1, decisión 2. `docs/adr/ADR-031-lista-insumos-solo-texto.md`.

### 7. ¿Se sostiene el negocio?

- **Responde:** Jorge
- **Respuesta:** Es un ejercicio de viabilidad sobre 200 familias, con la canasta medida en las entrevistas (una mediana de $70.000 y una compra al mes), una comisión del 10 %, una última milla supuesta de $3.500 y $600.000 de costos fijos. Solo con el despacho cada familia deja $1.400 al mes y harían falta 429, y con la suscripción de $5.990 deja $7.210 y bastan 84, que en una comuna de 100.000 habitantes es alcanzable. Lo que falta saber es cuánto cuesta conseguir cada familia, y la ampliación mostró que el municipio es un canal concreto.
- **Si repreguntan si ya se cobra:** no. Cobrar la suscripción (RF-41) queda fuera del semestre a propósito: el cálculo es de viabilidad, no un compromiso de alcance.
- **Si repreguntan por la disposición a pagar:** seis de diez ya pagan por algún servicio de cuidado. Ocho dijeron que sí a $5.990, y cuatro lo condicionaron a que resuelva los insumos. Por eso el precio se sostiene sobre las capas 1 y 2 juntas, nunca sobre la ficha sola.
- **Fuente:** `docs/arquitectura.md` §16.1, §16.2, §16.4 y §16.6. `docs/resultados-entrevistas.md` §3 (H4), §4 y §8 (H7).

### 8. ¿Qué faltó?

- **Responde:** Martín
- **Respuesta:** Del semestre faltaron tres cosas, y las dijimos en la presentación:
  - el objetivo 7 se cumplió el 20 de noviembre, un día tarde;
  - RF-31, conciliar la boleta del comercio, no se construyó, porque sin comercios reales no hay boletas, y quedó en el Product Backlog;
  - y el pago se encarece con el volumen, con su plan para antes de producción.

  Para operar con datos reales faltan la consulta legal, con 75 preguntas abiertas, la clave maestra en un servicio de custodia, el borrado automático a los 3 años de los accesos de relevo y de lo que se anotó de cada apertura, una persona jurídica para usar Webpay en producción y los convenios con comercios.
- **Fuente:** `TESTER/2026-11-20-MATU-80-recorridos.md`. `parte-tecnica-jorge.md` §2.3 y §5.2. `docs/arquitectura.md` §2.2 (RNF-05), §11.4, §16.6 y §18.1.

### 9. ¿Por qué un solo cobro y no una reserva?

- **Responde:** Martín
- **Respuesta:** La captura diferida de Transbank solo funciona con crédito, el débito es el medio más usado por estas familias, y una retención mayor que el pedido es difícil de explicar, como observó el análisis de la Ley 19.496. Con precios exactos, la familia ve el total antes de pagar, se cobra una sola vez en venta normal de Webpay Plus, y si un producto falta se anula su parte a la misma tarjeta. El 10 de noviembre lo probé contra el ambiente de integración, con crédito, débito, una anulación parcial de $8.990 con los dos medios y un retorno duplicado que dejó un solo cobro, y los cuatro casos dieron PASS.
- **Fuente:** `docs/adr/ADR-027-precios-exactos.md`. `parte-tecnica-jorge.md` §3.2. `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`.

### 10. ¿Cómo saben que el problema existe?

- **Responde:** Jorge
- **Respuesta:** Antes de entrevistar escribimos siete hipótesis, cada una con el resultado que la validaba y el que la refutaba. Con diez entrevistas a cuidadoras, entre agosto y septiembre, y cuatro más a familiares que aportan, H1 se refutó y la ficha bajó a tres campos, y las otras seis quedaron validadas, tres de ellas con la ampliación. Después, en la segunda ronda de usabilidad, ya con la app, tres de tres completaron la ficha en menos de tres minutos y armaron el pedido en menos de seis.
- **Si repreguntan por los límites de la muestra:** las diez primeras llegaron por la red del equipo, y lo declaramos. Por eso la ampliación se reclutó solo por un canal concentrado: los grupos de personas mayores del municipio. En la usabilidad, dos de tres tenían el mismo perfil, y también está escrito.
- **Fuente:** `docs/protocolo-entrevistas.md` §7. `docs/resultados-entrevistas.md` §1, §3 y §8. `docs/adr/ADR-023-cierre.md`. `docs/usabilidad/ronda-1-informe.md` y `docs/usabilidad/ronda-2-informe.md`.

### 11. ¿Por qué el objetivo 7 llegó un día tarde?

- **Responde:** Martín
- **Respuesta:** El objetivo decía 19 de noviembre, pero la última fila de PR con migraciones, del #123 al #127, se fusionó y se desplegó en orden, y la última revisión terminó el 20. Ese día desplegué `main` en la demo y recorrí los seis recorridos en el teléfono, con OK en todos. Preferimos un día tarde a desplegar migraciones fuera de orden, porque cada una se apila sobre la anterior y una prueba exige que haya una sola cabeza.
- **Fuente:** `TESTER/2026-11-20-MATU-80-recorridos.md`, «Despliegue» y la tabla de R1 a R6. `docs/arquitectura.md` §7.8 (`test_cadena_migraciones.py`) y §15.5, punto 3.

### 12. ¿Qué datos guardan de la persona, y quién los ve?

- **Responde:** Jorge
- **Respuesta:** De la persona guardamos su nombre, el nivel de apoyo, la ficha que escribe la familia, cifrada, y lo que usa, sin datos clínicos. Cada uno ve lo suyo:
  - quien «Se informa» no ve montos;
  - el relevo ve solo las secciones que se eligieron al compartir, y hasta que vence el enlace;
  - el comercio ve solo los productos, sin la persona ni la dirección;
  - el equipo de operación nunca ve la ficha.

  Y la familia puede descargar una copia de sus datos desde la app, en «Tus datos», o borrar los de la persona en el acto.
- **Fuente:** `docs/arquitectura.md` §3.1 (RF-01), §7.7 y §11.6. `docs/lenguaje.md` §14.3, §31 (MATU-113), §36 y §40. `TESTER/2026-11-12-MATU-54-mis-datos.md` y `TESTER/2026-11-09-MATU-72-borrar-al-tiro.md`.

---

### Si preguntan algo que no está aquí

- **Sobre una cifra que no tenemos:** «Eso no lo medimos. Lo que sí medimos es…», y se pasa al dato más cercano con fuente.
- **Sobre una decisión:** se nombra su ADR. Están en `docs/adr/`: el 023 (la ficha de tres campos), el 026 (la app en el navegador), el 027 (un solo cobro), el 028 (la ficha ampliada), el 029 (la ficha no se imprime), el 030 (los roles) y el 031 (la lista como texto).
- **Sobre cuánto se construyó:** en los sprints 3 a 5 se fusionaron 93 PR en el repositorio del código. Al 18/11/2026 había 2371 funciones de prueba en el backend y 103 archivos de prueba en la web, con 36 migraciones reversibles hasta hoy (`parte-tecnica-jorge.md` §1 y `docs/arquitectura.md` §7.8).

---

## Anexo B · Capturas del plan B

Se toman en la demo recién restablecida (`docs/entorno-demo.md` §3), con la ventana a 360 px o a 400 px y el texto legible desde el fondo. **Ninguna captura muestra la barra de direcciones con el enlace del relevo, el PIN, el código de retiro ni los datos de la tarjeta.**

| Código | Pantalla | Dónde se usa |
|---|---|---|
| C1 | Inicio de la app de Carmen | Lámina 11 |
| C2 | `TESTER/2026-11-20-MATU-80-recorridos.md` en GitHub, con la tabla R1 a R6 | Lámina 9 (miniatura) |
| PB1 | «Ficha de relevo» de María, «3 de 3 campos listos» | Plan B, capa 1 |
| PB2 | «Enlaces», con el de Luisa «Activo» | Plan B, capa 1 |
| PB3 | La ficha abierta por Luisa: «A quién llamar» arriba y «Su día» como línea de tiempo | Plan B, capa 1 |
| PB4 | «Quién la vio», con «Luisa abrió la ficha» | Plan B, capa 1 |
| PB5 | «Insumos», bloque «Se acaban pronto» con el pañal | Plan B, capa 2 |
| PB6 | «Lista de insumos» | Plan B, capa 2 |
| PB7 | «Antes de pagar», con el total | Plan B, capa 3 |
| PB8 | Webpay en integración (sin los datos de la tarjeta) | Plan B, capa 3 |
| PB9 | «Pagaste tu pedido», con el sello «Pago de prueba» | Plan B, capa 3 |
| PB10 | Consola del comercio: «Código correcto. Entrega el pedido…» | Plan B, capa 3 |
| PB-video | El recorrido de la demo completo, de 60 a 90 s, grabado en el ensayo | Plan B de cualquier capa |

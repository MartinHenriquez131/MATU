# MATU · Presentación final · Contenido de las láminas

**Versión 1.0 · 23/11/2026** · Lo escribe el guionista para que el orquestador arme la presentación. Lo revisan Jorge y Martín.
**Base:** 17 láminas, en el orden que fijó Jorge. El guion hablado está en `MATU_Guion_Presentacion_Fase3.md`, en esta misma carpeta, y las preguntas probables en `MATU_Preguntas_Comision_Fase3.md`.
**Regla de esta versión:** cada lámina tiene un título-afirmación y como máximo 3 o 4 piezas cortas. Lo que explica va en el guion, no en la lámina.
**Cómo se leen las tablas:** la columna «Texto exacto en pantalla» es lo único que se proyecta. La columna «Fuente del dato» es para el equipo y no va en la lámina.

---

## Idea visual de toda la presentación

1. **El hilo es «el sábado de María».** Una franja con horas reales de su ficha (08:00 · 11:00 · 15:00 · 20:00 · 22:00) aparece en la portada con la última hora vacía, vuelve en la lámina de la demo y se completa en el cierre: «22:00 · luz del pasillo encendida».
2. **Las tres capas son una pila de tres bloques** que se repite en la esquina superior derecha de cada lámina. La ficha va en turquesa lleno, el consumo en turquesa claro y el despacho en contorno punteado, porque se puede quitar. Se enciende la capa de la que se habla.
3. **El turquesa de MATU es el único color de acento,** sobre fondo claro. El logo es el corazón blanco en el círculo turquesa. La portada y el cierre van en fondo turquesa oscuro.
4. **Cifras enormes y capturas reales** de la app dentro de un marco de teléfono. Nada de fotos de archivo.
5. **La evidencia en Git va en una sola línea, en la lámina 6,** la de los objetivos. En el resto se dice en voz alta (bloques 3 y 4 del guion), y si la comisión la pide se muestra en GitHub. Un pie con rutas en cada lámina sumaba texto chico que no se lee desde el fondo.

---

## Tamaños de las piezas

Pensado para una sala con proyector, vista desde el fondo. Lámina de 13,33 × 7,5 pulgadas.

| Pieza | Para qué | Tamaño relativo | Referencia |
|---|---|---|---|
| **Título-afirmación** | La idea de la lámina, en 10 palabras o menos | Grande | 40 a 44 pt, en negrita |
| **P · Protagonista** | La cifra o el diagrama que se recuerda | El más grande de la lámina | Cifra de 120 a 160 pt. Diagrama que ocupe la mitad de la lámina |
| **A · Apoyo** | Una cifra secundaria con su etiqueta, o una frase de 6 a 8 palabras | Mediano | Cifra de 60 a 72 pt, etiqueta y frase de 28 a 32 pt |
| **F · Fuente** | De dónde sale una cifra, o un pie corto, solo cuando la lámina lo necesita | Chico, pero legible | 16 a 18 pt, en gris oscuro |

Ningún texto baja de 16 pt. Si una pieza no cabe con estos tamaños, se corta la pieza, no la letra.

---

## Las 17 láminas

### Lámina 1 · Portada

- **Bloque 1 · Martín**
- **Título-afirmación (10 palabras):** Que el cuidado no se corte cuando quien cuida sale

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Logo y nombre | P | Logo de MATU · **MATU** | Marca de MATU |
| Título | Título | Que el cuidado no se corte cuando quien cuida sale | — |
| Franja del sábado | A | El sábado de María · 08:00 · 11:00 · 15:00 · 20:00 · 22:00 (la última, vacía) | Horas de «Su día» en la ficha sintética de María (`infra/semillas/demo.py`, `FICHA_MARIA`) |
| Pie | F | Presentación final · Capstone 2026-2 · Ingeniería en Informática · Duoc UC, sede San Joaquín | Portada de la Fase 2. Los nombres van en la lámina 2 |

- **Concepto visual:** fondo turquesa oscuro, logo grande al centro. La franja es una regla de tiempo fina en blanco, al pie, con la casilla de las 22:00 vacía. Es **diagrama**, sin imagen ni captura.

### Lámina 2 · Equipo

- **Bloque 1 · Martín**
- **Título-afirmación (9 palabras):** Dos personas, seis agentes, y nadie fusiona lo suyo

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Las dos personas | P | Jorge Espinoza · Product Owner — Martín Henríquez · Scrum Master | ADR-030 |
| Qué hace cada uno | A | Bajo Jorge: «Decide y desarrolla con seis agentes». Bajo Martín: «Despliega, prueba y fusiona» | `docs/adr/ADR-030-roles-del-equipo.md` |
| Cifra | A | **45** · informes de revisión en Git | 45 informes en `TESTER/`, del 05/11/2026 al 22/11/2026, sin contar el README (listado de la carpeta en la rama `fase3-presentacion-final`, 23/11/2026) |

- **Concepto visual:** dos retratos (**imagen**, fotos del equipo) con una flecha fina entre ellos rotulada «PR». Se lee como el ciclo de trabajo: uno construye, el otro prueba y fusiona.

### Lámina 3 · Contexto

- **Bloque 2 · Jorge**
- **Título-afirmación (8 palabras):** No falta gente: falta poder traspasar el cuidado

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Cifra | P | **1.498.977** · personas adultas viven con dependencia | ENDIDE 2022, en `docs/arquitectura.md` §1.1 |
| Cifra | A | **96,4 %** · de quienes cuidan en casa no recibe pago | Ídem |
| Cifra | A | **41,3 %** · no tiene un cuidador formal | Ídem |
| Fuente | F | ENDIDE 2022, Ministerio de Desarrollo Social y Familia | `docs/arquitectura.md` §1.1 |

- **Concepto visual:** la cifra protagonista domina la mitad izquierda, en turquesa. Las dos de apoyo van apiladas a la derecha. Sin imagen. El título es la frase de la arquitectura que la Fase 1 ya usó, y que Jorge pidió recuperar.

### Lámina 4 · Qué entendimos del problema

- **Bloque 2 · Jorge**
- **Título-afirmación (9 palabras):** Dos problemas que parecen distintos y son el mismo

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Continuidad | P | **9 de 10** · dejaron de salir | `docs/arquitectura.md` §1.1 y `docs/resultados-entrevistas.md` §3 (H2) |
| Abastecimiento | P | **6 de 10** · se quedaron sin un insumo | Ídem (H3: al menos un insumo que se acabó en los últimos tres meses) |
| Cita | A | «Eso no estaba en la hoja porque yo lo sé y se me olvidó que los demás no.» — cuidadora entrevistada | `docs/resultados-entrevistas.md` §6, entrevista E06, anonimizada |
| Fuente | F | 10 entrevistas a cuidadoras, agosto y septiembre de 2026 | `docs/resultados-entrevistas.md` §1 |

- **Concepto visual:** **diagrama** de dos columnas, rotuladas «Continuidad» y «Abastecimiento», cuyas flechas se juntan abajo en un solo punto: una sola persona. La cita va como escrita a mano sobre una hoja de cuaderno (**ilustración**, no foto). La hoja anticipa el cierre.

### Lámina 5 · Propuesta de solución

- **Bloque 2 · Jorge**
- **Título-afirmación (6 palabras):** Tres capas, y el orden importa

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| La pila | P | 1 · Ficha de relevo · el producto — 2 · Consumo y predicción · el diferenciador — 3 · Despacho · se puede quitar | `docs/arquitectura.md` §1, decisiones 1 y 2. `CLAUDE.md` §1 |
| La decisión | A | **3 de 10** · H1 refutada: la ficha quedó en tres campos | `docs/resultados-entrevistas.md` §3 (H1). `docs/adr/ADR-023-cierre.md` |
| Pie | F | Criterios escritos antes de entrevistar | `docs/protocolo-entrevistas.md` §7. `docs/adr/ADR-023-cierre.md` |

- **Concepto visual:** **diagrama** de la pila, grande, a la izquierda. El bloque 3 va en contorno punteado y levemente separado, como si se pudiera sacar. Es la primera vez que la pila aparece entera: desde aquí queda en la esquina de las láminas siguientes.

### Lámina 6 · Objetivos

- **Bloque 3 · Jorge**
- **Título-afirmación (9 palabras):** Siete objetivos cumplidos, uno con un día de atraso

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Cifra | P | **7 de 7** | `Fase 3/Evidencias Grupales/parte-tecnica-jorge.md` §3. `TESTER/2026-11-20-MATU-80-recorridos.md` |
| Fila de sellos | A | 1 Validar · Fase 1 — 2 Aislar · sprint 0 — 3 Ficha y relevo · 29/10 — 4 Aviso · 05/11 — 5 Lista · 07/11 — 6 Un cobro · 12/11 — 7 Desplegar · 20/11 (con la marca «+1 día») | Ídem, tabla de la §3, y `docs/arquitectura.md` §15.4 |
| Objetivo general | A | Objetivo general · Del plan de cuidado al aviso y al pago | Objetivo general de la Fase 2, abreviado (ver `MATU_Guion_Presentacion_Fase3.md`, «Para decidir», punto 5) |
| Línea de evidencia | F | Evidencia en Git: `TESTER/` · `parte-tecnica-jorge.md` · `docs/` | La única lámina con rutas de Git (idea visual, punto 5) |

- **Concepto visual:** **diagrama** de siete sellos circulares en turquesa, en una fila. El séptimo lleva una pequeña etiqueta en contorno, «+1 día». La fila cuenta como una sola pieza. Cada sello lleva solo dos o tres palabras y la fecha, para que se lea desde el fondo.

### Lámina 7 · Alcance

- **Bloque 3 · Jorge**
- **Título-afirmación (8 palabras):** Primero lo que nunca se sacrifica, después el despacho

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Lo que nunca se sacrifica | P | Ficha, enlace con PIN, aviso y lista | `docs/arquitectura.md` §15.3, «Lo que no se saca bajo ninguna circunstancia» |
| El despacho | A | Y el despacho: precio exacto, un cobro, retiro | `docs/arquitectura.md` §3.3 y ADR-027 |
| Lo de después | A | Para más adelante: pago entre familiares, repartidor | `parte-tecnica-jorge.md` §5.1 |
| Pie | F | Piloto académico con datos de prueba | `docs/lenguaje.md` §11, el distintivo del piloto |

- **Concepto visual:** la pila de la esquina se agranda al centro. Los bloques 1 y 2 en turquesa lleno con sus cuatro palabras, el 3 en turquesa claro y, al lado, dos cajas grises en contorno para lo de después. Es **diagrama**.

### Lámina 8 · Requerimientos

- **Bloque 3 · Jorge**
- **Título-afirmación (10 palabras):** 24 de 25 requisitos obligatorios cumplidos, y decimos cuál falta

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Cifra | P | **24 / 25** | `parte-tecnica-jorge.md` §2.3, «Requisitos *Debe*». `docs/arquitectura.md` §3, «Cobertura» |
| Lo que falta | A | Falta RF-31: conciliar la boleta del comercio | Ídem. Sigue como *Debe* sin cumplir en `docs/arquitectura.md` §3.3 |
| La prueba | A | Cada uno con su prueba en el CI | `parte-tecnica-jorge.md` §2.3 (`.github/workflows/ci.yml`, paso «Trazabilidad») |
| Pie | F | 42 requisitos · 25 obligatorios (MoSCoW) | `docs/arquitectura.md` §3, «Cobertura» |

- **Concepto visual:** **diagrama** de 25 cuadros en cinco filas. Veinticuatro en turquesa lleno y uno en contorno, con la etiqueta «RF-31». El cuadro vacío es lo que se recuerda: la honestidad se ve.

### Lámina 9 · Metodología

- **Bloque 4 · Martín**
- **Título-afirmación (9 palabras):** Scrum semanal, y cada cambio lo prueba la otra persona

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| El ciclo | P | Jorge + agentes → PR con CI en verde → Martín lo prueba en el teléfono → fusiona | ADR-030. `docs/sprints/sprint-5-planificacion.md` §8 |
| Cifra | A | **45** · informes de revisión | `TESTER/`, 45 informes |
| Cifra | A | **3 de 3** · llenaron la ficha en menos de 3 minutos | `docs/usabilidad/ronda-2-informe.md` (U1, sin ayuda) |

- **Concepto visual:** **diagrama** circular de cuatro pasos. Junto al «45» va una miniatura de un informe real en GitHub (**captura de GitHub**, no de la app): `TESTER/2026-11-20-MATU-80-recorridos.md`, con su tabla de R1 a R6 en OK.

### Lámina 10 · Cronograma

- **Bloque 4 · Martín**
- **Título-afirmación (8 palabras):** Los objetivos llegaron en el orden que prometimos

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Línea de tiempo | P | S0 21/09–15/10 · S1 16–22/10 · S2 23–29/10 · S3 30/10–05/11 · S4 06–12/11 · S5 13–19/11 · Reserva 20/11–03/12, con los sellos 2 a 7 sobre su sprint | `docs/arquitectura.md` §15.4. `docs/sprints/calendario-sprints.md` |
| Cifra | A | **1,86** · factor de vibecoding (se supuso 1,8) | `parte-tecnica-jorge.md` §4.3 |

- **Concepto visual:** **diagrama** de una línea horizontal con siete tramos. Los mismos sellos de la lámina 6 se posan sobre su sprint. El 7 queda un poco a la derecha del final del sprint 5: el día de atraso se ve sin decirlo. El sello 1 queda antes del sprint 0, en la Fase 1.

### Lámina 11 · Tecnologías y herramientas

- **Bloque 4 · Martín**
- **Título-afirmación (10 palabras):** Una app móvil que hoy se abre desde el navegador

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| La app | P | Captura de la app de Carmen en un marco de teléfono | Demo restablecida |
| El stack | A | React + TypeScript · FastAPI · PostgreSQL 16 · Webpay | `CLAUDE.md` §2. ADR-026 |
| La decisión | A | Sin instalar nada, diseñada desde 360 px | ADR-026 |

- **Concepto visual:** el teléfono con la **captura** al centro. Alrededor, cuatro etiquetas del stack con sus logos. Es la lámina que dice que MATU es una app móvil, aunque en el semestre corra en el navegador.
- **Captura que hace falta:** C1, el inicio de la app de Carmen, a 360 px.

### Lámina 12 · Arquitectura

- **Bloque 5 · Martín**
- **Título-afirmación (7 palabras):** La ficha no sabe que existe el despacho

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| El diagrama | P | Tres bloques apilados (ficha, consumo, despacho), con flechas solo hacia abajo y un interruptor en la capa 3, en «apagado» | `docs/arquitectura.md` §1, decisiones 2 y 4. `CLAUDE.md` §2 (`test_arquitectura.py`) |
| Las pruebas | A | 21 pruebas: sin capa 3, todo sigue | `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md` (`test_capa3_desacoplable.py`) |
| La carga | A | Carga del piloto: cumple. Con volumen: a corregir | `TESTER/2026-11-22-MATU-80-carga-meta.md`. `docs/arquitectura.md` §2.2, RNF-05 |
| Pie | F | Monolito modular en FastAPI | `docs/arquitectura.md` §1, decisión 4 |

- **Concepto visual:** **diagrama** con la pila de siempre, ahora grande. El interruptor de la capa 3 es lo que se recuerda: está apagado y lo de abajo sigue encendido.

### Lámina 13 · Modelo de datos

- **Bloque 5 · Martín**
- **Título-afirmación (6 palabras):** Para otra familia, María no existe

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| El diagrama | P | Dos grupos familiares separados por un muro de vidrio. En cada uno: persona → ficha (con candado) · consumo · pedido | `docs/modelo-datos.md`. `docs/arquitectura.md` §2.2, RNF-07 |
| Cifra | A | **270** · pruebas de aislamiento | `parte-tecnica-jorge.md` §3, objetivo 2 (`test_aislamiento.py`, al 18/11/2026) |
| El cifrado | A | Una clave por persona: destruirla borra la ficha | `docs/arquitectura.md` §11.4 y RNF-08 |
| Pie | F | Row Level Security forzado · AES-256-GCM · 36 migraciones reversibles | `docs/arquitectura.md` §7.8 (de la 0001 a la 0036) y §11.4 |

- **Concepto visual:** **diagrama**. Del lado de la otra familia, el lugar de María aparece vacío, solo con la etiqueta «404». Es la imagen del título.

### Lámina 14 · Demo

- **Bloque 6 · Jorge (capa 1) y Martín (capas 2 y 3)**
- **Título-afirmación (8 palabras):** Carmen sale, Luisa sabe qué hacer, Rodrigo paga

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Las tres capas, en el orden de la demo | P | 1 Ficha de relevo → 2 Consumo y predicción → 3 Despacho | `CLAUDE.md` §1 |
| Franja del sábado | A | El sábado de María · 08:00 · 11:00 · 15:00 · 20:00 · 22:00 | `infra/semillas/demo.py` |
| Pie | F | En vivo · Piloto académico con datos de prueba | `docs/entorno-demo.md`. `docs/lenguaje.md` §11 |

- **Concepto visual:** es solo el telón de fondo. Se ve unos segundos, mientras se pasa a la app, y vuelve si hay que pasar al plan B. Durante la demo, la pantalla muestra la app en vivo, no esta lámina.
- **Capturas que hacen falta:** no van en la lámina. Son las del plan B (lista al final de este archivo).

### Lámina 15 · Modelo de negocios

- **Bloque 7 · Jorge**
- **Título-afirmación (6 palabras):** Con 84 familias, MATU se sostiene

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Cifra y cuadrícula | P | **84** · familias cubren los costos. Al lado, 84 puntos turquesa frente a 429 grises rotulados «solo despacho: 429» | `docs/arquitectura.md` §16.4 |
| El ingreso | A | $5.990 al mes + 10 % por pedido | `docs/arquitectura.md` §16.2 |
| Disposición a pagar | A | **8 de 10** · dijeron que pagarían $5.990 | `docs/resultados-entrevistas.md` §3 (H4). `docs/arquitectura.md` §16.1 |
| Pie | F | Ejercicio de viabilidad sobre 200 familias, no una proyección | `docs/arquitectura.md` §3 y §16.6 |

- **Concepto visual:** **diagrama** de puntos. La diferencia entre 84 y 429 se ve de un golpe, sin leer la tabla.

### Lámina 16 · Próximos pasos

- **Bloque 7 · Jorge**
- **Título-afirmación (8 palabras):** Primero, datos reales seguros. Después, pagar entre familiares

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Los tres pasos | P | 1 Antes de datos reales → 2 Pago entre familiares y medicamentos → 3 Piloto con un municipio | `parte-tecnica-jorge.md` §5.1 y §5.2. `docs/resultados-entrevistas.md` §8 |
| Bajo el paso 1 | A | Consulta legal · clave maestra · pago con volumen | `parte-tecnica-jorge.md` §5.2. `docs/arquitectura.md` §11.4 y RNF-05 |
| Bajo el paso 3 | A | Y la app nativa, con lo aprendido | ADR-026, «La app nativa se decide en una etapa posterior» |

- **Concepto visual:** **diagrama** de tres flechas en escalera hacia la derecha. El paso 3 va en turquesa más intenso: es lo que esperamos.

### Lámina 17 · Reflexión y cierre

- **Bloque 8 · Martín**
- **Título-afirmación (9 palabras):** Esta vez, la luz del pasillo estaba en la ficha

| Pieza | Tamaño | Texto exacto en pantalla | Fuente del dato |
|---|---|---|---|
| Franja completa | P | El sábado de María · 08:00 · 11:00 · 15:00 · 20:00 · **22:00 · luz del pasillo encendida** | «Su día» de María (`infra/semillas/demo.py`) |
| Cierre | A | Logo de MATU · Gracias · ¿Preguntas? | — |
| Pie | F | Jorge Espinoza · Martín Henríquez · MATU · continuidad del cuidado | — |

- **Concepto visual:** fondo turquesa oscuro, como la portada. La franja vuelve completa y la casilla de las 22:00, que estaba vacía en la portada, ahora tiene un pequeño resplandor cálido. El título responde a la cita de la lámina 4: «Eso no estaba en la hoja».

---

## Capturas que hay que tomar

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

---

## Lo que no va en las láminas, y sí en el guion

- Las razones de cada decisión: por qué un monolito, por qué la web, por qué un solo cobro.
- El detalle de la carga (medianas por paso, la base acumulada) y el de RF-31.
- Los 6 de 9 relevos que fallaron, el porqué de la ficha de tres campos y el objetivo general completo.
- La evidencia de cada objetivo, uno por uno. Está en `MATU_Guion_Presentacion_Fase3.md`, sección 4 («Mapa de evidencia por objetivo»), y en `MATU_Preguntas_Comision_Fase3.md`.
- Las rutas de Git, salvo la línea de la lámina 6. Se dicen en voz alta y se muestran en GitHub si la comisión las pide.

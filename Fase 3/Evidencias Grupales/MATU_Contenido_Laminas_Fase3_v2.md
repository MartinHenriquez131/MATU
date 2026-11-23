# MATU · Presentación final · Contenido de las láminas · v2

**Versión 2.0 · 23/11/2026** · El texto en pantalla está copiado de las láminas v2 ya construidas (`deck-v2/project/slides/`, en el orden de `deck.json`). Este archivo agrega la fuente de cada dato, el concepto visual y, donde hace falta, una observación del guionista. **No cambia los `.html`.**
**Va con:** `MATU_Guion_Presentacion_Fase3_v2.md` y `MATU_Preguntas_Comision_Fase3_v2.md`, en esta misma carpeta. La v1 (`MATU_Contenido_Laminas_Fase3.md`) queda como estaba.
**Cómo se lee:** «En pantalla» es lo único que se proyecta. «Fuente» es para el equipo. «Observación» marca un dato que no calza con `docs/` o con las reglas de Jorge. Se resumen todas al final.

**Las reglas de la v2** (observaciones de Jorge a la v1):
- sin nombres propios, salvo Jorge y Martín en la portada y el equipo;
- sin el día de atraso del objetivo 7, la cantidad de informes, la cantidad de agentes, el factor de vibecoding ni la consulta legal;
- el objetivo general con su texto formal;
- sin «lo que nunca se sacrifica»;
- el alcance dice qué es y qué hace MATU;
- los requerimientos, sin flaquezas;
- la metodología, por hitos y sin reparto;
- tres próximos pasos;
- la sección 4 se llama «Diagnóstico del problema».

---

## Lámina 1 · Portada · Bloque 1 · Martín

- **En pantalla:**
  - Logo de MATU (corazón blanco en un círculo turquesa) · **MATU**
  - Continuidad del cuidado para personas mayores con dependencia
  - Jorge Espinoza · Martín Henríquez
  - Presentación final · Capstone 2026-2 · Ingeniería en Informática · Duoc UC, sede San Joaquín
- **Fuente:** la marca de MATU. La definición de MATU, `CLAUDE.md` §1.
- **Concepto visual:** fondo turquesa oscuro, con el logo grande junto al nombre.

## Lámina 2 · Equipo · Bloque 1 · Martín

- **Título:** Dos roles complementarios, un mismo producto
- **En pantalla:**
  - JE · **Jorge Espinoza** · Product Owner · Visión del producto, backlog y construcción de la plataforma
  - MH · **Martín Henríquez** · Scrum Master · Proceso Scrum, calidad, despliegue y pruebas con usuarios
- **Fuente:** `docs/adr/ADR-030-roles-del-equipo.md`.
- **Concepto visual:** dos tarjetas iguales, con las iniciales en círculos turquesa. El mismo peso visual para los dos.

## Lámina 3 · Contexto · Bloque 2 · Jorge

- **Título:** No falta gente: falta poder traspasar el cuidado
- **En pantalla:**
  - **1.498.977** · personas adultas viven con dependencia en Chile
  - **96,4 %** · de quienes cuidan en casa no recibe pago
  - **41,3 %** · no tiene un cuidador formal
  - Fuente: ENDIDE 2022, Ministerio de Desarrollo Social y Familia
- **Fuente:** las tres cifras, ENDIDE 2022, en `docs/arquitectura.md` §1.1. El título es la frase de la misma sección: «no falta gente dispuesta, falta poder traspasar el cuidado».
- **Concepto visual:** la cifra protagonista ocupa la mitad izquierda, y las dos de apoyo van apiladas en tarjetas a la derecha.

## Lámina 4 · Diagnóstico del problema · Bloque 2 · Jorge

- **Título:** Dos problemas que parecen distintos y son el mismo
- **En pantalla:**
  - Continuidad · **9 de 10** · cuidadoras dejaron de salir
  - Abastecimiento · **6 de 10** · se quedaron sin un insumo
  - Todo depende de una sola persona
  - «Eso no estaba en la hoja porque yo lo sé y se me olvidó que los demás no.» — Cuidadora entrevistada
  - Fuente: 10 entrevistas a cuidadoras, agosto y septiembre de 2026
- **Fuente:**
  - 9 de 10 dejaron de salir por falta de relevo o por el costo de explicar, y 6 de 10 se quedaron sin un insumo en los últimos tres meses: `docs/arquitectura.md` §1.1 y `docs/resultados-entrevistas.md` §3 (H2 y H3).
  - La cita: `docs/resultados-entrevistas.md` §6, entrevista E06, sin código ni edad.
- **Concepto visual:** dos columnas cuyas líneas se juntan en un punto, el rótulo «Todo depende de una sola persona». La cita va en una tarjeta color papel.

## Lámina 5 · Propuesta de solución · Bloque 2 · Jorge

- **Título:** Tres capas, y el orden importa
- **En pantalla:**
  - **1** · Ficha de relevo · *El producto* · Su día, qué hacer si se altera y a quién llamar
  - **2** · Consumo y predicción · *El diferenciador* · Avisa antes de que se acabe un insumo
  - **3** · Despacho · *Un servicio que se puede quitar* · Pedido con precio exacto y un solo cobro
  - **La validación cambió el producto:** solo 3 de 10 completaron un plan largo en 5 minutos, así que la ficha quedó en tres campos.
  - Fuente: Criterios fijados antes de entrevistar · ADR-023
- **Fuente:**
  - Las tres capas y su orden: `docs/arquitectura.md` §1, decisiones 1 y 2, y `CLAUDE.md` §1.
  - El criterio de H1: `docs/protocolo-entrevistas.md` §7. El resultado: `docs/resultados-entrevistas.md` §3. El cambio de producto: `docs/adr/ADR-023-cierre.md`.
- **Concepto visual:** tres tarjetas. La de la capa 3 va con borde punteado y sin relleno, como si se pudiera sacar.
- **Observación (P2):** H1 no midió «un plan largo». Pedía que 7 de 10 respondieran **las 3 preguntas** del plan mínimo en menos de 5 minutos, y lo lograron 3 (`docs/protocolo-entrevistas.md` §7, fila H1). Propuesta: «solo 3 de 10 respondieron tres preguntas del plan en 5 minutos, así que el plan quedó en una ficha de tres campos». El guion lo dice así.

## Lámina 6 · Objetivos · Bloque 3 · Jorge

- **Título:** Siete de siete objetivos cumplidos
- **En pantalla:**
  - **Objetivo general:** Desarrollar una plataforma de software que convierta el plan de cuidado de una persona mayor con dependencia en una predicción de quiebre de insumos y coordine su reposición y pago, desplegada y operativa en un entorno de demostración al cierre del semestre 2026-2.
  - **Objetivos específicos, todos cumplidos:**
    1. Validar el problema con criterios fijados antes
    2. Aislar los datos de cada familia
    3. Compartir la ficha de forma segura y revocable
    4. Anticipar cuándo se acaba cada insumo
    5. Generar una lista de reposición exportable
    6. Pagar el pedido con un solo cobro
    7. Desplegar el sistema con seis recorridos críticos
  - Fuente: Evidencia de cada objetivo en Git: pruebas automáticas, informes de prueba y recorridos en el teléfono
- **Fuente:**
  - El objetivo general: presentación de la Fase 2, lámina 4, y de la Fase 1, lámina 10.
  - Los siete objetivos cumplidos: `Fase 3/Evidencias Grupales/parte-tecnica-jorge.md` §3 para los seis primeros. El 7: `TESTER/2026-11-20-MATU-80-recorridos.md`.
  - La redacción vigente de los objetivos 5, 6 y 7: `docs/arquitectura.md` §15.4. La evidencia de cada uno está en el guion, sección 4.
- **Concepto visual:** el objetivo general en una tarjeta ancha, y los siete en dos columnas con un número turquesa cada uno.
- **Observación (P3):** el objetivo general dice «predicción de quiebre». `docs/lenguaje.md` §3.2 evita «quiebre» en la app, pero aquí es el texto formal del objetivo y Jorge pidió decirlo así. Se deja.

## Lámina 7 · Alcance · Bloque 3 · Jorge

- **Título:** Una app web para la familia, quien la reemplaza y el comercio
- **En pantalla:**
  - **La familia** · Escribe la ficha, declara el consumo, recibe avisos, pide y paga
  - **Quien reemplaza** · Abre la ficha con un enlace y un PIN, sin crear cuenta
  - **El comercio** · Prepara el pedido y lo entrega con un código de retiro
  - Mobile first, sin instalar · Entorno de demostración · Datos de prueba · Webpay en ambiente de integración
  - Fuente: Arquitectura §15.1 · ADR-026 y ADR-027
- **Fuente:**
  - El alcance del MVP: `docs/arquitectura.md` §15.1.
  - Lo que hace quien reemplaza: `docs/lenguaje.md` §7.1, «No necesitas cuenta ni instalar nada».
  - Lo que hace el comercio: `docs/lenguaje.md` §36.
  - La app en el navegador: ADR-026. El precio exacto y Webpay en integración: ADR-027 y `docs/lenguaje.md` §11.
- **Concepto visual:** tres tarjetas con un ícono por actor (personas, llave y casa), y cuatro etiquetas de las condiciones del piloto.
- **Observación (P2):** el título dice «una app web». La lámina 11 y el mensaje del proyecto dicen «una app móvil que hoy se abre desde el navegador» (ADR-026). Propuesta: «Una app para la familia, quien la reemplaza y el comercio». La etiqueta «Mobile first, sin instalar» ya dice cómo corre.

## Lámina 8 · Requerimientos · Bloque 3 · Jorge

- **Título:** Cada requisito tiene una prueba que lo verifica
- **En pantalla:**
  - **Funcionales, por capa:**
    - Capa 1 · Ficha: Ficha de tres campos · enlace con PIN que vence · registro de quién la abrió
    - Capa 2 · Consumo: Consumo declarado · aviso antes del quiebre · lista exportable
    - Capa 3 · Despacho: Precio exacto · un solo cobro con Webpay · retiro con código
  - **No funcionales:** Integridad del pago · Confidencialidad y trazabilidad · Ficha en menos de 3 minutos · Texto legible al 200 % · Aislamiento entre familias · Ficha cifrada · Despacho que se puede quitar
  - Fuente: Arquitectura §2.2 y §3 · trazabilidad de requisitos en el CI
- **Fuente:**
  - Funcionales: `docs/arquitectura.md` §3, con RF-02, RF-05 a RF-08, RF-10 a RF-15, RF-20, RF-25 y RF-26.
  - Las pruebas de punta a punta de los seis recorridos: `backend/tests/e2e/` (`parte-tecnica-jorge.md` §3.3).
  - No funcionales, con su forma de verificar: `docs/arquitectura.md` §2.2.
    - Automáticos: RNF-01, RNF-02, RNF-07 y RNF-08.
    - Con personas: RNF-03, con 3 de 3 bajo 3 minutos (`docs/usabilidad/ronda-2-informe.md`), y RNF-09, con la revisión manual al 200 %.
    - El despacho que se quita: `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md`.
  - La trazabilidad en el CI: `parte-tecnica-jorge.md` §2.3.
- **Concepto visual:** los funcionales en tres tarjetas por capa, y los no funcionales en una columna de marcas de verificación.
- **Observaciones:**
  - **P3:** «aviso antes del quiebre» usa una palabra que `docs/lenguaje.md` §3.2 evita. Propuesta: «aviso antes de que se acabe».
  - **P3:** el título es cierto para los requisitos que se muestran. RF-31, la conciliación de la boleta, sigue como *Debe* sin construir (`docs/arquitectura.md` §3.3), y no se muestra, por decisión de Jorge. El guion dice «cada uno de **estos** requisitos», y la respuesta, si preguntan, está en la pregunta 8.

## Lámina 9 · Metodología · Bloque 4 · Martín

- **Título:** Scrum semanal, validado en terreno con quienes cuidan
- **En pantalla:**
  - Ago–Sep · **10 entrevistas** · Cuidadoras familiares
  - Sep–Nov · **Sprints semanales** · Planificación, revisión y retrospectiva
  - 07–10/11 · **Pruebas en vivo** · Ronda 1, con cuidadoras familiares
  - 10–11/11 · **4 entrevistas** · Familiares que aportan al cuidado
  - 12/11 · **Pruebas en vivo** · Ronda 2, con cuidadoras remuneradas
  - Revisión cruzada de cada cambio · Integración continua con pruebas automáticas · Tablero en Trello
  - Fuente: Resultados de las entrevistas · entrevistas E11 a E14 · usabilidad, rondas 1 y 2
- **Fuente:**
  - Las 10 entrevistas: `docs/resultados-entrevistas.md` §1.
  - Los sprints: `docs/sprints/calendario-sprints.md`.
  - La ronda 1, del 07 al 10/11: `docs/usabilidad/ronda-1-informe.md`.
  - E11 a E14, el 10 y el 11/11: `docs/resultados-entrevistas.md` §8.
  - La ronda 2, el 12/11: `docs/usabilidad/ronda-2-informe.md`.
  - La revisión de cada cambio por la otra persona: `docs/sprints/sprint-5-planificacion.md` §8, punto 5.
- **Concepto visual:** cinco hitos en fila, cada uno con su fecha en una etiqueta, y tres etiquetas llenas con las prácticas.
- **Observaciones:**
  - **P2:** las 10 entrevistas no fueron todas a cuidadoras familiares. Hubo una cuidadora remunerada (E07) y una familiar que aporta (E09) (`docs/resultados-entrevistas.md` §1). Propuesta: «Cuidadoras».
  - **P3:** los sprints semanales empiezan el 16/10. Del 21/09 al 15/10 fue la preparación (sprint 0). Propuesta: «Oct–Nov».
  - **P3:** en la ronda 2 participó también una familiar que aporta (P3), que pagó el pedido sin ayuda (`docs/usabilidad/ronda-2-informe.md`). Propuesta: «Ronda 2, ya con la app».
  - **P3:** la ronda 1 fue con un prototipo de pruebas, no con la app (`docs/usabilidad/ronda-1-informe.md`). «Pruebas en vivo» sirve, pero si preguntan, se dice.

## Lámina 10 · Cronograma · Bloque 4 · Martín

- **Título:** Siete objetivos entregados dentro del calendario
- **En pantalla:**
  - Preparación 21/09–15/10 (con el objetivo 2) · Sprint 1 16–22/10 · Sprint 2 23–29/10 (3) · Sprint 3 30/10–05/11 (4) · Sprint 4 06–12/11 (5 y 6) · Sprint 5 13–19/11 · Reserva 20/11–03/12 (7)
  - El objetivo 1 se cumplió en la Fase 1. Cinco sprints de construcción, de una semana cada uno, y dos de reserva para ajustes y la presentación.
  - Fuente: Arquitectura, tabla 15.4 · calendario de sprints
- **Fuente:**
  - Fechas y estado de cada sprint: `docs/arquitectura.md` §15.4 y `docs/sprints/calendario-sprints.md`.
  - Dónde cae cada objetivo:
    - el 2, en el sprint 0, con 31 pruebas;
    - el 3, el 29/10;
    - el 4, el 05/11;
    - el 5, el 07/11, y el 6, el 12/11 (`parte-tecnica-jorge.md` §3);
    - el 7, el 20/11 (`TESTER/2026-11-20-MATU-80-recorridos.md`).
- **Concepto visual:** una línea de siete tramos con los números de los objetivos posados sobre su sprint. La reserva va con borde punteado.
- **Observación:** el sello 7 queda sobre la reserva, que es el 20/11, y eso calza con `TESTER/2026-11-20-MATU-80-recorridos.md`. El título es cierto, porque la reserva es parte del calendario. El guion no lo comenta, por la regla 3.

## Lámina 11 · Tecnologías y herramientas · Bloque 4 · Martín

- **Título:** Una app móvil que hoy se abre desde el navegador
- **En pantalla:**
  - Marco de teléfono con **[Captura: inicio de la app]**
  - Interfaz: React + TypeScript · API: FastAPI · Python 3.12 · Datos: PostgreSQL 16 con RLS · Pago: Webpay Plus
  - GitHub Actions · Railway · Trello · Diseñada desde 360 px
  - Fuente: ADR-026: app web mobile first; la app nativa es la etapa siguiente
- **Fuente:**
  - El stack: `CLAUDE.md` §2.
  - La app web mobile first y el diseño desde 360 px: ADR-026.
  - Railway: `docs/entorno-demo.md`.
- **Concepto visual:** el teléfono con la captura a la izquierda, y cuatro tarjetas del stack a la derecha.
- **Observaciones:**
  - **P2:** falta la captura. **No puede mostrar nombres:** la app de la semilla dice los nombres de la familia sintética (sección «Para decidir» del guion v2, punto 1). Se toma recortada o con datos sin nombres.
  - **P3:** «la app nativa es la etapa siguiente» va más lejos que el ADR-026, que dice que se decide en una etapa posterior. Además, la app nativa no está entre los tres próximos pasos de la lámina 16. Propuesta: «ADR-026: app web mobile first; la app nativa se decide después del piloto».

## Lámina 12 · Arquitectura · Bloque 5 · Martín

- **Título:** La ficha no sabe que existe el despacho
- **En pantalla:**
  - Monolito modular en FastAPI
  - Capa 3 · Despacho, con el interruptor «se puede apagar» → Capa 2 · Consumo → Capa 1 · Ficha
  - **21** · pruebas automáticas: sin la capa 3, todo sigue funcionando
  - **Carga del piloto** · Sin fallos, con 10 usuarios a la vez
  - Fuente: Las flechas se leen «depende de», siempre hacia abajo · prueba de arquitectura en cada cambio
- **Fuente:**
  - El monolito modular: `docs/arquitectura.md` §1, decisión 4.
  - Las dependencias hacia abajo: `CLAUDE.md` §2 (`test_arquitectura.py`).
  - Las 21 pruebas: `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md`.
  - La carga: `TESTER/2026-11-21-MATU-80-k6-cierre.md` y `TESTER/2026-11-22-MATU-80-carga-meta.md`, con 0 % de fallos con 10 usuarios de k6. Ver `docs/arquitectura.md` §2.2, RNF-05.
- **Concepto visual:** la pila de tres capas con flechas hacia abajo, y la capa 3 con borde punteado y un interruptor apagado.
- **Observación:** la lámina no menciona que el pago se encarece con el volumen (K6). El guion lo dice en una frase, sin dramatizar (sección «Para decidir» del guion v2, punto 4).

## Lámina 13 · Modelo de datos · Bloque 5 · Martín

- **Título:** Ninguna familia puede ver los datos de otra
- **En pantalla:**
  - Una familia · Persona cuidada · Ficha cifrada · Consumo · Pedido
  - Otra familia · **404** · Para ella, esos datos no existen
  - **270** · pruebas de aislamiento
  - Una clave por persona: destruirla borra la ficha
  - Fuente: Seguridad por fila forzada en PostgreSQL · cifrado AES-256-GCM · 36 migraciones reversibles
- **Fuente:**
  - El aislamiento y el 404: `docs/arquitectura.md` §2.2, RNF-07.
  - Las 270 pruebas son las funciones de `test_aislamiento.py` al 18/11/2026 (`parte-tecnica-jorge.md` §3, objetivo 2).
  - La clave por persona y el borrado: `docs/arquitectura.md` §11.4 y RNF-08.
  - Las 36 migraciones, de la 0001 a la 0036: `docs/arquitectura.md` §7.8.
- **Concepto visual:** la familia en una tarjeta llena, separada por una barra de la otra familia, que es un recuadro punteado y vacío con «404».
- **Observación:** las 270 pruebas son del 18/11. Si se quiere la cifra del día, se recuenta antes de presentar.

## Lámina 14 · Demo · Bloque 6 · Jorge (capa 1) y Martín (capas 2 y 3)

- **Título:** La cuidadora sale, el relevo sabe qué hacer, la familia paga
- **En pantalla:**
  - **1** · Ficha de relevo · La ficha, el enlace con PIN y quién la abrió · Presenta Jorge
  - **2** · Consumo y predicción · Cuándo se acaba cada insumo, y la lista · Presenta Martín
  - **3** · Despacho · El pedido, un solo cobro y el retiro con código · Presenta Martín
  - Fuente: En vivo, en el entorno de demostración, con datos de prueba
- **Fuente:** `docs/entorno-demo.md`. `docs/lenguaje.md` §11.
- **Concepto visual:** fondo oscuro, con las tres capas en el orden en que se muestran. Es el telón de fondo: durante la demo se ve la app.
- **Observación (P2):** la lámina cumple la regla de los nombres, pero la app en vivo no. La semilla de la demo trae nombres, y se ven en pantalla (sección «Para decidir» del guion v2, punto 1).

## Lámina 15 · Modelo de negocios · Bloque 7 · Jorge

- **Título:** Con 84 familias, MATU se sostiene
- **En pantalla:**
  - **84** · familias cubren los costos
  - $5.990 al mes + 10 % por pedido
  - 8 de 10 entrevistadas dijeron que pagarían $5.990
  - Cuadrícula de 429 puntos, 84 en turquesa: «84 con suscripción y despacho» · «429 cobrando solo el despacho»
  - Fuente: Ejercicio de viabilidad, no una proyección · arquitectura §16 · entrevistas
- **Fuente:**
  - 84 y 429: `docs/arquitectura.md` §16.4.
  - $5.990 y el 10 %: §16.2.
  - 8 de 10 dijeron que sí: `docs/resultados-entrevistas.md` §3 (H4). Es una pregunta hipotética, y 4 lo condicionaron a que resuelva los insumos.
  - «Ejercicio de viabilidad»: `docs/arquitectura.md` §3 y §16.6.
- **Concepto visual:** una cuadrícula de puntos en la que la diferencia entre 84 y 429 se ve sin leer. Verifiqué que el SVG dibuja 429 puntos, con 84 en turquesa.

## Lámina 16 · Próximos pasos · Bloque 7 · Jorge

- **Título:** Del piloto a las familias, la salud pública y los municipios
- **En pantalla:**
  - **Pago dividido entre familias** · 4 de 4 familiares que aportan quieren pagar su parte por separado
  - **Retiro de medicamentos en farmacias y centros de salud pública** · Ya está diseñado en el modelo de datos
  - **Pilotos municipales** · Las últimas entrevistas llegaron por los grupos de adultos mayores del municipio
  - Fuente: Entrevistas E11 a E14 · arquitectura §15.1, medicamentos como primera prioridad de la fase siguiente
- **Fuente:**
  - 4 de 4 aportantes quieren pagar su parte por separado: `docs/resultados-entrevistas.md` §8.
  - Los medicamentos, diseñados en el modelo: `docs/modelo-datos.md` §11 (`rx`, «diseñado y no implementado») y `docs/arquitectura.md` §15.1.
  - El canal municipal: `docs/resultados-entrevistas.md` §8, H7.
- **Concepto visual:** tres tarjetas, y la tercera, los pilotos, en turquesa lleno: es lo que más esperamos.
- **Observaciones:**
  - **P2:** «entre familias». El pago dividido es entre los **familiares** de un mismo grupo, no entre familias distintas (`CLAUDE.md` §1, «pago dividido entre varios familiares». `docs/resultados-entrevistas.md` §8). Propuesta: «Pago dividido entre familiares».
  - **P3:** «adultos mayores». `docs/lenguaje.md` §3.2 pide «persona mayor» en textos institucionales. Propuesta: «grupos de personas mayores».
  - **P3:** la fuente dice «medicamentos como primera prioridad», como `docs/arquitectura.md` §15.1 (v1.2, 08/11). Pero el 11/11 Jorge dejó el pago dividido como «fase 2, prioridad 1» (`docs/resultados-entrevistas.md` §8 y `parte-tecnica-jorge.md` §5.1). Hay dos «primeras prioridades». Propuesta: quitar «como primera prioridad de la fase siguiente» de la fuente. El guion no ordena los tres pasos por prioridad.

## Lámina 17 · Reflexión y cierre · Bloque 8 · Martín

- **Título:** Que quien cuida pueda salir, y volver tranquila
- **En pantalla:**
  - La cuidadora · Puede delegar sin tener que explicarlo todo de nuevo
  - La persona cuidada · Recibe el mismo cuidado, la cuide quien la cuide
  - La familia · Comparte la información y no se queda sin insumos
  - Logo de MATU · Gracias · ¿Preguntas?
  - Fuente: MATU · continuidad del cuidado para personas mayores con dependencia
- **Fuente:** el problema de los bloques 2 y 3: `docs/arquitectura.md` §1.1 y `docs/resultados-entrevistas.md` §3.
- **Concepto visual:** fondo oscuro, como la portada, con una tarjeta por cada persona que se beneficia.

---

## Capturas que hay que tomar

Se toman con la demo recién restablecida (`docs/entorno-demo.md` §3). **Ninguna muestra nombres** (punto 1 de «Para decidir» del guion v2), ni la barra de direcciones con el enlace del relevo, el PIN, el código de retiro o los datos de la tarjeta.

| Código | Pantalla | Dónde se usa |
|---|---|---|
| C1 | Inicio de la app de la cuidadora | Lámina 11 |
| PB1 | La ficha, «3 de 3 campos listos» | Plan B, capa 1 |
| PB2 | «Enlaces», con el del relevo «Activo» | Plan B, capa 1 |
| PB3 | La ficha abierta por el relevo: «A quién llamar» arriba y «Su día» como línea de tiempo | Plan B, capa 1 |
| PB4 | «Quién la vio», con la apertura del relevo | Plan B, capa 1 |
| PB5 | «Insumos», con el bloque «Se acaban pronto» | Plan B, capa 2 |
| PB6 | «Lista de insumos» | Plan B, capa 2 |
| PB7 | «Antes de pagar», con el total | Plan B, capa 3 |
| PB8 | Webpay en integración, sin los datos de la tarjeta | Plan B, capa 3 |
| PB9 | «Pagaste tu pedido», con el sello «Pago de prueba» | Plan B, capa 3 |
| PB10 | Consola del comercio: «Código correcto. Entrega el pedido…» | Plan B, capa 3 |
| PB-video | El recorrido de la demo completo, de 60 a 90 s, grabado en el ensayo | Plan B de cualquier capa |

---

## Resumen de las observaciones

| Lámina | Severidad | Qué | Propuesta |
|---|---|---|---|
| 5 | P2 | «Un plan largo». H1 midió tres preguntas del plan | «respondieron tres preguntas del plan en 5 minutos» |
| 7 | P2 | «Una app web», contra el mensaje «app móvil» (ADR-026, lámina 11) | «Una app para la familia, quien la reemplaza y el comercio» |
| 9 | P2 | «Cuidadoras familiares» en las 10 entrevistas. Hubo una remunerada y una aportante | «Cuidadoras» |
| 11 | P2 | Falta la captura, que no puede mostrar nombres | Tomarla sin nombres |
| 14 | P2 | La app en vivo muestra los nombres de la semilla | Decidir (guion v2, «Para decidir», punto 1) |
| 16 | P2 | «Pago dividido entre familias» | «entre familiares» |
| 6 | P3 | «Quiebre» en el objetivo general | Se deja: es el texto formal |
| 8 | P3 | «Aviso antes del quiebre» | «aviso antes de que se acabe» |
| 8 | P3 | El título vale para los requisitos que se muestran. RF-31 no se muestra | Se deja. El guion dice «estos», y está la pregunta 8 |
| 9 | P3 | «Sep–Nov» en los sprints semanales, que empiezan el 16/10 | «Oct–Nov» |
| 9 | P3 | En la ronda 2 participó también una familiar que aporta | «Ronda 2, ya con la app» |
| 11 | P3 | «La app nativa es la etapa siguiente», más fuerte que el ADR-026 | «se decide después del piloto» |
| 16 | P3 | «Adultos mayores» | «personas mayores» |
| 16 | P3 | Dos «primeras prioridades»: medicamentos (§15.1) y pago dividido (decisión del 11/11) | Quitar «como primera prioridad» de la fuente |

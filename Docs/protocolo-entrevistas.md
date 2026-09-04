# MATU — Protocolo de validación con cuidadores

**Versión:** 1.0 · agosto 2026
**Documento asociado:** MATU · Arquitectura v1.0, sección 18 «Definiciones pendientes» y ADR-023
**Equipo:** Jorge Espinoza · Martín Henríquez
**Estado:** listo para ejecutar. Es la actividad que convierte al proyecto de deseable en viable.

---

## 1. Para qué sirve esto

Este protocolo existe para responder **una pregunta que puede invalidar todo el proyecto**, y otras seis que deciden si el proyecto es viable o solo deseable. No es investigación de mercado ni un sondeo de opinión. Es una prueba de hipótesis con criterio de falsación declarado antes de empezar.

**Qué parte de «viable» resuelve este instrumento y qué parte no.** Conviene tenerlo claro antes de empezar, porque un proyecto se declara viable por varias vías distintas y las entrevistas solo cubren algunas.

| Lo que hay que demostrar | Quién lo demuestra |
|---|---|
| Que el problema existe, es frecuente y duele | **Estas entrevistas** (H1, H2, H3) |
| Que alguien está dispuesto a pagar, y **quién** de la familia | **Estas entrevistas** (H4, H5, H6) |
| Que estas familias son alcanzables sin gastar una fortuna en llegar a ellas | **Estas entrevistas** (H7) |
| Que la aritmética del piloto cierra | La sección 16 de la arquitectura, **recalculada con lo medido aquí** |
| Que la tecnología de pago se comporta como dice el proveedor | La prueba de concepto de Transbank del sprint 0 |
| Que existe un comercio dispuesto a convenio | El **anexo A** de este documento, una conversación corta con un comercio |
| Que el equipo alcanza a construirlo en el semestre | La sección 15 de la arquitectura, capacidad declarada y recorte aplicado |

**Lo que diez entrevistas no pueden hacer:** estimar el tamaño del mercado ni proyectar una tasa de conversión. Lo que sí pueden hacer, y es lo que importa, es **falsar los supuestos sobre los que descansa ese cálculo**. Si la canasta mensual real resulta ser la mitad de la supuesta, el punto de equilibrio de 88 familias deja de ser 88 y hay que decirlo antes de construir, no después.

**La regla que gobierna todo el guion:** no se pregunta si algo *les serviría*. Se pregunta **qué hicieron la última vez**. La gente es un mal predictor de su propia conducta futura y un buen narrador de su conducta pasada. Toda pregunta hipotética que sobrevivió en este guion está marcada como tal y su respuesta se pondera menos.

---

## 2. Las siete hipótesis

| # | Hipótesis | Si es falsa |
|---|---|---|
| **H1** | Un cuidador principal está dispuesto a dedicar cinco minutos a completar una versión mínima del plan de cuidado | **Cae el ADR-001 completo.** Se activa el plan B ya escrito, el **ADR-023**: modo ficha de relevo de tres campos, con el peso del producto trasladado a la capa 2 |
| **H2** | El problema del relevo es real y frecuente: existen situaciones en que el cuidador necesita que otro lo reemplace y traspasar la información es una fricción concreta | El plan de cuidado sirve como registro, no como herramienta de relevo. Cambia el posicionamiento |
| **H3** | El quiebre de insumos ocurre de verdad y genera un costo real de tiempo o dinero | La capa 2 pierde urgencia y pasa a ser conveniencia. Baja el valor de la predicción |
| **H4** | Existe disposición a pagar del orden de $5.990 mensuales por continuidad del cuidado, que es el precio supuesto en la sección 16 de la arquitectura | Hay que revisar el precio de la sección 16 del documento de arquitectura y con él el punto de equilibrio |
| **H5** | El gasto de cuidado efectivamente se reparte entre varios familiares y ese reparto genera fricción | El reparto de pago baja de prioridad y libera casi dos sprints |
| **H6** | **Quien pagaría no es necesariamente quien cuida.** El cuidador principal suele ser el que menos ingreso disponible tiene y más carga soporta; el familiar que aporta dinero compensa con plata la ausencia de tiempo | El destinatario comercial es el propio cuidador, y el precio de la sección 16 tiene un techo mucho más bajo que el supuesto |
| **H7** | **Estas familias son alcanzables por un canal concentrado** —agrupación de familiares, consultorio, municipio, fundación— y no una por una | El costo de adquisición se dispara y las 88 familias del punto de equilibrio dejan de ser alcanzables en el horizonte del piloto. Es el hueco que la sección 16.4 declara explícitamente |

**Por qué H6 y H7 no estaban y ahora sí.** Las cinco primeras prueban que el problema existe y que el producto se puede usar. Ninguna prueba que el **negocio** funcione. H6 decide a quién se le vende y por lo tanto qué precio soporta; H7 decide si llegar a 88 familias cuesta un mes o cuesta un presupuesto que el proyecto no tiene. Sin ellas, las entrevistas demuestran deseabilidad y no viabilidad.

### 2.1 Las tres mediciones que la sección 16 necesita

Esto no son hipótesis: no se validan ni se refutan, **se miden**. Son los tres números que hoy la arquitectura declara como supuestos propios del equipo, y que estas entrevistas pueden reemplazar por evidencia.

| Medición | Valor supuesto hoy | Cómo se mide |
|---|---|---|
| Canasta mensual de insumos por persona cuidada | $50.000 a $70.000 | Pregunta 24, en pesos y por mes |
| Compras al mes | 1,5 entregas por familia | Pregunta 25, cuántas veces salen a comprar |
| Gasto ya desembolsado en servicios de cuidado | sin valor | Pregunta 30, qué pagan hoy y cuánto |

Se reportan **mediana y rango**, nunca promedio: con diez casos un valor extremo mueve el promedio y no dice nada. Y se reportan aunque contradigan lo que el documento supone, que es justamente el punto.

---

## 3. A quién entrevistar

**Meta: 10 entrevistas. Mínimo viable para decidir: 6.**

| Perfil | Cuántos | Por qué |
|---|---|---|
| Cuidador principal familiar, conviviente con la persona cuidada | 4 | Es el usuario central de la capa 1 |
| Cuidador principal familiar, no conviviente | 2 | Coordinan a distancia. Su fricción es distinta y probablemente mayor |
| Familiar que aporta dinero pero no cuida | 2 | Validan H5 desde el otro lado del reparto, y son **los únicos que pueden validar H6 directamente**: son quienes pagarían |
| Cuidador remunerado o de relevo | 2 | Validan H2 desde quien recibe la información, no desde quien la entrega |

**Criterio de inclusión:** la persona cuidada tiene demencia o dependencia que exige apoyo diario, y la situación lleva al menos tres meses.

**Criterio de exclusión:** cuidadores de personas en institución permanente, porque el problema logístico es otro.

**Dónde encontrarlos.** Agrupaciones de familiares de personas con Alzheimer, programas municipales de personas mayores, grupos de apoyo, y la red profesional del propio equipo. Se recomienda **no** empezar por conocidos cercanos: son los que más difícil dicen que no.

---

## 4. Encuadre ético

Este punto importa por dos razones: porque se conversa con personas en situación de carga, y porque el equipo tiene formación clínica y se le va a exigir el estándar.

- **Consentimiento informado verbal**, pedido y anotado al inicio de la entrevista, indicando propósito, uso de la información, anonimización y derecho a interrumpir.
- **No se graba audio ni video.** Solo se toma nota escrita. Es una decisión deliberada: en un proyecto cuyo núcleo es el tratamiento de datos sensibles, no generar una grabación evita crear el archivo más delicado de todo el proceso, y le permite al equipo decirlo así al pedir el consentimiento.
- **No se anotan** datos identificatorios de la persona cuidada, diagnósticos ni información clínica. Si la persona los ofrece, no se escriben.
- **No se ofrece consejo clínico** durante la entrevista, aunque quien entrevista esté habilitado para darlo. Confunde los roles y contamina la respuesta.
- **Si aparece sobrecarga significativa o malestar**, se detiene la entrevista, se acoge y se ofrece derivación. La entrevista es lo secundario.
- Duración máxima **45 minutos**, y se respeta aunque la conversación esté buena. Quien cuida no tiene tiempo de sobra.

**Cómo se registra.** Cada integrante conduce sus propias entrevistas y toma sus propias notas, sobre el guion impreso con espacio para escribir. Se anotan tres cosas por sobre el resto: **las cifras**, **los hechos con fecha** y **las frases textuales**, que son lo único que no se puede reconstruir después. La ficha de la sección 6 se completa apenas termina la entrevista, no al final del día.

---

## 5. Guion

### Bloque 0 · Apertura (3 min)

> Gracias por el tiempo. Estamos estudiando cómo se organiza el día a día de quienes cuidan a una persona mayor en la casa. No vengo a mostrarte nada ni a venderte nada, vengo a que me cuentes cómo es. No hay respuestas correctas. Si algo no lo quieres contestar, seguimos de largo sin problema. **No voy a grabar nada**: voy a ir tomando algunas notas, y no anoto ni tu nombre ni el de la persona que cuidas. ¿Te parece bien así?

### Bloque 1 · Contexto (3 min)

1. Cuéntame cómo es un día normal tuyo.
2. ¿Desde cuándo estás en esto?
3. ¿Hay alguien más que ayude? ¿Cómo se reparten?

*(Escuchar. No conducir. Aquí solo se establece el contexto y la confianza.)*

### Bloque 2 · El quiebre de insumos → H3 (6 min)

4. **¿Cuándo fue la última vez que se te acabó algo que necesitabas sí o sí?** ¿Qué pasó ese día?
5. ¿Cómo te diste cuenta de que se estaba acabando?
6. ¿Qué hiciste? ¿Quién fue a comprar?
7. ¿Cuánto te costó eso en tiempo, o en plata si tuviste que comprar más caro?
8. ¿Con qué frecuencia te pasa algo así?
9. ¿Llevas alguna cuenta de cuánto te dura cada cosa? ¿Cómo?

> **Qué buscar:** frecuencia real, costo concreto, y si ya existe un sistema propio, aunque sea una anotación en el refrigerador. **Un sistema propio ya existente es la mejor señal posible**: significa que el problema duele lo suficiente como para que alguien ya haya inventado una solución.

### Bloque 3 · El relevo → H2 (9 min)

10. **¿Cuándo fue la última vez que otra persona tuvo que hacerse cargo, aunque fueran unas horas?**
11. ¿Cómo le explicaste lo que había que hacer?
12. ¿Cuánto te tomó explicarle?
13. ¿Algo salió distinto de lo que esperabas?
14. ¿Hay cosas que te cuesta explicar, o que solo sabes tú?
15. ¿Alguna vez **no** pudiste salir porque no había a quién dejar, o porque explicarle iba a ser mucho trabajo?
16. ¿Tienes algo escrito de todo esto? *(Si sí: pedir verlo, con permiso. Es el dato más valioso de la entrevista.)*

> **Qué buscar:** la pregunta 15 es la más importante del guion completo. **Un "sí" concreto y reciente valida H2 mejor que cualquier otra cosa.** Y la 16 mide directamente la disposición a documentar, que es H1 disfrazada.

### Bloque 4 · El plan de cuidado → H1 (10 min)

*(Recién aquí se muestra algo. Antes no.)*

Mostrar el prototipo, pantallas del flujo 1, en un teléfono. No explicarlo. Decir solo:

> Te voy a mostrar algo que estamos probando. Mírate estas pantallas y dime qué entiendes.

17. ¿Qué entiendes que hace esto?
18. *(Mostrar las ocho preguntas.)* Si tuvieras que responder estas ocho preguntas ahora, ¿lo harías?
19. **Hagámoslo.** *(Pedirle que responda tres de verdad, cronometrar. Siempre tres: el criterio de decisión de la sección 7 se mide sobre tres.)*
20. ¿Cómo se sintió? ¿Muy largo, muy corto, muy invasivo?
21. ¿Hay algo de esto que no querrías dejar escrito?
22. ¿A quién le mandarías este enlace? *(Mostrar la pantalla de compartir.)*
23. *(Mostrar la pantalla «Quién ha visto el plan».)* ¿Esto te tranquiliza, te da lo mismo, o te incomoda? ¿Lo mirarías alguna vez?

> **Qué buscar:** la 19 es una **prueba de conducta, no de opinión**. Cronometrar de verdad. Si menos de siete de cada diez responden las tres en menos de cinco minutos sin abandonar, **H1 está en problemas** y se activa el ADR-023 antes del sprint 2, no después.
> La 21 es la pregunta de privacidad y puede revelar que hay contenido que la gente no quiere digitalizar. Eso cambia el diseño de las secciones.
> La 23 prueba si la auditoría de accesos (RF-08) se lee como confianza o como vigilancia. Si nadie la mira ni le importa, es una pantalla cara que se puede simplificar.

### Bloque 5 · El gasto real → las tres mediciones de la sección 16 (6 min)

*(Este bloque no valida hipótesis: mide. Anotar cifras, no impresiones. Si la persona no sabe el monto exacto, pedirle que estime y anotar que fue estimación.)*

24. Pensando en pañales, toallitas, cremas, suplementos y todo lo del cuidado: **¿cuánto se va al mes en eso, entre todos?**
25. ¿Cada cuánto compran? ¿Cuántas veces al mes alguien tiene que salir a comprar estas cosas?
26. ¿Dónde compran hoy? ¿Van al local, mandan a alguien, o lo piden por aplicación?
27. ¿Reciben pañales o insumos del consultorio, del municipio o de alguna fundación?

> **Qué buscar:** la 24 y la 25 son los dos números que sostienen todo el cálculo del punto de equilibrio. Insistir con delicadeza hasta tener una cifra, no un «harto».
> La 26 revela el sustituto real. Si ya piden por aplicación, MATU compite con un hábito instalado y hay que saberlo. Si nadie lo hace, el despacho es más novedad y más fricción de lo que el documento supone.
> La 27 es la señal del canal institucional. Una familia que ya recibe del CESFAM está dentro de un padrón, y ese padrón es exactamente el canal concentrado de H7.

### Bloque 6 · Quién paga → H4, H5 y H6 (6 min)

28. Del gasto mensual de cuidado, ¿quién pone qué?
29. ¿Cómo se coordinan? ¿Alguien lleva la cuenta? ¿Ha habido problemas con eso?
30. ¿Has pagado alguna vez por algo que te facilite el cuidado? ¿Qué, y cuánto?
31. *(Hipotética, se pondera menos.)* Si esto costara $5.990 al mes, ¿lo pagarías? ¿Y $9.990?
32. **Y si la familia decidiera pagarlo, ¿quién lo pondría?** ¿Tú, o alguno de los que aporta plata pero no está en el día a día?
33. **¿Qué tendría que hacer para que valiera la pena pagarlo?**

> **Qué buscar:** la 30 vale diez veces más que la 31, porque es conducta pasada. **Alguien que ya paga por algo del cuidado tiene disposición demostrada.** Alguien que dice que pagaría, no.
> **La 32 es la pregunta comercial más importante del guion.** Si el cuidador principal dice «yo no podría, tendría que ponerlo mi hermano», el destinatario del mensaje de venta no es quien usa el producto, y eso cambia el flujo de alta, el precio soportable y la forma de vender. Anotar la respuesta textual.
> La 33 suele entregar la mejor información de toda la entrevista y conviene dejar silencio después de hacerla.

### Bloque 7 · Canal y cierre → H7 (2 min)

34. **¿Cómo llegaste a este grupo, o a quien te puso en contacto conmigo?** Y cuando necesitas algo del cuidado y no sabes qué hacer, ¿a quién le preguntas?
35. Si pudieras arreglar una sola cosa de tu día a día, ¿cuál sería?
36. ¿Hay algo que no te pregunté y que debería haber preguntado? ¿Conoces a alguien más en tu situación con quien podríamos conversar?

> **Qué buscar:** la 34 dibuja el mapa de por dónde se llega a estas familias. Si siete de diez nombran el mismo tipo de lugar —una agrupación, un consultorio, un grupo de WhatsApp— ahí está el canal, y con él la respuesta a la pregunta que la sección 16.4 declara sin responder: cuánto cuesta conseguir una familia.
> **La forma en que se reclutó a cada entrevistado es en sí misma evidencia de H7.** Anotarla siempre, aunque la persona no responda la 34.

---

## 6. Cómo se registra

Una ficha por entrevista, en una planilla compartida, **completada el mismo día y antes de la siguiente entrevista**. Sin grabación no hay a qué volver: lo que no quedó escrito ese día, se perdió. Las notas de papel se pasan a la planilla mientras la conversación todavía está fresca.

| Campo | Tipo |
|---|---|
| Código de entrevista | E01 a E10 |
| Perfil | conviviente, no conviviente, aportante, relevo |
| Meses en la situación de cuidado | número |
| **Quiebres en los últimos 3 meses** | número. Evidencia de H3 |
| **Relevos en los últimos 3 meses** | número. Evidencia de H2 |
| **¿No pudo salir por falta de relevo?** | sí / no, con la cita textual |
| **¿Tiene algo escrito ya?** | no / notas sueltas / documento. Evidencia de H1 |
| **Minutos en responder 3 preguntas del plan** | cronometrado. Evidencia dura de H1 |
| **¿Terminó las 3 o abandonó?** | terminó / abandonó |
| ¿Reparte el gasto? | sí / no, y cómo. Evidencia de H5 |
| ¿Ya paga por algo del cuidado? | qué y cuánto. Evidencia de H4 |
| **Gasto mensual en insumos de cuidado** | pesos. Medición 1. Marcar si fue estimado |
| **Veces al mes que alguien sale a comprar** | número. Medición 2 |
| **Dónde compra hoy** | local / encargo a un tercero / aplicación de despacho |
| **¿Recibe insumos del CESFAM, municipio o fundación?** | sí / no, y cuáles. Evidencia de H7 |
| **¿Quién pagaría la suscripción?** | el propio cuidador / otro familiar / nadie. Evidencia de H6, con cita textual |
| **Cómo se llegó a esta persona** | agrupación / consultorio / municipio / fundación / red personal / referido de otro entrevistado. Evidencia de H7 |
| Tres citas textuales | las que más digan, en sus palabras. Se anotan **entre comillas solo si se alcanzaron a escribir literales**; si se reconstruyeron de memoria, se marcan como paráfrasis y no se citan como textuales en el informe |

---

## 7. Criterios de decisión, fijados antes de empezar

Esto es lo que impide interpretar los resultados a conveniencia. **Se escribe ahora y no se cambia después.**

| Hipótesis | Se considera validada si | Se considera refutada si | Qué se hace si se refuta |
|---|---|---|---|
| **H1** | ≥ 7 de 10 responden las 3 preguntas en menos de 5 minutos sin abandonar | ≤ 4 de 10 lo hacen | **Activar el ADR-023, modo ficha de relevo**: la capa 1 se reduce a tres campos —rutina en una línea, qué hacer si se altera, a quién llamar— y el peso pasa a la capa 2. Se decide antes del sprint 2 |
| **H2** | ≥ 6 de 10 reportan al menos un relevo en 3 meses, **y** ≥ 4 reportan haber dejado de salir por falta de relevo | ≤ 3 reportan relevos | El plan de cuidado se reposiciona como registro para la familia, no como herramienta de relevo |
| **H3** | ≥ 6 de 10 reportan al menos un quiebre en 3 meses | ≤ 3 lo reportan | La capa 2 baja de prioridad y sube el catálogo con reposición programada simple, sin predicción |
| **H4** | ≥ 4 de 10 ya pagan por algo del cuidado, **y** ≥ 5 responden que sí a $5.990 | ≤ 2 ya pagan algo | Revisar precio o mover el foco al canal institucional |
| **H5** | ≥ 5 de 10 reparten el gasto con otro familiar y reportan fricción | ≤ 3 reparten | El reparto de pago baja a fase 2 y **se liberan los sprints 9 y parte del 8** |
| **H6** | ≥ 5 de 10 responden que lo pagaría alguien distinto del cuidador principal, **o** los dos familiares aportantes entrevistados dicen que ellos lo pondrían | ≥ 7 responden que lo pagaría el propio cuidador **y** ese mismo cuidador dice que no podría | El destinatario comercial es el cuidador. Se baja el precio de la sección 16, se recalcula el punto de equilibrio y se evalúa el canal institucional como vía principal |
| **H7** | ≥ 7 de 10 fueron contactados a través de un canal concentrado, **o** pertenecen a uno, **o** reciben insumos de un programa público | ≤ 3 | Se declara que no hay canal barato de adquisición. El piloto se replantea sobre una agrupación o un consultorio específico como socio, o el proyecto asume que 88 familias no son alcanzables en el horizonte del piloto y lo dice |

**Las tres mediciones no tienen criterio de falsación, tienen consecuencia.** Si la canasta mensual medida queda bajo $40.000 o las compras al mes bajo 1, el margen por familia de la sección 16.2 cae y el punto de equilibrio sube. **Se recalcula con los valores medidos y se publica el número nuevo, sea cual sea.** Ese recálculo es el entregable de viabilidad del proyecto, no un anexo.

**Zona intermedia.** Un resultado entre "validada" y "refutada" se trata como no concluyente y obliga a cuatro entrevistas más antes de decidir, no a interpretar a favor.

---

## 8. Calendario

| Día | Actividad |
|---|---|
| 1 | Ajustar el guion, preparar la planilla e imprimir el guion con espacio para anotar. Repartir las entrevistas entre los dos integrantes |
| 2 | Contactar y agendar. Meta: 12 agendadas para conseguir 10 realizadas |
| 3 a 7 | Entrevistas, **máximo 2 por día por persona**. La ficha se completa entre una y otra: una tercera en el mismo día se registra mal |
| 8 | Análisis, llenado de la matriz de decisión |
| 9 | **Reunión de decisión de los dos integrantes**, con los criterios de la sección 7 sobre la mesa |
| 10 | **Recálculo de la sección 16 con los valores medidos**, informe de una página al profesor guía y ajuste del documento de arquitectura si corresponde |

**Esto ocurre antes del sprint 2.** Es la única actividad del proyecto que puede invalidar la arquitectura completa, y por eso va primero.

---

## 9. Qué hacer con los resultados aunque todo salga bien

Incluso con las siete hipótesis validadas, las entrevistas entregan cuatro insumos que se usan de inmediato:

1. **La sección 16 se reescribe con números medidos.** La tabla 16.1 deja de decir «estimación del equipo» en tres de sus filas y pasa a decir «mediana de diez entrevistas, rango X a Y». El punto de equilibrio se recalcula y se publica el resultado. **Este es el entregable que convierte al proyecto de deseable en viable**, y es lo primero que hay que hacer con los datos.
2. **Las citas textuales** son el mejor material para la introducción del informe de título y para la defensa. Una frase real de una cuidadora vale más que tres párrafos de estadística. Como no hay grabación, solo se presentan como cita literal las que quedaron escritas palabra por palabra durante la entrevista; el resto se usa como paráfrasis y se declara como tal.
3. **Las ocho preguntas del plan de cuidado se rediseñan** con las palabras que usó la gente, no con las que usó el equipo.
4. **Los quiebres reportados** entregan la lista real de productos que debe tener el catálogo semilla del sprint 6.

---

## Anexo A · Conversación con un comercio

La sección 18.1 de la arquitectura declara que ningún comercio ha comprometido nada, y ese es uno de los cinco huecos que el documento no cierra solo. Cerrarlo cuesta **una conversación de veinte minutos**, no un proyecto aparte, y por eso va aquí y no en otro documento.

**A quién.** Una farmacia de barrio, un supermercado mediano o una distribuidora de insumos médicos de la comuna candidata. No una cadena: en una cadena nadie en el local puede comprometer nada.

**Qué se pide.** No un contrato. Una **carta de intención de una página** que diga que el comercio estaría dispuesto a participar en un piloto. Eso basta para bajar el riesgo de crítico a medio y para poder decir en la defensa que la capa 3 tiene un interlocutor real.

**Las seis preguntas:**

1. ¿Preparan pedidos para que alguien los pase a buscar? ¿Cómo funciona hoy?
2. Si un pedido llega por pantalla y hay que dejarlo listo en una hora, ¿es factible? ¿Quién lo haría?
3. Cuando falta un producto, ¿qué hacen hoy? ¿Reemplazan, llaman, lo sacan de la boleta?
4. ¿Trabajan con cuenta corriente para algún cliente institucional? ¿Cómo se factura y cada cuánto?
5. Si alguien pasa a retirar mostrando un código en el teléfono, ¿lo pueden validar en caja sin instalar nada?
6. ¿Qué les tendría que dar esto para que valga la pena? ¿Volumen, pago garantizado, otra cosa?

> **Qué buscar:** la 2 y la 5 deciden si el modo preparado del ADR-009 es realista o es una suposición del equipo. La 4 decide si la liquidación de la sección 8.8 se puede operar. Y la 6 dice el precio real del convenio, que hasta ahora el documento supone sin preguntarle a nadie.

**Cuándo.** En la misma semana de las entrevistas con cuidadores. Es una sola conversación y cierra un hueco completo del anteproyecto.

---

*Protocolo de validación MATU · versión 1.0 · agosto 2026 · Jorge Espinoza y Martín Henríquez*

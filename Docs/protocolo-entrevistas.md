# MATU — Protocolo de validación con cuidadores

**Versión:** 1.0 · agosto 2026
**Documento asociado:** MATU · Arquitectura v1.0, sección 18 «Definiciones pendientes» y ADR-023
**Equipo:** Jorge Espinoza · Martín Henríquez
**Estado:** listo para ejecutar

---

## 1. Para qué sirve esto

Este protocolo existe para responder **una pregunta que puede invalidar todo el proyecto**, y otras cuatro que ajustan su diseño. No es investigación de mercado ni un sondeo de opinión. Es una prueba de hipótesis con criterio de falsación declarado antes de empezar.

**La regla que gobierna todo el guion:** no se pregunta si algo *les serviría*. Se pregunta **qué hicieron la última vez**. La gente es un mal predictor de su propia conducta futura y un buen narrador de su conducta pasada. Toda pregunta hipotética que sobrevivió en este guion está marcada como tal y su respuesta se pondera menos.

---

## 2. Las cinco hipótesis

| # | Hipótesis | Si es falsa |
|---|---|---|
| **H1** | Un cuidador principal está dispuesto a dedicar cinco minutos a completar una versión mínima del plan de cuidado | **Cae el ADR-001 completo.** Se activa el plan B ya escrito, el **ADR-023**: modo ficha de relevo de tres campos, con el peso del producto trasladado a la capa 2 |
| **H2** | El problema del relevo es real y frecuente: existen situaciones en que el cuidador necesita que otro lo reemplace y traspasar la información es una fricción concreta | El plan de cuidado sirve como registro, no como herramienta de relevo. Cambia el posicionamiento |
| **H3** | El quiebre de insumos ocurre de verdad y genera un costo real de tiempo o dinero | La capa 2 pierde urgencia y pasa a ser conveniencia. Baja el valor de la predicción |
| **H4** | Existe disposición a pagar del orden de $5.990 mensuales por continuidad del cuidado, que es el precio supuesto en la sección 16 de la arquitectura | Hay que revisar el precio de la sección 16 del documento de arquitectura y con él el punto de equilibrio |
| **H5** | El gasto de cuidado efectivamente se reparte entre varios familiares y ese reparto genera fricción | El reparto de pago baja de prioridad y libera casi dos sprints |

---

## 3. A quién entrevistar

**Meta: 10 entrevistas. Mínimo viable para decidir: 6.**

| Perfil | Cuántos | Por qué |
|---|---|---|
| Cuidador principal familiar, conviviente con la persona cuidada | 4 | Es el usuario central de la capa 1 |
| Cuidador principal familiar, no conviviente | 2 | Coordinan a distancia. Su fricción es distinta y probablemente mayor |
| Familiar que aporta dinero pero no cuida | 2 | Validan H5 desde el otro lado del reparto |
| Cuidador remunerado o de relevo | 2 | Validan H2 desde quien recibe la información, no desde quien la entrega |

**Criterio de inclusión:** la persona cuidada tiene demencia o dependencia que exige apoyo diario, y la situación lleva al menos tres meses.

**Criterio de exclusión:** cuidadores de personas en institución permanente, porque el problema logístico es otro.

**Dónde encontrarlos.** Agrupaciones de familiares de personas con Alzheimer, programas municipales de personas mayores, grupos de apoyo, y la red profesional del propio equipo. Se recomienda **no** empezar por conocidos cercanos: son los que más difícil dicen que no.

---

## 4. Encuadre ético

Este punto importa por dos razones: porque se conversa con personas en situación de carga, y porque el equipo tiene formación clínica y se le va a exigir el estándar.

- **Consentimiento informado verbal**, registrado al inicio de la grabación, indicando propósito, uso de la información, anonimización y derecho a interrumpir.
- **No se registran** datos identificatorios de la persona cuidada, diagnósticos ni información clínica. Si la persona los ofrece, no se transcriben.
- **No se ofrece consejo clínico** durante la entrevista, aunque quien entrevista esté habilitado para darlo. Confunde los roles y contamina la respuesta.
- **Si aparece sobrecarga significativa o malestar**, se detiene la entrevista, se acoge y se ofrece derivación. La entrevista es lo secundario.
- Duración máxima **45 minutos**, y se respeta aunque la conversación esté buena. Quien cuida no tiene tiempo de sobra.

---

## 5. Guion

### Bloque 0 · Apertura (3 min)

> Gracias por el tiempo. Estamos estudiando cómo se organiza el día a día de quienes cuidan a una persona mayor en la casa. No vengo a mostrarte nada ni a venderte nada, vengo a que me cuentes cómo es. No hay respuestas correctas. Si algo no lo quieres contestar, seguimos de largo sin problema. ¿Te parece bien si grabo el audio solo para no tomar notas mientras conversamos?

### Bloque 1 · Contexto (5 min)

1. Cuéntame cómo es un día normal tuyo.
2. ¿Desde cuándo estás en esto?
3. ¿Hay alguien más que ayude? ¿Cómo se reparten?

*(Escuchar. No conducir. Aquí solo se establece el contexto y la confianza.)*

### Bloque 2 · El quiebre de insumos → H3 (8 min)

4. **¿Cuándo fue la última vez que se te acabó algo que necesitabas sí o sí?** ¿Qué pasó ese día?
5. ¿Cómo te diste cuenta de que se estaba acabando?
6. ¿Qué hiciste? ¿Quién fue a comprar?
7. ¿Cuánto te costó eso en tiempo, o en plata si tuviste que comprar más caro?
8. ¿Con qué frecuencia te pasa algo así?
9. ¿Llevas alguna cuenta de cuánto te dura cada cosa? ¿Cómo?

> **Qué buscar:** frecuencia real, costo concreto, y si ya existe un sistema propio, aunque sea una anotación en el refrigerador. **Un sistema propio ya existente es la mejor señal posible**: significa que el problema duele lo suficiente como para que alguien ya haya inventado una solución.

### Bloque 3 · El relevo → H2 (10 min)

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

### Bloque 5 · Dinero → H4 y H5 (7 min)

24. Del gasto mensual de cuidado, ¿quién pone qué?
25. ¿Cómo se coordinan? ¿Alguien lleva la cuenta?
26. ¿Ha habido problemas con eso?
27. ¿Has pagado alguna vez por algo que te facilite el cuidado? ¿Qué, y cuánto?
28. *(Hipotética, se pondera menos.)* Si esto costara $5.990 al mes, ¿lo pagarías? ¿Y $9.990?
29. **¿Qué tendría que hacer para que valiera la pena pagarlo?**

> **Qué buscar:** la 27 vale diez veces más que la 28, porque es conducta pasada. **Alguien que ya paga por algo del cuidado tiene disposición demostrada.** Alguien que dice que pagaría, no.
> La 29 suele entregar la mejor información de toda la entrevista y conviene dejar silencio después de hacerla.

### Bloque 6 · Cierre (2 min)

30. Si pudieras arreglar una sola cosa de tu día a día, ¿cuál sería?
31. ¿Hay algo que no te pregunté y que debería haber preguntado?
32. ¿Conoces a alguien más en tu situación con quien podríamos conversar?

---

## 6. Cómo se registra

Una ficha por entrevista, en una planilla compartida, llenada **dentro de las 24 horas**.

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
| Tres citas textuales | las que más digan, en sus palabras |

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

**Zona intermedia.** Un resultado entre "validada" y "refutada" se trata como no concluyente y obliga a cuatro entrevistas más antes de decidir, no a interpretar a favor.

---

## 8. Calendario

| Día | Actividad |
|---|---|
| 1 | Ajustar el guion, preparar la planilla, imprimir el consentimiento |
| 2 | Contactar y agendar. Meta: 12 agendadas para conseguir 10 realizadas |
| 3 a 7 | Entrevistas, máximo 3 por día para poder registrar bien |
| 8 | Análisis, llenado de la matriz de decisión |
| 9 | **Reunión de decisión de los dos integrantes**, con los criterios de la sección 7 sobre la mesa |
| 10 | Informe de una página al profesor guía y ajuste del documento de arquitectura si corresponde |

**Esto ocurre antes del sprint 2.** Es la única actividad del proyecto que puede invalidar la arquitectura completa, y por eso va primero.

---

## 9. Qué hacer con los resultados aunque todo salga bien

Incluso con las cinco hipótesis validadas, las entrevistas entregan tres insumos que se usan de inmediato:

1. **Las citas textuales** son el mejor material para la introducción del informe de título y para la defensa. Una frase real de una cuidadora vale más que tres párrafos de estadística.
2. **Las ocho preguntas del plan de cuidado se rediseñan** con las palabras que usó la gente, no con las que usó el equipo.
3. **Los quiebres reportados** entregan la lista real de productos que debe tener el catálogo semilla del sprint 6.

---

*Protocolo de validación MATU · versión 1.0 · agosto 2026 · Jorge Espinoza y Martín Henríquez*

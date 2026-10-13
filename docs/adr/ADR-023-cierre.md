# ADR-023 · Modo ficha de relevo · CIERRE

**Estado:** Aceptado y activado
**Fecha de decisión:** septiembre 2026, antes del sprint 2 como exige el protocolo
**Decisores:** Jorge Espinoza (Product Owner) · Martín Henríquez (Scrum Master)
**Reemplaza:** la condición "se decide antes del sprint 2" del ADR-023 en la arquitectura v1.0

---

## Contexto

El ADR-023 dejó preparado un plan B para el riesgo número uno del proyecto: que un cuidador agotado no complete el plan de cuidado. La decisión quedó condicionada a la hipótesis H1 del protocolo de validación, con un criterio fijado **antes** de entrevistar:

| | Criterio |
|---|---|
| Validada | 7 o más de 10 responden 3 preguntas del plan en menos de 5 minutos, sin abandonar |
| Refutada | 4 o menos de 10 lo hacen |
| Si se refuta | Activar el modo ficha de relevo |

## Evidencia

| Entrevista | Perfil | Tiempo en 3 preguntas | Resultado |
|---|---|---|---|
| A38 | Cuidadora remunerada | 2:45 | Cumple |
| Y40 | Conviviente | 3:05 | Cumple |
| A55 | Conviviente | 4:00 | Cumple |
| J54 | Conviviente | 5:00 | No cumple (el criterio es *menos* de 5) |
| E64 | Familiar que aporta | 4:20 y abandona | No cumple |
| N71 | No conviviente | 5:50 | No cumple |
| C57 | Conviviente | 6:40 | No cumple |
| P55 | Conviviente | Se negó ("No por ahora") | No cumple |
| F52 | Conviviente | Sin dato (autoadministrada) | Sin dato |
| I63 | Conviviente | Sin dato (a distancia) | Sin dato |

**Resultado: 3 de 10.** Aun contando a J54 serían 4, y aunque F52 e I63 hubieran cumplido el máximo posible sería 6. **Con cualquier lectura, H1 no puede validarse, y con la lectura estricta queda refutada.**

Dos matices que conviene dejar escritos para que la decisión no se lea más dura de lo que es. Los casos más lentos (N71 y C57) **terminaron**: N71 se pasó por escribir de más, no por dificultad. Y 4 de las 10 personas ya tienen algo escrito (planilla, cuaderno, pizarra, hoja en el refrigerador). El problema no es que la gente no quiera documentar, es que el formato de ocho secciones pide demasiado.

## Decisión

**Se activa el modo ficha de relevo.** La capa 1 del MVP se reduce a tres campos:

| Campo en la interfaz | Tipo de sección en el modelo | Pregunta guía |
|---|---|---|
| **Su día** | `rutina` | ¿Cómo es un día normal, en una o dos líneas? |
| **Si se altera** | `manejo_situaciones` | ¿Qué la calma cuando se angustia o se desorienta? |
| **A quién llamar** | `red_apoyo` | ¿A quién se llama si algo pasa? |

Los nombres de los campos salen de las palabras que usó la gente en las entrevistas ("entrega de turno", "qué la calma", "indicaciones"), no del vocabulario del equipo.

**El modo completo de ocho secciones no se elimina.** Queda en el modelo (`plan_cuidado.modo = 'completo'`) y en el backlog como *Podría*, para quien quiera escribir más.

## Consecuencias

**En el modelo de datos:** ninguna tabla nueva. Los tres campos son tres tipos de sección que ya existían. Se agrega la columna `plan_cuidado.modo`.

**En el backlog:**

- El sprint 2 pasa de "plan de cuidado de ocho secciones" a "ficha de relevo de tres campos". Libera horas.
- **Las horas liberadas van a la capa 2**, como pide el ADR-023: el perfil de consumo sube de prioridad.
- RF-02 (ocho secciones) baja de *Debe* a *Podría*. RF-03 (versión mínima en 5 minutos) se reescribe: la ficha se completa en menos de 3 minutos.
- **Numeración final.** La arquitectura v1.1 renumeró los dos requisitos: **RF-02 es ahora la ficha de tres campos** y RF-03 las secciones opcionales. El backlog usa esa numeración.

**En la arquitectura:** actualizar la sección 3.1 (RF-02 y RF-03), la 10.4 c (las ocho preguntas pasan a tres campos), el ADR-018 (completitud progresiva sobre tres campos) y la sección 17 (el riesgo número uno cambia de "no completa el plan" a "no completa ni siquiera la ficha").

**En el producto:** el peso del valor se traslada a la capa 2, lo que coincide con otro hallazgo de las entrevistas. Cuatro de las ocho personas que aceptarían pagar $5.990 lo condicionan a que resuelva los insumos, no el plan.

## Hallazgos de las entrevistas que entran al diseño de la ficha

| Hallazgo | Quién | Qué cambia |
|---|---|---|
| La incontinencia y el aseo no se quieren escribir "así", por dignidad | J54, C57 | La ficha no pregunta por eso directamente. Si la persona lo escribe, la interfaz no lo nombra en términos clínicos |
| "Es distinto un instructivo que un expediente" | Y40 | Todo el lenguaje de la ficha es de instrucciones para otro, nunca de registro del deterioro |
| La cuidadora remunerada teme que lo que escribe la exponga | A38 | La ficha no tiene campo de incidentes ni de conductas. Es para el relevo, no para vigilar |
| La auditoría de accesos: 5 de 10 no la mirarían | Varias | RF-08 se mantiene por cumplimiento legal (Ley 21.719), no por uso. La pantalla se simplifica a una línea: "La vio Carla, el sábado a las 10:14" |
| Piden modo asistido: que alguien lea las preguntas y escriba | E64 | Se registra como *Podría*. El dictado por voz (ya previsto) cubre parte |

## Lo que esta decisión no resuelve

Las hipótesis **H5, H6 y H7 quedaron no concluyentes**. El protocolo exige cuatro entrevistas más antes de decidir sobre ellas. H5 decide si el pago dividido (110 de las 373 horas comprometidas) vuelve al alcance. Con el segundo recorte de la arquitectura v1.1 ya salió del semestre, así que no afecta a los sprints 1 a 3. **Las cuatro entrevistas tienen que estar hechas antes del sprint 4 del calendario v1.3, que empieza el 6 de noviembre** y trae el pedido y el pago.

Y un problema de método que hay que corregir antes de entregar el análisis: la ficha de A55 nombra a la entrevistada y a una tercera persona, lo que rompe la anonimización del protocolo. **Corregido el 13 de octubre:** se quitaron los nombres de A55, y la mención del integrante del equipo que hizo el contacto también de F52 y J54 (MATU-28).

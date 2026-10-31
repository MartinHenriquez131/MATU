# ADR-028 · La ficha de relevo crece con secciones complementarias

**Estado:** Aceptado
**Fecha de decisión:** 31 de octubre de 2026
**Decisores:** Jorge Espinoza (Product Owner) · Martín Henríquez (Scrum Master)
**Complementa:** el ADR-023 (modo ficha de relevo). **Reabre:** RF-03 para el semestre, con otra lista de secciones

---

## Contexto

El ADR-023 redujo la capa 1 a una ficha de tres campos (Su día, Si se altera y A quién llamar) porque el formato de ocho secciones pedía demasiado. Solo 3 de 10 personas respondían tres preguntas en menos de 5 minutos. La reducción resolvió **el llenado inicial**: la ficha se completa en menos de 3 minutos.

Al ver el producto en la demo del 30 de octubre apareció lo que la reducción dejó afuera. Tres campos bastan para que un relevo no cometa errores graves, pero no para que **conozca a la persona**: qué música la tranquiliza, de qué le gusta conversar, cómo se le habla si no oye bien o qué remedios toma. Las ocho secciones de RF-03 seguían en el backlog como *Podría*, fuera del semestre, y su lista mezclaba temas que repiten lo que ya dicen los tres campos.

## Decisión

**La ficha tiene dos niveles.**

1. **Ficha inicial, sin cambios:** los tres campos del ADR-023. Es lo único obligatorio, se llena en menos de 3 minutos y basta para compartir con un relevo.
2. **Secciones complementarias, opcionales:** la cuidadora las agrega cuando quiere y en el orden que quiere. Ningún flujo las exige, y la ficha nunca aparece como "incompleta" por no tenerlas.

**Las seis secciones complementarias:**

| Sección en la interfaz | Tipo en el modelo | Qué guarda | Pregunta guía |
|---|---|---|---|
| **Quién es** | `quien_es` (nuevo) | Cómo le gusta que la llamen, a qué se dedicó, de dónde es, personas y mascotas importantes, creencias | ¿Qué debería saber de ella alguien que la conoce hoy? |
| **Lo que la hace bien** | `preferencias` | Música, temas de conversación, programas, actividades y formas simples de distraerla | ¿Qué la pone contenta o la entretiene? |
| **Comer y beber** | `alimentacion` | Comidas favoritas, lo que no le gusta, texturas, cómo le gusta que le sirvan | ¿Qué le gusta comer y cómo? |
| **Moverse y descansar** | `movilidad` | Bastón o silla, cómo ayudarla a levantarse o acostarse, cómo duerme | ¿Cómo se la ayuda a moverse y a descansar? |
| **Cómo hablarle** | `comunicacion` (nuevo) | Audífonos, lentes, de qué lado oye mejor, cómo avisa que algo le duele o le molesta | ¿Qué ayuda a que te entienda y a entenderla? |
| **Sus remedios** | `remedios` (nuevo) | Texto libre: qué toma y a qué hora, tal como se lo da la familia | ¿Qué remedios toma y cuándo? |

### Por qué estas seis y no otras

**Respaldo.** Siguen el enfoque de cuidado centrado en la persona (Kitwood, *Dementia Reconsidered*, 1997), que pide que quien cuida conozca la historia, los gustos y la forma de comunicarse de la persona, y no solo sus necesidades. La lista coincide con los temas de *This is me*, la ficha que la Alzheimer's Society propone para que un cuidador nuevo conozca a la persona: quién es, qué la tranquiliza, cómo se comunica, cómo come, se mueve y duerme, y qué remedios toma. Los remedios además aparecieron en las entrevistas: tres de diez dependen del consultorio o del hospital para sus fármacos.

**Sin redundancia con los tres campos.** Cada tema tiene un solo lugar:

| Tema | Va en | Por qué no en otra parte |
|---|---|---|
| Horarios, rutina del día | **Su día** (campo inicial) | Se elimina la sección `horarios` de RF-03: repetía Su día |
| Qué hacer si se angustia | **Si se altera** (campo inicial) | Lo que se *hace* en el momento va ahí. **Lo que la hace bien** guarda los gustos que previenen y distraen, y Si se altera puede remitir a ella |
| Familia, vecinos, a quién llamar | **A quién llamar** (campo inicial) | Se elimina la sección `red_apoyo` como complementaria. **Quién es** nombra a las personas importantes en su vida, no los contactos |
| Actividades | **Lo que la hace bien** | Se unen `preferencias` y `actividades` de RF-03: la música o un programa podían ir en cualquiera de las dos |

**Lo que no entra, a propósito.** No hay una sección de aseo ni de cuidado personal. En el ADR-023, E01 y E10 dijeron que eso no se quiere escribir "así", por dignidad. Si la familia quiere decir algo, lo escribe en Moverse y descansar o en Si se altera, con sus palabras. Tampoco hay un campo de diagnóstico ni de "conductas": la ficha es un instructivo para el relevo, no un expediente (E07 y E08).

### Reglas para "Sus remedios"

Es la sección más útil para un relevo, y también la más delicada:

- **Solo texto libre.** No hay catálogo de fármacos, ni dosis estructuradas, ni recordatorios.
- **El aviso va siempre visible:** "Esto lo escribe la familia. No reemplaza la indicación del médico".
- **Antes de construirla, el analista normativo hace una revisión previa:** qué se informa en la política de privacidad, qué se recomienda escribir y cómo se comparte.
- **Al compartir, viene desmarcada por defecto.** La cuidadora decide si el relevo la ve.

### Cómo se comparte

Al crear un acceso de relevo, la cuidadora ve los tres campos iniciales, que siempre van. Debajo, marca qué secciones complementarias también ve ese relevo. Es lo que permite el cifrado por sección (arquitectura 7, decisión i).

## Consecuencias

**En el modelo de datos:** no hay tablas nuevas. `plan_seccion.tipo` suma `quien_es`, `comunicacion` y `remedios`, y deja de usar `horarios`, `actividades` y `red_apoyo` como complementaria. Cada sección se cifra igual que los tres campos (AES-256-GCM, clave por persona, AAD `plan_id ‖ tipo`), y la auditoría y el `ETag` de MATU-13 también aplican. `plan_cuidado.modo` deja de ser necesario: no hay "modo completo", solo secciones agregadas.

**En el backlog:**
- La tarjeta "Secciones opcionales del plan de cuidado" sale del Product Backlog.
- En el sprint 3, MATU-49 (diseño, revisión normativa y contrato).
- En el sprint 4, MATU-50 (backend y pantallas).
- La hoja imprimible (MATU-52) incluye las secciones que la familia haya agregado.

**En la arquitectura v1.2:**
- **RF-03** se reescribe con estas seis secciones, como *Debe* en el semestre.
- **Sección 7:** los tipos de sección.
- **Sección 10.4:** las preguntas guía.
- Este ADR se agrega a la lista.

**En `lenguaje.md`:** los nombres, las preguntas guía, un ejemplo por sección y el aviso de los remedios.

**En el producto:** una barra de avance que celebre lo agregado, sin castigar lo que falta (ADR-018). La ficha inicial sigue siendo la puerta de entrada y la meta de los 3 minutos no cambia. Lo que se mide en la usabilidad es la ficha inicial.

## Lo que esta decisión no resuelve

- **Si las seis secciones son las correctas para las cuidadoras chilenas.** Se pregunta en la segunda ronda de usabilidad (sprint 4) y en las entrevistas de MATU-35.
- **Plantillas por tipo de dependencia** (por ejemplo, demencia o movilidad reducida). Siguen fuera del semestre.
- **Los recordatorios de remedios.** Convertir el texto en alertas exige otra revisión normativa, y queda para después del semestre, junto con "Medicamentos y CESFAM".

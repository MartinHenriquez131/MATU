# Reparto del trabajo en prueba · Jorge desarrolla, Martín prueba y despliega

**Estado:** convertida en el [ADR-030](../adr/ADR-030-roles-del-equipo.md) el 5 de noviembre de 2026, por decisión de Jorge en la revisión del sprint 3. Esta nota queda como antecedente
**Aprobado por:** Jorge Espinoza (Product Owner) y Martín Henríquez (Scrum Master), el 4 de noviembre de 2026
**Se evalúa:** el jueves 5 de noviembre de 2026, en la revisión y la retrospectiva del sprint 3
**Resultado:** continuó. La evaluación del 5 de noviembre lo dejó como definitivo, y esta nota se convirtió en el ADR-030

---

## Por qué

Por economía. Jorge tiene el plan Max y Martín el plan Pro. El desarrollo con todos los agentes consume muchos tokens, así que lo concentra quien tiene más capacidad. Martín usa la suya para lo que mejor protege la calidad: probar, desplegar y revisar.

## El reparto

### Jorge · Product Owner y desarrollo

- **Todas las tarjetas de arquitectura, backend y frontend**, con todos los agentes actuales:
  - el QA previo al PR;
  - el analista normativo, en la revisión previa y en la de cierre;
  - el diseñador, en la especificación y en la revisión visual.
- **Como PO:**
  - las tarjetas de decisión;
  - las responsabilidades del rol;
  - cualquier decisión importante del proyecto, aunque venga de otra tarjeta.

### Martín · Tester/QA y despliegue

- **Dueño del despliegue:** staging, HTTPS y el entorno de demostración.
- **Dueño de la prueba en el teléfono** y de las pruebas con usuarios: usabilidad y entrevistas.
- **Prueba y evalúa lo que construye Jorge**, y revisa la consistencia de la redacción y la construcción de los documentos.
- **No toca código de producto ni cambia decisiones.** Da feedback profesional y exigente, con PASS/FAIL y evidencia.
- **Sigue revisando y fusionando los PR de Jorge.** Nadie fusiona su propio trabajo.

### El feedback de Martín: carpeta `TESTER/`

- Cada revisión de Martín es un archivo `.md` en `TESTER/`, en la raíz del repositorio MATU.
- **Nombre del archivo:** `AAAA-MM-DD-MATU-XX-<tema>.md`, por ejemplo `2026-11-05-MATU-50-ficha-ampliada.md`.
- **Contenido:**
  - la historia;
  - el PR revisado;
  - el veredicto por criterio (PASS/FAIL);
  - los hallazgos P1, P2 y P3 con evidencia;
  - lo que pide corregir.
- La plantilla está en [`TESTER/README.md`](../../TESTER/README.md).
- **Al retomar una historia, el orquestador de Jorge lee `TESTER/` y responde a cada hallazgo pendiente.** La respuesta queda en el mismo archivo, en la sección «Respuesta de Jorge».

### Cómo trabaja cada orquestador

Son dos modos. Se describen en el repositorio MATU_PROYECTO (`CLAUDE.md` y `.claude/modos-de-trabajo.md`):

- **Modo Jorge:** orquestador completo.
- **Modo Martín:** orquestador revisor. Usa agentes propios y livianos, con Opus y esfuerzo mínimo.

## Qué contradice, y qué manda mientras dure la prueba

**Mientras dure la prueba, esta nota manda sobre lo siguiente:**

| Documento | Qué dice hoy | Qué cambia en la prueba |
|---|---|---|
| `CLAUDE.md` de MATU_PROYECTO, sección 0 | «Ellos deciden», sin distinguir roles | Decide Jorge como PO. Martín no cambia decisiones: las evalúa |
| `CLAUDE.md`, sección 3 (agente 1) | Un solo orquestador, que dirige cualquier historia | Dos modos: completo (Jorge) y revisor (Martín) |
| `CLAUDE.md`, sección 3 (agentes 2 a 6) | Los agentes trabajan para cualquiera de los dos | Los seis agentes son de Jorge. Martín usa sus variantes revisoras, el desplegador y el revisor documental |
| `CLAUDE.md`, sección 3 (agente 2) | El backend developer toca `infra/` | La configuración de despliegue (Railway) y las variables de staging pasan al desplegador de Martín. El backend sigue con `infra/` local (`docker-compose.yml`, `postgres/init/` y `semillas/`) |
| `CLAUDE.md`, sección 4, pasos 8 y 10 | «La otra persona del equipo» revisa. Las horas son las de «la persona con quien trabaja» | Martín revisa y fusiona todos los PR de producto. Se anotan las horas de cada uno en sus propias tarjetas |
| `docs/backlog-sprints-1-3.md`, «Regla de ejes en este tramo» | Reparto por eje, con la regla suspendida solo en `care_circle`, `care_plan` y `shared` | Se suspende para todos los módulos: todo el desarrollo es de Jorge |
| `docs/arquitectura.md`, sección 15.5 | Reparto por eje vertical: A (Jorge) y B (Martín) | Igual que la fila anterior. Las etiquetas «Eje A - Jorge» y «Eje B - Martín» de Trello se usan como «dueño de la tarjeta» |
| `docs/sprints/sprint-1-planificacion.md` | «Jorge revisa los PR de Martín y Martín los de Jorge» | Martín revisa los PR de Jorge. Si Martín abre un PR de despliegue o de documentos, lo revisa Jorge |
| `docs/sprints/calendario-sprints.md` | Capacidad de 11 h para Jorge y 12 h para Martín, con desarrollo repartido | La capacidad no cambia, pero las 23 h de desarrollo pasan a las 11 h de Jorge. Es el principal riesgo (ver criterios) |

**Qué no cambia:**
- las políticas innegociables (`CLAUDE.md`, sección 5);
- la definición de terminado;
- la revisión obligatoria de la otra persona cuando una historia toca datos sensibles o dinero;
- la analista previa antes de implementar datos personales, consentimiento o dinero.

## Criterios para decidir el jueves 5

Cada criterio se mide con datos, no con impresiones:

1. **Tokens usados por cada uno.**
   - **Cómo se mide:** el uso del plan de cada uno en la semana (panel de uso de Claude), y si alguno llegó a su límite.
   - **Funciona si:** Martín no llega al límite del plan Pro, y Jorge no lo hace antes de terminar sus tarjetas.
2. **Tiempo hasta la fusión de los PR.**
   - **Cómo se mide:** desde que se abre el PR hasta que se fusiona, con la hora de GitHub.
   - **Funciona si:** el tiempo no sube respecto del sprint 3 (por ejemplo, #33 se abrió y se fusionó el mismo 03-11).
3. **Calidad del feedback.**
   - **Cómo se mide:** cuántos hallazgos de `TESTER/` tienen evidencia y cuántos llevaron a un cambio, y si apareció un defecto que la revisión no vio.
   - **Funciona si:** cada hallazgo trae evidencia reproducible y la prueba en el teléfono se hace antes de mover a Terminado.
4. **Cuellos de botella.**
   - **Cómo se mide:**
     - las tarjetas que esperaron a una sola persona, y por cuánto tiempo;
     - los PR apilados sin revisar;
     - las horas de Jorge frente a las 11 h de su capacidad.
   - **Funciona si:** ninguna historia que nunca se sacrifica queda bloqueada por falta de capacidad de Jorge.

El resultado de la evaluación quedó como comentario en la tarjeta de la retrospectiva del sprint 3. Como continuó, se redactó el ADR-030, y se actualizan `CLAUDE.md` (MATU_PROYECTO #56), el backlog, la arquitectura (v1.2, MATU-43) y `docs/sprints/`.

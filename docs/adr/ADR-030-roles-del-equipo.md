# ADR-030 · Roles del equipo: Jorge desarrolla, Martín despliega, prueba y revisa

**Estado:** Aceptado
**Fecha de decisión:** 5 de noviembre de 2026, en la revisión del sprint 3
**Decisor:** Jorge Espinoza (Product Owner). Martín Henríquez (Scrum Master) revisa en el PR
**Reemplaza:** la nota [`docs/sprints/reparto-en-prueba.md`](../sprints/reparto-en-prueba.md), que era una prueba aprobada el 4 de noviembre. **Ajusta:** el reparto por eje vertical de la arquitectura, sección 15.5

---

## Contexto

El 4 de noviembre Jorge y Martín probaron otro reparto por una semana: Jorge desarrolla todo y Martín prueba, despliega y revisa. El motivo fue económico: Jorge tiene el plan Max y Martín el plan Pro, y el desarrollo con todos los agentes consume muchos tokens.

Durante la prueba, el 4 y el 5 de noviembre:
- **Martín revisó y fusionó toda la fila de PR del sprint 3**, del #39 al #55, y dejó sus informes en `TESTER/`.
- **Probó en el teléfono, en staging,** MATU-39, 36, 37, 57, 50 y 48, y encontró hallazgos con evidencia. Por ejemplo, un 429 que se mostraba como problema de conexión, que se corrigió en el #51.
- **Jorge cerró en desarrollo** MATU-40, 41, 48 y 50, y los PR de calidad del #49 al #55.
- **El sprint 3 cerró con 15 historias en `main`** y el objetivo específico 4 cumplido.

## Decisión

**El reparto de la prueba queda como definitivo.**

**Jorge · Product Owner y desarrollo.**
- Todas las tarjetas de arquitectura, backend y frontend, con los seis agentes:
  - el QA previo al PR;
  - el analista normativo, antes y al cierre;
  - el diseñador, en la especificación y en la revisión visual.
- Como PO decide el alcance, las prioridades y los criterios.

**Martín · Scrum Master, despliegue y pruebas.**
- Dueño del despliegue: staging, HTTPS y el entorno de demostración.
- Dueño de la prueba en el teléfono y de las pruebas con usuarios (usabilidad y entrevistas).
- Revisa y fusiona los PR de Jorge, con su informe en `TESTER/` (PASS o FAIL, con evidencia).
- Revisa la redacción y la construcción de los documentos.
- No toca código de producto ni cambia decisiones: las evalúa.

**Se mantienen sin cambios:**
- las políticas innegociables de `CLAUDE.md`, sección 5;
- la definición de terminado;
- nadie fusiona su propio trabajo;
- la revisión obligatoria de la otra persona cuando una historia toca datos sensibles o dinero;
- la revisión previa del analista normativo antes de implementar datos personales, consentimiento o dinero.

**En Trello:**
- la etiqueta «Eje A - Jorge» o «Eje B - Martín» dice quién lleva la tarjeta;
- cada ítem de los checklists empieza con quién lo hace («Jorge ·» o «Martín ·»). La herramienta de Trello no permite asignar miembros a los ítems.

**Fusiones:** los PR apilados se fusionan con merge commit y no con squash, para que el siguiente PR de la pila no quede en conflicto. Pasó el 5 de noviembre con el #51 y el #53.

## Consecuencias

- **Capacidad:** las 23 horas semanales de desarrollo dependen de las 11 horas de Jorge. Es el riesgo principal, y se mide con el factor de vibecoding de cada retrospectiva.
- **Documentos que se actualizan:**
  - `CLAUDE.md` de MATU_PROYECTO (PR aparte);
  - la regla de ejes del backlog;
  - la arquitectura, sección 15.5, en la v1.2 (MATU-43);
  - `docs/sprints/`.
- **La nota de la prueba** queda como antecedente, con su estado cambiado a «Convertida en el ADR-030».
- **El sprint 4 se planificó con estos roles** el 5 de noviembre.

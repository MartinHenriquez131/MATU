# MATU — Planificación del sprint 5

**Sprint:** 5 · viernes 13 a jueves 19 de noviembre de 2026 · semanas 14 y 15 del ramo
**Equipo:** Jorge Espinoza (Product Owner, desarrolla con los seis agentes) · Martín Henríquez (Scrum Master, despliega, prueba y fusiona, ADR-030)
**Base:** [Calendario de sprints v1.3](calendario-sprints.md) · [Planificación del sprint 1](sprint-1-planificacion.md) · tarjetas de la lista «Sprint 5» de Trello al 12 de noviembre

---

## 1. Objetivo del sprint

> **La familia retira con código lo que pagó y ve sus pedidos, MATU queda desplegado con los seis recorridos críticos y el pipeline completo en verde, y se entrega la evidencia de la Fase 3 con el guion de demostración y la presentación final.**

Es el último sprint con alcance comprometido. Tiene tres partes:

1. **Cerrar la capa 3 de punta a punta.** El pedido (MATU-61) y el pago (MATU-62) ya están en `main`. Faltan la vista de comercio con el código de retiro (MATU-63), la pantalla «Mis pedidos» de la familia (MATU-92) y los avisos del pedido (MATU-76).
2. **Cumplir el objetivo específico 7.** El sistema en el entorno de demostración, con los seis recorridos críticos operativos y el pipeline completo en verde (MATU-64, MATU-79 y MATU-80).
3. **Entregar la Fase 3.** El informe con la evidencia (MATU-78), el guion de demostración (MATU-77) y la presentación final (MATU-104).

**El sprint se cruza con la entrega final de la Fase 2** (semana 15, del 16 al 21 de noviembre). Por eso el guion de demostración y el informe quedan listos el **lunes 16 de noviembre**, y desde ahí lo que queda del sprint es endurecimiento y corrección. Los sprints 6 y 7 son de reserva, y la presentación final de la Fase 3 es en las semanas 17 y 18.

## 2. Capacidad y compromiso

**Decisión de Jorge del 12 de noviembre: no hay plan de sacrificio en este sprint.**

La razón es que las estimaciones del semestre resultaron muy por encima de lo real con vibecoding. El caso más claro es MATU-61: se estimó en 10 h y tomó poco más de 3 h reales. Con ese factor, lo que está en la tabla de prioridad cabe en el sprint sin recortar.

| | Jorge | Martín |
|---|---|---|
| Qué hace | Desarrolla todo con los seis agentes, redacta lo técnico del informe y prepara las láminas | Revisa y fusiona la cola, despliega la demo, hace la usabilidad, escribe el guion y prueba en el teléfono |
| Estimaciones de las tarjetas (las que la tienen) | MATU-63 (6 h), MATU-76 (4 h), MATU-95 (1,5 h), MATU-81 (8 h), MATU-79 (8 h), MATU-96 (1,5 h), y su parte de MATU-78 (5 h), MATU-77 (2 h), MATU-80 (7 h) y MATU-104 (4 h) | MATU-64 (4 h), MATU-65 (5 h), y su parte de MATU-78 (3 h), MATU-77 (2 h), MATU-80 (2 h) y MATU-104 (2 h) |
| Sin estimación todavía | MATU-92, MATU-100 y MATU-103, que se estiman en su plan | La cola de revisión del sprint 4 |

**Las horas se miden y van al factor de vibecoding.** Al cerrar cada tarjeta se anotan en Trello las horas reales, con sus marcas de tiempo objetivas (movimientos de la tarjeta y commits) en hora de Chile. El factor del sprint y el del semestre se calculan en la ceremonia del jueves 19 y entran a MATU-78 y a MATU-104.

**Si de todas formas algo no alcanza**, se aplica el orden de sacrificio del calendario (sección 5), que sigue vigente para el proyecto: primero los indicadores del backoffice. **Nunca se sacrifican** la ficha de relevo, el acceso de relevo, la predicción de quiebre ni la exportación de la lista.

## 3. Estado al empezar

### En Revisión, esperando a Martín

MATU-62, MATU-94, MATU-86, MATU-93, MATU-55, MATU-42, MATU-53 y MATU-46. **MATU-54 entra hoy, 12 de noviembre.**

MATU-62 ya está fusionada en `main` de MATU_PROYECTO (PR #86, con la migración 0024 y la política 0.13). La tarjeta espera su cierre.

### La cola de fusión

En el orden de la fila de migraciones. Cada PR de código lleva su PR de documentos en el repositorio MATU.

| Orden | PR de MATU_PROYECTO | Tarjeta | Migración | Política | PR de documentos en MATU |
|---|---|---|---|---|---|
| 1 | #85 | MATU-94 · correcciones de la revisión de Martín a MATU-61 | — | — | #78 |
| 2 | #84 | MATU-86 · la ficha de la familia muestra los teléfonos | — | — | — |
| 3 | #87 | MATU-93 · ningún texto bajo 17 px | — | — | — |
| 4 | #88 | MATU-55 · Dónde entraste, ingresos y avisos | 0025 | 0.14 | #81 |
| 5 | #89 | MATU-42 y MATU-53 · invitar a un familiar y ver el grupo | 0026 | 0.15 | #82 |
| 6 | #90 | MATU-46 · el teléfono del relevo se borra a los 30 días | 0027 | 0.16 | #83 |
| 7 | MATU-54 (se abre hoy) | MATU-54 · Mis datos | 0028 | 0.17 | se abre con el PR |

**Hasta que estén en `main` los siete PR** (#84 a #90 y el de MATU-54), el despliegue final de MATU-80 no tiene todo lo que necesita.

### Migraciones y políticas

- **Migraciones:** `main` llega a la 0024 (MATU-62). La cola trae de la 0025 a la 0028. **La 0029 queda reservada para MATU-63**, por los permisos del comercio.
- **Política de privacidad:** `main` está en la 0.13 (MATU-62). La cola trae de la 0.14 a la 0.17, **una versión por fusión**.

## 4. Tabla de prioridad

El orden es el orden de ejecución.

| P | Tarjeta | Día | Responsable | Depende de |
|---|---|---|---|---|
| 1 | Ceremonia · Revisión y retrospectiva del sprint 4, y planificación del sprint 5 | vie 13 | Jorge y Martín | — |
| 2 | MATU-63 · Vista de comercio con código de retiro | vie 13 | Jorge | MATU-61, 62 |
| 3 | MATU-64 · Entorno de demostración (arrastre) | vie 13 y sáb 14 | Martín | MATU-63 para el recorrido 6 |
| 4 | MATU-92 · Mis pedidos | sáb 14 | Jorge | MATU-63 |
| 5 | MATU-76 · Avisos del pedido | sáb 14 | Jorge | MATU-63, 74 |
| 6 | MATU-95 · Ficha: «A quién llamar» y alergias | dom 15 | Jorge | — |
| 7 | MATU-81 · Backoffice mínimo | dom 15 | Jorge | MATU-61, 62, 63 |
| 8 | MATU-65 · Usabilidad ronda 2 (arrastre) | hasta dom 15 | Martín | la app en staging |
| 9 | MATU-78 · Evidencia de la Fase 3 | lun 16 | Jorge y Martín | MATU-65 |
| 10 | MATU-77 · Guion de demostración | lun 16 | Jorge y Martín | MATU-64 |
| 11 | MATU-80 · E2E, carga y despliegue final | mar 17 | Jorge y Martín | MATU-63, 64, 92 |
| 12 | MATU-79 · Endurecimiento, retención y CI | mar 17 y mié 18 | Jorge | MATU-74 |
| 13 | MATU-96 · Prueba de carrera | mié 18 | Jorge | — |
| 14 | MATU-103 · Velo de los diálogos | mié 18 | Jorge | — |
| 15 | MATU-100 · Coherencia de documentos | mié 18 | Jorge | — |
| 16 | MATU-104 · Presentación final | jue 19, y se pule en la reserva | Jorge y Martín | MATU-77, 78 |
| 17 | Ceremonia · Revisión final y retrospectiva del semestre | jue 19 | Jorge y Martín | — |

**Las que necesitan revisión previa del analista normativo** (tocan dinero o datos personales): MATU-63, MATU-92, MATU-76 y MATU-81. Va antes de implementar, sin excepción.

**Las que tienen pantallas** pasan por la especificación y la revisión visual del diseñador: MATU-63, MATU-92, MATU-95, MATU-81 y MATU-103.

## 5. Secuencia por día

| Día | Jorge, con los agentes | Martín |
|---|---|---|
| Viernes 13 | Ceremonia (P1) · MATU-63: revisión previa del analista, especificación del diseñador, migración 0029, backend y vista del comercio | Ceremonia (P1) · revisa y fusiona la cola del sprint 4 en orden: #85, #84 y #87 · MATU-64: el recorrido 6 apenas MATU-63 esté en staging |
| Sábado 14 | MATU-92 (Mis pedidos) · MATU-76 (avisos del pedido) | Revisa y fusiona #88, #89, #90 y MATU-54, con sus PR de documentos · cierra MATU-64 con los seis recorridos · revisa el PR de MATU-63 |
| Domingo 15 | MATU-95 (la ficha) · MATU-81 (backoffice) | Termina MATU-65 (usabilidad ronda 2) y su informe · revisa MATU-92 y MATU-76 |
| Lunes 16 | MATU-78: lo técnico y el estado de los siete objetivos · MATU-77: revisa el guion | MATU-78: usabilidad, entrevistas y revisión del documento · MATU-77: escribe y ensaya el guion. **El informe y el guion quedan listos hoy** |
| Martes 17 | MATU-80: las cinco pruebas de extremo a extremo que faltan y la carga con k6 · inicio de MATU-79 | MATU-80: corre las pruebas sobre la demo y hace el despliegue final desde `main` · revisa MATU-95 y MATU-81 |
| Miércoles 18 | MATU-79 (retención, pruebas y puertas del CI) · MATU-96 · MATU-103 · MATU-100 | Revisa MATU-79, MATU-96, MATU-103 y MATU-100 · restablece la demo desde cero |
| Jueves 19 | MATU-104: láminas y guion · ceremonia de cierre (P17) | MATU-104: la demo y su guion, ensayo con cronómetro · ceremonia de cierre (P17) |

**La cola del sprint 4 se fusiona el viernes 13 y el sábado 14**, antes del despliegue final. Martín la fusiona en el orden de la sección 3, con merge commit. Si pide cambios en un PR de abajo, el orquestador de Jorge los corrige y los propaga a los de arriba.

**Las historias de este sprint que tocan dinero o datos sensibles las revisa Martín siempre**, con su informe en `TESTER/` (definición de terminado, punto 5).

## 6. Fila de migraciones y políticas

Toda historia con migración parte de la punta de la última rama abierta que también tenga una y toma el número siguiente. Las que no tienen migración salen de `main` y se fusionan en cualquier orden.

| Migración | Tarjeta | Política | Estado al 12 de noviembre |
|---|---|---|---|
| 0024 | MATU-62 · pago con Webpay Plus | 0.13 | En `main` (PR #86) |
| 0025 | MATU-55 · Dónde entraste | 0.14 | PR #88, en revisión |
| 0026 | MATU-42 y MATU-53 · invitar y ver el grupo | 0.15 | PR #89, en revisión |
| 0027 | MATU-46 · teléfono del relevo | 0.16 | PR #90, en revisión |
| 0028 | MATU-54 · Mis datos | 0.17 | El PR se abre hoy |
| 0029 | MATU-63 · vista de comercio | La siguiente, si su revisión previa la pide | Reservada |
| Las que sigan | MATU-76 (tipos de aviso en un `CHECK`) y MATU-79 (retención), si la llevan | Una por fusión | Se fija en el plan de cada una |

**Sin migración:** MATU-94, MATU-86, MATU-93, MATU-92 (si su plan no la pide), MATU-95, MATU-96, MATU-103 y MATU-100.

## 7. Definición de terminado

Una historia está terminada cuando, y solo cuando:

1. Tiene pruebas de dominio de sus reglas nuevas
2. Tiene al menos una prueba de integración del camino feliz y una del principal camino de error
3. El pipeline pasa completo, incluidas las pruebas de arquitectura y de aislamiento
4. Si toca una pantalla, cumple el checklist de accesibilidad (estrategia de pruebas, sección 7) y la aprueba el diseñador
5. Si toca dinero o datos sensibles, la revisa la otra persona. Sin excepción. **Martín la revisa y deja su informe en `TESTER/`**, y recién entonces fusiona
6. Si corrige un defecto, deja una prueba que falla sin la corrección

**Con vibecoding no hay excepciones:** el código generado por los agentes cumple los mismos seis puntos que el escrito a mano.

## 8. Guion de la revisión del sprint

La revisión del jueves 19 muestra el objetivo con **los seis recorridos críticos de MATU-64**, en vivo contra el entorno de demostración restablecido desde cero (`docs/entorno-demo.md`) y con las cuentas sintéticas de la semilla:

1. **Crear la cuenta, la persona cuidada y su autorización, y llenar la ficha.**
2. **Compartir la ficha con un relevo con PIN**, abrirla en otro teléfono y cortar el acceso.
3. **Anotar los insumos y ver el aviso de quiebre.**
4. **Exportar, imprimir o compartir la lista de reposición**, y anotar lo que se compró.
5. **Armar el pedido desde la lista y pagar el total exacto** en el ambiente de integración de Transbank, con sus tarjetas de prueba publicadas.
6. **Retirar con código en el comercio simulado**, y ver el pedido entregado en «Mis pedidos».

Se dice en voz alta qué es simulado: el comercio, el envío de avisos y el pago en integración.

Y en pantalla, el pipeline completo en verde con `test_aislamiento.py`, `test_arquitectura.py` y las seis pruebas de extremo a extremo de MATU-80.

**Además, en la retrospectiva** se calcula el factor de vibecoding del sprint y del semestre (horas estimadas de lo terminado divididas por horas reales), y se revisa el trabajo con agentes y los roles del ADR-030.

## 9. Riesgos del sprint

| Riesgo | Probabilidad | Qué se hace |
|---|---|---|
| **La cola de revisión de Martín.** Siete PR del sprint 4, más los del sprint 5, con revisión obligatoria en los que tocan dinero o datos sensibles | **Alta** | La cola del sprint 4 se fusiona el viernes 13 y el sábado 14, en el orden de la fila. Los PR sin migración no esperan a nadie. Si el sábado en la noche queda algo sin fusionar, se avisa en Discord y se decide si el despliegue final del martes 17 sale sin eso |
| **La fecha de la presentación.** La de la semana 15 puede caer antes del jueves 19 | **Alta** | El informe y el guion quedan listos el lunes 16. La fecha exacta se confirma con el profesor (MATU-104). El plan B es el video y las capturas de MATU-78 |
| **Pruebas intermitentes.** La de carrera de MATU-96 (404 en vez de 403 según quién gane) y la de `envasesMeQuedan` cuando la máquina está cargada | Media | MATU-96 fija el orden con una sincronización explícita y la corre 50 veces seguidas. Si la de `envasesMeQuedan` vuelve a fallar en el CI, se abre una tarjeta propia con el mismo criterio. Una prueba inestable nunca se marca como omitida para que el pipeline pase |
| **Docker.** Las pruebas y las migraciones locales dependen de Docker Desktop, y la imagen de la demo todavía no trae la semilla del catálogo (hallazgo H1 de MATU-64) | Media | Se revisa que Docker esté arriba antes de cada auditoría del QA. El `Dockerfile` se corrige dentro de MATU-64 o MATU-80, antes del despliegue final |
| **Las dependencias de MATU-63.** MATU-92, MATU-76, MATU-81, MATU-80 y el recorrido 6 de MATU-64 esperan su vista y sus estados | Media | MATU-63 es la primera prioridad del viernes 13. Si se atrasa, en la demo el retiro se opera a mano (orden de sacrificio, punto 2) y MATU-95, que no depende de nada, se adelanta |

## 10. Qué queda para después del semestre

Lo que sigue no se construye en el sprint 5. Está en la columna Product Backlog de Trello y se presenta en MATU-104 como lo que viene.

**Fase 2 del producto:**
- El pago dividido entre varios familiares y el prorrateo (hipótesis H5 y H6)
- La reposición programada, la app de repartidor y la liquidación automática

**Antes de datos reales:**
- MATU-89, MATU-99, MATU-101 y MATU-102
- MATU-98
- Las consultas legales abiertas, en su tarjeta de Trello
- Lo de la épica «Paso a producción» que MATU-79 deja fuera: MFA, HSTS, monitoreo con alertas y quitar `auditoria.ip`

Mientras eso no esté cerrado, MATU trata **solo datos sintéticos**.

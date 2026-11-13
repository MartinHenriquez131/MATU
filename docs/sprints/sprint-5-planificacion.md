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
| Estimaciones de las tarjetas (las que la tienen) | MATU-63 (6 h), MATU-76 (4 h), MATU-95 (1,5 h), MATU-81 (8 h), MATU-79 (8 h), MATU-96 (1,5 h), MATU-106 (1 h), y su parte de MATU-78 (3 h), MATU-77 (2 h), MATU-80 (7 h) y MATU-104 (4 h) | MATU-64 (4 h), MATU-65 (5 h), y su parte de MATU-78 (5 h, lidera la redacción), MATU-77 (2 h), MATU-80 (2 h) y MATU-104 (2 h) |
| Sin estimación todavía | MATU-92 y MATU-103, que se estiman en su plan | MATU-100 y la cola de revisión del sprint 4 |

**Carga real.** Con los agentes, las cerca de 45 h estimadas de Jorge son unas 15 h reales. Martín carga cerca de 27 h de persona: la demo, la usabilidad, su parte de MATU-77, 78, 80 y 104, y la revisión de 9 PR con su informe en `TESTER/` y la prueba en el teléfono. Por eso se le pasaron solo MATU-100 y el liderazgo de la redacción de MATU-78 (decisión de Jorge del 12 de noviembre). La cola del sprint 4 ya quedó fusionada el 12 de noviembre, así que esas horas de Martín se liberan para MATU-64 y MATU-65.

**Las horas se miden y van al factor de vibecoding.** Al cerrar cada tarjeta se anotan en Trello las horas reales, con sus marcas de tiempo objetivas (movimientos de la tarjeta y commits) en hora de Chile. El factor del sprint y el del semestre se calculan en la ceremonia del jueves 19 y entran a MATU-78 y a MATU-104.

**Si de todas formas algo no alcanza**, se aplica el orden de sacrificio del calendario (sección 5), que sigue vigente para el proyecto: primero los indicadores del backoffice. **Nunca se sacrifican** la ficha de relevo, el acceso de relevo, la predicción de quiebre ni la exportación de la lista.

## 3. Estado al empezar

### El sprint 4 quedó cerrado en `main` el 12 de noviembre

Martín revisó, fusionó y desplegó en staging y en la demostración toda la cola, en el orden de la fila de migraciones. MATU-62, MATU-94, MATU-86, MATU-93, MATU-55, MATU-42, MATU-53, MATU-46 y MATU-54 están en Terminado.

| Orden | PR de MATU_PROYECTO | Tarjeta | Migración | Política | PR de documentos en MATU |
|---|---|---|---|---|---|
| 1 | MATU_PROYECTO#86 | MATU-62 · pago con Webpay Plus | 0024 | 0.13 | MATU#79 |
| 2 | MATU_PROYECTO#85 | MATU-94 · correcciones de la revisión de Martín a MATU-61 | — | — | MATU#78 |
| 3 | MATU_PROYECTO#84 | MATU-86 · la ficha de la familia muestra los teléfonos | — | — | — |
| 4 | MATU_PROYECTO#87 | MATU-93 · ningún texto bajo 17 px | — | — | — |
| 5 | MATU_PROYECTO#88 y #91 | MATU-55 · Dónde entraste, ingresos y avisos (el #91 agrega `web/public` a la imagen de Railway) | 0025 | 0.14 | MATU#81 |
| 6 | MATU_PROYECTO#89 | MATU-42 y MATU-53 · invitar a un familiar y ver el grupo | 0026 | 0.15 | MATU#82 |
| 7 | MATU_PROYECTO#90 | MATU-46 · el teléfono del relevo se borra a los 30 días | 0027 | 0.16 | MATU#83 |
| 8 | MATU_PROYECTO#92 | MATU-54 · Mis datos | 0028 | 0.17 | MATU#87 |

Los hallazgos P2 y P3 de esas revisiones están en MATU-107, que se trabaja desde el 12 de noviembre. Ninguno se acepta.

### Migraciones y políticas

- **Migraciones:** `main` y la demostración están en la 0028. **La 0029 queda reservada para MATU-63**, por los permisos del comercio.
- **Política de privacidad:** `main` está en la 0.17 (`docs/legal/`), y staging y la demostración publican `POLITICA_VERSION=0.17`. Cada historia que cambie la política sube una versión al fusionarse.

## 4. Tabla de prioridad

El orden es el orden de ejecución.

| P | Tarjeta | Día | Vence | Responsable | Depende de |
|---|---|---|---|---|---|
| 1 | Ceremonia · Revisión y retrospectiva del sprint 4, y planificación del sprint 5 | vie 13 | 13 de noviembre | Jorge y Martín | — |
| 2 | MATU-63 · Vista de comercio con código de retiro | vie 13 | 13 de noviembre | Jorge | MATU-61, 62 |
| 3 | MATU-64 · Entorno de demostración (arrastre) | vie 13 y sáb 14 | 14 de noviembre | Martín | MATU-63 para el recorrido 6 |
| 4 | MATU-92 · Mis pedidos | sáb 14 | 14 de noviembre | Jorge | MATU-63 |
| 5 | MATU-76 · Avisos del pedido | sáb 14 | 14 de noviembre | Jorge | MATU-63, 74 |
| 6 | MATU-95 · Ficha: «A quién llamar» y alergias | dom 15 | 15 de noviembre | Jorge | — |
| 7 | MATU-81 · Backoffice mínimo | dom 15 | 15 de noviembre | Jorge | MATU-61, 62, 63 |
| 8 | MATU-65 · Usabilidad ronda 2 (arrastre) | hasta dom 15 | 15 de noviembre | Martín | la app en staging |
| 9 | MATU-78 · Evidencia de la Fase 3 | lun 16 | 16 de noviembre | Martín (lidera la redacción) y Jorge | MATU-65 |
| 10 | MATU-77 · Guion de demostración | lun 16 | 16 de noviembre | Jorge y Martín | MATU-64 |
| 11 | MATU-80 · E2E, carga y despliegue final | mar 17 | 17 de noviembre | Jorge y Martín | MATU-63, 64, 92 |
| 12 | MATU-79 · Endurecimiento, retención y CI | mar 17 y mié 18 | 18 de noviembre | Jorge | MATU-74 |
| 13 | MATU-96 · Prueba de carrera | mié 18 | 18 de noviembre | Jorge | — |
| 14 | MATU-103 · Velo de los diálogos | mié 18 | 18 de noviembre | Jorge | — |
| 15 | MATU-100 · Coherencia de documentos | mié 18 | 18 de noviembre | Martín | — |
| 16 | MATU-104 · Presentación final | jue 19, y se pule en la reserva | 19 de noviembre | Jorge y Martín | MATU-77, 78 |
| 17 | Ceremonia · Revisión final y retrospectiva del semestre | jue 19 | 19 de noviembre | Jorge y Martín | — |

**Agregada el 12 de noviembre:** MATU-106 · Exportar la presentación y el canje del relevo al contrato oficial (Jorge, 1 h, sin migración). Es un hallazgo de la QA final de MATU-54: esas dos rutas son las únicas que no están en `openapi.json` y no tienen prueba de contrato. Va el miércoles 18 junto con MATU-96, sin cambiar la numeración.

**Cambios de responsable del 12 de noviembre (decisión de Jorge):**
- **MATU-100 pasa a Martín (Eje B).** Martín verifica y corrige los documentos con su agente `revisor-documental` y abre el PR. Jorge confirma contra las migraciones 0005 y 0025 quién lee la auditoría, y revisa y fusiona.
- **MATU-78: Martín lidera la redacción.** Martín se encarga de la guía de la Fase 3, la estructura, la usabilidad y las entrevistas, la integración y la edición final, y abre el PR. Jorge escribe lo técnico, el estado de los 7 objetivos y el factor de vibecoding con sus cifras, y revisa y fusiona. Estimación: unas 8 h (Martín 5 h, Jorge 3 h).

**R3, «Arrepentirme de la compra» (ADR-027):** MATU-63 hace la regla y la devolución en el backend, y MATU-92 pone el botón y la pantalla de la familia.

**Las que necesitan revisión previa del analista normativo** (tocan dinero o datos personales): MATU-63, MATU-92, MATU-76 y MATU-81. Va antes de implementar, sin excepción.

**Las que tienen pantallas** pasan por la especificación y la revisión visual del diseñador: MATU-63, MATU-92, MATU-95, MATU-81 y MATU-103.

## 5. Peso de las historias

| Peso | Tarjeta | Por qué pesa | Riesgo |
|---|---|---|---|
| L | MATU-63 · Vista de comercio | App nueva con su sesión y rol, migración 0029, stock, preparar, código de retiro, regla de R3 y devolución. Analista, especificación y revisión visual | Es la primera de la cadena: desbloquea 64, 92, 76, 81 y 80 |
| L | MATU-80 · E2E, carga y despliegue | Cinco recorridos E2E nuevos que cruzan todos los módulos, k6 y despliegue desde `main` | Depende de la cola de fusión y de la demo |
| L | MATU-79 · Endurecimiento y CI | Retención, 404 en seis rutas y prueba global, contrato del relevo, cinco puertas nuevas del CI, trazabilidad y `/v1/salud` | Las puertas pueden destapar fallas viejas (`ruff format` marca hoy 143 archivos). Conviene partirla en PR chicos |
| M+ | MATU-81 · Backoffice | Interfaz nueva de operación: línea de tiempo, incidencias (RF-40) y conciliación. Puede llevar migración | Que no vea nada de la persona cuidada |
| M | MATU-92 · Mis pedidos | Lista, detalle, código de retiro y botón de R3. El backend es sobre todo lectura | Que el código solo lo vea quien corresponde |
| M | MATU-76 · Avisos del pedido | Consumidores en `notifications`, tipos nuevos en un `CHECK` y preferencias | Bajo: copia el patrón de MATU-41 |
| M (humano) | MATU-78 · Informe Fase 3 | Documento grande con cifras de todo el semestre | La guía del curso |
| M (humano) | MATU-64 · Demo y MATU-65 · Usabilidad | Operación y sesiones con personas | Horarios ajenos |
| S–M | MATU-104 · Presentación y MATU-77 · Guion | Redacción y ensayo | La fecha |
| S | MATU-95, 96, 103, 100 y las ceremonias | Ajustes acotados | MATU-96 si la carrera no se puede fijar |

Los pesos son relativos a las historias del sprint 4, donde MATU-54 y MATU-42/53 serían L. No son horas. El factor de vibecoding medido (MATU-61: estimadas 10 h, reales poco más de 3) es la razón de que no haya plan de sacrificio.

## 6. Secuencia por día

| Día | Jorge, con los agentes | Martín |
|---|---|---|
| Viernes 13 | Ceremonia (P1) · MATU-63: revisión previa del analista, especificación del diseñador, migración 0029, backend y vista del comercio | Ceremonia (P1) · MATU-64: el recorrido 6 apenas MATU-63 esté en staging |
| Sábado 14 | MATU-92 (Mis pedidos) · MATU-76 (avisos del pedido) | Cierra MATU-64 con los seis recorridos · revisa el PR de MATU-63 |
| Domingo 15 | MATU-95 (la ficha) · MATU-81 (backoffice) | Termina MATU-65 (usabilidad ronda 2) y su informe · revisa MATU-92 y MATU-76 |
| Lunes 16 | MATU-78: lo técnico, el estado de los siete objetivos y el factor de vibecoding con cifras, y revisa y fusiona el PR · MATU-77: revisa el guion | MATU-78: lidera la redacción (guía de la Fase 3, estructura, usabilidad y entrevistas, integración, edición final y PR) · MATU-77: escribe y ensaya el guion. **El informe y el guion quedan listos hoy** |
| Martes 17 | MATU-80: las cinco pruebas de extremo a extremo nuevas, que se suman a la que ya existe, y la carga con k6 · inicio de MATU-79 | MATU-80: corre las pruebas sobre la demo y hace el despliegue final desde `main` · revisa MATU-95 y MATU-81 |
| Miércoles 18 | MATU-79 (retención, pruebas y puertas del CI) · MATU-96 · MATU-103 · MATU-100: confirma contra las migraciones 0005 y 0025 quién lee la auditoría, y revisa y fusiona el PR de Martín | MATU-100: verifica y corrige los documentos con su agente `revisor-documental` y abre el PR · revisa MATU-79, MATU-96 y MATU-103 · restablece la demo desde cero |
| Jueves 19 | MATU-104: láminas y guion · ceremonia de cierre (P17) | MATU-104: la demo y su guion, ensayo con cronómetro · ceremonia de cierre (P17) |

**La cola del sprint 4 se fusiona el viernes 13 y el sábado 14**, antes del despliegue final. Martín la fusiona en el orden de la sección 3, con merge commit. Si pide cambios en un PR de abajo, el orquestador de Jorge los corrige y los propaga a los de arriba.

**Las historias de este sprint que tocan dinero o datos sensibles las revisa Martín siempre**, con su informe en `TESTER/` (definición de terminado, punto 5).

## 7. Fila de migraciones y políticas

Toda historia con migración parte de la punta de la última rama abierta que también tenga una y toma el número siguiente. Las que no tienen migración salen de `main` y se fusionan en cualquier orden.

| Migración | Tarjeta | Política | Estado al 12 de noviembre |
|---|---|---|---|
| 0024 | MATU-62 · pago con Webpay Plus | 0.13 | En `main` (PR #86) |
| 0025 | MATU-55 · Dónde entraste | 0.14 | En `main` (PR #88) |
| 0026 | MATU-42 y MATU-53 · invitar y ver el grupo | 0.15 | En `main` (PR #89) |
| 0027 | MATU-46 · teléfono del relevo | 0.16 | En `main` (PR #90) |
| 0028 | MATU-54 · Mis datos | 0.17 | En `main` (PR #92) |
| 0029 | MATU-63 · vista de comercio | La siguiente, si su revisión previa la pide | Reservada |
| Las que sigan | MATU-76 (tipos de aviso en un `CHECK`) y MATU-79 (retención), si la llevan | Una por fusión | Se fija en el plan de cada una |

**Sin migración:** MATU-94, MATU-86, MATU-93, MATU-92 (si su plan no la pide), MATU-95, MATU-96, MATU-103 y MATU-100.

## 8. Definición de terminado

Una historia está terminada cuando, y solo cuando:

1. Tiene pruebas de dominio de sus reglas nuevas
2. Tiene al menos una prueba de integración del camino feliz y una del principal camino de error
3. El pipeline pasa completo, incluidas las pruebas de arquitectura y de aislamiento
4. Si toca una pantalla, cumple el checklist de accesibilidad (estrategia de pruebas, sección 7) y la aprueba el diseñador
5. Si toca dinero o datos sensibles, la revisa la otra persona. Sin excepción. **Martín la revisa y deja su informe en `TESTER/`**, y recién entonces fusiona
6. Si corrige un defecto, deja una prueba que falla sin la corrección

**Con vibecoding no hay excepciones:** el código generado por los agentes cumple los mismos seis puntos que el escrito a mano.

## 9. Guion de la revisión del sprint

La revisión del jueves 19 muestra el objetivo con **los seis recorridos críticos de MATU-64**, en vivo contra el entorno de demostración restablecido desde cero (`docs/entorno-demo.md`) y con las cuentas sintéticas de la semilla:

1. **Crear la cuenta, la persona cuidada y su autorización, y llenar la ficha.**
2. **Compartir la ficha con un relevo con PIN**, abrirla en otro teléfono y cortar el acceso.
3. **Anotar los insumos y ver el aviso de quiebre.**
4. **Exportar, imprimir o compartir la lista de reposición**, y anotar lo que se compró.
5. **Armar el pedido desde la lista y pagar el total exacto** en el ambiente de integración de Transbank, con sus tarjetas de prueba publicadas.
6. **Retirar con código en el comercio simulado**, y ver el pedido entregado en «Mis pedidos».

Se dice en voz alta qué es simulado: el comercio, el envío de avisos y el pago en integración.

Y en pantalla, el pipeline completo en verde con `test_aislamiento.py`, `test_arquitectura.py` y las seis pruebas de extremo a extremo de MATU-80 (la que ya existe y las cinco nuevas).

**Además, en la retrospectiva** se calcula el factor de vibecoding del sprint y del semestre (horas estimadas de lo terminado divididas por horas reales), y se revisa el trabajo con agentes y los roles del ADR-030.

## 10. Riesgos del sprint

| Riesgo | Probabilidad | Qué se hace |
|---|---|---|
| **La cola de revisión de Martín.** Siete PR del sprint 4, más los del sprint 5, con revisión obligatoria en los que tocan dinero o datos sensibles | **Alta** | La cola del sprint 4 se fusiona el viernes 13 y el sábado 14, en el orden de la fila. Los PR sin migración no esperan a nadie. Si el sábado en la noche queda algo sin fusionar, se avisa en Discord y se decide si el despliegue final del martes 17 sale sin eso |
| **La fecha de la presentación.** La de la semana 15 puede caer antes del jueves 19 | **Alta** | El informe y el guion quedan listos el lunes 16. La fecha exacta se confirma con el profesor (MATU-104). El plan B es el video y las capturas de MATU-78 |
| **Pruebas intermitentes.** La de carrera de MATU-96 (404 en vez de 403 según quién gane) y la de `envasesMeQuedan` cuando la máquina está cargada | Media | MATU-96 fija el orden con una sincronización explícita y la corre 50 veces seguidas. Si la de `envasesMeQuedan` vuelve a fallar en el CI, se abre una tarjeta propia con el mismo criterio. Una prueba inestable nunca se marca como omitida para que el pipeline pase |
| **Docker.** Las pruebas y las migraciones locales dependen de Docker Desktop, y la imagen de la demo todavía no trae la semilla del catálogo (hallazgo H1 de MATU-64) | Media | Se revisa que Docker esté arriba antes de cada auditoría del QA. El `Dockerfile` se corrige dentro de MATU-64 o MATU-80, antes del despliegue final |
| **Las dependencias de MATU-63.** MATU-92, MATU-76, MATU-81, MATU-80 y el recorrido 6 de MATU-64 esperan su vista y sus estados | Media | MATU-63 es la primera prioridad del viernes 13. Si se atrasa, en la demo el retiro se opera a mano (orden de sacrificio, punto 2) y MATU-95, que no depende de nada, se adelanta |

## 11. Qué queda para después del semestre

Lo que sigue no se construye en el sprint 5. Está en la columna Product Backlog de Trello y se presenta en MATU-104 como lo que viene.

**Fase 2 del producto:**
- El pago dividido entre varios familiares y el prorrateo (hipótesis H5 y H6)
- La reposición programada, la app de repartidor y la liquidación automática

**Antes de datos reales:**
- MATU-89, MATU-99, MATU-101 y MATU-102
- MATU-98
- Las consultas legales abiertas, en su tarjeta de Trello
- Lo de la épica «Paso a producción» que MATU-79 deja fuera: MFA, HSTS y monitoreo con alertas (quitar `auditoria.ip` ya lo hizo la 0025 de MATU-55)

Mientras eso no esté cerrado, MATU trata **solo datos sintéticos**.

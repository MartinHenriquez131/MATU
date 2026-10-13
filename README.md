# MATU · Sistema de continuidad del cuidado

Proyecto de Capstone · Ingeniería en Informática · DUOC UC · segundo semestre 2026

> **Estado: anteproyecto validado, en desarrollo.** Este repositorio reúne las
> evidencias de cada fase del curso y los documentos que las respaldan: el
> diseño del sistema —arquitectura v1.1, modelo de datos, decisiones técnicas y
> prototipo de interfaz—, el protocolo de validación y **sus resultados**: las
> diez entrevistas con cuidadoras que fijó el protocolo como meta, con veredicto
> por hipótesis contra criterios escritos antes de entrevistar.
>
> **El código vive en un repositorio aparte:
> [MATU_PROYECTO](https://github.com/MartinHenriquez131/MATU_PROYECTO).**

## Descripción

MATU es un **sistema de continuidad del cuidado** para personas mayores con
demencia y, por extensión, con cualquier grado de dependencia.

Su núcleo es el **plan de cuidado**: convierte lo que sabe quien cuida —la
rutina del día, los horarios, qué hacer cuando la persona se agita a las tres de
la mañana, qué la calma, qué la altera, qué come— en algo escrito, ordenado y
**transferible**. Hoy ese conocimiento vive en la cabeza de una sola persona, y
esa es exactamente la razón por la que esa persona no puede ausentarse:
explicárselo a un relevo cuesta horas que no tiene. Con el plan, el relevo entra
por un enlace acotado y con vencimiento, y el cuidador puede salir.

**La validación con cuidadoras cambió la forma de esa capa.** La versión mínima
obligatoria ya no son ocho secciones sino una **ficha de relevo de tres campos**
—la rutina en una línea, qué hacer si la persona se altera, a quién llamar—, y
las ocho secciones quedan como ampliación opcional. La razón está en la
sección 3 de este README y en el ADR-023.

De ese mismo plan se desprende lo segundo: **cuánto se consume de cada insumo**.
Con dos datos por producto —cuánto se usa al día y cuánto queda— el sistema
anticipa la fecha en que cada cosa se acaba y arma la lista de reposición antes
del quiebre. Y sobre esa lista opera, de forma opcional, la compra y el
despacho, con el gasto repartido entre los familiares que comparten el cuidado.

**El orden importa, y es lo que define al producto.** La predicción de consumo
existe *porque* existe el plan: nadie que no conozca a la persona cuidada puede
saber que usa cuatro pañales al día. Por eso el activo del sistema es el plan de
cuidado, la predicción es lo que lo vuelve accionable, y el despacho es un
servicio derivado —desacoplado, y reemplazable por "exporta tu lista y compra
donde quieras".

**MATU no es una aplicación de delivery.** Un delivery genérico puede traer
pañales. No puede saber cuándo se acaban ni permitirle a un hijo tomar el turno
del sábado.

## Problema que resuelve

Quien cuida a una persona mayor dependiente enfrenta dos problemas que parecen
distintos y no lo son.

**El primero es de continuidad.** El conocimiento de cómo se cuida a alguien
—la rutina, las señales, lo que funciona y lo que no— no está escrito en ninguna
parte. Vive en una sola cabeza. Traspasarlo a un hermano, a una cuidadora nueva
o a quien cubra un fin de semana cuesta horas de explicación, así que en la
práctica no se traspasa, y el cuidador principal queda sin poder ausentarse. Es
la raíz del agotamiento del cuidador.

**El segundo es de abastecimiento.** Los insumos de cuidado se consumen de forma
recurrente y su demanda cambia con el estado de la persona. El cálculo se lleva
de memoria y se compra cuando alguien nota que se está acabando, en artículos
que no admiten quedarse sin stock. La salida de urgencia recae siempre en el
mismo familiar, y el gasto se reparte de manera informal entre hermanos, lo que
genera fricción y silencios.

Son el mismo problema visto dos veces: **el cuidado depende de una sola persona
que no puede delegar ni ausentarse.** MATU ataca esa dependencia haciendo
transferible el conocimiento y previsible el abastecimiento.

## Validación con cuidadoras

Documento completo: [docs/resultados-entrevistas.md](docs/resultados-entrevistas.md)

Diez entrevistas realizadas entre agosto y septiembre de 2026, cinco por
integrante, sin grabación, con consentimiento verbal anotado y con los criterios
de validación y refutación de cada hipótesis
[fijados por escrito antes de la primera](docs/protocolo-entrevistas.md).

| Hipótesis | Resultado |
|---|---|
| H1 · cinco minutos para el plan mínimo | **Refutada** — 3 de 10 bajo el umbral, el criterio exigía 7. Activa el ADR-023 |
| H2 · el relevo es real y frecuente | **Validada** — 7 con relevo, 9 dejaron de salir, 6 de 9 relevos fallaron por conocimiento tácito |
| H3 · el quiebre ocurre y cuesta | **Validada en el límite** — 6 de 10, el criterio exigía 6 |
| H4 · disposición a pagar $5.990 | **Validada** — 6 de 10 ya pagan por algo del cuidado |
| H5 · el gasto se reparte con fricción | **Zona intermedia** — 4 de 10 reparten, el criterio pedía 5 para validar y 3 para refutar |
| H6 · quien paga no es quien cuida | **Zona intermedia, tendencia en contra** — 8 de 10 dicen que pagaría la cuidadora |
| H7 · canal concentrado de captación | **Zona intermedia** — 4 de 10 en padrón público, 0 reclutadas por canal |

**Las tres mediciones**, con mediana y rango, reemplazan a los supuestos del
equipo en la sección 16 de la arquitectura: canasta mensual de insumos con
mediana de $70.000 y rango de $0 a $300.000, una compra al mes, y seis de diez
familias pagando hoy por algún servicio de cuidado. Con esos valores el punto de
equilibrio del piloto se recalculó en **84 familias** para el modelo con
suscripción, contra 429 para el modelo de solo despacho.

**La meta de diez entrevistas se cumplió íntegra.** Las cuatro entrevistas
adicionales que quedan pendientes no vienen de un déficit de muestra: vienen de
la **regla de zona intermedia** que el propio protocolo fija, según la cual un
resultado entre el umbral de validación y el de refutación obliga a ampliar la
muestra antes de decidir, no a interpretarlo a favor. Se realizan en la semana
9, con reclutamiento solo por canal concentrado.

**Qué cambió el producto por esta validación.** La versión mínima del plan de
cuidado pasó de ocho secciones a una ficha de tres campos (ADR-023), se agregó
el llenado asistido por un tercero, y el reparto del gasto entre varios
pagadores salió del alcance comprometido del semestre.

## Arquitectura de la solución

Documento completo: [docs/arquitectura.md](docs/arquitectura.md) — versión 1.1,
42 requisitos trazados a módulos, 13 diagramas y 24 decisiones de arquitectura
vigentes (ADR, numerados hasta el 25 porque la numeración no se reutiliza) con
alternativas descartadas y consecuencias. GitHub lo renderiza con los diagramas incluidos. Existe también
en [versión navegable](docs/arquitectura.html), con índice lateral, para leer
fuera de GitHub o imprimir.

El sistema se diseñó en **tres capas con dependencia estrictamente
descendente**:

* **Capa 1 · Plan de cuidado — es el producto.** Persona cuidada, círculo
  familiar, ficha de relevo de tres campos como versión mínima, secciones
  opcionales, consentimientos y acceso de relevo con auditoría y revocación. Es
  el núcleo del dominio, el activo diferenciador y el único lugar donde vive el
  dato sensible, cifrado con una clave propia por persona.
  **Sin esta capa, MATU es un despacho más.**
* **Capa 2 · Consumo y predicción — es el diferenciador computable.** Del perfil
  de consumo declarado en la capa 1 deriva cuándo se acaba cada insumo y produce
  la lista de reposición. Es un cálculo que un delivery genérico no puede hacer,
  porque exige conocer a la persona cuidada.
* **Capa 3 · Despacho — es un servicio, no la razón de existir.** Catálogo,
  pedido, pago con un solo pagador, retiro con código y liquidación. Desacoplada
  por diseño (ADR-002): sin convenio comercial, la familia exporta su lista y
  compra donde quiera, y el sistema sigue entregando su valor central. El
  reparto del gasto entre varios pagadores queda diseñado y fuera del MVP.

Las dependencias apuntan siempre hacia abajo y nunca hacia arriba: `care_plan`
no sabe que existe `fulfillment`. Eso es lo que permite construir y demostrar el
producto sin haber cerrado un solo convenio.

Módulos previstos: `iam`, `care_circle`, `care_plan` en la capa 1, `consumption` y
`replenishment` en la capa 2, y `catalog`, `ordering`, `payments`, `fulfillment`,
`settlement`, `rx`, `notifications` y `backoffice` en la capa 3. Cada uno con
estructura `domain / application / infrastructure / api`.

Definiciones de diseño relevantes:

* **Aislamiento multi-tenant** con Row Level Security forzado en PostgreSQL,
  sobre tres ejes de acceso: familia (`grupo_id`), comercio (`comercio_id`) y
  operación (`app.rol`).
* **Datos sensibles cifrados** con AES-256-GCM y una clave por persona cuidada,
  lo que permite borrado criptográfico. Alineado con la Ley 21.719.
* **Dinero en aritmética entera**, sin punto flotante, con prorrateo por resto
  mayor para el pago dividido.
* **Pago con autorización diferida y captura por el monto real**
  (Webpay Plus diferido), con un solo pagador en el MVP. El reparto entre varios
  familiares queda diseñado, con su regla de prorrateo y su prueba escritas, y
  fuera del alcance comprometido. Ver ADR-007.

## Estructura del repositorio

```
MATU/
├── README.md
├── Fase 1/                        evidencias del curso · fase 1
│   ├── Evidencias Grupales/
│   └── Evidencias Individuales/
├── Fase 2/                        evidencias del curso · fase 2
│   ├── Evidencias Grupales/
│   ├── Evidencias Individuales/
│   └── Evidencias Proyecto/
├── Fase 3/                        evidencias del curso · fase final
│   ├── Evidencias Grupales/
│   └── Evidencias Individuales/
└── docs/                          documentos que respaldan las evidencias
    ├── arquitectura.md            documento de arquitectura · se lee en GitHub
    ├── arquitectura.html          la misma versión, navegable y para imprimir
    ├── modelo-datos.md            modelo de datos completo, con diagramas
    ├── estrategia-pruebas.md      niveles, metas, puertas del pipeline y definición de terminado
    ├── backlog-sprints-1-3.md     historias, criterios y estimación del tramo
    ├── protocolo-entrevistas.md   guion y criterios de falsación
    ├── resultados-entrevistas.md  veredicto por hipótesis y mediciones
    ├── ficha-proyecto.docx        ficha de una página, formato del curso
    ├── adr/
    │   └── ADR-023-cierre.md      se activa el modo ficha de relevo
    ├── diagramas/
    │   └── modelo-datos/          13 diagramas en .mmd, .svg y .png
    ├── entrevistas/               diez fichas anonimizadas
    ├── prototipo/
    │   ├── prototipo-v1.1.html    36 pantallas · 7 recorridos · documentado
    │   ├── prototipo-pruebas.html la misma interfaz, limpia, para pruebas
    │   └── gen_prototipo.py       genera las dos versiones
    └── sprints/
        └── sprint-1-planificacion.md
```

El código no está en este repositorio. Vive en
[MATU_PROYECTO](https://github.com/MartinHenriquez131/MATU_PROYECTO), con la estructura
comprometida en el anexo 19.1 del documento de arquitectura: `backend/`,
`mobile/`, `web/` e `infra/`. El modelo de datos ejecutable, con sus 31 pruebas
de aislamiento, está ahí en `backend/db/`.

## Tecnologías previstas

| Área | Tecnología |
|---|---|
| Backend | Python 3.12, FastAPI, Pydantic v2 |
| Base de datos | PostgreSQL 16 con Row Level Security |
| Acceso a datos | SQLAlchemy 2 (async), asyncpg, Alembic |
| Trabajos asíncronos | ARQ sobre Redis, patrón *transactional outbox* |
| Aplicación móvil | Flutter |
| Panel web y consola de operación | React + TypeScript |
| Pagos | Transbank — Webpay Plus diferido y OneClick |
| Infraestructura | Docker, Docker Compose |
| Integración continua | GitHub Actions |
| Control de versiones | Git, GitHub |
| Gestión de tareas | Trello |

Las decisiones detrás de cada elección, y las alternativas que se descartaron,
están en los ADR del documento de arquitectura.

## Instrucciones para ejecutar

Este repositorio no tiene nada que ejecutar. Los documentos `.md` se leen
directo en GitHub, y los `.html` y `.docx` se descargan y se abren en el
computador.

Las instrucciones para levantar el sistema están en el README de
[MATU_PROYECTO](https://github.com/MartinHenriquez131/MATU_PROYECTO).

## Integrantes del equipo

* **Jorge Espinoza** — Product Owner / Developer
* **Martín Henríquez** — Scrum Master / Developer

## Metodología de trabajo

Scrum adaptado a un equipo de dos personas, con **sprints de una semana**. La
definición, la arquitectura y la validación ocuparon las seis primeras semanas
del semestre. La construcción ocupa **nueve semanas**, un sprint 0 de
preparación en la semana 7 y ocho sprints de una semana entre las semanas 8 y
15. El sprint N corresponde a la semana N más 7.

Capacidad declarada de **15 horas semanales por persona**, es decir **270 horas**
en la ventana de construcción, contra un alcance comprometido de **213 horas**,
un 21% de holgura. El alcance se recortó dos veces y siempre antes de construir:
41 horas al cerrar el diseño y 160 al cerrar la Fase 1. La segunda tanda saca el
reparto multi-pagador y la reposición programada, y cada línea de ese recorte
tiene justificación de evidencia además de la de capacidad.

El plan de sprints está en la sección 15 del documento de arquitectura.

## Otros documentos

* [Ficha de proyecto](docs/ficha-proyecto.docx) — una página, en el formato que
  entregó el profesor.
* [Modelo de datos](docs/modelo-datos.md) — 49 tablas, aislamiento por fila,
  cifrado del plan de cuidado y 13 diagramas. Probado con 31 pruebas contra
  PostgreSQL real.
* [Estrategia de pruebas](docs/estrategia-pruebas.md) — niveles de prueba,
  metas por capa, puertas del pipeline y definición de terminado.
* [Backlog de los sprints 1 a 3](docs/backlog-sprints-1-3.md) — historias con
  criterios de aceptación, estimación y orden de sacrificio.
* [Prototipo de interfaz](docs/prototipo/prototipo-v1.1.html) — 36 pantallas y
  7 recorridos, más una [versión limpia](docs/prototipo/prototipo-pruebas.html)
  para pruebas con usuarios.
* [Protocolo de validación con cuidadores](docs/protocolo-entrevistas.md) —
  siete hipótesis con criterios de falsación fijados antes de entrevistar.
* [Resultados de la validación](docs/resultados-entrevistas.md) — veredicto por
  hipótesis, las tres mediciones y el recálculo del punto de equilibrio.
* [Cierre del ADR-023](docs/adr/ADR-023-cierre.md) — H1 refutada con 3 de 10:
  la capa 1 pasa a ser una ficha de relevo de tres campos.
* [Arquitectura en versión navegable](docs/arquitectura.html).

GitHub no renderiza archivos `.html` ni `.docx`: hay que descargarlos y abrirlos.
El documento de arquitectura en `.md` sí se lee directo en el navegador, con sus
diagramas.

---

Proyecto académico. Todo el diseño y la documentación son originales del equipo.

# MATU · Sistema de continuidad del cuidado

Proyecto de Capstone · Ingeniería en Informática · DUOC UC · segundo semestre 2026

> **Estado: anteproyecto.** Este repositorio contiene por ahora el diseño del
> sistema —arquitectura, modelo de datos, decisiones técnicas y prototipo de
> interfaz— y las evidencias del curso. **Todavía no hay código.** El desarrollo
> comienza en el sprint 1.

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
pañales; no puede saber cuándo se acaban ni permitirle a un hijo tomar el turno
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

## Arquitectura de la solución

Documento completo: [docs/arquitectura.md](docs/arquitectura.md) — 13 diagramas
y 24 decisiones de arquitectura vigentes (ADR, numerados hasta el 25 porque la
numeración no se reutiliza) con alternativas descartadas y
consecuencias. GitHub lo renderiza con los diagramas incluidos. Existe también
en [versión navegable](docs/arquitectura.html), con índice lateral, para leer
fuera de GitHub o imprimir.

El sistema se diseñó en **tres capas con dependencia estrictamente
descendente**:

* **Capa 1 · Plan de cuidado — es el producto.** Persona cuidada, círculo
  familiar, plan por secciones, consentimientos y acceso de relevo con auditoría
  y revocación. Es el núcleo del dominio, el activo diferenciador y el único
  lugar donde vive el dato sensible, cifrado con una clave propia por persona.
  **Sin esta capa, MATU es un despacho más.**
* **Capa 2 · Consumo y predicción — es el diferenciador computable.** Del perfil
  de consumo declarado en la capa 1 deriva cuándo se acaba cada insumo y produce
  la lista de reposición. Es un cálculo que un delivery genérico no puede hacer,
  porque exige conocer a la persona cuidada.
* **Capa 3 · Despacho — es un servicio, no la razón de existir.** Catálogo,
  pedido, pago dividido, reparto y liquidación. Desacoplada por diseño
  (ADR-002): sin convenio comercial, la familia exporta su lista y compra donde
  quiera, y el sistema sigue entregando su valor central.

Las dependencias apuntan siempre hacia abajo y nunca hacia arriba: `care_plan`
no sabe que existe `fulfillment`. Eso es lo que permite construir y demostrar el
producto sin haber cerrado un solo convenio.

Módulos previstos: `iam`, `care_circle`, `care_plan` (capa 1); `consumption` y
`replenishment` (capa 2); `catalog`, `ordering`, `payments`, `fulfillment`,
`settlement`, `rx`, `notifications` y `backoffice` (capa 3). Cada uno con
estructura `domain / application / infrastructure / api`.

Definiciones de diseño relevantes:

* **Aislamiento multi-tenant** con Row Level Security forzado en PostgreSQL,
  sobre tres ejes de acceso: familia (`grupo_id`), comercio (`comercio_id`) y
  operación (`app.rol`).
* **Datos sensibles cifrados** con AES-256-GCM y una clave por persona cuidada,
  lo que permite borrado criptográfico. Alineado con la Ley 21.719.
* **Dinero en aritmética entera**, sin punto flotante, con prorrateo por resto
  mayor para el pago dividido.
* **Pago dividido** mediante autorización diferida y captura posterior
  (Webpay Plus diferido), con pagador de respaldo.

## Estructura del repositorio

```
MATU/
├── docs/
│   ├── arquitectura.md      documento de arquitectura v1.0 · se lee en GitHub
│   ├── arquitectura.html    la misma versión, navegable y para imprimir
│   ├── prototipo.html       prototipo navegable · 32 pantallas · 7 recorridos
│   ├── protocolo-entrevistas.md  guion y criterios de falsación
│   └── ficha-proyecto.docx  ficha de una página, formato del curso
├── Fase 1/                  evidencias del curso
├── Fase 2/
└── Fase 3/
```

El código se incorporará en `backend/`, `mobile/`, `web/` e `infra/` a medida
que avancen los sprints, según la estructura comprometida en el anexo 19.1 del
documento de arquitectura.

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
| Gestión de tareas | GitHub Projects |

Las decisiones detrás de cada elección, y las alternativas que se descartaron,
están en los ADR del documento de arquitectura.

## Instrucciones para ejecutar

Aún no hay código ejecutable en el repositorio. Esta sección se completará al
cierre del **sprint 1**, cuando exista la primera rebanada vertical de la capa 1.

El entorno previsto será:

```
git clone https://github.com/MartinHenriquez131/MATU.git
cd MATU/backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
docker compose up -d db
uvicorn app.main:app --reload --port 8000
```

## Integrantes del equipo

* **Jorge Espinoza** — Product Owner / Developer
* **Martín Henríquez** — Scrum Master / Developer

## Metodología de trabajo

Scrum adaptado a un equipo de dos personas, con **sprints de una semana** a lo
largo de 12 sprints y una capacidad declarada de **15 horas semanales por
persona**. El alcance se recortó explícitamente para caber en esa capacidad: no
se comprometen funcionalidades por sobre las horas disponibles.

El plan de sprints, con la capacidad y el alcance comprometido, está en la
sección correspondiente del documento de arquitectura.

## Otros documentos

* [Ficha de proyecto](docs/ficha-proyecto.docx) — una página, en el formato que
  entregó el profesor.
* [Prototipo de interfaz](docs/prototipo.html) — 32 pantallas y 7 recorridos.
* [Protocolo de validación con cuidadores](docs/protocolo-entrevistas.md) —
  cinco hipótesis con criterios de falsación fijados antes de entrevistar.
* [Arquitectura en versión navegable](docs/arquitectura.html).

GitHub no renderiza archivos `.html` ni `.docx`: hay que descargarlos y abrirlos.
El documento de arquitectura en `.md` sí se lee directo en el navegador, con sus
diagramas.

---

Proyecto académico. Todo el diseño y la documentación son originales del equipo.

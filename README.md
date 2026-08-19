# MATU · Plataforma de continuidad del cuidado

Proyecto de Capstone · Ingeniería en Informática · DUOC UC · segundo semestre 2026

> **Estado: anteproyecto.** Este repositorio contiene por ahora el diseño del
> sistema —arquitectura, modelo de datos, decisiones técnicas y prototipo de
> interfaz— y las evidencias del curso. **Todavía no hay código.** El desarrollo
> comienza en el sprint 1.

## Descripción

MATU convierte el plan de cuidado de una persona mayor —con o sin demencia— en
una **predicción de consumo de insumos**, y cierra el ciclo gestionando la
reposición antes de que el insumo se acabe. Está pensada para familias que se
reparten el cuidado: contempla pago dividido entre varios familiares, bitácora
compartida y control de quién puede ver qué.

**No es una aplicación de delivery.** El despacho es la última capa y está
diseñada de forma desacoplada: el sistema debe poder funcionar sin ella.

## Problema que resuelve

Quien cuida a una persona mayor dependiente administra un flujo constante de
insumos —pañales, suplementos, apósitos, artículos de higiene— cuya demanda
depende del estado de la persona y cambia con el tiempo. Hoy ese cálculo se
lleva de memoria: se compra cuando alguien nota que se está acabando, y el
quiebre de stock se resuelve con una salida de urgencia que recae siempre en el
mismo familiar. A eso se suma que el gasto se reparte de forma informal entre
hermanos, lo que genera fricción y silencios.

MATU busca modelar el consumo a partir del plan de cuidado, anticipar la fecha
de quiebre de cada insumo, y coordinar la reposición y su pago entre quienes
comparten el cuidado.

## Arquitectura de la solución

Documento completo: [docs/arquitectura.md](docs/arquitectura.md) — 13 diagramas
y 25 decisiones de arquitectura (ADR) con alternativas descartadas y
consecuencias. GitHub lo renderiza con los diagramas incluidos. Existe también
en [versión navegable](docs/arquitectura.html), con índice lateral, para leer
fuera de GitHub o imprimir.

El sistema se diseñó en **tres capas con dependencia estrictamente
descendente**:

* **Capa 1 · Plan de cuidado.** Persona cuidada, círculo familiar, plan,
  consentimientos y bitácora. Es el núcleo del dominio y el único lugar donde
  vive el dato sensible, cifrado con una clave propia por persona.
* **Capa 2 · Consumo y predicción.** Transforma el plan en un perfil de consumo
  y proyecta la fecha de quiebre de cada insumo. Produce la lista de reposición.
  **Es el diferenciador del producto.**
* **Capa 3 · Despacho.** Catálogo, pedido, pago dividido, reparto y liquidación.
  Desacoplada por diseño (ADR-002), para que la falta de convenio comercial no
  bloquee el resto del sistema.

Módulos previstos: `iam`, `care_circle`, `care_plan`, `consumption`, `catalog`
(capas 1–2) y `replenishment`, `ordering`, `payments`, `fulfillment`,
`settlement` (capa 3), cada uno con estructura `domain / application /
infrastructure / api`.

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
│   ├── prototipo.html       prototipo navegable · 30 pantallas · 7 flujos
│   └── ficha-proyecto.docx  ficha de una página, formato del curso
├── Fase 1/                  evidencias del curso
├── Fase 2/
└── Fase 3/
```

El código se incorporará en `backend/` y `frontend/` a medida que avancen los
sprints.

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
* [Prototipo de interfaz](docs/prototipo.html) — 30 pantallas y 7 flujos.
* [Arquitectura en versión navegable](docs/arquitectura.html).

GitHub no renderiza archivos `.html` ni `.docx`: hay que descargarlos y abrirlos.
El documento de arquitectura en `.md` sí se lee directo en el navegador, con sus
diagramas.

---

Proyecto académico. Todo el diseño y la documentación son originales del equipo.

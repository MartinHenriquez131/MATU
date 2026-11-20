# MATU · Parte técnica para el informe de la Fase 3

**Tarjeta:** MATU-78 · Evidencia de la Fase 3 · **Escribe:** Jorge Espinoza (Product Owner y desarrollo, ADR-030) · **Integra:** Martín Henríquez · **Estado:** versión final con el estado al 19/11/2026, entregada a Martín para la integración

**Cómo se lee.** Cada afirmación lleva su fuente entre paréntesis: un documento del repositorio MATU, un PR del repositorio MATU_PROYECTO (`#NN`) o del repositorio MATU (`MATU #NN`), un informe de `TESTER/` o una tarjeta de Trello. Las horas están en hora de Chile. Lo que sigue abierto al 19/11/2026 se dice tal cual, con su fecha y su responsable. Este archivo no cambia nada de `Fase 1/` ni de `Fase 2/`.

MATU es una app de continuidad del cuidado. En el semestre se construye como aplicación web mobile first, que se instala desde el navegador del teléfono (ADR-026, `docs/adr/ADR-026-aplicacion-web.md`).

---

## 1. Resumen de la parte técnica

- Entre el 30/10/2026 y el 19/11/2026 se cerraron **15 historias en el sprint 3, 30 en el sprint 4 y 23 tarjetas en el sprint 5** (columna Terminado de Trello, por etiqueta y nombre de sprint, leída el 19/11/2026). Las 23 del sprint 5 son 22 historias y tareas más la ceremonia de inicio.
- En ese tramo se fusionaron **93 PR en MATU_PROYECTO**: 23 en el sprint 3, 44 en el sprint 4 y 26 en el sprint 5, el último el 18/11/2026 a las 22:49 (`gh pr list --state merged`, fecha de fusión en UTC).
- `main` llega a la migración **0031** (`backend/alembic/versions/0001` a `0031`), con **2371 funciones de prueba en 196 archivos** de `backend/tests/` y **103 archivos de prueba** en `web/pruebas/` (conteo estático con `git grep` y `git ls-tree` sobre `origin/main`, c5db15a, del 18/11/2026). El CI de `main` está en verde en la corrida 44439817400 sobre c5db15a, del 18/11/2026 a las 22:49.
- De los siete objetivos específicos, **seis están cumplidos**. Del 7, la parte de código quedó cumplida el 17/11/2026: los seis recorridos críticos corren como pruebas de punta a punta en cada push, con el CI en verde. Falta lo que hace Martín el 19/11/2026: el despliegue final desde `main` y los seis recorridos en el teléfono con la demo restablecida (MATU-80, sección 3).
- **De los 25 requisitos *Debe*, 24 están cumplidos.** El que queda pendiente es RF-31, la conciliación con el comercio (sección 3).
- **El factor de vibecoding medido en el semestre es 1,86** sobre el trabajo de Jorge con estimación y horas propias, contra el 1,8 que suponía el calendario y el umbral de 1,4 (sección 4).

---

## 2. Los sprints 3 a 5

El calendario v1.3 agrupó en cinco sprints de viernes a jueves el alcance que la arquitectura v1.1 repartía en ocho (`docs/sprints/calendario-sprints.md`, sección 3). Desde el 05/11/2026 rige el reparto por rol del ADR-030: Jorge desarrolla con los seis agentes, y Martín despliega, prueba en el teléfono, hace la usabilidad y las entrevistas, y revisa y fusiona cada PR con su informe en `TESTER/` (`docs/adr/ADR-030-roles-del-equipo.md`).

### 2.1 Sprint 3 · del 30/10/2026 al 05/11/2026 · App de familia, consumo y predicción

**Resultado:** 15 historias terminadas y desplegadas en staging (tarjeta «S3 · Ceremonia · Revisión del sprint 3», comentario del 05/11/2026).

| Bloque | Historias | Qué deja en la app |
|---|---|---|
| Base | MATU-32, 33, 38, 25 y 58 | Contrato de la API de la app de familia, `main` protegida en los dos repositorios, sesión con refresco rotativo y dispositivos, staging con HTTPS y límite por IP, y la app publicada en staging |
| App de familia | MATU-39, 57, 48 y 45 | Crear la cuenta, el grupo y la persona, recuperar el acceso con un código, compartir la ficha con un relevo y cortar el acceso, y ver quién abrió la ficha |
| Ficha ampliada | MATU-49 y 50 | Seis secciones complementarias, con revisión normativa, diseño y contrato (ADR-028) |
| Capa 2 | MATU-36, 37 y 41 | Perfil de consumo, fecha de quiebre con alertas, y avisos por push y correo con publicador del outbox (envío simulado) |
| Arquitectura | MATU-40 | Prueba de que la capa 3 se puede quitar: 21 pruebas en `test_capa3_desacoplable.py` (#44, `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md`, PASS sin hallazgos) |

- **Objetivo específico 4 cumplido el 05/11/2026:** MATU-37 en `main` con PASS en el teléfono (revisión del sprint 3 en Trello, y `docs/arquitectura.md`, tabla 15.4).
- **No alcanzó:** MATU-34 (usabilidad, ronda 1), que pasó al sprint 4 (misma fuente).
- Entraron además siete PR de calidad que no estaban planificados, #49 a #55: Vitest en la web, Redis en el CI y avisos accesibles, entre otros. Al cierre, `main` tenía 2082 pruebas de backend y 48 de la web (vault, `Planificación/Sprints/Sprint 3.md`, estado del 05/11 a las 23:10).
- El 04/11 se probó el reparto por rol y el 05/11 quedó como definitivo (ADR-030).

### 2.2 Sprint 4 · del 06/11/2026 al 12/11/2026 · Catálogo, lista, pedido y pago

**Objetivo del sprint:** la familia exporta e imprime su lista de reposición y arma con ella un pedido que se paga en el ambiente de integración de Transbank, en un entorno de demostración propio. Son los objetivos 5 y 6 (vault, `Planificación/Sprints/Sprint 4.md`, planificación del 05/11).

**Resultado:** 30 tarjetas terminadas, más MATU-71, que se absorbió en MATU-72 (columna Terminado de Trello).

| Bloque | Historias | Evidencia |
|---|---|---|
| Lista de reposición (objetivo 5) | MATU-60 y 51 | #57 y #60. `TESTER/2026-11-07-MATU-60-lista-insumos.md` y `TESTER/2026-11-07-MATU-51-compre-me-quedan.md`: PASS sin P1 |
| Pedido y pago (objetivo 6) | MATU-59, 61 y 62 | #67, #83 (migración 0023) y #86 (0024). `TESTER/2026-11-11-MATU-61-pedido.md` y `TESTER/2026-11-12-MATU-62-pago.md`: PASS en el código y en el teléfono, sin P1 |
| Derechos y datos personales | MATU-44, 72, 54, 55, 75, 46, 42 y 53 | Retirar la autorización, borrar los datos de la persona en el acto, «Mis datos», «Dónde entraste», la política visible en la app, el borrado del teléfono del relevo, e invitar a un familiar. `TESTER/2026-11-07-MATU-44-retirar-autorizacion.md`, `2026-11-09-MATU-72-borrar-al-tiro.md`, `2026-11-12-MATU-54-mis-datos.md`, `2026-11-12-MATU-55-donde-entraste.md`, `2026-11-09-MATU-75-politica-visible.md`, `2026-11-12-MATU-46-telefono-relevo.md` y `2026-11-12-MATU-42-53-invitar-grupo.md` |
| Seguridad de la base | MATU-47, 66 y 74 | Permisos por operación en RLS (0020) y tareas programadas con sus roles propios (0022). `TESTER/2026-11-09-MATU-47-66-permisos-rls.md` y `2026-11-09-MATU-74-programador-tareas.md` |
| Calidad del pipeline | MATU-70 y 73 | Una sola cabeza de Alembic y una prueba de conservación estable. `TESTER/2026-11-07-MATU-70-una-cabeza-alembic.md` y `2026-11-07-MATU-73-conservacion-estable.md` |
| Ajustes y correcciones | MATU-67, 68, 83, 84, 85, 86, 88, 93 y 94 | Aviso de versión nueva, textos de 17 px como mínimo y los hallazgos de Martín, todos corregidos. `TESTER/2026-11-10-MATU-67-aviso-version.md`, `2026-11-11-MATU-85-83-correcciones-y-relevo.md`, `2026-11-11-MATU-88-correcciones.md` y `2026-11-12-MATU-86-93-ficha-y-17px.md` |
| Arquitectura v1.2 | MATU-43 | `docs/arquitectura.md` v1.2, del 08/11/2026 |
| Validación (Martín) | MATU-34 y 35 | Usabilidad, ronda 1 (`docs/usabilidad/ronda-1-informe.md`) y cuatro entrevistas de ampliación (`docs/resultados-entrevistas.md`, sección 8) |

- **Prueba manual contra Transbank, 10/11/2026:** los cuatro casos de la estrategia 10.2 dieron PASS: crédito, débito, anulación parcial de $8.990 con los dos medios y retorno duplicado con un solo cobro (`TESTER/2026-11-10-MATU-62-transbank-venta-normal.md` y `docs/pruebas-concepto/transbank.md`).
- **Entorno de demostración, 09/11/2026:** proyecto aparte de staging en Railway, con secretos propios y una semilla sintética que se restablece en 2,0 s (`docs/entorno-demo.md` y `TESTER/2026-11-09-MATU-64-demo.md`).
- **Pasaron al sprint 5**, por decisión de Jorge: MATU-63 (vista de comercio), MATU-64 (le faltaban los recorridos 5 y 6) y MATU-65 (usabilidad, ronda 2) (vault, `Planificación/Sprints/Sprint 4.md`, 11/11).

### 2.3 Sprint 5 · del 13/11/2026 al 19/11/2026 · Cierre (estado al 19/11/2026)

**Objetivo del sprint:** la familia retira con código lo que pagó y ve sus pedidos, MATU queda desplegado con los seis recorridos críticos y el pipeline completo en verde, y se entrega la evidencia de la Fase 3 con el guion de demostración y la presentación final (`docs/sprints/sprint-5-planificacion.md`, sección 1).

**Terminadas al 19/11/2026:** 23 tarjetas (columna Terminado de Trello, leída el 19/11/2026).

| Bloque | Tarjetas | Qué deja | Evidencia |
|---|---|---|---|
| Capa 3 de punta a punta | MATU-63, 92, 81, 113 y 114 | El comercio prepara sin ver datos de la familia, y el pedido se retira con un código de un solo uso, guardado como HMAC y con bloqueo al quinto intento (0029). La familia ve «Tus pedidos», puede arrepentirse de la compra y cancelar después de pagar. El equipo opera la demo desde una consola con contraseña y segundo factor (0030). Quien «Se informa» no ve montos, y operación deja de leer cuentas y membresías (0031) | #98, #100, #101, #108 y #114. `TESTER/2026-11-16-sprint-5-cola.md`, `TESTER/2026-11-17-MATU-92-tus-pedidos.md` y `TESTER/2026-11-18-MATU-81-113-76-114-y-cola.md`: PASS sin P1 |
| Demo y validación (Martín) | MATU-64 y 65 | La demo con los seis recorridos fijados, y la usabilidad ronda 2: U1 y U2 pasan de 1 de 3 a 3 de 3, y el pedido se hace en menos de 6 minutos en 3 de 3 | `TESTER/2026-11-16-sprint-5-cola.md` y `docs/usabilidad/ronda-2-informe.md` |
| La ficha y la app | MATU-95, 103, 109, 110, 117 y 118 | «A quién llamar» a primera vista en el relevo, una pregunta cotidiana por sección, el velo de los diálogos, «Me quedan» con envases cerrados y unidades sueltas, el envase en ml o g, etiquetas de varios renglones y el foco que no se pierde al escribir | #103, #102, #97, #105, #110 y #109 |
| Correcciones de las revisiones de Martín | MATU-105, 106, 107 y 112 | Todos los hallazgos corregidos, el contrato oficial del relevo y la segunda cuenta de comercio de la demo (H7) | #96, #94, #93 y #99. `TESTER/2026-11-17-MATU-112-correcciones.md` |
| Pruebas estables | MATU-96, 108 y 119 | Las pruebas de concurrencia esperan el bloqueo en PostgreSQL, y las de la web no fallan con la máquina cargada | #95, #104, #107 y #111 |
| Documentos y alcance | MATU-82 y 123 | Las preguntas de la consulta legal en un solo archivo, y el recorte escrito de RF-32 a *Debería* | MATU #54, MATU #116 y #115 |
| Ceremonia | S5 · P1 | Revisión y retrospectiva del sprint 4, y planificación del sprint 5 | MATU #84 |

**En Revisión al 19/11/2026** (lista «En Revisión» de Trello):
- MATU-76, avisos del pedido a quien pagó: #112 fusionado el 18/11 y la tarjeta todavía no pasa a Terminado.
- MATU-115, textos de «Si falta» y retractos en la copia de los datos: #117 fusionado el 18/11.
- MATU-121, cuatro avisos con su prueba de anuncio al lector de pantalla: #116 fusionado el 18/11.
- MATU-116, quien pagó sigue viendo sus pagos: #119 abierto, con la migración 0032.
- MATU-122, operación lee solo lo que usa: #120 abierto, con la migración 0033.
- MATU-126, enlaces de correo de 48 px: #121 abierto.

**En curso al 19/11/2026** (lista «En Progreso» de Trello):
- MATU-80, pruebas de punta a punta, carga y despliegue final: #106 y #118 fusionados. Falta lo de Martín (sección 3.3).
- MATU-79, seguridad, retención y puertas del CI: partes 1 y 2 fusionadas (#113 y #115). La parte 3 está en curso, con la migración 0034, y cierra MATU-102 (comentario de Jorge en MATU-102, 18/11).
- MATU-127, un enlace partido en dos renglones conserva su área táctil.
- MATU-100 (coherencia de documentos), MATU-77 (guion de demostración), MATU-78 (este informe) y MATU-111 (ensayos), con trabajo de Martín.

**Por hacer en la lista «Sprint 5»:** MATU-104 (presentación final), la ceremonia de cierre del semestre (P17), MATU-124 (la conservación borra con su propio marcador) y MATU-128 (quien pagó ve «Lo que pasó con tu pedido»). Las dos últimas llevan migración y se crearon el 18/11.

**Requisitos *Debe*.** El recorte de MATU-123 dejó 25 requisitos *Debe* sobre un catálogo de 42 (`docs/arquitectura.md`, sección 3, «Cobertura»). Jorge decidió el 17/11 informar RF-31 como el requisito obligatorio que queda pendiente: con comercios ficticios no hay boletas reales que conciliar, y va al Product Backlog (comentario de Jorge en MATU-78, 17/11). MATU-81 muestra en solo lectura lo que MATU le debe a cada comercio. Por eso quedan **24 de 25** cumplidos. La puerta de trazabilidad del CI exige al menos una prueba marcada para cada requisito *Debe* y corre sin pendientes desde el 18/11 (`.github/workflows/ci.yml`, paso «Trazabilidad»).

---

## 3. Estado final de los siete objetivos específicos

La redacción original es la del documento de avance de la Fase 2 (`Fase 2/Evidencias Grupales/2.4_GuiaEstudiante_Fase 2_Desarrollo Proyecto APT(Español).docx`, sección de objetivos). La vigente de los objetivos 5, 6 y 7 está en `docs/arquitectura.md` v1.2, sección 15.4.

| # | Objetivo | Estado al 19/11/2026 | Evidencia |
|---|---|---|---|
| 1 | Validar las siete hipótesis con diez entrevistas y criterios de falsación fijados antes de entrevistar | **Cumplido** en la Fase 1 | Informe de avance de la Fase 2 |
| 2 | Modelo de datos multi-tenant con Row Level Security forzado, verificado contra una base real | **Cumplido** en el sprint 0, con 31 pruebas de aislamiento. Al 18/11, `test_aislamiento.py` tiene 270 funciones de prueba | `docs/arquitectura.md`, tabla 15.4. Conteo con `git grep` sobre c5db15a |
| 3 | Plan de cuidado con acceso de relevo temporal y revocable, auditoría de todo acceso y borrado criptográfico (Ley 21.719) | **Cumplido** el 29/10/2026, sprint 2 | `docs/arquitectura.md`, tabla 15.4 |
| 4 | Fecha de quiebre y alerta anticipada por insumo, con ocho pruebas de dominio | **Cumplido** el 05/11/2026, sprint 3 | Revisión del sprint 3 en Trello. ADR-030 |
| 5 | La lista de reposición, operativa sin convenio comercial | **Cumplido** el 07/11/2026, sprint 4 | #57. `TESTER/2026-11-07-MATU-60-lista-insumos.md` |
| 6 | El flujo de pedido con un solo cobro del total exacto, con los nueve casos de la sección 12.4 | **Cumplido** el 12/11/2026, sprint 4. MATU-63 completó el retiro y la devolución el 15/11, y MATU-92 «Tus pedidos» el 17/11 | #83, #86, #98 y #100. `backend/tests/modules/payments/test_casos_pago.py` |
| 7 | El sistema desplegado en un entorno de demostración, con los seis recorridos críticos y el pipeline en verde | **En cierre el 19/11/2026.** La parte de código está cumplida desde el 17/11. Falta el despliegue final y la prueba en el teléfono, que hace Martín el 19/11 | `docs/entorno-demo.md`. #106 y #118. Tarjeta MATU-80 en Trello |

### 3.1 Objetivo 5 · La lista sin enlace (ADR-031)

- **Redacción original:** «Entregar la lista de reposición exportable como documento y como enlace compartible, operativa sin convenio comercial, al 12 de noviembre (sprint 4).»
- **Redacción vigente:** «La lista de reposición, operativa sin convenio comercial. Se comparte como texto, sin enlace: se imprime o se guarda como PDF desde el navegador y se comparte desde el teléfono» (`docs/arquitectura.md`, 15.4).
- **Por qué cambió (ADR-031, 06/11/2026):** la lista muestra qué insumos usa la persona, y el diseño trata el consumo como un dato de salud. Un enlace lo puede abrir cualquiera que lo reciba, y obligaría a construir otro acceso con token, vencimiento y corte, como el del relevo. Un PDF hecho en el servidor obligaría a guardar archivos con datos de consumo. Por eso MATU no genera archivos ni crea un acceso público. La lista sale del teléfono como texto, con «Copiar la lista», la hoja de compartir del teléfono o la impresión del navegador (`docs/adr/ADR-031-lista-insumos-solo-texto.md`).
- **Cómo se cumple:** la lista no lleva el nombre de la persona ni nada de la ficha, y la cantidad sugerida va en envases cuando el insumo los tiene anotados (ADR-031, puntos 4 y 6). Funciona con la capa 3 apagada (MATU-40, #44).
- **Evidencia:** MATU-60, #57 fusionado el 07/11/2026. Informe de Martín: PASS, sin P1, con el único P2 corregido antes de fusionar. Recorrido 4 en PASS en el teléfono el 09/11 (`TESTER/2026-11-09-MATU-64-demo.md`), y como prueba de punta a punta desde el 17/11 (`backend/tests/e2e/test_recorrido_4_lista_y_compra.py`, #106).

### 3.2 Objetivo 6 · Un solo cobro del total exacto (ADR-027)

- **Redacción original:** «Construir el flujo de pedido con autorización diferida y captura por el monto real, con los siete casos obligatorios del flujo de pago en verde, al 12 de noviembre (sprint 4). Para tarjetas de débito se aplica el plan B del ADR-006.»
- **Redacción vigente:** «El flujo de pedido con un solo cobro del total exacto (ADR-027), con los nueve casos obligatorios de la sección 12.4 en verde. Sin captura diferida ni autorización con margen» (`docs/arquitectura.md`, 15.4).
- **Por qué cambió (ADR-027, 26/10/2026):** la prueba de concepto de Transbank mostró que la captura diferida solo opera con crédito, y el débito es el medio más usado por estas familias. El plan B del débito obligaba a cobrar un estimado y devolver diferencias. Explicar una retención mayor que el pedido es difícil para una familia cansada, y lo observó el análisis de la Ley 19.496 (`docs/adr/ADR-027-precios-exactos.md`, contexto). Con precios exactos de comercios en convenio, la familia ve el monto exacto antes de pagar, se cobra una sola vez en venta normal de Webpay Plus, crédito y débito funcionan igual, y la única devolución es la anulación parcial a la misma tarjeta (ADR-027, decisión).
- **De siete a nueve casos:** salen los de autorizar, capturar por menos y capturar más que lo autorizado. Entran la venta normal con los dos medios, la anulación parcial y el total vencido a los 15 minutos (`docs/arquitectura.md`, 12.4).
- **Evidencia:**
  - los nueve casos están en `backend/tests/modules/payments/test_casos_pago.py`, uno por bloque («Caso 1 y 2» a «Caso 9»), con los casos 3, 4 y 9 también contra PostgreSQL en `test_devoluciones_base.py`, y la `PasarelaFalsa` contrastada con Transbank en `test_pasarela_falsa.py`.
  - prueba manual contra el ambiente de integración de Transbank el 10/11/2026: PASS en los cuatro casos de la estrategia 10.2.
  - MATU-61 (#83) y MATU-62 (#86): PASS de Martín en el código y en el teléfono. Martín midió que la venta de Webpay vence a los 7 minutos, y la venta quedó en 8 (`TESTER/2026-11-12-MATU-62-pago.md`, hallazgo H1, corregido en MATU-94).
  - MATU-63 (#98): un producto que falta después de pagar se devuelve a la misma tarjeta, también si es parcial. Martín lo probó en dos teléfonos el 16/11 con un pedido de dos productos y uno marcado «No lo tengo» (comentario de Martín en MATU-63, 16/11).
  - MATU-92 (#100): «Arrepentirme de la compra» y cancelar después de pagar, con PASS en el teléfono el 17/11 (`TESTER/2026-11-17-MATU-92-tus-pedidos.md`).

### 3.3 Objetivo 7 · Los seis recorridos fijados en MATU-64

- **Redacción original:** «Desplegar el sistema en un entorno de demostración con los seis recorridos críticos operativos y el pipeline de integración continua en verde, al 19 de noviembre (sprint 5).»
- **Redacción vigente:** «El sistema desplegado en un entorno de demostración, con los seis recorridos críticos operativos y el pipeline en verde» (`docs/arquitectura.md`, 15.4).
- **Por qué cambió:** el objetivo nombraba seis recorridos críticos, pero ningún documento decía cuáles eran. Jorge los fijó el 08/11/2026 en MATU-64, y quedaron alineados con el ADR-027 (pago del total exacto) y el ADR-031 (lista como texto) (vault, `Planificación/Historias/MATU-64 Entorno de demostración.md`).

| # | Recorrido (MATU-64) | PASS en el teléfono | Prueba de punta a punta (#106, 17/11) |
|---|---|---|---|
| 1 | Crear la cuenta, la persona cuidada y su autorización, y llenar la ficha | 09/11/2026 (`TESTER/2026-11-09-MATU-64-demo.md`) | `test_recorrido_1_alta_y_ficha.py` |
| 2 | Compartir con un relevo con PIN, abrir la ficha en otro teléfono y cortar el acceso | 09/11/2026 (mismo informe) | `test_recorrido_2_relevo.py` |
| 3 | Anotar los insumos y ver el aviso de quiebre | 09/11/2026 (mismo informe) | `test_recorrido_3_insumos_y_aviso.py` |
| 4 | Exportar, imprimir o compartir la lista, y anotar lo que se compró | 09/11/2026 (mismo informe) | `test_recorrido_4_lista_y_compra.py` |
| 5 | Armar el pedido y pagar el total exacto en el ambiente de integración de Transbank | 12/11/2026 (`TESTER/2026-11-12-MATU-62-pago.md`, pruebas W1 a W6) | `test_recorrido_5_pedido_y_pago.py`, con la pasarela falsa |
| 6 | Retirar con código en el comercio simulado | 15/11/2026, y el 16/11 con un pedido de dos productos y uno que falta (`TESTER/2026-11-16-sprint-5-cola.md` y comentario de Martín en MATU-63) | `test_recorrido_6_retiro_con_codigo.py` |

**Lo que ya está cumplido:**
- **Los seis recorridos corren en cada push.** Están en `backend/tests/e2e/` y entran en el `pytest -q` del CI. Martín revisó el código con PASS el 17/11: QA PASS y analista CUMPLE, con datos sintéticos, la pasarela falsa y solo hosts locales (comentario de Martín en MATU-80, 17/11, y `TESTER/2026-11-17-MATU-103-95-108-110-80.md`).
- **El pipeline está en verde:** corrida 44439817400 sobre c5db15a, 18/11/2026 a las 22:49.
- **La demo opera** con la consola de operación y su segundo factor desde el 18/11 (`TESTER/2026-11-18-MATU-81-113-76-114-y-cola.md`). El hallazgo H7 de la semilla, la cuenta del segundo comercio, se cerró el 17/11 con MATU-112 (comentario de Martín en MATU-112, 17/11).

**Lo que sigue abierto el 19/11/2026** (checklist de MATU-80 en Trello):
- **Martín, 19/11:** el despliegue final desde `main` con el pipeline en verde, la demo restablecida desde cero y los seis recorridos en el teléfono, con su informe en `TESTER/`. Es el ítem que cierra el objetivo 7, y al 19/11 no está marcado.
- **Jorge:** el recorrido 6 de punta a punta todavía entra como operación sin el segundo factor. MATU-81 ya está en `main`, y la prueba lo deja anotado como `[PENDIENTE]` (`backend/tests/e2e/test_recorrido_6_retiro_con_codigo.py`, líneas 8 a 11).
- **La carga con k6** es parte de MATU-80 y del requisito RNF-05, no del texto del objetivo. La corrida de Martín del 17/11, en una copia local de la demo con la pasarela falsa, dio 50 usuarios durante 3 minutos, 485 compras completas, 100 % de `checks` y 0 % de fallas, pero un percentil 95 de 6,62 s contra la meta de 800 ms (MATU #112 y comentario de Martín en MATU-80, 17/11). El #118 agregó umbrales por paso el 18/11. Falta la segunda corrida de Martín y la decisión entre optimizar el paso lento o ajustar la meta, que Jorge delegó al orquestador el 19/11 (checklist de MATU-80).

---

## 4. Factor de vibecoding del semestre

### 4.1 Qué se mide

El factor es **las horas estimadas de lo terminado divididas por las horas reales usadas** (`docs/sprints/calendario-sprints.md`, sección 2). El calendario supuso 1,8, y fijó que bajo 1,4 se aplicaba el orden de sacrificio. Las estimaciones del backlog son horas reales sin asistencia de IA, y no se cambiaron (misma sección).

**Es la primera vez que se calcula completo.** La retrospectiva del sprint 1 no lo cerró porque faltaban horas (vault, `Planificación/Sprints/Sprint 1.md`), y la del sprint 3 lo dejó pendiente (tarjeta «S3 · Ceremonia · Retrospectiva del sprint 3», 05/11/2026).

### 4.2 Cómo se calculó

1. **Fuente de las horas reales:** los comentarios de horas de cada tarjeta de Trello, con marcas objetivas en hora de Chile (movimientos de la tarjeta, commits, PR y CI). Se leyeron los 500 comentarios del tablero el 16/11/2026, y el 19/11/2026 los de las tarjetas del sprint 5 que pasaron a Terminado desde entonces. No se agregó ninguna cifra que no esté en un comentario.
2. **Fuente de las estimaciones:** la descripción de la tarjeta, más los ajustes escritos en sus comentarios o en la planificación del sprint 4 del 08/11/2026 (por ejemplo, MATU-44 de 6 h a 11 h, y MATU-42 y MATU-55 con 1,5 h y 2,5 h más). En el sprint 3, la propuesta de Jorge del 28/10 (vault, `Planificación/Sprints/Sprint 3 · Propuesta de Jorge (28-10).md`). En el sprint 5, la descripción de la tarjeta y la planificación del sprint 5, sección 2.
3. **Horas de Jorge, sin contar dos veces:** varios comentarios anotan el mismo bloque en varias tarjetas. Cuando los intervalos se conocen, se suma la unión de los intervalos, no la suma de las tarjetas. Cuando un comentario dice «en paralelo» sin dar el intervalo (MATU-59 con MATU-64, y MATU-47/66, 67 y 75 el 09/11), se suman las dos cifras. Eso puede contar de más, así que en esos casos el factor es una cota inferior.
4. **Las horas de los agentes no son horas de Jorge.** Así lo anotan las tarjetas. En los mandatos autónomos del 11/11 al 13/11 y del 16/11 al 18/11, el orquestador y los agentes trabajaron mientras Jorge no estaba, y solo cuentan los minutos en que Jorge decidió.
5. **Tres grupos, para no mezclar cosas distintas:**
   - **A · Trabajo dirigido por Jorge:** tarjetas con estimación y horas propias. Es el factor principal.
   - **M · Mandato autónomo:** Jorge solo decidió y delegó. Se informa aparte, porque mide la autonomía de los agentes y no la velocidad de Jorge.
   - **C · Correcciones:** los bloques de corrección de los hallazgos de Martín, que casi no tienen estimación propia.
6. **Cada sprint se asigna por la etiqueta de la tarjeta en Trello** (S1 a S5). La semilla de MATU-64 va en el sprint 4, porque se hizo el 08/11 y su nota del vault es del sprint 4.
7. **Las tarjetas del 18/11 y el 19/11 que hicieron los agentes con 0 h de Jorge** van en el grupo M, como dice el punto 5: MATU-117, 118 y 119 con 0 h, y MATU-114 con 10 min de aprobaciones. Una tarjeta con 0 h no tiene factor propio, porque no se puede dividir por cero. Por eso sus estimaciones solo se suman al total del grupo M.
8. **Solo entra lo terminado.** Las tarjetas que al 19/11 siguen En Revisión o En Progreso no entran, aunque su PR esté fusionado (sección 4.7). La única excepción es la parte de Jorge de MATU-80: todos sus ítems del checklist están hechos y fusionados (#106 y #118), y lo que falta es de Martín. Por eso entra con la estimación de Jorge, 7 h de las 9 h de la tarjeta.

### 4.3 Factor de Jorge por sprint (grupo A)

| Sprint | Horas estimadas | Horas reales | Factor | Tarjetas que entran |
|---|---|---|---|---|
| 1 | 11,0 | 6,10 | **1,80** | MATU-03, 07, 26, 27 y 28 |
| 2 | 15,5 | 5,60 | **2,77** | MATU-11, 12 y 18 |
| 3 | 17,5 | 11,80 | **1,48** | MATU-37, 39 y 58 |
| 4 | 90,5 | 41,20 | **2,20** | Las 18 de la tabla 4.4 |
| 5 | 20,0 | 18,41 | **1,09** | MATU-82, 96, 105, 106, 107 y 109, más el bloque del 17/11 (tabla 4.5) |
| **Semestre** | **154,5** | **83,11** | **1,86** | 40 tarjetas |

**Lectura:**
- El factor del semestre, **1,86**, supera el 1,8 que suponía el calendario y queda sobre el umbral de 1,4.
- **El sprint 5 quedó bajo 1,4, en 1,09.** Tiene dos causas, y las dos están en los comentarios:
  - Sus tarjetas del grupo A son correcciones y tareas técnicas chicas, estimadas entre 0,5 h y 2 h, salvo la parte de Jorge de MATU-80.
  - El bloque del 17/11 (tabla 4.5) duró 11 h 2 min y también cubrió trabajo sin estimación: la segunda vuelta de MATU-81 por el P2 de Martín y MATU-103. Esas horas no se pueden separar, así que el factor del sprint 5 es una cota inferior.
- Los intervalos del 17/11 están escritos como «aproximadamente», y en ellos Jorge decidía por chat mientras los agentes construían (comentarios de horas de MATU-95, 103, 108 y 110). Si Jorge no estuvo activo todo el bloque, las horas reales son menos y el factor sube.
- El sprint 4 tiene casi seis de cada diez horas estimadas del semestre (90,5 de 154,5), así que es el dato más sólido.
- **El grupo A no incluye la revisión de Martín**, que es parte de la definición de terminado de cada historia (sección 4.6).

### 4.4 Detalle del sprint 4 (grupo A)

| Tarjetas | Estimadas | Reales de Jorge | Cómo se midió (comentario de la tarjeta) |
|---|---|---|---|
| MATU-60 y MATU-44 | 8 + 11 | 8 h 17 min | 06/11 de 00:15 a 02:22 (contiene el bloque de 00:47 a 01:20 de MATU-44), de 20:09 a 21:00 y de 21:22 a 02:18 del 07/11, y 08/11 de 12:06 a 12:29 |
| MATU-70 y MATU-51 | 0,5 + 4 | 4 h 25 min | 07/11 de 08:42 a 09:47 y de 10:06 a 13:26 |
| MATU-73 | 0,5 | 53 min | 07/11 de 13:33 a 14:26 |
| MATU-43, 68, 72, 71 y 74 | 6 + 4,5 + 8 + 2,5 + 3 | 3 h 16 min | 08/11 de 12:32 a 15:48, un solo bloque compartido por las cinco. De MATU-74 solo cuentan las 3 h de Jorge |
| MATU-59 | 5 | 3 h 18 min | 08/11, sin intervalo escrito |
| MATU-64, semilla | 4 | 1 h 44 min | 08/11 de 20:06 a 21:50, en paralelo con el cierre de MATU-59 |
| MATU-47 y MATU-66 | 2 + 4,5 | 3 h 56 min | 09/11, un bloque para las dos |
| MATU-67 | 3 | 2 h 25 min | 09/11, en paralelo con MATU-47/66 y MATU-75 |
| MATU-75 | 5 | 3 h 43 min | 09/11, en paralelo con MATU-67 y MATU-47/66 |
| MATU-61 | 11 | 3 h 55 min | 11/11 de 08:55 a 13:10, menos 20 min de espera |
| MATU-54 | 8 | 5 h 20 min | 12/11 de 09:21 a 14:41 |
| **Total** | **90,5** | **41 h 12 min** | **Factor 2,20** |

### 4.5 Detalle del sprint 5 y factor con todo el trabajo de Jorge (sprints 4 y 5)

**Grupo A del sprint 5:**

| Tarjetas | Estimadas | Reales de Jorge | Cómo se midió (comentario de la tarjeta) |
|---|---|---|---|
| MATU-82, 96, 105, 106, 107 y 109 | 1 + 1,5 + 1,5 + 1 + 2 + 1,5 | 7 h 23 min | Medido el 16/11 con los comentarios de cada tarjeta. MATU-109 va con 1,5 h, la estimación que usa su comentario de cierre del 14/11 (la descripción dice 1 h) |
| Bloque del 17/11: MATU-80 (parte de Jorge), 95, 108, 110 y 113 | 7 + 1,5 + 1,5 + 0,5 + 1 | 11 h 2 min | Unión de los bloques escritos en cada tarjeta, del 17/11 a las 13:13 al 18/11 a las 00:15: MATU-95, 103, 108 y 110 desde las 13:13, MATU-81 de 13:20 a 22:55, MATU-80 de 15:45 a 20:15, MATU-113 de 16:06 a 00:15 y el H1 de MATU-108 de 22:15 a 00:05. Los comentarios dicen que no se reparte entre tarjetas |
| **Total** | **20,0** | **18 h 25 min** | **Factor 1,09** |

**Todos los grupos:**

| Sprint | Grupo | Estimadas | Reales de Jorge | Detalle |
|---|---|---|---|---|
| 4 | A | 90,5 | 41,20 | Tabla 4.4 |
| 4 | M | 38,0 | 1,38 | MATU-62 (11 h, 15 min el 11/11), MATU-42 (6,5), 53 (5), 46 (3) y 55 (8,5), en el bloque del 12/11 de 00:21 a 01:25, MATU-93 (1,5, 2 min), MATU-86 (1,5, 2 min) y MATU-88 (1, 0 min) |
| 4 | C | 4,0 | 9,17 | 10/11 de 15:00 a 23:29, la unión del bloque de correcciones (15:00 a 21:41) y el de MATU-85, 83 y 84 (19:51 a 23:29), más el 11/11 de 00:32 a 01:03 y 10 min de MATU-94. Solo MATU-83 (1,5) y MATU-84 (2,5) tienen estimación |
| **4** | **Todo** | **132,5** | **51,75** | **Factor 2,56** |
| 5 | A | 20,0 | 18,41 | Tabla de arriba |
| 5 | M | 26,0 | 1,00 | MATU-63 (6 h, 30 min el 14/11, de 09:35 a 10:05), MATU-92 (6 h, 0 h), MATU-112 (2 h, 0 h), MATU-81 (8 h, 20 min de decisiones el 17/11 entre las 11:15 y las 11:35 y la aprobación de la 0.20), MATU-114 (1,5 h, 10 min el 18/11 entre las 10:15 y las 10:30), MATU-117 (0,5 h, 0 h), MATU-118 (0,5 h, 0 h) y MATU-119 (1,5 h, 0 h) |
| 5 | C | 0 | 1,00 | Revisión del informe de MATU-65, como máximo 1 h (13/11 de 12:04 a 13:03). La segunda vuelta de MATU-81 y el H1 de MATU-108 ya están dentro del bloque del 17/11 |
| **5** | **Todo** | **46,0** | **20,41** | **Factor 2,25** |

- **MATU-63 va con 6 h**, la estimación de su descripción y de la planificación del sprint 5, sección 2. El borrador del 16/11 la contaba con 7 h, mientras Jorge decidía entre 6 y 7 h. No hay un comentario que la cambie, así que vale la escrita.
- En los sprints 1 a 3 este cálculo no se hace, porque mucho trabajo de Jorge no tiene estimación: la demo del 30/10 (8,9 h), el ADR-027 (2 h 32 min) y siete historias del sprint 3 (sección 4.7).
- El grupo M da un factor muy alto: unas 27 veces en el sprint 4 y unas 26 en el sprint 5. No mide velocidad. Muestra que, con la definición de terminado y la revisión de Martín, los agentes pudieron construir historias completas mientras Jorge solo decidía.

### 4.6 Martín

| Sprint | Tarjetas | Estimadas | Reales | Factor |
|---|---|---|---|---|
| 2 | MATU-13, 14, 19 con 23, y 20 | 17,5 | 5,45 | **3,21** |
| 3 | MATU-25, 32 y 33 | 9,0 | 5,74 | **1,57** |
| **2 y 3** | | **26,5** | **11,19** | **2,37** |

- **Fuentes:** MATU-13 (0,7 h), 14 (0,2 h), 19 y 23 (3,2 h compartidas, más 0,6 h propias y 0,4 h de prueba el 29/10 de 23:15 a 23:39) y 20 (0,35 h). MATU-25 (4 h 31 min en cinco bloques), 32 (51 min) y 33 (22 min). Todas, de los comentarios de Martín en cada tarjeta.
- **Desde el sprint 4, Martín ya no desarrolla** (ADR-030). Su trabajo con personas o de despliegue se anota, pero no es vibecoding: MATU-34, 1 h 32 min de sesiones (estimadas 5 h), MATU-35, 1 h 34 min de entrevistas (6 h), MATU-65, 1 h 50 min (5 h), y MATU-64, 1 h 27 min el 09/11 más 17 min el 15/11 (4 h). Son cotas mínimas, porque la preparación y la transcripción no tienen marcas.
- **En el sprint 5 también se anotan sus pruebas en el teléfono**, por ejemplo 50 min en MATU-63 (15/11 y 16/11), 16 min en MATU-112 (17/11) y 15 min de carga en MATU-80 (17/11). Tampoco entran en el factor (comentarios de Martín en cada tarjeta).
- **Sus revisiones y fusiones** se anotan en bloques compartidos entre muchas tarjetas, por ejemplo de 3 h 59 min el 10/11 entre diez tarjetas. No se reparten por historia y no entran en el factor.
- **Equipo, sprints 1 a 5, grupo A:** 181,0 h estimadas contra 94,30 h reales, **factor 1,92**.

### 4.7 Lo que quedó fuera de la cuenta

| Tarjeta | Por qué |
|---|---|
| S0-A, MATU-02, 04, 05a y 06 (sprint 1, Martín) | Sin horas reales anotadas. Se pidieron el 25/10 y no llegaron (comentarios de MATU-02) |
| S0-E (sprint 1) | Tiene 0,3 h de Jorge, pero la tarjeta no tiene estimación |
| MATU-09 y MATU-30 (sprint 2, Martín) | El comentario da el lapso de los agentes y dice «Martín confirma sus horas reales», y no llegó la confirmación. Las 1 h 41 min de Jorge validándolas tampoco entran, porque la estimación es de las tarjetas de Martín |
| MATU-31 y las dos tarjetas sin número del sprint 2 | Sin horas anotadas |
| Demo del 30/10 y ADR-027 (sprint 2) | 8,9 h y 2 h 32 min de Jorge, sin estimación en la tarjeta |
| MATU-36 (sprint 3) | Solo tiene el lapso de 00:14 a 19:29 del 03/11, que la tarjeta declara «no es tiempo activo». Al 19/11 no hay horas activas anotadas, así que queda fuera |
| MATU-40, 41, 45, 48, 49, 50 y 57 (sprint 3) | Tienen horas de Jorge (en total 1 h 28 min, 5 h 13 min, 3 h 44 min, 1 h 42 min, 47 min, 2 h 34 min y 4 h 21 min), pero ninguna estimación escrita. Al 19/11 sigue sin haberla, y no se estima después de hecho, así que quedan fuera |
| MATU-38 (sprint 3, Martín) | 45 min, sin estimación |
| MATU-85 y MATU-94 (sprint 4) | Sin estimación. Sus horas están en el grupo C |
| MATU-103 (sprint 5) | Sin estimación. Sus horas están dentro del bloque del 17/11 |
| MATU-123 (sprint 5) | 2 min de Jorge el 18/11, sin estimación (no tiene código) |
| MATU-76, 115, 116, 121, 122, 126, 127 y 79, y la parte de Martín de MATU-80 (sprint 5) | No están en Terminado al 19/11. Se suman con el mismo método cuando pasen, en la ceremonia de cierre del semestre (P17) |

**Advertencias:**
- MATU-12 (sprint 2) es una cota superior, porque su bloque incluye una pausa por límite de uso.
- En el sprint 3, el bloque de MATU-37 se cruza con MATU-45 y MATU-57, que no entran por falta de estimación.

---

## 5. Trabajo futuro

### 5.1 Las siete tarjetas «Fuera del semestre»

Son las tarjetas que la columna Product Backlog de Trello marca como fuera del semestre, verificadas ahí el 19/11/2026. Jorge decidió el 08/11/2026 nombrarlas en este informe como trabajo futuro (vault, `Planificación/Sprints/Sprint 5.md`). El modelo de datos ya tiene sus tablas, pero no se construyen en el semestre (CLAUDE.md del repositorio MATU_PROYECTO, sección 1).

| # | Tarjeta de Trello | Requisitos | Por qué salió | Lo que ya existe |
|---|---|---|---|---|
| 1 | Fase 2 · prioridad 1 · Reparto del gasto entre varios pagadores | RF-22, RF-23 y RF-24 | Segundo recorte, 75 h. **Vuelve como prioridad 1** (decisión de Jorge del 11/11): en las entrevistas de ampliación, 7 de 14 reparten el gasto con roces, y los cuatro aportantes quieren pagar su parte por separado (`docs/resultados-entrevistas.md`, sección 8) | Tablas `participacion` y `medio_pago_inscrito`, y los cinco casos de varios pagadores escritos como `skip` |
| 2 | Fase 2 · prioridad 1 · Prorrateo del cobro entre pagadores | RF-25 completo | Con un solo pagador no hace falta. RF-25 bajó de XL a M (25 h menos) | El método del mayor resto y una prueba de propiedad de 300 casos, como `skip` |
| 3 | Fuera del semestre · Reposición programada | RF-16 a RF-19 | Segundo recorte, 64 h. Nadie lo pidió en las entrevistas: pidieron el aviso y el botón para pedir en el momento | Tablas `plan_reposicion`, `plan_reposicion_linea` y `ocurrencia` |
| 4 | Fuera del semestre · App de repartidor y seguimiento de posición | RF-27 a RF-30 | Primer recorte, 28 h. En el semestre operación marca el retiro y la entrega desde su consola | El eje `repartidor_id` con sus políticas de aislamiento. MATU-125 (18/11) deja escrito el acceso acotado a la dirección del pedido que lleva quien reparte |
| 5 | Fuera del semestre · Liquidación automática al comercio | Mitad de RF-31 | Primer recorte, 5 h. El consumo se registra por pedido y el cierre se hace en planilla | Tablas `consumo_comercio` y `liquidacion` |
| 6 | Fuera del semestre · Indicadores avanzados del backoffice | Parte de RF-32 | Primer recorte, 8 h. Es lo primero que se sacrifica. Con MATU-123, RF-32 bajó a *Debería* el 18/11 y los cuatro indicadores que quedaban también pasan a después | El catálogo de los comercios ficticios se gestiona desde la consola de operación (MATU-81) |
| 7 | Fuera del semestre · Envío del PIN de relevo por SMS | *Debería* de MATU-18 | La cuidadora dicta el PIN por teléfono, que cumple la misma función de segundo factor sin depender de un proveedor de SMS | El PIN se muestra una sola vez |

### 5.2 Antes de operar con datos reales

No es trabajo futuro opcional: es condición para salir del piloto sintético. Mientras no esté cerrado, MATU trata **solo datos sintéticos** (`docs/sprints/sprint-5-planificacion.md`, sección 11, y épica «Antes de datos reales · Paso a producción» del Product Backlog). Verificado en Trello el 19/11/2026:

| Tarjeta | Qué falta | Estado al 19/11/2026 |
|---|---|---|
| MATU-89 · Borrar a los 3 años los accesos de relevo y la auditoría | Las funciones de conservación que faltan: el token del relevo, el acceso y la auditoría a los 3 años, los pedidos pagados a los 2 años y los pagos a los 6 años. Trae la política 0.26 | Product Backlog. El 18/11 recibió la retención que traía MATU-79, con las decisiones D4 a D8 pendientes, dos de ellas con consulta legal (comentario de Jorge del 18/11) |
| MATU-99 · Cómo se responde un pedido de acceso fuera de la app | El procedimiento escrito en `docs/legal/` | Product Backlog |
| MATU-101 · Borrar a pedido el teléfono o el nombre de un relevo | Una función de operación y su procedimiento, si la CL-34 responde que el relevo puede pedirlo | Product Backlog |
| MATU-98 · Quien administra ve el registro de cambios del grupo | La ruta y su pantalla en «Grupo familiar» | Product Backlog |
| Las consultas legales abiertas | 75 preguntas, de la CL-01 a la CL-75, en `docs/legal/consulta-legal.md`. La cuestión central es si basta el consentimiento de un cuidador de hecho | Tarjeta «Antes de datos reales · Consulta legal sobre el cuidador de hecho» |
| Lo de la épica que MATU-79 deja fuera | HSTS y monitoreo con alertas. El segundo factor de operación ya se construyó en MATU-81 (18/11) | Épica «Paso a producción», junto con la rotación de la clave maestra, el alta comercial en Transbank y MATU-69 |

**MATU-102 sale de esta lista.** Los miembros del grupo dejan de leer el correo y el celular de otros también en SQL, con permisos por columna en `usuario`. Lo cierra la parte 3 de MATU-79, con la migración 0034, por decisión de Jorge del 18/11. Al 19/11 esa parte sigue en curso, y MATU-102 pasa a Terminado cuando se fusione (comentario de Jorge en MATU-102, 18/11).

---

## 6. Pendientes del borrador del 16/11, resueltos

| Pendiente del borrador | Cómo quedó al 19/11/2026 |
|---|---|
| MATU-80, los seis recorridos automatizados en el CI | **Resuelto el 17/11** (#106, CI en verde). Lo que queda del objetivo 7 es de Martín el 19/11, y está en la sección 3.3 |
| La estimación de MATU-40, 41, 45, 48, 49, 50 y 57 | **Quedan fuera del factor.** No hay estimación escrita, y no se inventa una después de hecho (sección 4.7) |
| Las horas activas de Jorge en MATU-36 | **Queda fuera.** La tarjeta solo tiene un lapso declarado como no activo (sección 4.7) |
| El factor del sprint 5, parcial al 16/11 | **Recalculado al 19/11** con lo terminado (sección 4.5). Si en la ceremonia de cierre (P17) pasan más tarjetas a Terminado, Jorge y Martín las suman con el mismo método |
| La guía de la Fase 3 | **Lo integra Martín.** La guía no está en el repositorio al 19/11. En `Fase 3/` están la planilla de evaluación y las plantillas de la autoevaluación y del diario. Martín ajusta los títulos de este texto a la guía al integrarlo (MATU-78) |
| La usabilidad, las entrevistas, las capturas y el video del recorrido principal | **Lo integra Martín** (MATU-78, ítems de Martín del checklist) |

**Cómo verificar las cifras del repositorio de código** (solo lectura, en MATU_PROYECTO, el 19/11/2026):

```
git fetch && git log origin/main -1 --format='%h %ci'
gh pr list --state merged --limit 300 --json number,title,mergedAt
git ls-tree -r --name-only origin/main | grep 'alembic/versions/.*\.py$'
git grep -h -c -E "^\s*(async )?def test_" origin/main -- backend/tests | awk '{s+=$1} {n++} END {print s, n}'
git ls-tree -r --name-only origin/main -- web/pruebas | grep -cE '\.test\.(ts|tsx)$'
gh run list --branch main --limit 1
```

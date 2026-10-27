# MATU — Backlog de producto · sprints 1 a 3

**Versión:** 1.3 · dos rondas de revisión aplicadas y calendario ajustado
**Product Owner:** Jorge Espinoza · **Scrum Master:** Martín Henríquez
**Base:** Arquitectura v1.1 · Modelo de datos v1.0 · Estrategia de pruebas v1.1 · Cierre del ADR-023

> **Calendario v1.3 (13 de octubre).** Los sprints corren de viernes a jueves y el sprint 1 empieza el viernes 16 de octubre. Con desarrollo asistido por IA, **las historias del sprint 3 de este backlog se ejecutan en el sprint 2**, salvo MATU-25 (staging), que pasa al sprint 3. Las estimaciones de este documento no cambian: el factor de vibecoding se aplica al comprometer. Detalle en [sprints/calendario-sprints.md](sprints/calendario-sprints.md).
>
> **Numeración.** Los títulos de las secciones 4 a 6 conservan la agrupación original del backlog. Toda referencia a un sprint posterior al 3 usa la numeración del calendario v1.3: el sprint 3 es la app de familia y el perfil de consumo, el 4 es catálogo, pedido y pago, y el 5 es el cierre.

---

## 1. Capacidad

| Supuesto | Valor |
|---|---|
| Duración del sprint | 1 semana |
| Capacidad bruta | 15 h por persona, 30 h por sprint |
| Ceremonias y refinamiento | 2 h por persona por sprint. La coordinación diaria es asíncrona por Discord |
| Reserva para imprevistos y aprendizaje | 2 h por persona por sprint (13%) |
| **Capacidad comprometible** | **11 h por persona, 22 h por sprint**, incluidas las tareas de equipo y la revisión cruzada |
| Estimación | Horas reales, incluido el aprendizaje del stack |
| Compromiso | **El sprint 1 es compromiso. Los sprints 2 y 3 son pronóstico** y se recalculan con la velocidad real del sprint 1 |
| Modo del plan de cuidado | Ficha de relevo de tres campos (ADR-023 activado) |
| Datos | Los sprints 1 a 3 operan **solo con datos sintéticos** |

**Uso declarado de la reserva.** El tramo compromete 67 h contra 66 comprometibles: usa 1 de las 12 h de reserva (1 h de Jorge en el sprint 2). Queda dicho aquí para que no ocurra sin que nadie lo decida. Si un sprint no usa su reserva, se toma la siguiente historia del sprint siguiente.

**Regla de ejes en este tramo.** En los sprints 1 a 3 la regla "nadie edita módulos del otro eje" (sección 15.5 de la arquitectura) **se suspende para `care_circle`, `care_plan` y `shared`**, porque el tramo concentra el trabajo de la capa 1. El dueño del módulo revisa todo PR que lo toque. Se registra en la arquitectura v1.2.

## 2. Resumen

| Sprint | Objetivo | Cómo se demuestra en la revisión | Horas |
|---|---|---|---|
| 1 | Una familia se registra, crea su grupo y da de alta a la persona cuidada con su consentimiento, y otra familia no puede ver nada de eso | Guion `httpie` de punta a punta con dos familias (la segunda recibe 404) + `test_aislamiento.py` en verde en el pipeline | 22 |
| 2 | Una cuidadora completa la ficha de relevo, que queda cifrada, auditada y sin posibilidad de pisar lo que escribió otro | Guion `httpie` + consulta directa a la base que muestra solo texto cifrado + demostración del 412 con dos miembros | 23 |
| 3 | Una cuidadora comparte la ficha con un relevo, que la abre desde un teléfono real con PIN, y la cuidadora la revoca | Demostración en staging con un teléfono real + prueba e2e `test_recorrido_relevo` en verde | 22 |

---

## 3. Antes del sprint 1 · lo que el sprint 0 tiene que dejar cerrado

| ID | Tarea | Criterios de cierre | Responsable | Estado al 13-10 |
|---|---|---|---|---|
| S0-A | Esqueleto de la API | `app/main.py`, configuración, errores RFC 7807 y logs JSON con `request_id` y **sin cuerpos de petición**. Sin esto no se puede probar que la ficha nunca llega a un log | Martín | **Pendiente.** Pasa al sprint 1 como prioridad 0 |
| S0-B | Ambiente local | `docker compose up` levanta PostgreSQL 16 con los cuatro roles y **Redis** | Martín | **Cerrada.** El script `infra/postgres/init/10_matu.sh` crea los roles, la base y `btree_gist` |
| S0-C | Migración inicial | `backend/db/*.sql` convertido en la migración 0001 de Alembic, reversible. La revisa Jorge antes de fusionar | Martín | **Cerrada.** `0001_esquema_inicial`, con subida, bajada y subida verificadas. `btree_gist` la crea el script de arranque, no una migración |
| S0-D | Pipeline | ruff, mypy, pytest unitarias e integración, detect-secrets, y `upgrade`, `downgrade -1`, `upgrade`. Un PR con un fallo no se fusiona | Martín | **Cerrada.** `.github/workflows/ci.yml`. La regla que impide fusionar con el pipeline en rojo se activa cuando el equipo pase a trabajar con pull requests |
| S0-E | Prueba de concepto de Transbank | Resultado de los cinco casos en `docs/pruebas-concepto/transbank.md`, **incluido el débito** | Los dos | **Parcial.** El débito (caso 4) está respondido: no admite captura diferida. Los casos 1, 2, 3 y 5 pasan al sprint 1 |

**Si alguna queda abierta** pasa a prioridad 0 del sprint 1 y se aplica el orden de sacrificio de la sección 7 desde el punto 1. **S0-E abierta es prioridad 0 para los dos**, porque su resultado puede cambiar el ADR-006 y el ADR-007.

Las rutas de código de este documento (`app/`, `backend/`, `infra/`, `web/`, `spikes/`, `tests/`) son del repositorio **MATU_PROYECTO**.

---

## 4. Sprint 1 · Identidad, grupo y persona cuidada · compromiso

El orden de la tabla es el orden de ejecución.

| Prioridad | ID | Tipo | Título | Traza | Responsable | Horas |
|---|---|---|---|---|---|---|
| 1 | MATU-04 | Historia | Crear una cuenta | RF-37 | Martín | 2 |
| 2 | MATU-05a | Historia | Iniciar sesión y validar el token en cada petición | RF-37 | Martín | 3,5 |
| 3 | MATU-02 | Técnica | Contexto de tenant en la API | ADR-013 | Martín | 3 |
| 4 | MATU-06 | Historia | Crear el grupo familiar | RF-38 | Martín | 2,5 |
| 5 | MATU-26 | Equipo | Política de privacidad v0.9 | Ley 21.719 | Jorge | 1,5 |
| 6 | MATU-07 | Historia | Dar de alta a la persona cuidada con su consentimiento | RF-01 · Ley 21.719 | Jorge | 6 |
| 7 | MATU-03 | Técnica | Puertos y prueba de arquitectura | ADR-021 | Jorge | 2 |
| 8 | MATU-27 | Equipo | Decidir la figura legal del piloto | Riesgo sección 17 | Jorge | 1 |
| 9 | MATU-28 | Equipo | Corregir la anonimización de la entrevista E05 | Protocolo, sección 4 | Jorge | 0,5 |
| | | | | | **Martín 11 · Jorge 11** | **22** |

Jorge empieza por MATU-26 y MATU-07 contra una sesión simulada de pruebas mientras Martín cierra la autenticación. MATU-07 se integra con el contexto real cuando MATU-02 está fusionada.

### MATU-04 · Crear una cuenta

**Como** familiar de una persona mayor, **quiero** crear una cuenta con mi email, **para** empezar a organizar el cuidado.

- Con nombre, email y contraseña de al menos 10 caracteres, se crea la cuenta y responde 201. La contraseña se guarda con Argon2id
- El email se normaliza a minúsculas y se registra `HMAC-SHA256(pepper, email)` en `indice_credencial`. El pepper viene de la configuración, nunca del repositorio
- Un email ya registrado responde 409. **Riesgo aceptado:** el registro revela si un email existe. Se mitiga con un límite por IP (MATU-25) y la verificación por correo entra con el adaptador de correo (sprint 3)

**Pruebas** (`@pytest.mark.rf("RF-37")`): `test_registro_guarda_argon2id`, `test_email_duplicado_409`, `test_indice_credencial_no_guarda_email`

### MATU-05a · Iniciar sesión y validar el token en cada petición

**Como** usuaria, **quiero** entrar con mi email y contraseña, **para** usar la app.

- Un login correcto entrega un access token JWT de 15 minutos
- Email o contraseña incorrectos responden 401 con el mismo mensaje, para no revelar cuál falló
- El login resuelve el usuario por `indice_credencial` y después fija `app.usuario_id` (hallazgo 4 del modelo de datos)
- La dependencia `usuario_actual` valida firma, vencimiento y algoritmo en cada petición. Rechaza `alg=none`, un token alterado y un token vencido con 401

**Pruebas** (`@pytest.mark.rf("RF-37")`): `test_login_correcto_entrega_jwt`, `test_login_incorrecto_mismo_mensaje`, `test_token_vencido_401` (con `RelojFijo`), `test_token_alterado_401`, `test_alg_none_401`

### MATU-02 · Contexto de tenant en la API

**Qué:** el helper `sesion_tenant` de la sección 7.7 y la dependencia de FastAPI que lo usa.

- Toda petición autenticada fija `app.usuario_id` primero y `app.grupo_id` desde `X-Grupo-Id` después
- Si el usuario no es miembro activo del grupo, la API responde **404**, nunca 403
- El contexto es local a la transacción: dos peticiones seguidas en la misma conexión del pool no comparten contexto
- El helper acepta `rol = 'sistema'` (worker, desde el sprint 3) y `app.acceso_relevo_id` (relevo, sprint 2)
- `test_aislamiento.py` se mueve a `backend/tests/` y corre en el pipeline contra la migración de Alembic. **Cumplido en el sprint 0**, por eso la historia baja de 4 a 3 horas

**Pruebas:** `test_contexto_no_se_filtra_entre_peticiones`, `test_no_miembro_recibe_404`, `test_sistema_sin_grupo_cero_filas`, suite `test_aislamiento.py` completa

### MATU-06 · Crear el grupo familiar

**Como** familiar, **quiero** crear el grupo de cuidado de mi mamá, **para** reunir ahí a quienes ayudan.

- Al crear un grupo, quien lo crea queda como `admin` en la misma transacción. Si falla la membresía, no queda grupo
- El identificador del grupo se genera en la aplicación antes del `INSERT` (con RLS, un `INSERT … RETURNING` sin membresía previa devuelve cero filas)
- `GET /v1/grupos` lista los grupos del usuario y ningún otro

**Pruebas** (`@pytest.mark.rf("RF-38")`): `test_crear_grupo_deja_admin`, `test_no_ve_grupos_ajenos`

### MATU-26 · Política de privacidad v0.9

- Documento en `docs/legal/politica-privacidad.md` con finalidades, datos tratados, derechos del titular y el aviso para el cuidador de hecho
- Declara que el piloto de los sprints 1 a 3 no trata datos reales
- Su versión se publica en la configuración como `POLITICA_VERSION`

### MATU-07 · Dar de alta a la persona cuidada con su consentimiento

**Como** cuidadora, **quiero** registrar a la persona que cuido y declarar en qué calidad autorizo el uso de sus datos, **para** que todo se organice en torno a ella y el tratamiento sea legal.

- Dado un `admin` o `cuidador`, cuando envía nombre, nombre de pila, nivel de apoyo (`autovalente_con_supervision`, `apoyo_parcial` o `apoyo_total`), dirección **opcional** y calidad del otorgante, entonces la persona y su consentimiento para `plan_cuidado` se crean **en una sola transacción, o no se crea nada**
- **La dirección es opcional en el alta** (decisión del 24-10, por minimización): la ficha y el relevo no la usan, y se pide con el primer pedido
- `titular`: la persona cuidada declara en presencia del usuario, y el usuario lo registra
- `representante_legal` sin referencia al documento responde 422
- `cuidador_de_hecho` fija la revisión en 12 meses, y la respuesta incluye el texto del aviso de limitación. **La evidencia del consentimiento registra el identificador y la versión del aviso mostrado** (decisión del 24-10)
- Se guarda la versión de la política vigente. Fuera del ambiente de pruebas, sin `POLITICA_VERSION` configurada la API no arranca. En pruebas se usa la versión de la fábrica
- **No se pide ni se acepta diagnóstico:** un campo extra en el cuerpo responde 422
- `pagador` y `observador` reciben 404 al intentar crear
- `GET /v1/grupos/{id}/personas-cuidadas` lista las personas del grupo, con lo que cada rol puede ver (arquitectura 11.2). `admin` y `cuidador` ven además la calidad del consentimiento vigente (11.5). Un usuario de otro grupo recibe 404
- La clave de datos **no** se crea aquí: se crea en la primera escritura de la ficha (MATU-11)

**Pruebas** (`@pytest.mark.rf("RF-01")`): `test_alta_con_consentimiento_atomica`, `test_representante_sin_documento_422`, `test_cuidador_de_hecho_fija_revision`, `test_campo_diagnostico_422`, `test_observador_no_da_de_alta`, `test_otro_grupo_no_ve_persona_404`

### MATU-03 · Puertos y prueba de arquitectura

- Existen los puertos `Reloj` y `CustodiaClaves`, cada uno con su doble en `tests/dobles/`. `Notificador`, `PasarelaPago` y `AlmacenObjetos` se diseñan cuando se usan
- `test_arquitectura.py` verifica las cuatro reglas de la sección 6.4
- **No pasa en vacío:** un módulo de prueba con una importación prohibida hace fallar la prueba
- Una prueba falla si algún archivo de `domain/` llama a `datetime.now()` o importa un SDK externo

**Pruebas:** `test_reglas_de_dependencia`, `test_importacion_prohibida_falla`, `test_dominio_sin_reloj_del_sistema`

### MATU-27 · Decidir la figura legal del piloto

- Decisión escrita: constituir una persona jurídica (plazo y costo), o declarar que el piloto opera en el ambiente de integración de Transbank y lo dice en el informe
- El trámite de alta comercial de Transbank se inicia **solo si** la decisión es constituir la persona jurídica

**Decisión del 24-10 (Jorge):** durante el semestre el piloto opera solo en el ambiente de integración de Transbank, con datos sintéticos y sin cobros reales, y se declara en el informe. La persona jurídica y el alta comercial quedan para después del semestre. Detalle en `docs/legal/figura-legal-piloto.md`

### MATU-28 · Corregir la anonimización de E05

- La ficha de E05 no contiene nombres propios. El análisis de las entrevistas no cambia
- Se decide qué hacer con las versiones anteriores que siguen en el historial público del repositorio

**Estado al 13-10:** los nombres se quitaron de E05, y la mención del integrante del equipo que hizo el contacto se quitó también de E03 y E01. Queda la decisión sobre el historial.

---

## 5. Sprint 2 · Ficha de relevo · pronóstico

| Prioridad | ID | Tipo | Título | Traza | Responsable | Horas |
|---|---|---|---|---|---|---|
| 1 | MATU-09 | Técnica | Contrato de API: primero la ficha, después el relevo | Sección 15.5, regla 1 | Martín | 3 |
| 2 | MATU-12 | Historia | Completar la ficha de relevo | RF-02 | Jorge | 6 |
| 3 | MATU-11 | Técnica | Cifrado de secciones con clave por persona | ADR-014, ADR-016 | Jorge | 6 |
| 4 | MATU-14 | Técnica | Auditoría de lectura y escritura de la ficha | RF-08 | Martín | 1,5 |
| 5 | MATU-13 | Historia | Editar sin pisar lo que escribió otro | RF-04 | Martín | 3 |
| 6 | MATU-30 | Técnica | Fábricas, semilla y lista de lenguaje | Estrategia, sección 9 | Martín | 1,5 |
| 7 | MATU-31 | Equipo | Revisión cruzada de MATU-11 y MATU-12 | Definición de terminado, punto 5 | Martín | 2 |
| | | | | | **Jorge 12 · Martín 11** | **23** |

**Orden de ejecución.** Martín cierra la parte de ficha de MATU-09 en sus primeras 2 h. Jorge implementa MATU-12 contra el puerto `CifradorSecciones` con un doble, y después MATU-11 detrás de ese puerto. MATU-13 empieza cuando el PUT de MATU-12 está fusionado. Mientras tanto Martín hace MATU-30 y MATU-14.

### MATU-09 · Contrato de API: primero la ficha, después el relevo

**Qué:** acordar el OpenAPI **antes** de implementar.

- **Parte 1, ficha (primeras 2 h):** lectura y escritura de los tres campos, con `ETag`, `If-Match` e `If-None-Match`
- **Parte 2, relevo:** `POST /v1/personas-cuidadas/{id}/plan/accesos-relevo`, `DELETE /v1/accesos-relevo/{id}`, `POST /v1/relevo/canje` (token y PIN en el cuerpo, responde cookie), `GET /v1/relevo/ficha` y `GET /v1/personas-cuidadas/{id}/plan/aperturas`
- Declara los errores 403, 404, 410, 412, 423 y 428 con su `type` RFC 7807 y un ejemplo por respuesta
- **Los contratos acordados y no implementados viven en `docs/api/propuestos/`.** La puerta openapi-diff compara solo las rutas implementadas, y una ruta pasa a `docs/api/openapi.json` cuando su historia se termina
- Jorge revisa y aprueba cada parte

### MATU-12 · Completar la ficha de relevo

**Como** cuidadora, **quiero** escribir en tres campos cortos cómo es su día, qué hacer si se altera y a quién llamar, **para** poder dejarla con otra persona sin pasar horas explicando.

- La ficha tiene tres campos: **Su día** (`rutina`), **Si se altera** (`manejo_situaciones`) y **A quién llamar** (`red_apoyo`), con sus preguntas guía y un ejemplo de respuesta tomados de `docs/lenguaje.md`
- Leen `admin`, `cuidador` y `pagador` con `puede_ver_plan`. Escriben `admin` y `cuidador`. Un `observador` recibe 404
- Cada campo acepta hasta 500 caracteres y se guarda por separado. El plan nace en la primera escritura con `modo = 'ficha_relevo'`
- La completitud es `round(100 × campos_con_texto / 3)`: 0, 33, 67 o 100
- Sin consentimiento vigente para `plan_cuidado`, leer o escribir responde 403 con el `type` de consentimiento
- Ningún registro de log contiene el texto enviado
- Se construye contra el puerto `CifradorSecciones` con un doble. La integración con MATU-11 es el último paso

**Pruebas** (`@pytest.mark.rf("RF-02")`): `test_ficha_tres_campos`, `test_observador_404`, `test_pagador_sin_permiso_404`, `test_sin_consentimiento_403`, `test_completitud_por_campo`, `test_log_sin_texto_de_ficha` (con `caplog`)

La meta de tiempo ("menos de 3 minutos") no es un criterio de esta historia: se mide en la prueba de usabilidad (estrategia de pruebas, sección 11).

### MATU-11 · Cifrado de secciones con clave por persona

- Implementa el puerto `CifradorSecciones`. Cada sección se cifra con AES-256-GCM usando la clave de datos (DEK) de la persona, envuelta con la KEK del puerto `CustodiaClaves`
- La DEK se crea en la primera escritura de la ficha. "No existe" y "destruida" son estados distintos y se distinguen
- Cada escritura usa un nonce aleatorio nuevo de 12 bytes
- **El AAD es `plan_id ‖ tipo`:** mover un texto cifrado a otra sección o a otro plan falla al descifrar
- Un texto cifrado alterado falla al descifrar
- Con la clave destruida, escribir lanza un error de dominio explícito, nunca genera una clave nueva
- `kek_version` queda registrada. **La rotación de la KEK se implementa después del semestre, antes de operar con datos reales**

**Pruebas:** `test_cifrar_descifrar_ida_y_vuelta`, `test_nonces_distintos`, `test_texto_alterado_falla`, `test_mover_cifrado_a_otra_seccion_falla`, `test_escribir_con_clave_destruida_falla`, `test_dek_se_crea_en_primera_escritura`

### MATU-14 · Auditoría de lectura y escritura de la ficha

- Un servicio en `shared/` registra actor, momento, acción, entidad y motivo
- Toda lectura y escritura de la ficha inserta una fila en `auditoria`

**Pruebas** (`@pytest.mark.rf("RF-08")`): `test_lectura_queda_auditada`, `test_escritura_queda_auditada`, `test_auditoria_no_se_modifica` (un `UPDATE auditoria` con `matu_app` falla)

### MATU-13 · Editar sin pisar lo que escribió otro

**Como** hermana que también cuida, **quiero** que si mi hermano editó la ficha mientras yo la editaba no se pierda lo suyo, **para** no borrar sin querer lo que él escribió.

- Cada campo viaja con su `ETag`
- Guardar con un `If-Match` desactualizado responde 412 con el contenido actual
- Guardar sin `If-Match` sobre un campo que ya existe responde 428
- La primera escritura de un campo usa `If-None-Match: *`. Si otro lo creó antes, responde 412
- No hay fusión automática (ADR-015)
- Se prueba con dos miembros creados por las fábricas de MATU-30

**Pruebas** (`@pytest.mark.rf("RF-04")`): `test_if_match_desactualizado_412`, `test_sin_if_match_428`, `test_primera_escritura_concurrente_412`

### MATU-30 · Fábricas, semilla y lista de lenguaje

- Fábricas de usuario, grupo, membresía con cada rol, persona cuidada con consentimiento y ficha
- `infra/semillas/demo.py` crea dos familias y un pagador con `puede_ver_plan`
- `docs/lenguaje.md` con la lista de palabras de las entrevistas, los términos prohibidos (diagnóstico, conducta, incidente, deterioro, incontinencia) y los textos de la ficha y de los errores del relevo

### MATU-31 · Revisión cruzada de MATU-11 y MATU-12

- Martín revisa los dos PR contra la definición de terminado, en especial el punto 5 (datos sensibles)
- Contrasta los textos de la ficha con `docs/lenguaje.md`

---

## 6. Sprint 3 · Relevo · pronóstico

| Prioridad | ID | Tipo | Título | Traza | Responsable | Horas |
|---|---|---|---|---|---|---|
| 1 | MATU-25 | Técnica | Staging con HTTPS y límite por IP | ADR-019 · sección 13.2 | Martín | 5,5 |
| 2 | MATU-18 | Historia | Compartir la ficha con un relevo | RF-05 | Jorge | 3,5 |
| 3 | MATU-19 | Historia | Abrir la ficha como relevo con enlace y PIN | RF-06 | Jorge | 6,5 |
| 4 | MATU-20 | Historia | Revocar un acceso de relevo | RF-07 | Jorge | 1 |
| 5 | MATU-23 | Historia | Página web del relevo | RF-06 | Martín | 5,5 |
| | | | | | **Jorge 11 · Martín 11** | **22** |

### MATU-25 · Staging con HTTPS y límite por IP

- La API responde por HTTPS en un dominio de staging, en la plataforma gestionada del ADR-019, con base de datos gestionada, roles y `btree_gist`, Redis y secretos fuera del repositorio
- **El límite por IP vive en la API, con Redis** (contador por ventana), no en el proxy: `/v1/usuarios` 5 por hora y `/v1/relevo/canje` 10 por hora
- Tras correr el e2e, un `grep` sobre los logs del proxy y de la API no encuentra el token ni el PIN
- El despliegue es un comando documentado en el README

### MATU-18 · Compartir la ficha con un relevo

**Como** cuidadora, **quiero** mandarle la ficha a quien me va a reemplazar el sábado, **para** poder salir tranquila.

- Elijo qué campos compartir, hasta cuándo y el motivo. Vigencia por defecto de 24 horas, máxima de 30 días
- Se genera un token de 256 bits (se guarda solo su hash) y un PIN de 4 dígitos
- **El PIN se muestra una sola vez a la cuidadora**, para que se lo dicte al relevo por teléfono. El envío por SMS queda como *Debería*: el PIN viaja por un canal distinto del enlace, que es lo que lo hace un segundo factor
- El acceso se puede generar aunque la ficha esté incompleta. Un campo vacío se le muestra al relevo como "Sin completar"
- El acceso guarda `nombre_pila_persona`, para que el relevo nunca lea `persona_cuidada`

**Pruebas** (`@pytest.mark.rf("RF-05")`): `test_acceso_guarda_solo_hash`, `test_vigencia_maxima_30_dias`, `test_acceso_con_ficha_incompleta`

### MATU-19 · Abrir la ficha como relevo con enlace y PIN

**Como** persona que reemplaza a la cuidadora, **quiero** abrir la ficha con el enlace y el PIN que me dieron, **para** saber qué hacer.

- El enlace lleva el token en el **fragmento** (`/r#<token>`), que el navegador no envía al servidor ni al proxy. La página lo manda por POST a `/v1/relevo/canje` junto con el PIN
- El canje responde una cookie de sesión efímera (Redis, `HttpOnly`, `Secure`, `SameSite=Strict`) y la página limpia la URL con `history.replaceState`
- La sesión de relevo fija **solo** `app.rol = 'relevo'` y `app.acceso_relevo_id`, nunca `app.grupo_id`
- El relevo ve solo los campos habilitados y el nombre de pila
- Un enlace vencido o revocado responde 410
- Cinco PIN incorrectos responden 423 y el acceso queda bloqueado. Un acceso bloqueado se reemplaza generando uno nuevo
- Cada apertura, y cada PIN incorrecto, queda auditada

**Pruebas** (`@pytest.mark.rf("RF-06")`): `test_relevo_ve_solo_campos_habilitados`, `test_relevo_vencido_410`, `test_cinco_pin_incorrectos_423`, `test_relevo_no_hereda_nada_de_la_familia`, `test_apertura_auditada`. El cliente de prueba usa `base_url="https://testserver"` para que la cookie `Secure` viaje

### MATU-20 · Revocar un acceso de relevo

**Como** cuidadora, **quiero** cortar el acceso de un relevo cuando termina su turno, **para** que nadie siga leyendo la ficha.

- `admin` o `cuidador` revoca el acceso
- La siguiente petición del relevo responde 410, aunque tenga una cookie válida

**Pruebas** (`@pytest.mark.rf("RF-07")`): `test_revocacion_efecto_inmediato`, `test_recorrido_relevo` (e2e: crear ficha, compartir, canjear, leer, revocar, 410)

### MATU-23 · Página web del relevo

**Como** persona que reemplaza a la cuidadora, **quiero** leer la ficha desde el celular sin instalar nada, **para** saber qué hacer desde el primer minuto.

- HTML y JavaScript sin framework en `web/relevo/`, servidos por la API con `StaticFiles` desde el mismo origen (sin CORS)
- Texto base de 17 px expresado en `rem`. Con zoom al 200% y 320 px de ancho no hay desplazamiento horizontal (WCAG 1.4.4 y 1.4.10)
- Cada estado (PIN incorrecto, bloqueado, vencido, revocado) muestra el texto definido en `docs/lenguaje.md` y una acción: "Pídele a quien te envió el enlace uno nuevo"
- Respuestas con `Cache-Control: no-store`, `Referrer-Policy: no-referrer` y `X-Robots-Tag: noindex`
- Se construye contra el contrato de MATU-09 con un doble, mientras el backend se termina

**Pruebas:** revisión manual en un teléfono real con el checklist de accesibilidad de la estrategia (sección 7)

---

## 7. Qué se cae primero

Si un sprint se atrasa, o si una tarea del sprint 0 queda abierta, se sacrifica en este orden:

1. **MATU-28 y MATU-27** pasan al sprint 2. MATU-27 nunca después del sprint 2
2. **MATU-30** se reduce a las fábricas de prueba. La demostración usa el guion `httpie`, que crea sus propios datos
3. **En MATU-23, el estilo visual** se reduce a la hoja base. **Los criterios de accesibilidad no se sacrifican**, porque son el punto 4 de la definición de terminado
4. **MATU-25** se reemplaza por un túnel HTTPS temporal para la demostración, y el staging pasa al sprint 4

Si aun así no alcanza, MATU-03 se reduce a `Reloj` y a la prueba de arquitectura.

**Nunca se sacrifican:** MATU-02, 04, 05a, 06, 07, 09, 11, 12, 13, 14, 18, 19 y 20, ni el aislamiento en el pipeline. Son el objetivo del tramo.

**Regla:** si la velocidad del sprint 1 queda bajo el 80% de lo comprometido, los puntos 1 y 2 se aplican **antes** de planificar el sprint 2, no a mitad de camino.

---

## 8. Lo que salió de este tramo y a dónde fue

Los destinos usan la numeración del calendario v1.3.

| Historia | Destino | Por qué |
|---|---|---|
| Mantener la sesión abierta: refresh rotativo, reutilización y registro de dispositivos (RF-37) | Sprint 3, con la app | Nadie usa el refresh hasta que exista la app. La demora progresiva por email e IP va como ítem aparte |
| Prueba de capa 3 desacoplable (ADR-002) | Sprint 3 | La arquitectura la pide junto con el relevo. Se mueve un sprint por capacidad, y se registra en la v1.2 |
| Arquitectura v1.2 | Sprint 3 (4 h) | Solo la sección 7 tiene 16 cambios. El cierre del ADR-023 ya documenta la decisión urgente |
| Ver quién abrió la ficha (RF-08, pantalla) | Sprint 3, con la app | La auditoría se registra desde el sprint 2. Solo falta mostrarla |
| Exportar la ficha imprimible (RF-09) | Sprint 3, con la app | Es *Debería* y se ve en la app |
| Contrato de los endpoints de la app familia | Sprint 3, primer día (3 h) | Para que el desarrollo de la app no se bloquee |
| Invitar a un familiar y gestionar roles (RF-38) | Sprint 3 | No aporta al objetivo de los sprints 1 a 3. La concurrencia se prueba con las fábricas |
| Publicador del outbox y avisos por push y correo (RF-39) | Sprint 3 | Sin eventos que publicar hasta las alertas de quiebre, y FCM necesita el token que da la app |
| Revocar el consentimiento y cortar los accesos de relevo vigentes | Sprint 3 | Derecho de la Ley 21.719. Obligatorio antes de operar con datos reales |

**Sobre las horas que libera el ADR-023.** La ficha de tres campos cuesta menos que el plan de ocho secciones. Esas horas no se reasignan a funciones nuevas: **se usan como la reserva de los sprints 1 a 3**, que es donde faltaba. La capa 2 sigue en el sprint 3.

## 9. Tareas del equipo fuera de este tramo

| Tarea | Responsable | Plazo |
|---|---|---|
| Alta comercial de Transbank, solo si MATU-27 decide constituir persona jurídica | Martín | Después de MATU-27 |
| Cuatro entrevistas adicionales para H5, H6 y H7, fuera de la red personal del equipo | Los dos | Antes del sprint 4 (6 de noviembre) |
| Carta de intención de un comercio | Jorge | Antes del sprint 4 (6 de noviembre) |
| Consulta legal sobre el cuidador de hecho | Jorge | Antes de operar con datos reales |

---

## 10. Historial de revisión

| Versión | Cambio |
|---|---|
| 1.0 | Primer borrador: 27 h por sprint, 24 historias |
| 1.1 | Primera revisión experta (nota 4,5). Capacidad real con reserva, alta de la persona fusionada con el consentimiento, dependencias invertidas corregidas, seguridad del relevo (token en el fragmento, AAD, HMAC), invitaciones y notificaciones fuera del tramo, orden de sacrificio |
| 1.2 | Segunda revisión experta (nota 5,5). Orden de ejecución dentro de cada sprint, validación del JWT, listado con 404 cruzado para demostrar el aislamiento, estimaciones corregidas (MATU-12, 19 y 25), límite por IP en la API, fábricas y lista de lenguaje, revisión cruzada con horas, orden de sacrificio coherente con la definición de terminado, suspensión declarada de la regla de ejes |
| 1.3 | Calendario v1.3: sprints de viernes a jueves desde el 16 de octubre, sprint 3 fusionado con el sprint 2 por el desarrollo asistido por IA, MATU-25 al sprint 3, estado del sprint 0 al 13 de octubre. Segunda revisión: MATU-02 baja a 3 h porque una tarea se cerró en el sprint 0, MATU-12 se traza a RF-02 como en la arquitectura v1.1 y los sprints posteriores al 3 usan la numeración del calendario |

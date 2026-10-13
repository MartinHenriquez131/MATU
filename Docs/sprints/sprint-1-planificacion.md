# MATU — Planificación del sprint 1

**Sprint:** 1 · semana 9 del ramo · lunes 5 a sábado 10 de octubre de 2026
**Equipo:** Jorge Espinoza (Product Owner) · Martín Henríquez (Scrum Master)
**Base:** Backlog sprints 1 a 3 v1.2

---

## 1. Objetivo del sprint

> **Una familia se registra, crea su grupo y da de alta a la persona cuidada con su consentimiento, y otra familia no puede ver nada de eso.**

Es el primer incremento con código del proyecto. Deja resuelta la identidad y el aislamiento, que son la base de todo lo que viene, y entrega la primera evidencia de desarrollo para el **informe de avance de la semana 10** (20% de la nota semestral).

## 2. Capacidad y compromiso

| | Jorge | Martín | Total |
|---|---|---|---|
| Capacidad bruta | 15 h | 15 h | 30 h |
| Ceremonias y refinamiento | 2 h | 2 h | 4 h |
| Reserva | 2 h | 1 h (usa 1 h declarada) | 3 h |
| **Comprometido** | **11 h** | **12 h** | **23 h** |

**Dos condiciones que hay que confirmar en la planificación, antes de comprometer:**

1. **Jorge empieza la práctica profesional en MSD el 1 de octubre**, con 540 horas hasta el 30 de diciembre (unas 40 horas semanales). Las 15 horas semanales para el capstone se declararon antes de eso. **Si Jorge tiene menos de 15 h reales, su compromiso baja en la misma cantidad** siguiendo el orden de sacrificio: primero MATU-28 y MATU-27, después MATU-03 reducida a `Reloj`. MATU-26 y MATU-07 no se tocan.
2. **Las tareas del sprint 0 (S0-A a S0-E) tienen que estar cerradas.** Si alguna quedó abierta, pasa a prioridad 0 y se aplica el mismo orden de sacrificio. La prueba de Transbank (S0-E) es prioridad 0 para los dos si no se hizo.

## 3. Historias comprometidas y sus tareas

El orden es el orden de ejecución.

### Martín · 12 h

| # | Historia | Tareas | Horas |
|---|---|---|---|
| 1 | **MATU-04** Crear una cuenta | Esquema Pydantic y `POST /v1/usuarios` (0,5) · servicio con Argon2id y HMAC del email (0,5) · repositorio de `usuario` e `indice_credencial` (0,5) · pruebas (0,5) | 2 |
| 2 | **MATU-05a** Iniciar sesión y validar el token | `POST /v1/sesiones` (1) · emisión del JWT y configuración de la clave (0,5) · dependencia `usuario_actual` con validación de firma, vencimiento y algoritmo (1) · pruebas con `RelojFijo` (1) | 3,5 |
| 3 | **MATU-02** Contexto de tenant | Helper `sesion_tenant` (1) · dependencia con `X-Grupo-Id` y 404 (1) · mover `test_aislamiento.py` y conectarlo a Alembic (1) · pruebas de contexto entre peticiones (1) | 4 |
| 4 | **MATU-06** Crear el grupo familiar | `POST` y `GET /v1/grupos` (1) · transacción grupo más admin, con identificador generado en la app (0,5) · pruebas (1) | 2,5 |

### Jorge · 11 h

| # | Historia | Tareas | Horas |
|---|---|---|---|
| 1 | **MATU-26** Política de privacidad v0.9 | Redactar `docs/legal/politica-privacidad.md` (1) · publicar `POLITICA_VERSION` en la configuración (0,5) | 1,5 |
| 2 | **MATU-07** Alta de la persona cuidada con consentimiento | Esquemas con rechazo de campos extra (1) · servicio transaccional persona más consentimiento (1,5) · `POST` y `GET /v1/grupos/{id}/personas-cuidadas` (1) · reglas por calidad del otorgante (0,5) · pruebas (2) | 6 |
| 3 | **MATU-03** Puertos y prueba de arquitectura | Puertos `Reloj` y `CustodiaClaves` con sus dobles (1) · `test_arquitectura.py` con caso negativo (1) | 2 |
| 4 | **MATU-27** Figura legal | Revisar opciones y escribir la decisión (1) | 1 |
| 5 | **MATU-28** Anonimizar A55 | Editar la ficha (0,5) | 0,5 |

**Dependencia dentro del sprint.** Jorge construye MATU-07 contra una sesión simulada en las pruebas mientras Martín termina MATU-02. La integración con el contexto real es el último paso de MATU-07, y ocurre cuando MATU-02 está fusionada. Si el jueves MATU-02 no está fusionada, Jorge avisa en Discord y Martín la prioriza sobre MATU-06.

## 4. Secuencia sugerida de la semana

| Día | Martín | Jorge |
|---|---|---|
| Lunes 5 | Planificación (1 h) · MATU-04 | Planificación (1 h) · MATU-26 |
| Martes 6 | MATU-05a | MATU-07: esquemas y servicio |
| Miércoles 7 | MATU-05a · inicio MATU-02 | MATU-07: endpoints y reglas |
| Jueves 8 | MATU-02 fusionada | MATU-07: pruebas · MATU-03 |
| Viernes 9 | MATU-06 · revisión del PR de MATU-07 | Integración de MATU-07 con MATU-02 · MATU-27 · MATU-28 |
| Sábado 10 | Revisión y retrospectiva (1 h) | Revisión y retrospectiva (1 h) |

Jorge revisa los PR de Martín y Martín los de Jorge. **MATU-07 toca datos sensibles: la revisión de Martín es obligatoria** (definición de terminado, punto 5).

## 5. Definición de terminado

Una historia está terminada cuando, y solo cuando:

1. Tiene pruebas de dominio de sus reglas nuevas
2. Tiene al menos una prueba de integración del camino feliz y una del principal camino de error
3. El pipeline pasa completo, incluidas las pruebas de arquitectura y de aislamiento
4. Si toca una pantalla, cumple el checklist de accesibilidad (no aplica en este sprint: no hay pantallas)
5. Si toca dinero o datos sensibles, la revisa la otra persona. Sin excepción
6. Si corrige un defecto, deja una prueba que falla sin la corrección

## 6. Guion de la revisión del sprint

La revisión del sábado muestra el objetivo con este guion, en vivo contra el ambiente local:

```bash
# 1. Dos familias se registran e inician sesión
http POST :8000/v1/usuarios nombre="Ana" email=ana@demo.cl password=clave-segura-1
http POST :8000/v1/usuarios nombre="Luis" email=luis@demo.cl password=clave-segura-2
ANA=$(http POST :8000/v1/sesiones email=ana@demo.cl password=clave-segura-1 | jq -r .access_token)
LUIS=$(http POST :8000/v1/sesiones email=luis@demo.cl password=clave-segura-2 | jq -r .access_token)

# 2. Ana crea su grupo y da de alta a su mamá con consentimiento de cuidadora de hecho
G=$(http POST :8000/v1/grupos nombre="Familia Soto" "Authorization:Bearer $ANA" | jq -r .id)
http POST :8000/v1/grupos/$G/personas-cuidadas "Authorization:Bearer $ANA" "X-Grupo-Id:$G" \
     nombre="María Soto" nombre_pila="María" nivel_apoyo=apoyo_total \
     direccion:='{"calle":"Los Aromos","numero":"123","comuna":"La Reina"}' \
     calidad_otorgante=cuidador_de_hecho

# 3. Luis intenta ver la persona de la familia de Ana: 404
http GET :8000/v1/grupos/$G/personas-cuidadas "Authorization:Bearer $LUIS" "X-Grupo-Id:$G"

# 4. Un diagnóstico en el cuerpo se rechaza: 422
http POST :8000/v1/grupos/$G/personas-cuidadas "Authorization:Bearer $ANA" "X-Grupo-Id:$G" \
     nombre="X" nombre_pila="X" nivel_apoyo=apoyo_total diagnostico="Alzheimer" calidad_otorgante=titular
```

Y en pantalla, el pipeline en verde con `test_aislamiento.py` y `test_arquitectura.py`.

## 7. Riesgos del sprint

| Riesgo | Probabilidad | Qué se hace |
|---|---|---|
| Jorge tiene menos horas por la práctica | **Alta** | Se confirma en la planificación y se ajusta el compromiso antes de empezar, no a mitad de semana |
| Una tarea del sprint 0 sigue abierta | Media | Prioridad 0 y orden de sacrificio |
| El `INSERT … RETURNING` con RLS falla al crear el grupo | Media | Ya está previsto en MATU-06: el identificador se genera en la aplicación |
| MATU-02 se atrasa y bloquea la integración de MATU-07 | Media | Aviso el jueves y reprioriza sobre MATU-06 |
| La entrega formativa 2.3 del ramo cae esta misma semana | Alta | No está en las 23 h. Se prepara con la evidencia de este sprint y se estima aparte |

## 8. Lo que este sprint deja para el informe de avance (semana 10)

- Repositorio con código ejecutable y pipeline en verde
- Suite de aislamiento con 31 pruebas contra PostgreSQL real
- Modelo de datos completo, documentado, con 13 diagramas
- Cierre del ADR-023 con la evidencia de las 10 entrevistas
- Guion de demostración reproducible

**El sprint 2 cae en la semana 10, la del informe de avance.** Su planificación tiene que descontar las horas de redacción del informe, o el informe se hace fuera de las 15 horas. Conviene decidirlo en la retrospectiva de este sprint.

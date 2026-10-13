# MATU — Planificación del sprint 1

**Sprint:** 1 · viernes 16 a jueves 22 de octubre de 2026 · semanas 10 y 11 del ramo
**Equipo:** Jorge Espinoza (Product Owner) · Martín Henríquez (Scrum Master)
**Base:** [Backlog sprints 1 a 3 v1.3](../backlog-sprints-1-3.md) · [Calendario de sprints v1.3](calendario-sprints.md)

---

## 1. Objetivo del sprint

> **Una familia se registra, crea su grupo y da de alta a la persona cuidada con su consentimiento, y otra familia no puede ver nada de eso.**

Es el primer incremento con código de producto. Deja resueltas la identidad y el aislamiento, que son la base de todo lo que viene. **También mide el factor de vibecoding** del calendario v1.3, que decide si los sprints 2 a 5 se mantienen como están planificados.

## 2. Capacidad y compromiso

| | Jorge | Martín | Total |
|---|---|---|---|
| Capacidad bruta | 15 h | 15 h | 30 h |
| Ceremonias y refinamiento | 2 h | 2 h | 4 h |
| Reserva | 2 h | 1 h | 3 h |
| **Capacidad real** | **11 h** | **12 h** | **23 h** |
| **Horas estimadas comprometidas** | **12 h** | **14 h** | **26 h** |

Se comprometen 26 h estimadas contra 23 h reales, un factor de 1,13. Es menos de lo que supone el calendario (1,8) **a propósito**: el primer sprint con vibecoding es el que da el dato real, y comprometer de más justo ahí haría que el dato saliera de un sprint atrasado.

**Dos condiciones que se confirman en la planificación del viernes 16, antes de comprometer:**

1. **Jorge está en práctica profesional en MSD** desde el 1 de octubre, con unas 40 horas semanales. Si tiene menos de 11 h reales, su compromiso baja en la misma cantidad siguiendo el orden de sacrificio: primero MATU-28 y MATU-27, después MATU-03 reducida a `Reloj`. MATU-26 y MATU-07 no se tocan.
2. **El factor real se registra al cierre.** Al terminar cada historia se anotan sus horas reales en la tarjeta de Trello.

## 3. Pendientes del sprint 0 · prioridad 0

| Tarea | Responsable | Horas | Criterio de cierre |
|---|---|---|---|
| **S0-A · Esqueleto de la API** | Martín | 2 | `app/main.py`, configuración, errores RFC 7807 y logs JSON con `request_id` y sin cuerpos de petición. MATU-04 lo necesita para empezar |
| **S0-E · Prueba de concepto de Transbank** | Los dos | 1 | Casos 1, 2, 3 y 5 de la estrategia de pruebas (sección 10) con su resultado real en `docs/pruebas-concepto/transbank.md`. El caso 4 (débito) ya está respondido, y queda escrita la decisión que se toma con él: plan B para el débito o MVP solo con crédito |

Las rutas de código de este documento (`app/`, `spikes/`) son del repositorio **MATU_PROYECTO**. `docs/pruebas-concepto/` está en este repositorio.

## 4. Historias comprometidas y sus tareas

El orden es el orden de ejecución.

### Martín · 14 h

| # | Historia | Tareas | Horas |
|---|---|---|---|
| 0 | **S0-A** Esqueleto de la API | Ver sección 3 | 2 |
| 1 | **MATU-04** Crear una cuenta | Esquema Pydantic y `POST /v1/usuarios` (0,5) · servicio con Argon2id y HMAC del email (0,5) · repositorio de `usuario` e `indice_credencial` (0,5) · pruebas (0,5) | 2 |
| 2 | **MATU-05a** Iniciar sesión y validar el token | `POST /v1/sesiones` (1) · emisión del JWT y configuración de la clave (0,5) · dependencia `usuario_actual` con validación de firma, vencimiento y algoritmo (1) · pruebas con `RelojFijo` (1) | 3,5 |
| 3 | **MATU-02** Contexto de tenant | Helper `sesion_tenant` (1) · dependencia con `X-Grupo-Id` y 404 (1) · pruebas de contexto entre peticiones (1). Mover la suite de aislamiento y correrla contra la migración de Alembic se cerró en el sprint 0 | 3 |
| 4 | **MATU-06** Crear el grupo familiar | `POST` y `GET /v1/grupos` (1) · transacción grupo más admin, con identificador generado en la app (0,5) · pruebas (1) | 2,5 |
| 5 | **S0-E** Prueba de Transbank, con Jorge | Ver sección 3 | 1 |

### Jorge · 12 h

| # | Historia | Tareas | Horas |
|---|---|---|---|
| 1 | **MATU-26** Política de privacidad v0.9 | Redactar `docs/legal/politica-privacidad.md` (1) · publicar `POLITICA_VERSION` en la configuración (0,5) | 1,5 |
| 2 | **MATU-07** Alta de la persona cuidada con consentimiento | Esquemas con rechazo de campos extra (1) · servicio transaccional persona más consentimiento (1,5) · `POST` y `GET /v1/grupos/{id}/personas-cuidadas` (1) · reglas por calidad del otorgante (0,5) · pruebas (2) | 6 |
| 3 | **MATU-03** Puertos y prueba de arquitectura | Puertos `Reloj` y `CustodiaClaves` con sus dobles (1) · `test_arquitectura.py` con caso negativo (1) | 2 |
| 4 | **MATU-27** Figura legal | Revisar opciones y escribir la decisión (1) | 1 |
| 5 | **MATU-28** Anonimizar A55 | Los nombres ya se quitaron el 13 de octubre. Queda decidir qué hacer con las versiones anteriores en el historial público del repositorio (0,5) | 0,5 |
| 6 | **S0-E** Prueba de Transbank, con Martín | Ver sección 3 | 1 |

**Si sobra capacidad**, se adelantan en este orden: **MATU-09** (contrato de API de la ficha y del relevo, Martín) y **MATU-30** (fábricas y lista de lenguaje, Martín). Las dos abren el sprint 2.

**Dependencia dentro del sprint.** Jorge construye MATU-07 contra una sesión simulada en las pruebas mientras Martín termina MATU-02. La integración con el contexto real es el último paso de MATU-07, y ocurre cuando MATU-02 está en `main`. Si el martes 20 MATU-02 no está lista, Jorge avisa en Discord y Martín la prioriza sobre MATU-06.

## 5. Secuencia sugerida

| Día | Martín | Jorge |
|---|---|---|
| Viernes 16 | Planificación (1 h) · S0-A | Planificación (1 h) · MATU-26 |
| Sábado 17 | MATU-04 · MATU-05a | MATU-07: esquemas y servicio |
| Domingo 18 | MATU-05a · inicio MATU-02 | MATU-07: endpoints y reglas |
| Lunes 19 | MATU-02 · S0-E con Jorge | S0-E con Martín · MATU-07: pruebas |
| Martes 20 | MATU-02 en `main` · MATU-06 | MATU-03 |
| Miércoles 21 | MATU-06 · revisión del PR de MATU-07 | Integración de MATU-07 con MATU-02 · MATU-27 · MATU-28 |
| Jueves 22 | Revisión y retrospectiva (1 h) | Revisión y retrospectiva (1 h) |

Jorge revisa los PR de Martín y Martín los de Jorge. **MATU-07 toca datos sensibles: la revisión de Martín es obligatoria** (definición de terminado, punto 5).

## 6. Definición de terminado

Una historia está terminada cuando, y solo cuando:

1. Tiene pruebas de dominio de sus reglas nuevas
2. Tiene al menos una prueba de integración del camino feliz y una del principal camino de error
3. El pipeline pasa completo, incluidas las pruebas de arquitectura y de aislamiento
4. Si toca una pantalla, cumple el checklist de accesibilidad (no aplica en este sprint: no hay pantallas)
5. Si toca dinero o datos sensibles, la revisa la otra persona. Sin excepción
6. Si corrige un defecto, deja una prueba que falla sin la corrección

**Con vibecoding no hay excepciones:** el código generado por el asistente cumple los mismos seis puntos que el escrito a mano.

## 7. Guion de la revisión del sprint

La revisión del jueves 22 muestra el objetivo con este guion, en vivo contra el ambiente local:

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

**Además, en la retrospectiva se calcula el factor de vibecoding** (horas estimadas de lo terminado dividido por horas reales) y se decide con él la planificación del sprint 2, según la sección 2 del calendario.

## 8. Riesgos del sprint

| Riesgo | Probabilidad | Qué se hace |
|---|---|---|
| Jorge tiene menos horas por la práctica | **Alta** | Se confirma en la planificación y se ajusta el compromiso antes de empezar, no a mitad de semana |
| El código generado pasa las pruebas pero no cumple la arquitectura | Media | `test_arquitectura.py` (MATU-03) y la revisión cruzada lo detectan. Por eso MATU-03 va en este sprint |
| La prueba de Transbank vuelve a terminar anulada | Media | Se diagnostica con `poc_estado.py`. Si no se resuelve, el débito ya está respondido y los casos 1, 2, 3 y 5 se cierran en el sprint 2, antes de que importen (sprint 4) |
| El `INSERT … RETURNING` con RLS falla al crear el grupo | Media | Ya está previsto en MATU-06: el identificador se genera en la aplicación |
| MATU-02 se atrasa y bloquea la integración de MATU-07 | Media | Aviso el martes y repriorización sobre MATU-06 |

## 9. Qué deja este sprint para la entrega final (semana 15)

- Primeros endpoints de producto con pruebas, en un pipeline que ya corre en verde
- La suite de aislamiento corriendo contra la API real, no solo contra la base
- El factor de vibecoding medido, con el que se confirma o se ajusta el calendario
- La prueba de concepto de Transbank cerrada con sus cinco casos

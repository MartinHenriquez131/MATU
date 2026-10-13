# MATU — Estrategia de pruebas

**Versión:** 1.1 · septiembre 2026 · sprint 0 · alineada con el backlog v1.2
**Equipo:** Jorge Espinoza · Martín Henríquez
**Documentos asociados:** Arquitectura v1.0, sección 12 · Modelo de datos v1.0 · Backlog sprints 1 a 3
**Estado:** propuesta para aprobar entre los dos en el sprint 0.

---

## 1. El principio

**Un sistema cuyo atributo de calidad número uno es la integridad del pago no puede tener como plan de pruebas una meta de cobertura.** La estrategia apunta las pruebas donde está el riesgo: el dinero, el aislamiento entre familias y el dato de salud. Todo lo demás se prueba en proporción a lo que cuesta que falle.

Tres reglas gobiernan todo el documento:

1. **La testabilidad es una decisión de diseño** (ADR-021). Toda dependencia externa entra por un puerto con un doble determinista. Si algo no se puede probar sin llamar a Transbank, el diseño está mal.
2. **Lo que se afirma sobre el aislamiento se prueba contra PostgreSQL real**, nunca contra un doble. Un doble de base de datos no tiene RLS.
3. **Todo defecto encontrado deja una prueba de regresión.** Un error que se corrige sin prueba vuelve.

---

## 2. Niveles de prueba

| Nivel | Qué cubre | Herramienta | Dónde corre | Tiempo máximo | Meta |
|---|---|---|---|---|---|
| **Unitarias de dominio** | Reglas puras: prorrateo, quiebre, transiciones, validaciones | pytest, Hypothesis | Cada push | 10 s | **85%** de líneas en `modules/*/domain` y `shared` |
| **Integración** | Repositorios, RLS, migraciones, transacciones, cifrado | pytest + PostgreSQL 16 en contenedor | Cada push | 3 min | **70%** en `modules/*/application` |
| **Arquitectura** | Regla de dependencias entre módulos, capa 3 desacoplable | pytest recorriendo importaciones | Cada push | 10 s | Las 4 reglas de la sección 6.4, siempre verdes |
| **Aislamiento** | Qué filas alcanza cada eje de acceso | pytest contra PostgreSQL real | Cada push | 30 s | 100% de las celdas de la matriz de acceso |
| **Contrato de API** | Que el código no rompa el contrato acordado | openapi-diff + schemathesis | Cada push | 2 min | 100% de endpoints |
| **Extremo a extremo** | Los recorridos críticos de punta a punta, contra la API | pytest + httpx + dobles de puertos | Cada push a `main` | 5 min | Los recorridos del sprint, siempre verdes |
| **Interfaz móvil** | Widgets críticos, semántica y escalado de texto | flutter test | Cada push de `mobile/` | 3 min | Flujos del prototipo |
| **Manual con Transbank** | Autorizar, capturar por menos, revertir, tipo de tarjeta | Guion escrito, ambiente de integración | Sprint 0 y un sprint por medio | 1 h | Los casos del guion |
| **Accesibilidad manual** | TalkBack, texto al 200%, contraste en pantalla real | Checklist de la sección 7 | Cada historia con pantalla | 15 min | Checklist completo |
| **Usabilidad** | Tres personas reales, tres perfiles | Guion de tareas | Antes del sprint 10 | 45 min c/u | 3 sesiones |
| **Carga básica** | 50 usuarios concurrentes en el flujo de pedido | k6 | Sprint 12 | 15 min | p95 bajo 800 ms |

**Sobre la cobertura.** La meta es por capa y **ninguna en `infrastructure/`**. Una meta global de 70% se cumple probando adaptadores triviales y dejando sin probar el prorrateo. El pipeline mide `domain` y `application` por separado y falla si alguna baja de su umbral.

---

## 3. Estructura del repositorio de pruebas

```
backend/tests/
├── conftest.py                  fixtures globales: reloj, dobles, base de datos
├── dobles/                      una implementación falsa por puerto
│   ├── pasarela_falsa.py        respuestas programables, incluidas las de falla
│   ├── almacen_en_memoria.py
│   ├── notificador_registrador.py
│   ├── reloj_fijo.py
│   └── custodia_en_memoria.py
├── fabricas/                    constructores de datos sintéticos (factory-boy)
├── unit/                        reglas de dominio, sin base de datos
│   ├── test_prorrateo.py
│   ├── test_quiebre.py
│   └── test_transiciones_pedido.py
├── integration/                 contra PostgreSQL real
├── e2e/                         recorridos críticos contra la API
├── test_arquitectura.py         regla de dependencias
├── test_aislamiento.py          RLS en API y en workers
└── test_capa3_desacoplable.py   la app arranca sin la capa 3
```

`test_aislamiento.py` **ya existe** en `backend/tests/` del repositorio de desarrollo (MATU_PROYECTO), con 31 pruebas en verde. Desde el sprint 0 corre en el pipeline contra la base creada por la migración de Alembic.

---

## 4. Los dobles de los puertos

| Puerto | Implementación real | Doble | Qué permite probar |
|---|---|---|---|
| `PasarelaPago` | `TransbankAdapter` | `PasarelaFalsa` | Rechazo, timeout, retorno duplicado, retorno perdido, débito vs crédito |
| `AlmacenObjetos` | `S3Adapter` | `AlmacenEnMemoria` | Evidencias y exportaciones sin red |
| `Notificador` | `FcmAdapter` | `NotificadorRegistrador` | Que un evento produce exactamente un aviso |
| `Reloj` | `RelojSistema` | `RelojFijo` | Vencimiento de recaudación, del token de relevo y predicción de quiebre |
| `CustodiaClaves` | `KmsAdapter` | `CustodiaEnMemoria` | Cifrado, rotación de KEK y borrado criptográfico |

**`Reloj` es el puerto más importante del sistema para las pruebas.** Sin él no se puede probar ninguna regla que dependa del tiempo, y en MATU casi todas dependen: el quiebre, el relevo, la recaudación, la ventana de 24 horas, las ocurrencias. Toda función de dominio recibe el reloj, nunca llama a `datetime.now()`.

Una prueba de arquitectura verifica que `domain/` no importe `datetime.now`, `time.time` ni ningún SDK externo.

---

## 5. Cómo se escribe una prueba

- **Nombre que dice la regla**, no el método: `test_relevo_vencido_devuelve_410`, no `test_get_relevo_2`.
- **Estructura Dado, Cuando, Entonces**, separada por una línea en blanco.
- **Una regla por prueba.** Si una prueba falla, el nombre ya dice qué se rompió.
- **Datos sintéticos siempre.** Nunca datos reales, ni siquiera anonimizados. Las fábricas generan nombres y direcciones chilenas ficticias.
- **Sin dependencias entre pruebas.** Cada prueba de integración corre en una transacción que se revierte.
- **Las pruebas de propiedades** (Hypothesis) se usan donde hay aritmética: prorrateo y quiebre. Buscan el caso que el equipo no imaginó.

```python
def test_quiebre_con_tasa_fraccionaria_redondea_hacia_abajo(reloj_fijo):
    # Dado un suplemento que se usa uno cada cinco días, con 3 en stock
    perfil = PerfilConsumo(tasa_unidades=1, tasa_dias=5, stock_unidades=3,
                           stock_medido_en=date(2026, 9, 14))

    # Cuando se calcula la fecha de quiebre
    fecha = calcular_quiebre(perfil)

    # Entonces alcanza para 15 días exactos
    assert fecha == date(2026, 9, 29)
```

---

## 6. Pruebas obligatorias por área de riesgo

### 6.1 Aislamiento y privacidad

Las diez de la sección 12.5 de la arquitectura, más las que agregó el modelo de datos:

| # | Caso | Resultado esperado | Estado |
|---|---|---|---|
| 1 | Usuario del grupo A pide una persona cuidada del grupo B | 404, nunca 403 | Sprint 1 (MATU-07) |
| 2 | Consulta sin `app.grupo_id` | Cero filas en toda tabla de negocio | **Prototipo en verde** |
| 3 | Job del worker sin contexto | Cero filas | **Prototipo en verde** |
| 4 | Repartidor pide el plan de cuidado | 404, el router no está montado | Sprint 10, cuando exista el eje repartidor |
| 5 | Respuesta al repartidor | Sin campos del plan ni del consumo | Sprint 10 |
| 6 | Token de relevo vencido | 410 y apertura auditada como intento | Sprint 3 (MATU-19) |
| 7 | Relevo con dos secciones | Exactamente esas dos | **Prototipo en verde** |
| 8 | Plan sin consentimiento vigente | 403 con motivo | Sprint 2 (MATU-12) |
| 9 | `idempotencia` de otro grupo | Cero filas | **Prototipo en verde** |
| 10 | Escritura tras borrado criptográfico | Error de dominio explícito | **Prototipo en verde** (restricción) + sprint 2 (servicio) |
| 11 | El relevo no hereda nada de la familia | Cero filas en pedidos, pagos, direcciones | **Prototipo en verde** |
| 12 | Observador y pagador sin permiso piden el plan | Cero filas | **Prototipo en verde** |
| 13 | Operación pide plan o consumo | Cero filas | **Prototipo en verde** |
| 14 | `FORCE` activo tabla por tabla | Toda tabla de negocio | **Prototipo en verde** |
| 15 | El outbox rechaza un payload con datos | Violación de `CHECK` | **Prototipo en verde** |

### 6.2 Pagos

Los doce casos de la sección 12.4 de la arquitectura, sin cambios. Casos 1 a 6 y 12 en el sprint 8, casos 7 a 11 en el sprint 9. El caso 11 es una **prueba de propiedad sobre 300 casos generados**: para cualquier total y cualquier reparto, la suma capturada es exacta al peso, nadie captura más de lo autorizado, y la prueba falla si se invierte el criterio del mayor resto.

### 6.3 Máquinas de estado

Una prueba parametrizada recorre las **400 combinaciones** de los 20 estados del pedido y las **64** de los 8 estados del cargo. Toda transición no declarada lanza `TransicionInvalida`. Dos pruebas más verifican que todo estado es alcanzable desde `borrador` y que ningún estado no terminal queda sin salida.

### 6.4 Capa 1 · Plan de cuidado

| Caso | Nivel |
|---|---|
| Cifrar y descifrar una sección devuelve el texto original | Unitaria |
| Dos escrituras de la misma sección usan nonces distintos | Unitaria |
| Un texto cifrado alterado falla la verificación del tag | Unitaria |
| Mover un texto cifrado a otra sección o a otro plan falla al descifrar (AAD = `plan_id ‖ tipo`) | Unitaria |
| Editar con un `If-Match` desactualizado devuelve 412 con el contenido actual | Integración |
| Rotar la KEK no cambia el texto de ninguna sección | Integración |
| La ficha de relevo con 1 de 3 secciones ya permite generar un acceso | Integración |
| El PIN falla 5 veces y el acceso responde 423 | Integración |
| Guardar sin `If-Match` sobre un campo existente responde 428 | Integración |
| Revocar un acceso lo invalida en la petición siguiente | Integración |
| Ninguna línea de log contiene texto del plan | Integración, capturando los logs |

### 6.5 Capa 2 · Consumo

Ocho pruebas de dominio sobre el cálculo del quiebre (sección 7.3 de la arquitectura), incluida la regresión del ancla en `stock_medido_en`. Una prueba de propiedad: para cualquier tasa y stock, la fecha de quiebre nunca es anterior a la medición y nunca es posterior al cálculo con división exacta.

---

## 7. Accesibilidad

Todo criterio de la sección 10.3 de la arquitectura tiene cómo verificarse:

| Criterio | Automático | Manual |
|---|---|---|
| Área táctil de 48 × 48 dp | Prueba de widget que mide los controles | — |
| Texto escalable al 200% sin pérdida | Prueba de widget con `textScaleFactor = 2.0` sin desbordes | Revisión en un teléfono real |
| Contraste 4,5:1 | Script del pipeline sobre los tokens de color | — |
| Nunca solo color | — | Checklist por pantalla |
| Etiqueta semántica en todo control | Prueba de widget que recorre el árbol de semántica | TalkBack en el flujo principal |
| Lenguaje sin jerga | — | Revisión cruzada con la lista de palabras de las entrevistas |

**Dos hallazgos de las entrevistas entran a este checklist.** Primero, lenguaje de dignidad: la incontinencia y el aseo se nombran como los nombró la gente, no en términos clínicos. Segundo, el encuadre de "instructivo" y no de "expediente": ningún texto de la interfaz sugiere que se lleva un registro del deterioro de la persona.

---

## 8. Integración continua

El pipeline de la sección 12.7 de la arquitectura, con estas puertas. Un pull request no se puede fusionar si falla cualquiera:

| Puerta | Falla si |
|---|---|
| `ruff check` y `ruff format --check` | Hay errores de estilo o formato |
| `mypy app/` | Hay errores de tipos |
| Unitarias con cobertura | `domain` baja de 85% |
| Integración con cobertura | `application` baja de 70% |
| `test_arquitectura.py` | Alguna importación cruza una regla de dependencia |
| `test_aislamiento.py` | Algún eje alcanza una fila que no debe |
| `test_capa3_desacoplable.py` | La app no arranca sin la capa 3 (desde el sprint 3) |
| openapi-diff | El código rompe el contrato versionado |
| `alembic upgrade`, `downgrade -1`, `upgrade` | Una migración no es reversible |
| `detect-secrets` y `pip-audit` | Hay un secreto o una dependencia con vulnerabilidad conocida |

**Pruebas inestables.** Una prueba que falla de forma intermitente se marca `@pytest.mark.flaky` con un issue asociado y tiene **un sprint** para arreglarse o eliminarse. Una prueba inestable que se tolera enseña a ignorar el pipeline.

---

## 9. Datos de prueba

- **Local y CI:** datos sintéticos generados por las fábricas. Se crean y se revierten en cada prueba.
- **Staging y demostración:** semilla sintética verosímil, versionada en `infra/semillas/`. Catálogo con los productos que más aparecieron en los quiebres de las entrevistas.
- **Nunca** se copian datos de producción a otro ambiente, ni anonimizados. El plan de cuidado es dato sensible bajo la Ley 21.719.
- **Las entrevistas no son datos de prueba.** Sus hallazgos informan el diseño, sus registros no entran al repositorio.

---

## 10. Prueba de concepto de Transbank · sprint 0

Es la prueba manual más importante del proyecto: si falla, caen juntos el ADR-006 y el ADR-007.

| # | Caso | Cómo | Resultado esperado | Si falla |
|---|---|---|---|---|
| 1 | Autorizar y capturar el mismo monto | Webpay Plus diferido, tarjeta de prueba de crédito | Captura aprobada | Revisar la integración |
| 2 | Autorizar $69.000 y capturar $51.340 | Captura parcial | Se cobra $51.340 y se libera el resto | **Cae el ADR-006.** Plan B: cobro exacto y reembolso |
| 3 | Autorizar y revertir sin capturar | Reversa | Autorización anulada, nada cobrado | **Cae el ADR-007** |
| 4 | Autorización diferida con tarjeta de **débito** | Tarjeta de prueba de débito | Registrar qué pasa | Si no admite diferido: rechazar débito en el flujo con reparto y decirlo en la interfaz (sección 17) |
| 5 | Retorno de pasarela recibido dos veces | Repetir el `commit` con el mismo token | Un solo cobro | Revisar la idempotencia |

**Se registra** cada caso con fecha, monto, código de respuesta y captura de pantalla en `docs/pruebas-concepto/transbank.md`. El resultado real reemplaza a la afirmación del proveedor en la sección 18.1 de la arquitectura.

---

## 11. Pruebas de usabilidad · antes del sprint 10

Tres personas reales, de tres perfiles distintos: una cuidadora conviviente, un familiar que aporta y una cuidadora remunerada. Tareas cronometradas:

1. Completar la ficha de relevo (meta: menos de 3 minutos, ADR-023)
2. Generar un acceso de relevo y compartirlo (meta: menos de 2 minutos)
3. Declarar el consumo de dos productos (meta: menos de 3 minutos)
4. Armar un pedido desde la lista de reposición (meta del atributo de calidad 3: primer pedido en menos de 6 minutos)

Se aplica el mismo encuadre ético del protocolo de entrevistas: sin grabación, consentimiento verbal, sin datos identificatorios. **No se recluta en la red personal del equipo**, que es el sesgo que tuvo la ronda de entrevistas.

---

## 12. Definición de terminado

Una historia está terminada cuando, y solo cuando:

1. Tiene pruebas de dominio de sus reglas nuevas
2. Tiene al menos una prueba de integración del camino feliz y una del principal camino de error
3. El pipeline pasa completo, incluidas las pruebas de arquitectura y de aislamiento
4. Si toca una pantalla, cumple el checklist de accesibilidad de la sección 7
5. Si toca dinero o datos sensibles, la revisa la otra persona del equipo. Sin excepción
6. Si corrige un defecto, deja una prueba que falla sin la corrección

El punto 6 es nuevo respecto de la arquitectura y formaliza la regla 3 de la sección 1.

---

## 13. Entregables de prueba por sprint

| Sprint | Entregable de prueba |
|---|---|
| 0 | Esta estrategia · prueba de concepto de Transbank (parcial) · `test_aislamiento.py` conectado a Alembic y en verde en el pipeline |
| 1 | Casos pendientes de la prueba de Transbank · `test_arquitectura.py` que no pasa en vacío · dobles de `Reloj` y `CustodiaClaves` · pruebas de identidad, grupo, persona cuidada y consentimiento |
| 2 | Pruebas de cifrado con AAD, ficha, concurrencia optimista (412 y 428) y auditoría · fábricas de datos sintéticos |
| 3 | Pruebas del relevo completo (410, 423, sesión sin grupo) · e2e `test_recorrido_relevo` en staging |
| 4 | `test_capa3_desacoplable.py` · pruebas de widget con accesibilidad · prueba en un dispositivo real de gama baja · refresh rotativo |
| 5 | Las ocho pruebas del quiebre + propiedad · doble de `Notificador` · consumidor del outbox idempotente |
| 8 | Casos de pago 1 a 6 y 12 |
| 9 | Casos de pago 7 a 11 + propiedad del prorrateo |
| 10 | Usabilidad con tres personas |
| 12 | Carga con k6 · revisión final de la matriz de trazabilidad |

---

## 14. Trazabilidad

Cada historia del backlog lista los requisitos (RF) que cubre y cada prueba se etiqueta con el requisito que verifica (`@pytest.mark.rf("RF-05")`). Al cierre de cada sprint un script lista los requisitos *Debe* sin ninguna prueba asociada. **Un requisito comprometido sin prueba no está terminado**, aunque la pantalla funcione.

---

*Estrategia de pruebas MATU · versión 1.0 · septiembre 2026 · Jorge Espinoza y Martín Henríquez*

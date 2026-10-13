# MATU · Calendario de sprints · v1.3

**Vigente desde:** 13 de octubre de 2026
**Reemplaza:** las fechas y la agrupación de la tabla 15.4 de la arquitectura v1.1. El alcance comprometido (sección 15.3) y el orden de sacrificio no cambian.

---

## 1. Por qué cambia

1. **El desarrollo empieza tres semanas después de lo planificado.** La arquitectura ubicaba el sprint 1 en la semana 8. El sprint 0 se extendió hasta la semana 10 mientras se acordaba con el profesor el entorno y las herramientas de desarrollo. La entrega final de la Fase 2 sigue en la semana 15.
2. **Los sprints parten el viernes y terminan el jueves siguiente.** El jueves se hacen la revisión y la retrospectiva, y el viernes la planificación del sprint que empieza.
3. **El equipo desarrolla con asistencia de IA (vibecoding).** Un asistente genera código, pruebas y documentación a partir de instrucciones del equipo, y el equipo revisa, corrige y decide. Eso acelera la implementación, que es la mayor parte de las horas estimadas, y permite agrupar en cinco sprints el alcance que la v1.1 repartía en ocho.

## 2. El supuesto de vibecoding

| | Backlog v1.2 | Calendario v1.3 |
|---|---|---|
| Capacidad real por sprint | 23 h (11 h Jorge, 12 h Martín) | **23 h**, sin cambio |
| Horas estimadas que caben en un sprint | 23 h | **Hasta 41 h** de las estimaciones originales (factor 1,8) |
| Estimaciones del backlog | Horas reales sin asistencia | **Se mantienen.** El factor se aplica al comprometer, no a cada historia |

**El factor 1,8 es una hipótesis, no un dato.** Se mide en el sprint 1: horas estimadas de las historias terminadas divididas por las horas reales usadas.

- **Si el factor real es 1,4 o más**, el calendario se mantiene.
- **Si queda bajo 1,4**, antes de planificar el sprint 2 se aplica el orden de sacrificio de la sección 5, no a mitad de camino.

**Lo que el vibecoding no cambia:**

- **La definición de terminado se aplica completa.** El código generado se revisa como cualquier pull request, y lo que toca datos sensibles, aislamiento o dinero lo revisa siempre la otra persona.
- **Las pruebas de las reglas críticas las define una persona.** El asistente puede escribirlas, pero el caso que se prueba (RLS, cifrado, captura por monto real) lo decide el equipo y lo contrasta con la estrategia de pruebas.
- **Nunca se ponen datos reales ni secretos en las instrucciones al asistente.** Solo datos sintéticos, como exigen la Ley 21.719 y la sección 9 de la estrategia de pruebas.

## 3. Calendario

| Sprint | Fechas | Semanas del ramo | Objetivo | Agrupa (tabla 15.4) | Hito del ramo |
|---|---|---|---|---|---|
| 0 | 21 sep – 15 oct | 7 a 10 | Preparación | 0 | **Semana 10:** entrega de avance (2.3 y 2.4) |
| **1** | **vie 16 – jue 22 oct** | 10 y 11 | Identidad y grupo, y cierre de la prueba de Transbank | 1 | |
| **2** | **vie 23 – jue 29 oct** | 11 y 12 | Ficha de relevo y acceso de relevo: **primer producto de punta a punta** | 2 y 3 | |
| **3** | **vie 30 oct – jue 5 nov** | 12 y 13 | App de familia y perfil de consumo con predicción | 4 y 5 | |
| **4** | **vie 6 – jue 12 nov** | 13 y 14 | Catálogo, lista de reposición, pedido y pago | 6 y 7 | |
| **5** | **vie 13 – jue 19 nov** | 14 y 15 | Cierre: endurecimiento, despliegue y guion de demostración | 8 | **Semana 15 (16 a 21 nov):** entrega final de la Fase 2 (2.6) |
| 6 | vie 20 – jue 26 nov | 15 y 16 | **Reserva:** ajustes por la retroalimentación | | Semana 16: retroalimentación |
| 7 | vie 27 nov – jue 3 dic | 16 y 17 | **Reserva:** preparación de la presentación | | Semanas 17 y 18: presentación final (Fase 3) |

**El sprint 5 se cruza con la entrega final.** La presentación de la semana 15 puede caer antes del jueves 19. Por eso el guion de demostración y el informe final quedan listos el **lunes 16 de noviembre**, y el resto del sprint es solo corrección.

**Los sprints 6 y 7 no tienen alcance comprometido.** Son la reserva que en la v1.1 era el 21% de holgura. Si no se usan, se dedican a pulir y a preparar la presentación.

## 4. Qué entra en cada sprint

| Sprint | Historias | Horas estimadas |
|---|---|---|
| 1 | Pendientes del sprint 0 (esqueleto de la API y prueba de Transbank) y las 9 historias del sprint 1 del backlog v1.3 | 26 h comprometidas, más MATU-09 y MATU-30 si sobra capacidad |
| 2 | Las 7 historias del sprint 2 del backlog v1.3 (ficha) y 4 del sprint 3 (relevo): MATU-18, 19, 20 y 23 | 39,5 h |
| 3 | MATU-25 (staging) y las historias de la app de familia y del perfil de consumo | Se refina en la revisión del sprint 2 |
| 4 | Catálogo, lista, pedido con un solo pagador y vista de comercio | Se refina en la revisión del sprint 3 |
| 5 | Cierre de la tabla 15.4 | Se refina en la revisión del sprint 4 |

El sprint 1 se deja liviano a propósito: es el que mide el factor real. Si termina antes, se adelantan MATU-09 (contrato de API) y MATU-30 (fábricas y lista de lenguaje), que abren el sprint 2.

## 5. Qué se cae primero

El orden de la arquitectura (sección 15.4) y del backlog (sección 7) se mantiene:

1. Los indicadores del backoffice
2. La vista de comercio automatizada, que se puede operar a mano en la demostración
3. El catálogo curado, que se reduce a diez productos
4. El staging (MATU-25) se reemplaza por un túnel HTTPS temporal para la demostración

**Nunca se sacrifican** la ficha de relevo, el acceso de relevo, la predicción de quiebre ni la exportación de la lista. Son el producto.

# Usabilidad · Ronda 1 con el prototipo de pruebas (MATU-34)

**Fecha:** 07, 09 y 10 de noviembre de 2026 · **Condujo:** Martín Henríquez · **Revisa:** Jorge Espinoza
**Guion:** [estrategia de pruebas, sección 11](../estrategia-pruebas.md), más las tareas de la tarjeta MATU-34 · **Prototipo:** `docs/prototipo/prototipo-pruebas.html`, en el teléfono del equipo
**Resultado:** las 3 personas completaron las 5 tareas. **La ficha no bajó de 3 minutos en 2 de 3 sesiones**, y compartir con PIN tampoco bajó de 2 minutos en 2 de 3. Ningún hallazgo bloquea, y hay 3 P2 para las pantallas de la app.

## Participantes

Sin nombres. Consentimiento verbal en las tres, sin grabación y solo con datos de prueba.

| Código | Perfil | Llegó por | Sesión |
|---|---|---|---|
| P01 | Cuidadora conviviente, 7 años a cargo de su padre | Amigos de la familia | 07/11, 17:38 a 18:09 |
| P02 | Hija, cuidadora de medio tiempo, cuida junto a su padre | Conocido de una vecina | 09/11, 22:13 a 22:40 |
| P03 | Familiar cuidadora joven, con mucho manejo del celular | Vecino del equipo | 10/11, 14:30 a 15:04 |

## Tiempos por tarea (minutos:segundos)

| Tarea | Meta | P01 | P02 | P03 | ¿Cumple? |
|---|---|---|---|---|---|
| 1 · Completar la ficha | < 3:00 sin ayuda | 3:30, con guía leve | 3:15, con ayuda leve | 2:45, sin ayuda | **1 de 3** |
| 2 · Compartir con PIN | < 2:00 | 2:30 | 2:20 | 1:30 | **1 de 3** |
| 3 · Declarar insumos y consumo | < 3:00 | 2:20 | 2:10 | 1:30 | 3 de 3 |
| 4 · Armar un pedido desde la alerta | < 6:00 | 3:00 | 2:40 | 1:45 | 3 de 3 |
| 5 · Abrir la ficha como relevo con el PIN (opcional) | — | 1:20 | 1:10 | 1:20 | — |

## Hallazgos

| ID | Prioridad | Hallazgo | Evidencia | Propuesta (decide Jorge) |
|---|---|---|---|---|
| U1 | P2 | La ficha toma más de 3 minutos a quien no tiene la rutina escrita: necesitó guía para redactarla y entender los campos | P01 3:30, P02 3:15; P03 2:45 | Revisar en la app la pregunta guía de cada campo y un ejemplo breve **en la pantalla de quien escribe** (no en la hoja del relevo, decisión de MATU-64). Medir otra vez en MATU-65 |
| U2 | P2 | Compartir con PIN toma más de 2 minutos: el botón para generar el acceso no se encuentra a la primera, y se busca compartir directo por WhatsApp | P01 2:30, P02 2:20 y buscó WhatsApp | Verificar en la app que el botón esté a la vista en la ficha y que el enlace se pueda mandar por WhatsApp. El PIN va aparte, nunca en el mismo mensaje |
| U3 | P2 | Declarar cuánto se usa cuesta a quien controla el stock «a la vista», sin registros | P01 confusión con cantidades; P02: «tenemos todo guardado en una repisa y ahí vamos revisando el stock» | Permitir declarar lo que queda con unidades simples (paquetes) y explicar que es aproximado. Revisarlo con MATU-60 y MATU-68 |
| U4 | P3 | Ajustar la cantidad de un producto en el pedido costó con las toallitas | P02, tarea 4 | Revisar el control de cantidad en el pedido (MATU-61) |
| U5 | P3 (a favor) | La pantalla de quién vio la ficha da confianza, y la privacidad importa | P01: «me interesa saber quién tiene acceso a los datos del plan de cuidado»; P03: «pondría solamente lo necesario» | Mantenerla visible. Respalda que las secciones sean opcionales (ADR-028) |

Lo que más piden, en sus palabras: que avise cuando se acaban los productos y que se pueda compartir fácil con quien ayuda (P01 y P03). Es justo lo que hacen las capas 1 y 2.

## Limitaciones

- **Reclutamiento:** las tres personas llegaron por la red personal del equipo o de su familia, y la estrategia (sección 11) pide no reclutar ahí. Pueden ser más benevolentes.
- **Perfiles:** son tres familiares cuidadoras. Faltan un familiar que aporta y una cuidadora remunerada. **Se buscan para MATU-65.**
- **Prototipo, no la app:** los tiempos son del prototipo de pruebas. La ronda 2 (MATU-65) mide lo mismo en la app.

## Para MATU-65

- Reclutar fuera de la red personal, con los dos perfiles que faltan.
- Medir de nuevo las tareas 1 y 2 con las metas de 3 y 2 minutos.

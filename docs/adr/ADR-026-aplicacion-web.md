# ADR-026 · La aplicación de la familia es web, mobile first

**Estado:** Aceptado
**Fecha de decisión:** 14 de octubre de 2026, en la reunión de avance con el profesor guía, que la sugirió. Se registra por escrito el 28 de octubre
**Decisores:** Jorge Espinoza (Product Owner) · Martín Henríquez (Scrum Master)
**Reemplaza:** el ADR-005 (Flutter con un repositorio y dos aplicaciones) durante el semestre

---

## Contexto

El ADR-005 eligió Flutter con un paquete `core` compartido entre la app de familia y la app de repartidor. Su única razón era la app de repartidor, que necesita ubicación en segundo plano y cámara. Desde el primer recorte, la app de repartidor quedó fuera del alcance comprometido, y el propio ADR-005 lo dejó escrito: **"si el proyecto continuara sin app de repartidor, React Native sería la elección correcta"**.

Al llegar a la Fase 2 se sumaron tres hechos:

- **La ventana de construcción es de nueve semanas** y el equipo es de dos personas sin dedicación completa. Aprender Dart y Flutter es un costo que la arquitectura v1.1 reconoce en la tabla de riesgos y en las tallas.
- **El equipo ya construye en React con TypeScript.** La arquitectura ya preveía `web/` para el backoffice, la vista de comercio y la página del relevo (anexo 19.1). Flutter sumaba un tercer lenguaje y un segundo cliente.
- **Publicar una app nativa** exige decidir entre iOS y Android, cuentas de desarrollador y revisión de las tiendas. Nada de eso aporta a lo que se evalúa en el semestre.

## Decisión

**En el semestre, la aplicación de la familia se construye como aplicación web mobile first**, en el mismo cliente web que ya tenía la página del relevo.

- **React 19 con TypeScript**, inicializado con Vite. **Tailwind CSS v4**, con los tokens del sistema de diseño. Iconos de `lucide-react`.
- **Mobile first:** cada pantalla se diseña primero para un teléfono de 360 px de ancho y después se amplía.
- **La API sirve la aplicación desde el mismo origen**, sin CORS.
- **Cliente HTTP tipado desde el contrato OpenAPI** (`docs/api/`).

**MATU sigue siendo una app móvil en su visión.** La web es el paso práctico del semestre: corre en el navegador del teléfono, sin instalar nada. **La app nativa se decide en una etapa posterior**, con lo que se aprenda en el piloto.

## Por qué

- **Un solo lenguaje para todo el frontend.** Familia, relevo, comercio y backoffice comparten componentes, tokens y cliente de la API.
- **Accesibilidad que se hereda.** El HTML sí tiene el árbol de accesibilidad del navegador, y los lectores de pantalla lo leen sin una capa de semántica propia, que en Flutter había que construir y probar a mano (ADR-005). Los criterios de la sección 10.3 se siguen verificando igual.
- **Se puede probar desde el primer día** en cualquier teléfono, con un enlace. Sirve para la usabilidad y para la demostración.
- **Ya se probó.** La demo del 30 de octubre (`MATU_PROYECTO/Demo/`) está hecha con este mismo stack, y pasó la revisión de diseño y de QA, incluido el reflujo sin desplazamiento horizontal a 320 px con el texto al 200%.

## Consecuencias

**Lo que cambia en el producto:**

- **Avisos push.** En Android, el push web funciona desde el navegador. En iPhone solo funciona si la persona agrega MATU a la pantalla de inicio. **El correo queda como canal garantizado** de los avisos de quiebre (RF-39), y el push como complemento. Lo precisa la tarjeta de avisos del sprint 3.
- **Dictado por voz.** Lo da el teclado del teléfono en cualquier campo de texto, sin código propio. El criterio de la sección 10.3 se mantiene.
- **Sin tiendas de aplicaciones.** No hay revisión de Apple ni de Google, ni cuentas de desarrollador.
- **La app de repartidor y el ADR-025** siguen fuera del semestre. Si vuelven, la decisión nativa se toma entonces.

**Lo que cambia en la arquitectura v1.1** (se lleva a la v1.2 en el sprint 3, tarjeta "Actualizar la arquitectura a la v1.2"):

| Lugar | Hoy dice | Pasa a decir |
|---|---|---|
| Sección 1, decisión 5 | Un repositorio Flutter con dos aplicaciones | Una aplicación web mobile first, React con TypeScript |
| Sección 6.1, diagrama | App Familia · Flutter · iOS y Android | App Familia · web mobile first, en el navegador del teléfono |
| Sección 6.1, nota del repartidor | El paquete Flutter compartido se mantiene | La app nativa se decide después del semestre |
| Sección 12.2, nivel de interfaz | flutter test | Pruebas de componentes web, con la herramienta que se fije en la v1.2, y revisión manual con el checklist de accesibilidad |
| Sección 15, tallas y holgura | Incluyen aprender Flutter | Sin el costo de un lenguaje nuevo |
| Sección 15.5 | El `core` de Flutter se construye en conjunto | Los componentes base de `web/` se construyen en conjunto |
| Sección 17, riesgos | El equipo no domina Dart | Se retira. Entra: el push web en iPhone exige agregar la app a la pantalla de inicio |
| Anexo 19.1 | `mobile/` con `packages/core` y `apps/familia` | Sin `mobile/`. `web/` tiene familia, relevo, comercio y backoffice |
| ADR-005 | Vigente | Reemplazado por este ADR durante el semestre |

**Lo que cambia fuera de la arquitectura:**

- **Estrategia de pruebas, sección 2:** el nivel "Interfaz móvil" con `flutter test` pasa a la interfaz web.
- **README de los dos repositorios:** la fila "Aplicación móvil · Flutter".
- **Trello:** la tarjeta del sprint 3 "App de familia: núcleo, autenticación y ficha de relevo en móvil" todavía habla del `core` de Flutter.

## Lo que esta decisión no resuelve

- **Si la app nativa futura será Flutter, React Native o una app web instalable.** Se decide con los datos del piloto. Con la experiencia del semestre en React, React Native sería el camino más corto, como ya anticipaba el ADR-005.
- **Las evidencias de la Fase 1** dicen Flutter (informe 1.4, guía 1.5 y ficha del proyecto). Son evidencias entregadas y no se modifican. El cambio se explica en las de la Fase 2.

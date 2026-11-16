# MATU · Guion de la presentación final ante la comisión

**Duración:** 10 minutos (600 segundos).
**Orden:**
1. Jorge abre.
2. Martín sigue.
3. Jorge muestra la ficha en la demo.
4. Martín muestra las capas 2 y 3.
5. Jorge cuenta los próximos pasos de MATU.
6. Martín cierra.

**Borrador del orquestador · 16 de noviembre de 2026.** Jorge y Martín lo ajustan en los ensayos (MATU-111).

**Estructura:** sigue la de la presentación de la Fase 2 (`Fase 2/Evidencias Proyecto/MATU_Presentacion_Fase2.pptx`), que a su vez ordenó la de la Fase 1. Son las mismas láminas, en el mismo orden y con la misma forma de nota: **quién habla, cuánto dura, en qué minuto termina y el texto dicho.** El contenido cambia porque cuenta el proyecto terminado: lo que se cumplió, lo que se construyó y lo que viene. Cada nota se puede pegar tal cual en las notas del orador de su lámina.

**Las cifras marcadas con `[VERIFICAR]`** hay que contrastarlas con la parte técnica de la Fase 3 (MATU#99) antes del primer ensayo.

---

## Resumen de tiempos

| Lámina | Título | Habla | Dura | Termina |
|---|---|---|---|---|
| 1 | Portada | Jorge | 10 s | 0:10 |
| 2 | Equipo | Jorge | 15 s | 0:25 |
| 3 | Contexto · problema y propuesta | Jorge | 40 s | 1:05 |
| 4 | Objetivo general | Jorge | 15 s | 1:20 |
| 5 | Objetivos específicos | Martín | 30 s | 1:50 |
| 6 | Alcance | Martín | 20 s | 2:10 |
| 7 | Requerimientos | Martín | 15 s | 2:25 |
| 8 | Metodología y validación | Martín | 25 s | 2:50 |
| 9 | Cronograma | Martín | 20 s | 3:10 |
| 10 | Tecnologías y herramientas | Martín | 10 s | 3:20 |
| 11 | Arquitectura de la aplicación | Martín | 20 s | 3:40 |
| 12 | Modelo de datos y seguridad | Martín | 15 s | 3:55 |
| 13 | Modelo de negocio | Martín | 15 s | 4:10 |
| 14 | Demostración · Capa 1, la ficha de relevo | Jorge | 1 min 50 s | 6:00 |
| 15 | Demostración · Capas 2 y 3, insumos y despacho | Martín | 2 min 15 s | 8:15 |
| 16 | Próximos pasos de MATU | Jorge | 45 s | 9:00 |
| 17 | Conclusión | Martín | 45 s | 9:45 |
| 18 | Gracias | Martín | 15 s | 10:00 |

**Respecto de la Fase 2:**
- La demostración pasa de una lámina a dos, una para cada uno.
- «Mejoras futuras» pasa a llamarse «Próximos pasos de MATU», y la presenta Jorge.
- La validación con usuarios entra en «Metodología», con las dos rondas de usabilidad.

---

## Notas por lámina

### Lámina 1 · Portada
**Habla Jorge · 10 s · al terminar 0:10.**
Buenas tardes. Somos Jorge Espinoza y Martín Henríquez, y les presentamos el resultado final de MATU, un sistema de continuidad del cuidado para personas mayores con dependencia.

### Lámina 2 · Equipo
**Habla Jorge · 15 s · al terminar 0:25.**
Yo soy el Product Owner y desarrollé MATU con un equipo de seis agentes de IA. Martín es el Scrum Master. Él revisó cada cambio, lo desplegó y lo probó en un teléfono real antes de fusionarlo. Los agentes proponen, y nosotros decidimos.

### Lámina 3 · Contexto · problema y propuesta
**Habla Jorge · 40 s · al terminar 1:05.**
En Chile, casi un millón y medio de personas adultas viven con dependencia, y el 96,4% de quienes las cuidan en el hogar no recibe pago. Entrevistamos a diez cuidadoras: nueve de cada diez habían dejado de salir por falta de alguien que las reemplazara, y cuando las reemplazaban, el relevo fallaba por algo que solo sabía ella. Ese conocimiento vive en una sola cabeza. MATU lo saca de ahí, en tres capas y en este orden: la ficha de relevo, que es el producto; la predicción de cuándo se acaba cada insumo, que es lo que nos diferencia; y el despacho, que es un servicio y se puede quitar sin que lo demás deje de funcionar.

### Lámina 4 · Objetivo general
**Habla Jorge · 15 s · al terminar 1:20 · pasa la palabra a Martín.**
Nos comprometimos a construir una plataforma que convierta el cuidado de una persona mayor en una ficha que se puede traspasar, y en una predicción de sus insumos con su reposición. Hoy está desplegada y funcionando. Martín les cuenta cómo llegamos.

### Lámina 5 · Objetivos específicos
**Habla Martín, recibe la palabra de Jorge · 30 s · al terminar 1:50.**
Gracias, Jorge. Teníamos siete objetivos, y seis están cumplidos. Tres cambiaron su redacción por decisiones que tomamos en el camino. La lista de reposición se exporta sin enlace. El pago es un solo cobro del total exacto, en vez de reservar un monto y cobrarlo después. Y fijamos seis recorridos críticos. El séptimo objetivo es que esos seis recorridos corran solos en cada cambio. Ya pasaron todos en un teléfono real, y estamos terminando de automatizarlos `[VERIFICAR: estado de MATU-80 el día de la presentación]`.

### Lámina 6 · Alcance
**Habla Martín · 20 s · al terminar 2:10.**
Construimos lo que nunca se sacrifica: la ficha, el acceso del relevo, la predicción de quiebre y la exportación de la lista. Lo que dejamos fuera del semestre está diseñado y tiene sus tablas en la base de datos: el pago dividido entre familiares, el prorrateo, la reposición programada, la app de repartidor y la liquidación automática.

### Lámina 7 · Requerimientos
**Habla Martín · 15 s · al terminar 2:25.**
De los requerimientos funcionales, cumplimos todos los obligatorios `[VERIFICAR: cuántos de 42]`. En los no funcionales pesan tres: el aislamiento entre familias, el cifrado de la ficha y la accesibilidad, con texto que se puede agrandar al doble sin perder nada en la pantalla de un teléfono.

### Lámina 8 · Metodología y validación
**Habla Martín · 25 s · al terminar 2:50.**
Usamos Scrum con sprints de una semana. Cada historia va en su rama, con pruebas junto al código, y no se fusiona sin el CI en verde y sin la revisión de la otra persona. Validamos con usuarias en dos rondas de usabilidad. En la segunda, las tres participantes completaron la ficha en menos de tres minutos sin ayuda, cuando en la primera lo había logrado solo una de tres.

### Lámina 9 · Cronograma
**Habla Martín · 20 s · al terminar 3:10.**
Cerramos cinco sprints de construcción. Medimos el factor de vibecoding con las horas reales anotadas en cada tarjeta: 1,98. Es decir, cada hora de trabajo de Jorge rindió lo que habíamos estimado en casi dos. Suponíamos 1,8, y el mínimo aceptable era 1,4.

### Lámina 10 · Tecnologías y herramientas
**Habla Martín · 10 s · al terminar 3:20.**
Usamos tecnología conocida y documentada: Python con FastAPI, PostgreSQL y Redis en el backend, React con TypeScript en la app, y despliegue en Railway con dos entornos, uno de pruebas y otro de demostración.

### Lámina 11 · Arquitectura de la aplicación
**Habla Martín · 20 s · al terminar 3:40.**
Es un monolito modular: una sola API, con módulos que solo dependen hacia abajo, y una prueba automática que lo verifica en cada cambio. La capa de despacho se puede apagar, y probamos que la ficha y la predicción siguen funcionando sin ella.

### Lámina 12 · Modelo de datos y seguridad
**Habla Martín · 15 s · al terminar 3:55.**
Todo cuelga del grupo familiar. La base de datos aísla a cada familia por fila, así que una consulta sin contexto no devuelve nada. La ficha se guarda cifrada con una clave por persona, y el comercio nunca ve el nombre ni la dirección de la familia.

### Lámina 13 · Modelo de negocio
**Habla Martín · 15 s · al terminar 4:10 · pasa la palabra a Jorge.**
El modelo se sostiene con suscripción más despacho, y el equilibrio llega con 84 familias `[VERIFICAR: cifra vigente del modelo de negocio]`. Ahora Jorge les muestra la ficha funcionando.

### Lámina 14 · Demostración · Capa 1, la ficha de relevo
**Habla Jorge, recibe la palabra de Martín · demo de 1 min 50 s · al terminar 6:00.**
Esto es MATU en vivo, en el entorno de demostración y con datos de prueba. Entro como Carmen, que cuida a su madre.

- **(25 s) La ficha.** Estos son los tres campos: su día, qué hacer si se altera y a quién llamar. Carmen los llenó en menos de tres minutos.
- **(35 s) Compartir con un relevo.** Carmen crea un enlace para quien la reemplaza este sábado. El enlace vence solo, y el PIN se entrega por separado.
- **(30 s) En el teléfono del relevo.** Quien la reemplaza lo abre sin cuenta y sin instalar nada: el enlace y el PIN bastan. Ve lo que necesita, y nada más.
- **(20 s) Cortar el acceso.** Si Carmen vuelve antes, corta el acceso, y el otro teléfono ya no ve la ficha. El texto de la ficha va cifrado, y la familia ve quién la abrió.

Martín, ¿nos muestras los insumos?

### Lámina 15 · Demostración · Capas 2 y 3, insumos y despacho
**Habla Martín, recibe la palabra de Jorge · demo de 2 min 15 s · al terminar 8:15.**

- **(30 s) Insumos y aviso de quiebre.** Carmen anotó cuánto usa de cada insumo, y MATU calcula cuándo se acaba. Aquí hay un aviso: los pañales se acaban en pocos días.
- **(20 s) La lista de reposición.** La lista se puede imprimir o compartir aunque nunca se compre por MATU, porque las dos primeras capas sirven solas.
- **(40 s) Pedido y pago.** Si la familia quiere, arma el pedido desde la lista y paga en Transbank, aquí en su ambiente de integración y con una tarjeta de prueba. Es un solo cobro del total exacto: precios finales y un solo envío.
- **(45 s) El comercio y el retiro.** En el otro teléfono está el comercio, con un pedido que dejamos preparado antes. Ve solo los productos y una referencia, sin el nombre ni la dirección de la familia. Quien retira por MATU dice el código, el comercio lo valida y Carmen ve su pedido retirado. Si al comercio le falta un producto, MATU le devuelve ese monto el mismo día, a la misma tarjeta, sin cambiarlo por otra marca.

El comercio, los avisos y el pago son simulados. Todo lo demás es la app real. Jorge les cuenta lo que viene.

### Lámina 16 · Próximos pasos de MATU
**Habla Jorge, recibe la palabra de Martín · 45 s · al terminar 9:00 · pasa la palabra a Martín.**
Lo primero es la app nativa: en el semestre MATU es una app web pensada para el teléfono, y la versión nativa es la etapa siguiente. Después viene lo que ya dejamos diseñado: el pago dividido entre familiares, la reposición programada y la liquidación a los comercios. Antes de usar datos reales y dinero real, cerramos la consulta legal abierta, sobre todo la Ley 21.719, que rige plenamente desde diciembre, y la verificación en dos pasos para operación. Y el paso que más nos importa es un piloto con familias y comercios reales.

### Lámina 17 · Conclusión
**Habla Martín · 45 s · al terminar 9:45.**
En resumen: el problema está medido, la solución está construida y validada con usuarias, y las tres capas funcionan en un entorno desplegado, con los seis recorridos críticos probados en un teléfono real. Lo que más aprendimos fue a dejar que la evidencia recortara el alcance: la ficha quedó en tres campos porque las cuidadoras nos mostraron que un plan largo no se completa. MATU no reemplaza a quien cuida. Hace que lo que ella sabe no dependa de una sola persona.

### Lámina 18 · Gracias
**Habla Martín · 15 s · al terminar 10:00.**
Gracias. Jorge y yo quedamos atentos a sus preguntas.

---

## Preparación de la demo (Martín, 30 minutos antes)

1. **Restablecer la demo** con el instructivo (`docs/entorno-demo.md`), en menos de 10 minutos.
2. **Dejar un pedido ya pagado y preparado en el comercio** para la lámina 15. Desde el pago, el pedido tarda hasta 5 minutos en llegarle al comercio (H8), y en vivo no hay tiempo de esperarlo.
3. **Usar solo productos con stock en Almacén El Ejemplo** mientras no esté la cuenta del segundo comercio (H7, MATU-112).
4. **Generar el código de retiro justo antes,** porque vale 90 minutos. Nunca escribirlo en un chat.
5. Dejar los dos teléfonos con la sesión abierta, el brillo al máximo y las notificaciones en silencio.
6. **Plan B:** tener abiertos, y disponibles sin conexión, el video del recorrido principal y las capturas de los recorridos.

## Si el tiempo no alcanza

Se recorta en este orden, sin tocar la demo:
1. lámina 10 (tecnologías): se dice solo en una frase;
2. lámina 7 (requerimientos): se pasa con la cifra y nada más;
3. lámina 15, la frase del producto que falta.

## Preguntas probables de la comisión

| Pregunta | Responde | Idea central |
|---|---|---|
| ¿Por qué una app web y no nativa? | Jorge | Fue la decisión del semestre (ADR-026): llega a cualquier teléfono sin instalar nada, y las participantes de usabilidad lo valoraron |
| ¿Cómo protegen los datos de salud? | Jorge | La ficha va cifrada con una clave por persona, la base aísla a cada familia por fila, el relevo vence y se puede cortar, y no hay analítica de terceros |
| ¿Cuál fue el rol de la IA? | Jorge | Seis agentes con roles y reglas escritas. Las personas deciden, revisan y fusionan, y el factor de vibecoding está medido con horas reales |
| ¿Qué pasa si la cuidadora no tiene tiempo? | Martín | Por eso son tres campos (lo pidió la evidencia, H1), y se llenan en menos de 3 minutos (usabilidad, ronda 2) |
| ¿Por qué el despacho se puede quitar? | Martín | Para que la ficha y la predicción sirvan aunque la familia compre en otra parte. La lista se exporta |
| ¿Es legal cobrar? | Martín | En el piloto no se cobra dinero real. Hay una consulta legal abierta y documentada que se cierra antes de hacerlo |

**Palabras que no se usan** (`docs/lenguaje.md`): diagnóstico, conducta, incidente, deterioro, incontinencia.

# MATU · Guion de la presentación final ante la comisión

**Duración total:** 10 minutos · **Orden:** Jorge → Martín → Jorge (demo de la ficha) → Martín (demo de las capas 2 y 3) → Jorge (próximos pasos) → Martín (conclusión)
**Borrador del orquestador · 16 de noviembre de 2026.** Lo ajustan Jorge y Martín en los ensayos (MATU-111). Las láminas son las de la presentación ya cerrada. Este guion solo fija qué se dice, quién lo dice y cuánto dura.

Cada bloque trae su tiempo, lo que se dice (para decirlo con palabras propias, no para leerlo) y lo que se ve en pantalla. Las frases entre comillas son las que conviene decir casi textuales.

---

## Resumen de tiempos

| # | Minuto | Quién | Bloque | Dura |
|---|---|---|---|---|
| 1 | 0:00 – 1:30 | Jorge | El problema y qué es MATU | 1:30 |
| 2 | 1:30 – 3:00 | Martín | Cómo lo validamos y cómo lo construimos | 1:30 |
| 3 | 3:00 – 5:00 | Jorge | Demo · Capa 1: la ficha de relevo | 2:00 |
| 4 | 5:00 – 7:30 | Martín | Demo · Capas 2 y 3: insumos, pedido y retiro | 2:30 |
| 5 | 7:30 – 8:45 | Jorge | Próximos pasos de MATU | 1:15 |
| 6 | 8:45 – 10:00 | Martín | Conclusión | 1:15 |

**Margen:** no hay. Si un bloque se pasa 20 segundos, el siguiente los recupera saltándose lo marcado como **[recortable]**.

---

## 1 · Jorge · El problema y qué es MATU (0:00 – 1:30)

**En pantalla:** portada y la lámina del problema.

- Presentarse en una frase: «Somos Jorge Espinoza y Martín Henríquez, y este es MATU».
- **El problema, con una escena:** una cuidadora que lleva años cuidando a su madre tiene que ausentarse un día. Quien la reemplaza no sabe cómo es el día de esa persona, qué hacer si se altera ni a quién llamar. Y en la casa se acaban los pañales un domingo, sin aviso.
- «Ese conocimiento vive en la cabeza de una sola persona. MATU lo saca de ahí.»
- **Qué es MATU:** una app de **continuidad del cuidado** para personas mayores con dependencia, con tres capas. Decir el orden, porque importa:
  1. **La ficha de relevo**, que es el producto: tres campos que se comparten con quien reemplaza.
  2. **El consumo de insumos y su predicción**, que es el diferenciador: MATU avisa antes de que algo se acabe.
  3. **El despacho**, que es un servicio: pedir y pagar. Está construido para poder quitarse sin que las dos primeras capas dejen de funcionar.
- Pasar la palabra: «Martín les cuenta cómo llegamos a esto».

## 2 · Martín · Cómo lo validamos y cómo lo construimos (1:30 – 3:00)

**En pantalla:** la lámina de validación y la de método.

- **Partimos escuchando:** 10 entrevistas a cuidadoras (con 4 más de ampliación), con hipótesis y criterios fijados antes de entrevistar.
- **La evidencia nos cambió el producto:** la hipótesis de «un plan completo en cinco minutos» se refutó (3 de 10). Por eso la ficha quedó en **tres campos**, y el pago dividido entre varios familiares salió del semestre. «No construimos lo que creíamos, construimos lo que las cuidadoras validaron.»
- **Dos rondas de usabilidad.** En la segunda, las 3 participantes completaron la ficha en menos de 3 minutos sin ayuda (en la primera lo logró 1 de 3), y armaron un pedido en menos de 6 minutos.
- **Cómo trabajamos:** Scrum en cinco sprints, con roles definidos (ADR-030):
  - Jorge, como Product Owner, desarrolla con un equipo de agentes de IA, cada uno con su rol y sus reglas;
  - Martín revisa cada cambio, lo despliega y lo prueba en un teléfono real antes de fusionarlo.
- **[recortable]** El factor de vibecoding medido en el semestre: **1,98**. Por cada hora de trabajo de Jorge, salió lo que se había estimado en casi dos (143 h estimadas y 72 h reales, medidas en Trello). Para el equipo, 2,04.
- Pasar la palabra: «Jorge les muestra la ficha funcionando».

## 3 · Jorge · Demo de la capa 1: la ficha de relevo (3:00 – 5:00)

**En pantalla:** la demo en el teléfono, proyectado. Cuenta de Carmen (`carmen@example.com`), ya con la sesión abierta.

1. **(0:30) La ficha:** mostrar los tres campos ya llenos de la persona cuidada: «Su día», «Si se altera» y «A quién llamar». Decir que se llena en menos de 3 minutos.
2. **(0:45) Compartir con un relevo:** crear el enlace con PIN. «El enlace vence solo, y el PIN viaja por separado.»
3. **(0:30) Abrirlo en el segundo teléfono,** como lo vería quien reemplaza: sin cuenta y sin instalar nada, solo el enlace y el PIN.
4. **(0:15) Cortar el acceso:** revocarlo desde la cuenta de Carmen y mostrar que el segundo teléfono ya no lo ve.

**Decir en voz alta:** «El texto de la ficha va cifrado, y cada familia ve solo lo suyo».

**Plan B:** si la red falla, mostrar las capturas del recorrido 2 (MATU-77).

## 4 · Martín · Demo de las capas 2 y 3: insumos, pedido y retiro (5:00 – 7:30)

**En pantalla:** la demo. La cuenta de Carmen y la de `comercio@example.com` en el segundo teléfono.

1. **(0:40) Insumos y aviso de quiebre:** la pantalla de Insumos con una alerta abierta. «MATU calcula cuándo se acaba cada insumo según cuánto se usa, y avisa antes.»
2. **(0:20) La lista de reposición:** se puede imprimir o compartir aunque nunca se compre por MATU. Las capas 1 y 2 sirven solas.
3. **(0:50) Pedido y pago:** armar el pedido desde la lista y pagar en el ambiente de integración de Transbank con la tarjeta de prueba. «Es un solo cobro del total exacto, con los precios finales y un solo envío.»
4. **(0:40) El comercio y el retiro:** mostrar en el segundo teléfono el **pedido ya preparado de antes** (ver «Preparación»). El comercio ve solo los productos y una referencia, sin el nombre de la familia ni la dirección. Validar el código de retiro y mostrar el pedido «Retirado» en la cuenta de Carmen.

**Decir en voz alta qué es simulado:** el comercio, el envío de los avisos y el pago, que es de integración.

**[recortable]** Si falta un producto, el comercio marca «No lo tengo» y MATU devuelve ese monto el mismo día a la misma tarjeta, sin cambiarlo por otra marca.

**Plan B:** el video del recorrido principal (MATU-78) o las capturas de los recorridos 3 a 6.

## 5 · Jorge · Próximos pasos de MATU (7:30 – 8:45)

**En pantalla:** la lámina de próximos pasos.

- **La app nativa:** en el semestre MATU es una app web mobile first (ADR-026), y la app nativa se decide en la etapa siguiente.
- **Lo que dejamos diseñado, pero fuera del semestre:** el pago dividido entre familiares y el prorrateo, la reposición programada, la app de repartidor y la liquidación automática a los comercios. El modelo de datos ya tiene sus tablas, así que activarlos no exige rehacer nada.
- **Antes de usar dinero y datos reales:** cerrar la consulta legal abierta (Ley 21.719, que rige plenamente desde diciembre de 2026, y Ley 19.496) y la verificación en dos pasos para operación.
- **El piloto:** con familias reales y comercios en convenio.

## 6 · Martín · Conclusión (8:45 – 10:00)

**En pantalla:** la lámina de cierre.

- Volver a la escena del inicio: la cuidadora que se ausenta un día ahora deja la ficha en manos de quien la reemplaza, y los pañales no se acaban un domingo sin aviso.
- **Lo logrado:** las tres capas funcionan en un entorno de demostración, y los seis recorridos críticos pasaron en un teléfono real.
- **Lo aprendido:** validar primero y dejar que la evidencia recorte el alcance.
- Cerrar con una frase: «MATU no reemplaza a quien cuida. Hace que su conocimiento no dependa de una sola persona».
- «Gracias. Quedamos atentos a sus preguntas.»

---

## Preparación antes de presentar (Martín, 30 minutos antes)

1. **Restablecer la demo** con el instructivo (`docs/entorno-demo.md`), en menos de 10 minutos.
2. **Dejar un pedido ya pagado y preparado** en el comercio, listo para retirar, para el paso 4.4. Desde el pago, el pedido tarda hasta 5 minutos en llegarle al comercio (H8), y en vivo no hay tiempo de esperarlo.
3. **Usar solo productos con stock en Almacén El Ejemplo** mientras no esté la cuenta del segundo comercio (H7, MATU-112). Si MATU-112 ya está desplegada, se puede mostrar un pedido con productos de los dos comercios.
4. **Generar el código de retiro** en la consola justo antes, porque vale 90 minutos. Nunca escribirlo en un chat.
5. Dejar los dos teléfonos con la sesión abierta, el brillo al máximo y las notificaciones en silencio.
6. Tener a mano el plan B: el video y las capturas, abiertos y sin conexión.

## Preguntas probables de la comisión

| Pregunta | Quién responde | Idea central |
|---|---|---|
| ¿Por qué una app web y no nativa? | Jorge | Fue una decisión del semestre (ADR-026): llega a cualquier teléfono sin instalar nada, y las participantes de usabilidad lo valoraron |
| ¿Cómo protegen los datos de salud? | Jorge | La ficha va cifrada con una clave por persona, cada familia está aislada a nivel de base de datos (RLS), el relevo vence y se revoca, y no hay analítica de terceros |
| ¿Qué pasa si una cuidadora no tiene tiempo de llenar la ficha? | Martín | Por eso son tres campos (lo pidió la evidencia, H1), y se llenan en menos de 3 minutos (usabilidad, ronda 2) |
| ¿Cuál fue el rol de la IA en el desarrollo? | Jorge | Agentes con roles y reglas escritas. Las personas deciden, revisan y fusionan, y el factor de vibecoding está medido |
| ¿Por qué el despacho es una capa que se puede quitar? | Martín | Para que la ficha y la predicción sirvan aunque la familia compre en otra parte. La lista se exporta |
| ¿Es legal cobrar? | Martín | En el piloto no se cobra dinero real. Hay una consulta legal abierta y documentada antes de hacerlo |

**Palabras que no se usan** (`docs/lenguaje.md`): diagnóstico, conducta, incidente, deterioro, incontinencia.

# MATU · Guion de la presentación final ante la comisión

**Duración:** 10 minutos (600 segundos).
**Orden:**
1. Jorge abre: problema, diagnóstico y solución.
2. Martín sigue: objetivos, cómo se construyó y la arquitectura.
3. Jorge muestra la ficha en la demo.
4. Martín muestra las capas 2 y 3.
5. Jorge cuenta los próximos pasos de MATU.
6. Martín cierra.

**Borrador del orquestador, versión 2 · 16 de noviembre de 2026.** Jorge y Martín lo ajustan en los ensayos (MATU-111).

**Estructura y profundidad:**
- **Estructura:** las láminas y el orden son los de la presentación de la Fase 2 (`Fase 2/Evidencias Proyecto/MATU_Presentacion_Fase2.pptx`). Cada nota tiene la misma forma: quién habla, cuánto dura, en qué minuto termina y el texto dicho.
- **Problema y solución:** el contexto de la Fase 2 se abre en las tres láminas de la Fase 1 (`Fase 1/Evidencias Grupales/MATU_Presentacion_Fase1.pptx`): el problema con sus cifras, el diagnóstico (dos problemas que son el mismo) y la solución (tres capas, y el orden importa). Es lo que más pesa en la presentación.
- **El equipo son Jorge y Martín.** Las entrevistas y la usabilidad aparecen como respaldo en una frase, no tienen lámina propia.

**Cifras verificadas el 16-11** en el código (`main`, eb32e70), en `docs/arquitectura.md` y en GitHub: 26 requisitos *Debe* sobre 42 (arquitectura, 3.6), 23 cumplidos, 98 PR fusionados en MATU_PROYECTO, 29 migraciones, 251 pruebas en `test_aislamiento.py`, 10 módulos, $5.990 y 84 familias (arquitectura, 16.2) y el factor de 1,98 (MATU#99). Las cifras del problema son las de la presentación de la Fase 1 (ENDIDE 2022). Las dos marcadas con `[VERIFICAR el día de la presentación]` dependen de MATU-80 y MATU-81.

---

## Resumen de tiempos

| Lámina | Título | Habla | Dura | Termina |
|---|---|---|---|---|
| 1 | Portada | Jorge | 10 s | 0:10 |
| 2 | Equipo | Jorge | 15 s | 0:25 |
| 3 | El problema | Jorge | 40 s | 1:05 |
| 4 | El diagnóstico | Jorge | 30 s | 1:35 |
| 5 | La solución | Jorge | 45 s | 2:20 |
| 6 | Objetivo general | Jorge | 10 s | 2:30 |
| 7 | Objetivos específicos | Martín | 25 s | 2:55 |
| 8 | Alcance | Martín | 15 s | 3:10 |
| 9 | Requerimientos | Martín | 15 s | 3:25 |
| 10 | Metodología | Martín | 15 s | 3:40 |
| 11 | Cronograma | Martín | 10 s | 3:50 |
| 12 | Tecnologías y herramientas | Martín | 10 s | 4:00 |
| 13 | Arquitectura de la aplicación | Martín | 30 s | 4:30 |
| 14 | Modelo de datos | Martín | 20 s | 4:50 |
| 15 | Modelo de negocio | Martín | 15 s | 5:05 |
| 16 | Demostración · Capa 1, la ficha de relevo | Jorge | 1 min 35 s | 6:40 |
| 17 | Demostración · Capas 2 y 3, consumo y despacho | Martín | 1 min 50 s | 8:30 |
| 18 | Próximos pasos de MATU | Jorge | 40 s | 9:10 |
| 19 | Conclusión | Martín | 35 s | 9:45 |
| 20 | Gracias | Martín | 15 s | 10:00 |

---

## Notas por lámina

### Lámina 1 · Portada
**Habla Jorge · 10 s · al terminar 0:10.**
Buenas tardes. Somos Jorge Espinoza y Martín Henríquez, y les presentamos MATU terminado: un sistema de continuidad del cuidado para personas mayores con dependencia.

### Lámina 2 · Equipo
**Habla Jorge · 15 s · al terminar 0:25.**
Yo soy el Product Owner y desarrollé el sistema. Martín es el Scrum Master: desplegó los entornos, probó cada cambio en un teléfono real y revisó y fusionó cada entrega. Ninguno de los dos fusiona su propio trabajo.

### Lámina 3 · El problema
**Habla Jorge · 40 s · al terminar 1:05.**
En Chile, un millón y medio de personas adultas viven en situación de dependencia. El 96,4% de quienes las cuidan en el hogar no recibe remuneración, y siete de cada diez son mujeres. El 41,3% no tiene un cuidador formal. Y hay doscientas mil personas con demencia, que en 2024 fue la cuarta causa de muerte del país. El cuidado lo sostienen las familias, sin pago y sin herramientas.

### Lámina 4 · El diagnóstico
**Habla Jorge · 30 s · al terminar 1:35.**
Hay dos problemas que parecen distintos y son el mismo. El primero es la continuidad: cómo se cuida a alguien vive en una sola cabeza, y traspasarlo cuesta horas. El segundo es el abastecimiento: el consumo se lleva de memoria, y se compra cuando alguien nota que se acabó. Las dos son la misma falla: el cuidado depende de una persona que no puede delegar ni ausentarse. Nueve de cada diez cuidadoras que entrevistamos habían dejado de salir por falta de relevo.

### Lámina 5 · La solución
**Habla Jorge · 45 s · al terminar 2:20.**
MATU tiene tres capas, y el orden importa. La capa 1 es el producto: una ficha de relevo con tres campos, su día, qué hacer si se altera y a quién llamar. Se comparte con quien reemplaza por un enlace con PIN, que vence y se puede cortar. La capa 2 es el diferenciador: del mismo cuidado se declara el consumo, y MATU anticipa cuándo se acaba cada insumo y arma la lista de reposición. La capa 3 es el despacho, y es un servicio, no la razón de existir: sin ella, la familia exporta su lista y compra donde quiera. El orden importa porque la predicción existe gracias al cuidado: nadie que no conozca a la persona sabe que usa cuatro pañales al día.

### Lámina 6 · Objetivo general
**Habla Jorge · 10 s · al terminar 2:30 · pasa la palabra a Martín.**
Nos comprometimos a construir esta plataforma y dejarla operativa en un entorno de demostración. Hoy lo está, y Martín les cuenta cómo la construimos.

### Lámina 7 · Objetivos específicos
**Habla Martín, recibe la palabra de Jorge · 25 s · al terminar 2:55.**
Gracias, Jorge. Teníamos siete objetivos, y seis están cumplidos. Tres cambiaron su redacción por decisiones del camino: la lista se exporta sin enlace, el pago es un solo cobro del total exacto y fijamos seis recorridos críticos. El séptimo es que esos recorridos corran solos en cada cambio. Ya pasaron todos en un teléfono real, y uno ya corre solo en cada cambio. Los otros cinco se automatizan esta semana `[VERIFICAR el día de la presentación: MATU-80]`.

### Lámina 8 · Alcance
**Habla Martín · 15 s · al terminar 3:10.**
Construimos lo que nunca se sacrifica: la ficha, el acceso del relevo, la predicción de quiebre y la exportación de la lista. Es un piloto académico, sin dinero real y sin convenios, y es una app web pensada para el teléfono.

### Lámina 9 · Requerimientos
**Habla Martín · 15 s · al terminar 3:25.**
De 42 requerimientos funcionales, 26 son obligatorios, y cumplimos 23. Los tres que faltan son de la operación interna de MATU: conciliar con el comercio, gestionar el catálogo y resolver incidencias `[VERIFICAR el día de la presentación: RF-31, RF-32 y RF-40, con MATU-81]`. Entre los no funcionales hay dos que no se negocian: ningún pago sin registrar y la accesibilidad. El texto se puede agrandar al doble sin perder nada en la pantalla de un teléfono.

### Lámina 10 · Metodología
**Habla Martín · 15 s · al terminar 3:40.**
Usamos Scrum con sprints de una semana. Cada cambio va en su rama, con sus pruebas, y no entra sin el CI en verde y sin la revisión de la otra persona. Además medimos cuánto nos aceleró el desarrollo asistido por IA, en vez de suponerlo: un factor de 1,98.

### Lámina 11 · Cronograma
**Habla Martín · 10 s · al terminar 3:50.**
Cerramos los cinco sprints de construcción, con 98 entregas fusionadas al código, y todavía quedan los dos sprints de reserva.

### Lámina 12 · Tecnologías y herramientas
**Habla Martín · 10 s · al terminar 4:00.**
Usamos tecnología conocida: Python con FastAPI, PostgreSQL 16, React con TypeScript y Webpay Plus de Transbank. El despliegue está en Railway, con un entorno de pruebas y otro de demostración.

### Lámina 13 · Arquitectura de la aplicación
**Habla Martín · 30 s · al terminar 4:30.**
Es un monolito modular: una sola API con diez módulos, y las dependencias van siempre hacia abajo. La ficha no sabe que existe el despacho, y por eso la capa 3 se puede apagar: una prueba automática verifica que la ficha y la predicción siguen funcionando. La seguridad está en el diseño. Cada familia está aislada en la base de datos, de modo que una consulta sin contexto devuelve cero filas. La ficha va cifrada, con una clave por persona. Y diseñamos para la Ley 21.719, que rige plenamente desde diciembre.

### Lámina 14 · Modelo de datos
**Habla Martín · 20 s · al terminar 4:50.**
Todo el modelo cuelga del grupo familiar, que es la unidad de aislamiento. No guardamos datos clínicos. El comercio no lee las tablas de la familia: solo ve, por funciones cerradas, sus productos, las cantidades y una referencia al azar. Cada cambio de la base es una migración reversible, ya van 29, y 251 pruebas de aislamiento corren en cada entrega.

### Lámina 15 · Modelo de negocio
**Habla Martín · 15 s · al terminar 5:05 · pasa la palabra a Jorge.**
Solo con despacho, el negocio no se sostiene. Con una suscripción de $5.990, el equilibrio baja a 84 familias, y seis de cada diez entrevistadas ya pagan por algún servicio de cuidado. Jorge les muestra MATU funcionando.

### Lámina 16 · Demostración · Capa 1, la ficha de relevo
**Habla Jorge, recibe la palabra de Martín · demo de 1 min 35 s · al terminar 6:40.**
Carmen cuida a su mamá, y este sábado la reemplaza otra persona.

- **(25 s) La ficha.** Estos son los tres campos de Carmen: su día, qué hacer si se altera y a quién llamar.
- **(30 s) Compartir.** Carmen crea un enlace para quien la reemplaza. El enlace vence solo, y el PIN se entrega por separado.
- **(25 s) El relevo.** En el otro teléfono, quien reemplaza abre el enlace sin cuenta y sin instalar nada. Escribe el PIN y ve lo que necesita, y nada más.
- **(15 s) Quién la vio y cortar el acceso.** Carmen ve que el relevo abrió la ficha. Si vuelve antes, corta el acceso, y el otro teléfono ya no la ve.

Martín, ¿qué pasa con los insumos?

### Lámina 17 · Demostración · Capas 2 y 3, consumo y despacho
**Habla Martín, recibe la palabra de Jorge · demo de 1 min 50 s · al terminar 8:30.**

- **(30 s) Lo que se está acabando.** Carmen anotó cuánto usa de cada insumo, y MATU le avisa que los pañales se acaban en pocos días.
- **(15 s) La lista.** La lista se imprime o se comparte aunque nunca se compre por MATU.
- **(35 s) Pedido y pago.** Si quiere, arma el pedido desde la lista y paga en Transbank, aquí en su ambiente de integración. Es un solo cobro del total exacto: precios finales y un solo envío.
- **(30 s) El comercio y el retiro.** En el otro teléfono, el comercio ve solo los productos y una referencia, sin el nombre ni la dirección de la familia. Valida el código de retiro, y Carmen ve su pedido retirado. Si falta un producto, MATU devuelve ese monto el mismo día, a la misma tarjeta.

El comercio, los avisos y el pago son simulados. Todo lo demás es el sistema real.

### Lámina 18 · Próximos pasos de MATU
**Habla Jorge, recibe la palabra de Martín · 40 s · al terminar 9:10 · pasa la palabra a Martín.**
Lo que quedó fuera está diseñado. Primero, los medicamentos y el retiro en el CESFAM, que fue la demanda más repetida en las entrevistas. Después, la app nativa, el pago dividido entre familiares, la reposición programada y los comercios reales. Y antes de tratar datos reales o cobrar dinero real, cerramos la consulta legal abierta, la figura jurídica para vender y la verificación en dos pasos para operación. El paso siguiente es un piloto con familias reales.

### Lámina 19 · Conclusión
**Habla Martín · 35 s · al terminar 9:45.**
En resumen: el problema está medido, la solución va en orden y la seguridad está en el diseño. Las tres capas funcionan en un entorno desplegado, y la capa 3 se puede quitar sin que la familia pierda su ficha ni su predicción. MATU no reemplaza a quien cuida. Hace que lo que ella sabe no dependa de una sola persona.

### Lámina 20 · Gracias
**Habla Martín · 15 s · al terminar 10:00.**
Gracias. Jorge y yo quedamos atentos a sus preguntas.

---

## Preparación de la demo (Martín, 30 minutos antes)

1. **Restablecer la demo** con el instructivo (`docs/entorno-demo.md`), en menos de 10 minutos.
2. **Dejar un pedido ya pagado y preparado en el comercio** para la lámina 17. Desde el pago, el pedido tarda hasta 5 minutos en llegarle al comercio (H8), y en vivo no hay tiempo de esperarlo.
3. **Usar solo productos con stock en Almacén El Ejemplo** mientras no esté la cuenta del segundo comercio (H7, MATU-112).
4. **Generar el código de retiro justo antes,** porque vale 90 minutos. Nunca escribirlo en un chat.
5. Dejar los dos teléfonos con la sesión abierta, el brillo al máximo y las notificaciones en silencio.
6. **Plan B:** el video del recorrido principal y las capturas, abiertos y disponibles sin conexión.

## Si el tiempo no alcanza

Se recorta en este orden, sin tocar el problema, la solución ni la demo:
1. lámina 12 (tecnologías);
2. lámina 11 (cronograma), que se dice en una frase dentro de la 10;
3. lámina 9 (requerimientos), solo con la cifra.

## Preguntas probables de la comisión

| Pregunta | Responde | Idea central |
|---|---|---|
| ¿Cómo protegen los datos de salud? | Jorge | No guardamos datos clínicos. La ficha va cifrada con una clave por persona, cada familia está aislada en la base, el relevo vence y se puede cortar, y no hay analítica de terceros |
| ¿Por qué el despacho se puede quitar? | Jorge | Para que la ficha y la predicción sirvan aunque la familia compre en otra parte. Una prueba automática lo verifica |
| ¿Por qué una app web y no nativa? | Martín | Fue la decisión del semestre (ADR-026): llega a cualquier teléfono sin instalar nada. La nativa es el próximo paso |
| ¿Cómo usaron la IA? | Jorge | Como asistencia al desarrollo, con revisión humana en cada entrega y el aporte medido con horas reales (factor 1,98) |
| ¿Es legal cobrar? | Martín | En el piloto no se cobra dinero real. Hay una consulta legal abierta y documentada que se cierra antes de hacerlo |
| ¿Cómo saben que la ficha sirve? | Martín | La ficha quedó en tres campos porque las entrevistas mostraron que un plan largo no se completa, y en la usabilidad se llenó en menos de 3 minutos |

**Palabras que no se usan** (`docs/lenguaje.md`): diagnóstico, conducta, incidente, deterioro, incontinencia. La lámina 4 se llama «El diagnóstico» en la Fase 1. Ese término es para la comisión, no es un texto de la app.

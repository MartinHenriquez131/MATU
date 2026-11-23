# MATU · Presentación final · Preguntas probables de la comisión · v2

**Versión 2.0 · 23/11/2026** · Va con `MATU_Guion_Presentacion_Fase3_v2.md` y `MATU_Contenido_Laminas_Fase3_v2.md`, en esta misma carpeta. La v1 queda como estaba.
**Es el criterio 3 de la planilla** (20 puntos). Son 12 preguntas, seis para cada uno, y cada respuesta tiene dos o tres frases, unos 30 segundos.

---

## Cómo se responde

- **Responde quien está asignado.** El otro agrega una frase solo si suma un dato.
- **Primero la respuesta, después la evidencia.** «Sí, y está en…».
- **Si es una limitación, se dice una vez, con su plan y sin dramatizar.** Después se pasa a lo que sí está.
- **Si no se sabe:** «Eso no lo medimos. Lo que sí medimos es…». Nunca se inventa una cifra.
- **Sin nombres propios.** Se habla de la cuidadora, la persona cuidada, el relevo, la familia y el comercio.
- **No se ofrecen sin que los pidan:** la cantidad de agentes de IA, el factor de vibecoding ni el atraso del objetivo 7. Si los preguntan, se responden con el dato.

| # | Pregunta | Responde |
|---|---|---|
| 1 | ¿Escala? ¿Qué pasó con la carga? | Martín |
| 2 | ¿Cómo protegen los datos de salud? | Jorge |
| 3 | ¿Quién autoriza por la persona cuidada, si ella no puede? | Jorge |
| 4 | ¿Por qué una app en el navegador y no una nativa? | Martín |
| 5 | ¿Cómo controlaron la calidad con agentes de IA? | Jorge |
| 6 | ¿Qué pasa si se quita la capa 3? | Martín |
| 7 | ¿Se sostiene el negocio? | Jorge |
| 8 | ¿Quedó algún requisito pendiente? | Jorge |
| 9 | ¿Por qué un solo cobro y no una reserva? | Martín |
| 10 | ¿Cómo saben que el problema existe? | Martín |
| 11 | ¿Cómo se repartieron el trabajo? | Martín |
| 12 | ¿Qué datos guardan de la persona, y quién los ve? | Jorge |

---

## 1. ¿Escala? ¿Qué pasó con la carga?

- **Responde:** Martín
- **Respuesta:** Para el piloto, sí: con diez compras simultáneas sobre una base recién preparada, no hubo fallos y las medianas fueron de 453 ms al confirmar y de 421 ms en el retorno del pago. Con mucho volumen acumulado, el pago se vuelve más lento: con los pedidos de cinco corridas en la misma base, esas medianas se duplicaron. Está documentado, con su plan para antes de producción: medir con volumen creciente, encontrar la consulta que crece y corregirla con una migración revisada.
- **Si repreguntan por 50 compras simultáneas:** es la meta de producción (percentil 95 bajo 800 ms), y se mide en un equipo representativo. El computador de prueba, con 2 núcleos y un solo proceso de la API, se saturaba entero con 50, y eso apunta a la máquina, no a un paso del código.
- **Fuente:** `TESTER/2026-11-22-MATU-80-carga-meta.md`, anexo. `TESTER/2026-11-20-MATU-80-k6-tercera.md`. `docs/arquitectura.md` §2.2, RNF-05, con los párrafos «La meta de RNF-05 para el piloto» y «El pago se encarece con el volumen».

## 2. ¿Cómo protegen los datos de salud?

- **Responde:** Jorge
- **Respuesta:** Cada familia está aislada en PostgreSQL con Row Level Security forzado, la app entra con un rol sin privilegios de dueño y un recurso de otra familia responde 404, lo que verifican 270 pruebas en cada cambio. La ficha va cifrada con AES-256-GCM y una clave por persona, nunca aparece en registros, direcciones ni en el almacenamiento del navegador, y destruir la clave la deja ilegible. La Ley 21.719, en plena vigencia desde el 1 de diciembre de 2026, trata los datos de salud como sensibles, y la tomamos como requisito de diseño: MATU no pide datos clínicos, tiene su política de privacidad y su registro de tratamientos, y cada historia con datos personales se revisó contra la normativa antes y al cierre.
- **Si repreguntan por la clave maestra:** en el piloto vive en una variable de entorno, porque solo hay datos de prueba. Antes de tratar datos reales pasa a un servicio de custodia, sin tocar el cifrado, porque está detrás de un puerto.
- **Fuente:** `docs/arquitectura.md` §2.2 (RNF-07 y RNF-08), §11.4 y §11.6. `parte-tecnica-jorge.md` §3. `docs/legal/politica-privacidad.md` y `docs/legal/registro-tratamientos.md`. `CLAUDE.md` §3, analista normativo.

## 3. ¿Quién autoriza por la persona cuidada, si ella no puede?

- **Responde:** Jorge
- **Respuesta:** Sin una autorización vigente, MATU no guarda ni muestra la ficha. Al registrar a la persona, MATU anota quién autoriza y en qué calidad: la propia persona, su representante legal o quien la cuida de hecho, que hace una declaración, ve un aviso de su límite y la renueva cada año. La ficha, los insumos y los pedidos tienen cada uno su propia autorización, y cada una se puede retirar.
- **Si repreguntan si eso basta ante la ley:** el diseño reconoce la zona gris. MATU no puede verificar la representación, y no trata la declaración de quien cuida de hecho como si fuera la del titular. Por eso el piloto opera solo con datos de prueba, y esa pregunta se resuelve con asesoría legal antes de tratar datos reales.
- **Fuente:** `docs/arquitectura.md` §11.5. `docs/lenguaje.md` §6.4, §6.4b y §22.

## 4. ¿Por qué una app en el navegador y no una nativa?

- **Responde:** Martín
- **Respuesta:** MATU es una app móvil que en el semestre corre en el navegador del teléfono, sin instalar nada, por una decisión del 14 de octubre que sugirió el profesor guía. Nos dio un solo lenguaje para la familia, el relevo y el comercio, la accesibilidad que trae el navegador, y algo clave para el relevo: abrir la ficha con un enlace, sin descargar nada. Una participante de las pruebas en vivo lo dijo así: «Me gusta que sea rápido de usar en el celular, sin tener que descargar aplicaciones pesadas».
- **Si repreguntan por los límites:** en iPhone, los avisos push solo llegan si se agrega MATU a la pantalla de inicio, así que el correo es el canal garantizado. La app nativa se decide con los datos del piloto.
- **Fuente:** `docs/adr/ADR-026-aplicacion-web.md`. `docs/usabilidad/ronda-2-informe.md`, citas (P1). `docs/arquitectura.md` §17.

## 5. ¿Cómo controlaron la calidad con agentes de IA?

- **Responde:** Jorge
- **Respuesta:** Los agentes de IA fueron una herramienta de desarrollo, cada uno con un perímetro: uno planifica y no programa, otros construyen el backend o la interfaz, otro solo prueba y reporta, otro revisa la normativa y otro el diseño. El código generado cumple la misma definición de terminado que el escrito a mano: pruebas de cada regla, y un CI que en cada cambio corre el análisis estático, la detección de secretos, las migraciones que suben y bajan, y las pruebas de aislamiento, de arquitectura y de trazabilidad. Y ningún cambio entra sin la revisión de la otra persona, con su prueba en el teléfono.
- **Solo si preguntan cuánto aceleró:** medimos las horas estimadas sin IA contra las reales, y dio un factor de 1,86 en el semestre (154,5 h contra 83,11 h), contando solo las horas de la persona, no las de los agentes.
- **Fuente:** `CLAUDE.md` §3 y §5. `docs/sprints/sprint-5-planificacion.md` §8, «Con vibecoding no hay excepciones». `parte-tecnica-jorge.md` §2.3 y §4.

## 6. ¿Qué pasa si se quita la capa 3?

- **Responde:** Martín
- **Respuesta:** Se apaga con un interruptor, `CAPA3_HABILITADA`, y la API arranca sin los módulos del despacho: su contrato muestra solo las capas 1 y 2. Hay 21 pruebas que verifican que nada de las capas 1 y 2 depende de la capa 3, y que la ficha, compartir, el relevo con PIN, el consumo y los avisos funcionan con ella bloqueada. La familia sigue con su lista de insumos, que se imprime o se comparte y sirve en cualquier tienda: es el objetivo 5.
- **Si repreguntan por qué se diseñó así:** ningún convenio con comercios estaba garantizado, y el despacho desacoplable elimina el único punto de falla externo del proyecto.
- **Fuente:** `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md`. `docs/arquitectura.md` §1, decisión 2. `docs/adr/ADR-031-lista-insumos-solo-texto.md`.

## 7. ¿Se sostiene el negocio?

- **Responde:** Jorge
- **Respuesta:** Es un ejercicio de viabilidad sobre 200 familias, con la canasta medida en las entrevistas (una mediana de $70.000 y una compra al mes), una comisión del 10 %, una última milla supuesta de $3.500 y $600.000 de costos fijos. Solo con el despacho cada familia deja $1.400 al mes y harían falta 429, y con la suscripción de $5.990 deja $7.210 y bastan 84, que en una comuna de 100.000 habitantes es alcanzable. Lo que falta saber es cuánto cuesta conseguir cada familia, y las últimas entrevistas mostraron que el municipio es un canal concreto.
- **Si repreguntan por la disposición a pagar:** seis de diez ya pagan por algún servicio de cuidado, y ocho dijeron que sí a $5.990. Cuatro de ellas lo condicionaron a que resuelva los insumos, así que el precio se sostiene sobre las capas 1 y 2 juntas.
- **Si repreguntan si ya se cobra:** no. Cobrar la suscripción queda fuera del semestre a propósito.
- **Fuente:** `docs/arquitectura.md` §3 (RF-41), §16.1, §16.2, §16.4 y §16.6. `docs/resultados-entrevistas.md` §3 (H4), §4 y §8 (H7).

## 8. ¿Quedó algún requisito pendiente?

- **Responde:** Jorge
- **Respuesta:** Uno: conciliar la boleta del comercio contra el pedido. Sin comercios reales no hay boletas que conciliar. Hoy la consola de operación muestra, en solo lectura, lo que MATU le debe a cada comercio, y la conciliación entra con el primer convenio.
- **Si preguntan por las fechas:** el despliegue final, con los seis recorridos en el teléfono, fue el 20 de noviembre, el primer día de la reserva del calendario.
- **Fuente:** `docs/arquitectura.md` §3.3 (RF-31). `parte-tecnica-jorge.md` §2.3. `docs/legal/revision-previa-matu-81.md` (D-81-11). `TESTER/2026-11-20-MATU-80-recorridos.md`.

## 9. ¿Por qué un solo cobro y no una reserva?

- **Responde:** Martín
- **Respuesta:** La captura diferida de Transbank solo funciona con crédito, el débito es el medio más usado por estas familias, y una retención mayor que el pedido es difícil de explicar, como observó el análisis de la Ley 19.496. Con precios exactos, la familia ve el total antes de pagar, se cobra una sola vez en venta normal de Webpay Plus, y si un producto falta se anula su parte a la misma tarjeta. El 10 de noviembre lo probé contra el ambiente de integración, con crédito, débito, una anulación parcial de $8.990 con los dos medios y un retorno duplicado que dejó un solo cobro, y los cuatro casos dieron PASS.
- **Fuente:** `docs/adr/ADR-027-precios-exactos.md`. `parte-tecnica-jorge.md` §3.2. `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`.

## 10. ¿Cómo saben que el problema existe?

- **Responde:** Martín
- **Respuesta:** Antes de entrevistar escribimos siete hipótesis, cada una con el resultado que la validaba y el que la refutaba. Con diez entrevistas a cuidadoras y cuatro a familiares que aportan, seis quedaron validadas y una se refutó, la de responder el plan en cinco minutos, con lo que el plan se volvió una ficha de tres campos. Después, en las pruebas en vivo con la app, tres de tres llenaron la ficha en menos de tres minutos y armaron el pedido en menos de seis.
- **Si repreguntan por los límites de la muestra:** las diez primeras llegaron por la red del equipo, y lo declaramos. Por eso las cuatro de la ampliación se reclutaron solo por un canal concentrado, los grupos de personas mayores del municipio.
- **Fuente:** `docs/protocolo-entrevistas.md` §7. `docs/resultados-entrevistas.md` §1, §3 y §8. `docs/adr/ADR-023-cierre.md`. `docs/usabilidad/ronda-2-informe.md`.

## 11. ¿Cómo se repartieron el trabajo?

- **Responde:** Martín
- **Respuesta:** Por rol, como en Scrum:
  - el Product Owner lleva la visión, el backlog y la construcción;
  - el Scrum Master lleva el proceso, la calidad, el despliegue y las pruebas con usuarios.

  Ningún cambio entra a la rama principal sin la revisión de la otra persona. Las diez entrevistas las hicimos cinco cada uno, y cada sprint lo planificamos, revisamos y cerramos juntos.
- **Fuente:** `docs/adr/ADR-030-roles-del-equipo.md`. `docs/resultados-entrevistas.md` §1 (columna «Entrevistador»). `docs/sprints/sprint-5-planificacion.md` §4 (ceremonias) y §8.

## 12. ¿Qué datos guardan de la persona, y quién los ve?

- **Responde:** Jorge
- **Respuesta:** De la persona guardamos su nombre, el nivel de apoyo, la ficha que escribe la familia, cifrada, y lo que usa, sin datos clínicos. Cada uno ve lo suyo:
  - quien solo se informa no ve montos;
  - el relevo ve solo las secciones que se eligieron al compartir, y hasta que vence el enlace;
  - el comercio ve solo los productos, sin la persona ni la dirección;
  - el equipo de operación nunca ve la ficha.

  La familia puede descargar una copia de sus datos desde la app, o borrar los de la persona en el acto.
- **Fuente:** `docs/arquitectura.md` §3.1 (RF-01), §7.7 y §11.6. `docs/lenguaje.md` §14.3, §31, §36 y §40. `TESTER/2026-11-12-MATU-54-mis-datos.md` y `TESTER/2026-11-09-MATU-72-borrar-al-tiro.md`.

---

## Si preguntan algo que no está aquí

- **Una cifra que no tenemos:** «Eso no lo medimos. Lo que sí medimos es…», y se pasa al dato más cercano con fuente.
- **Una decisión:** se nombra su ADR, que está en `docs/adr/`:
  - el 023: la ficha de tres campos;
  - el 026: la app en el navegador;
  - el 027: un solo cobro;
  - el 028: la ficha ampliada;
  - el 029: la ficha no se imprime;
  - el 030: los roles;
  - el 031: la lista como texto.
- **Cuánto se construyó:** al 18/11/2026 había 2371 funciones de prueba en el backend y 103 archivos de prueba en la web, y hoy hay 36 migraciones reversibles (`parte-tecnica-jorge.md` §1 y `docs/arquitectura.md` §7.8).

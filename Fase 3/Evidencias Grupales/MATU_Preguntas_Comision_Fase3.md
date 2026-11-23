# MATU · Presentación final · Preguntas probables de la comisión

**Versión 1.0 · 23/11/2026** · Lo escribe el guionista para la presentación final (MATU-104). Va con `MATU_Guion_Presentacion_Fase3.md` y `MATU_Contenido_Laminas_Fase3.md`, en esta misma carpeta.
**Es el criterio 3 de la planilla** (20 puntos). Son 12 preguntas, seis para cada uno, y cada respuesta tiene entre dos y tres frases, unos 30 segundos.

---

## Cómo se responde

- **Responde quien está asignado,** y el otro solo agrega una frase si suma un dato. No se responde a dos voces.
- **Primero la respuesta, después la evidencia.** «Sí, y está en…» convence más que una explicación larga.
- **Si no se sabe, se dice:** «Eso no lo medimos. Lo que sí medimos es…». Nunca se inventa una cifra.
- **La evidencia está en Git.** Si la comisión la pide, se muestra la pestaña de GitHub preparada (guion, sección 7, punto 6).
- **Mismo lenguaje que la app** (`docs/lenguaje.md` §3): «autorización», «cortar el enlace», «Quién la vio», «cuándo se acaba».

| # | Pregunta | Responde |
|---|---|---|
| 1 | ¿Escala? ¿Qué pasó con la carga? | Martín |
| 2 | ¿Cómo protegen los datos de salud? | Jorge |
| 3 | ¿Quién autoriza por la persona cuidada, si ella no puede? | Jorge |
| 4 | ¿Por qué una app en el navegador y no una nativa? | Martín |
| 5 | ¿Cómo controlaron la calidad con agentes de IA? | Jorge |
| 6 | ¿Qué pasa si se quita la capa 3? | Martín |
| 7 | ¿Se sostiene el negocio? | Jorge |
| 8 | ¿Qué faltó? | Martín |
| 9 | ¿Por qué un solo cobro y no una reserva? | Martín |
| 10 | ¿Cómo saben que el problema existe? | Jorge |
| 11 | ¿Por qué el objetivo 7 llegó un día tarde? | Martín |
| 12 | ¿Qué datos guardan de la persona, y quién los ve? | Jorge |

---

## 1. ¿Escala? ¿Qué pasó con la carga?

- **Responde:** Martín
- **Respuesta:** Para el piloto, sí: con diez compras simultáneas sobre una base recién preparada, no hubo fallos y las medianas fueron de 453 ms al confirmar y de 421 ms en el retorno del pago. Encontramos una limitación: con los pedidos de cinco corridas acumulados en la base, esas dos medianas se duplicaron, porque el pago se encarece con el volumen. No se corrige en el semestre, porque la demo se restablece desde cero, pero antes de producción se mide con volumen creciente, se confirma qué consulta crece y se corrige con una migración revisada.
- **Si repreguntan por la causa:** la más probable es el costo de las políticas de seguridad por fila de las tablas del pago (`transaccion_pasarela`, `cargo` y `participacion`) o un índice que falta. No está confirmada.
- **Si repreguntan por 50 compras simultáneas:** esa es la meta de producción (percentil 95 bajo 800 ms), y se mide en un equipo representativo. En el computador de prueba, de 2 núcleos y con un solo proceso de la API, todos los pasos subían juntos con 50: eso apunta a la máquina, no a un paso del código.
- **Fuente:** `TESTER/2026-11-22-MATU-80-carga-meta.md`, anexo. `TESTER/2026-11-20-MATU-80-k6-tercera.md`. `docs/arquitectura.md` §2.2, RNF-05, con los párrafos «La meta de RNF-05 para el piloto» y «El pago se encarece con el volumen».

## 2. ¿Cómo protegen los datos de salud?

- **Responde:** Jorge
- **Respuesta:** Cada familia está aislada en PostgreSQL con Row Level Security forzado, la app entra con un rol sin privilegios de dueño y un recurso de otra familia responde 404, lo que verifican 270 pruebas en cada push. La ficha va cifrada con AES-256-GCM y una clave por persona, nunca aparece en registros, direcciones ni en el almacenamiento del navegador, y destruir la clave la deja ilegible. La Ley 21.719, en plena vigencia desde el 1 de diciembre de 2026, trata los datos de salud como sensibles, y la tomamos como requisito de diseño: MATU no pide datos clínicos, tiene su política de privacidad y su registro de tratamientos, y el analista normativo revisó antes y al cierre cada historia con datos personales.
- **Si repreguntan por la clave maestra:** hoy está en una variable de entorno, porque solo hay datos sintéticos. Antes de tratar datos reales pasa a un servicio de custodia, sin tocar el cifrado, porque está detrás de un puerto.
- **Fuente:** `docs/arquitectura.md` §2.2 (RNF-07 y RNF-08), §11.4 y §11.6. `parte-tecnica-jorge.md` §3 (270 pruebas). `docs/legal/politica-privacidad.md` y `docs/legal/registro-tratamientos.md`. `CLAUDE.md` §3 (analista normativo) y §5.

## 3. ¿Quién autoriza por la persona cuidada, si ella no puede?

- **Responde:** Jorge
- **Respuesta:** Sin una autorización vigente, MATU no guarda ni muestra la ficha. Al registrar a la persona, MATU anota quién autoriza y en qué calidad: la propia persona, su representante legal o quien la cuida de hecho, que hace una declaración, ve un aviso de su límite y la renueva cada año. La ficha, los insumos y los pedidos tienen cada uno su propia autorización, y cada una se puede retirar.
- **Si repreguntan si eso basta ante la ley:** no lo sabemos, y lo decimos. Si basta la declaración de quien cuida de hecho es la pregunta central de la consulta legal, que tiene 75 preguntas abiertas. Por eso MATU trata solo datos sintéticos hasta tener la respuesta. En la demo, María está autorizada por Carmen como cuidadora de hecho.
- **Fuente:** `docs/arquitectura.md` §11.5. `docs/lenguaje.md` §6.4, §6.4b y §22. `parte-tecnica-jorge.md` §5.2. `docs/legal/consulta-legal.md`. La calidad de la autorización de María: `infra/semillas/demo.py`.

## 4. ¿Por qué una app en el navegador y no una nativa?

- **Responde:** Martín
- **Respuesta:** MATU es una app móvil que en el semestre corre en el navegador del teléfono, sin instalar nada, por una decisión del 14 de octubre que sugirió el profesor guía. Nos dio un solo lenguaje para la familia, el relevo, el comercio y la operación, la accesibilidad que trae el navegador, y algo clave para el relevo: abrir la ficha con un enlace, sin descargar nada. Una participante de la usabilidad lo dijo así: «Me gusta que sea rápido de usar en el celular, sin tener que descargar aplicaciones pesadas».
- **Si repreguntan por los límites:** en iPhone, los avisos push solo llegan si se agrega MATU a la pantalla de inicio, así que el correo es el canal garantizado. La app nativa se decide con los datos del piloto, y con lo que ya está en React, React Native sería el camino más corto.
- **Fuente:** `docs/adr/ADR-026-aplicacion-web.md`. `docs/usabilidad/ronda-2-informe.md`, citas (P1). `docs/arquitectura.md` §17, riesgo del push en iPhone.

## 5. ¿Cómo controlaron la calidad con agentes de IA?

- **Responde:** Jorge
- **Respuesta:** Cada agente tiene un perímetro: el orquestador no programa, el backend no toca la interfaz, el QA solo prueba y reporta, el analista normativo revisa antes y al cierre lo que toca datos o dinero, y el diseñador especifica y revisa cada pantalla. El código generado cumple la misma definición de terminado que el escrito a mano: el CI corre en cada push el análisis estático, la detección de secretos, las migraciones que suben y bajan, y las pruebas de aislamiento, de arquitectura y de trazabilidad, y nada entra a `main` sin la revisión de Martín, que dejó 45 informes. Y medimos el efecto en vez de suponerlo: un factor de 1,86 en 40 tarjetas, contando solo las horas de Jorge, no las de los agentes.
- **Si repreguntan por el factor:** son las horas estimadas sin IA divididas por las horas reales. En el semestre, 154,5 h estimadas contra 83,11 h reales. El sprint 5 dio 1,09, porque sus tarjetas fueron correcciones chicas, y está informado así.
- **Fuente:** `CLAUDE.md` §3 y §5. `docs/sprints/sprint-5-planificacion.md` §8 («Con vibecoding no hay excepciones»). `parte-tecnica-jorge.md` §2.3 (trazabilidad) y §4. ADR-030. `TESTER/`.

## 6. ¿Qué pasa si se quita la capa 3?

- **Responde:** Martín
- **Respuesta:** Se apaga con un interruptor, `CAPA3_HABILITADA`, y la API arranca sin los módulos del despacho: el contrato de la API muestra solo las capas 1 y 2. Hay 21 pruebas que verifican que nada de las capas 1 y 2 depende de la capa 3, y que la ficha, compartir, el relevo con PIN, el consumo y los avisos funcionan con ella bloqueada. La familia sigue con su lista de insumos, que se imprime o se comparte y sirve en cualquier tienda: es el objetivo 5, operativo sin convenio comercial.
- **Si repreguntan por qué se diseñó así:** porque ningún convenio con comercios estaba garantizado. El despacho desacoplable elimina el único punto de falla externo del proyecto.
- **Fuente:** `TESTER/2026-11-05-MATU-40-capa3-desacoplable.md` (`test_capa3_desacoplable.py`). `docs/arquitectura.md` §1, decisión 2. `docs/adr/ADR-031-lista-insumos-solo-texto.md`.

## 7. ¿Se sostiene el negocio?

- **Responde:** Jorge
- **Respuesta:** Es un ejercicio de viabilidad sobre 200 familias, con la canasta medida en las entrevistas (una mediana de $70.000 y una compra al mes), una comisión del 10 %, una última milla supuesta de $3.500 y $600.000 de costos fijos. Solo con el despacho cada familia deja $1.400 al mes y harían falta 429, y con la suscripción de $5.990 deja $7.210 y bastan 84, que en una comuna de 100.000 habitantes es alcanzable. Lo que falta saber es cuánto cuesta conseguir cada familia, y la ampliación mostró que el municipio es un canal concreto.
- **Si repreguntan si ya se cobra:** no. Cobrar la suscripción (RF-41) queda fuera del semestre a propósito: el cálculo es de viabilidad, no un compromiso de alcance.
- **Si repreguntan por la disposición a pagar:** seis de diez ya pagan por algún servicio de cuidado. Ocho dijeron que sí a $5.990, y cuatro lo condicionaron a que resuelva los insumos. Por eso el precio se sostiene sobre las capas 1 y 2 juntas, nunca sobre la ficha sola.
- **Fuente:** `docs/arquitectura.md` §16.1, §16.2, §16.4 y §16.6. `docs/resultados-entrevistas.md` §3 (H4), §4 y §8 (H7).

## 8. ¿Qué faltó?

- **Responde:** Martín
- **Respuesta:** Del semestre faltaron tres cosas, y las dijimos en la presentación:
  - el objetivo 7 se cumplió el 20 de noviembre, un día tarde;
  - RF-31, conciliar la boleta del comercio, no se construyó, porque sin comercios reales no hay boletas, y quedó en el Product Backlog;
  - y el pago se encarece con el volumen, con su plan para antes de producción.

  Para operar con datos reales faltan la consulta legal, con 75 preguntas abiertas, la clave maestra en un servicio de custodia, el borrado automático a los 3 años de los accesos de relevo y de lo que se anotó de cada apertura, una persona jurídica para usar Webpay en producción y los convenios con comercios.
- **Fuente:** `TESTER/2026-11-20-MATU-80-recorridos.md`. `parte-tecnica-jorge.md` §2.3 y §5.2. `docs/arquitectura.md` §2.2 (RNF-05), §11.4, §16.6 y §18.1.

## 9. ¿Por qué un solo cobro y no una reserva?

- **Responde:** Martín
- **Respuesta:** La captura diferida de Transbank solo funciona con crédito, el débito es el medio más usado por estas familias, y una retención mayor que el pedido es difícil de explicar, como observó el análisis de la Ley 19.496. Con precios exactos, la familia ve el total antes de pagar, se cobra una sola vez en venta normal de Webpay Plus, y si un producto falta se anula su parte a la misma tarjeta. El 10 de noviembre lo probé contra el ambiente de integración, con crédito, débito, una anulación parcial de $8.990 con los dos medios y un retorno duplicado que dejó un solo cobro, y los cuatro casos dieron PASS.
- **Fuente:** `docs/adr/ADR-027-precios-exactos.md`. `parte-tecnica-jorge.md` §3.2. `TESTER/2026-11-10-MATU-62-transbank-venta-normal.md`.

## 10. ¿Cómo saben que el problema existe?

- **Responde:** Jorge
- **Respuesta:** Antes de entrevistar escribimos siete hipótesis, cada una con el resultado que la validaba y el que la refutaba. Con diez entrevistas a cuidadoras, entre agosto y septiembre, y cuatro más a familiares que aportan, H1 se refutó y la ficha bajó a tres campos, y las otras seis quedaron validadas, tres de ellas con la ampliación. Después, en la segunda ronda de usabilidad, ya con la app, tres de tres completaron la ficha en menos de tres minutos y armaron el pedido en menos de seis.
- **Si repreguntan por los límites de la muestra:** las diez primeras llegaron por la red del equipo, y lo declaramos. Por eso la ampliación se reclutó solo por un canal concentrado: los grupos de personas mayores del municipio. En la usabilidad, dos de tres tenían el mismo perfil, y también está escrito.
- **Fuente:** `docs/protocolo-entrevistas.md` §7. `docs/resultados-entrevistas.md` §1, §3 y §8. `docs/adr/ADR-023-cierre.md`. `docs/usabilidad/ronda-1-informe.md` y `docs/usabilidad/ronda-2-informe.md`.

## 11. ¿Por qué el objetivo 7 llegó un día tarde?

- **Responde:** Martín
- **Respuesta:** El objetivo decía 19 de noviembre, pero la última fila de PR con migraciones, del #123 al #127, se fusionó y se desplegó en orden, y la última revisión terminó el 20. Ese día desplegué `main` en la demo y recorrí los seis recorridos en el teléfono, con OK en todos. Preferimos un día tarde a desplegar migraciones fuera de orden, porque cada una se apila sobre la anterior y una prueba exige que haya una sola cabeza.
- **Fuente:** `TESTER/2026-11-20-MATU-80-recorridos.md`, «Despliegue» y la tabla de R1 a R6. `docs/arquitectura.md` §7.8 (`test_cadena_migraciones.py`) y §15.5, punto 3.

## 12. ¿Qué datos guardan de la persona, y quién los ve?

- **Responde:** Jorge
- **Respuesta:** De la persona guardamos su nombre, el nivel de apoyo, la ficha que escribe la familia, cifrada, y lo que usa, sin datos clínicos. Cada uno ve lo suyo:
  - quien «Se informa» no ve montos;
  - el relevo ve solo las secciones que se eligieron al compartir, y hasta que vence el enlace;
  - el comercio ve solo los productos, sin la persona ni la dirección;
  - el equipo de operación nunca ve la ficha.

  Y la familia puede descargar una copia de sus datos desde la app, en «Tus datos», o borrar los de la persona en el acto.
- **Fuente:** `docs/arquitectura.md` §3.1 (RF-01), §7.7 y §11.6. `docs/lenguaje.md` §14.3, §31 (MATU-113), §36 y §40. `TESTER/2026-11-12-MATU-54-mis-datos.md` y `TESTER/2026-11-09-MATU-72-borrar-al-tiro.md`.

---

## Si preguntan algo que no está aquí

- **Sobre una cifra que no tenemos:** «Eso no lo medimos. Lo que sí medimos es…», y se pasa al dato más cercano con fuente.
- **Sobre una decisión:** se nombra su ADR. Están en `docs/adr/`: el 023 (la ficha de tres campos), el 026 (la app en el navegador), el 027 (un solo cobro), el 028 (la ficha ampliada), el 029 (la ficha no se imprime), el 030 (los roles) y el 031 (la lista como texto).
- **Sobre cuánto se construyó:** en los sprints 3 a 5 se fusionaron 93 PR en el repositorio del código. Al 18/11/2026 había 2371 funciones de prueba en el backend y 103 archivos de prueba en la web, con 36 migraciones reversibles hasta hoy (`parte-tecnica-jorge.md` §1 y `docs/arquitectura.md` §7.8).

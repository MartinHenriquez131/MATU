# Revisión previa del analista normativo · MATU-54 · Mis datos: ver y descargar todo lo que MATU guarda de la persona

**11 de noviembre de 2026, madrugada** · Agente analista normativo, a pedido de Jorge · Estado: **decisiones D-54-1 a D-54-13 pendientes de Jorge**

Esto no es asesoría legal: sirve para que Jorge decida. Lo que queda en REQUIERE CONSULTA LEGAL va a `consulta-legal.md`, desde la CL-61. El analista leyó las cinco revisiones de esta noche (MATU-61, 55, 62, 42/53 y 46) y esta revisión no contradice ninguna. Depende de dos de ellas: la 0024 de MATU-55, para los ingresos de la cuenta, y la D-42-10, para mostrar a quien salió del grupo.

**Nota del orquestador:** los faltantes 2 (la persona cuidada entra con su propia cuenta) y 3 (corregir los datos) de la sección 8 quedaron como tarjetas propias en el Product Backlog: MATU-90 y MATU-91.

## 0. Resumen para la planificación

- **Hay que corregir un hallazgo del código antes de construir «Quién abrió o editó la ficha».** La auditoría no guarda a qué persona se refiere cada fila. `plan.editar` y `plan.quitar_seccion` guardan el id de la sección (`care_plan/infrastructure/auditoria_ficha.py:64,73,81`). `consumo.*`, `alerta.*` y `reposicion.declarar` guardan el id de su fila. Esas filas se borran al quitar una sección, al destruir la clave a los 90 días o al eliminar un insumo, y entonces la auditoría ya no se puede asociar a la persona. En un grupo que cuida a dos personas, la copia saldría incompleta o mezclada. Se propone la **0028** (sección 2).
- **Los ingresos de la cuenta dependen de la 0024 de MATU-55.** MATU-54 no repite esa política. Si por algún motivo MATU-54 se fusionara antes que MATU-55, lleva ella `auditoria_cuenta_propia` y MATU-55 la quita de la suya (regla de «una sola vez, en la que vaya primero»).
- **La acción nueva de auditoría no necesita migración.** `auditoria.accion` y `auditoria.entidad` son texto sin `CHECK`, y la descarga se registra sin detalle. El `CHECK auditoria_detalle_acotado` no cambia, así que no hay choque con la 0026 (D-42-8) ni con la 0027.
- **La política §9 hoy contradice la historia.** Dice «MATU no imprime ni exporta la ficha». Hay que reescribirla, y eso obliga a publicar una versión nueva (regla de MATU-75: cambia la huella).
- **Dos contradicciones de fecha:** el ADR-029 (línea 30) y la arquitectura 11.1 (línea 1279) ponen MATU-54 en el **sprint 5**. La tarjeta está en el sprint 4. Hay que corregirlo en `docs/`.

## 1. Veredicto por punto

| # | Punto | Veredicto | Condiciones y notas |
|---|---|---|---|
| P1 | **Quién pide la copia de la persona, y con qué base** | Para admin y cuidador, **CUMPLE** con condiciones. Que actúen en nombre de la persona **REQUIERE CONSULTA LEGAL** (CL-04 ampliada y CL-61). La propia persona con cuenta: hoy **NO CUMPLE** en la app, porque el modelo no la vincula con una cuenta. Por ahora lo pide por correo (CL-30 ampliada) | La Ley 19.628, art. 12, da a la titular el derecho a saber qué datos hay sobre ella, de dónde vienen, para qué se guardan y a quién se comunican. La Ley 21.719 mantiene el acceso y agrega la portabilidad, pero el analista no cita su artículo. **C1:** pueden pedirla admin y cuidador, los mismos que retiran y borran (MATU-44 y MATU-72). Pagador, observador, otro grupo y persona borrada reciben 404. **C2:** no importa quién dio la autorización, igual que en el retiro. **C3:** con la autorización retirada o en pausa se puede pedir igual, pero sin el texto de la ficha ni lo anotado de los insumos (D-54-5) |
| P2 | **Qué incluye y qué no** | **CUMPLE** con condiciones (D-54-4). Llevar datos de terceros en la copia de la titular **REQUIERE CONSULTA LEGAL** (CL-61) | Ver la sección 3. **C4:** nunca el teléfono del relevo, ni el correo o el celular de otros miembros, ni `usuario_id` o cualquier otro id interno, ni `ip`, `request_id`, hashes de token o PIN, `evidencia` en bruto, `referencia_documento`, `push_token` ni la clave. **C5:** respuesta con `extra="forbid"` y una prueba que falle si aparece cualquiera de esos campos. **C6:** columnas nombradas, sin `SELECT *` |
| P3 | **Formato, ADR-029, servidor o cliente, archivo en el teléfono** | **CUMPLE** con condiciones (D-54-3). Si el JSON basta como formato portable **REQUIERE CONSULTA LEGAL** (CL-63) | **C7:** lo legible es la pantalla, que muestra «Esta pantalla no se imprime.» en la impresión, igual que el resto de la app. No hay PDF, ni HTML, ni estilo de impresión. **C8:** lo estructurado es un archivo JSON, que arma el servidor en un solo GET y en una transacción de lectura coherente. El cliente lo guarda tal como llegó, desde la memoria (Blob, `URL.createObjectURL` y `revokeObjectURL` de inmediato). **C9:** el archivo se llama `matu-datos-AAAA-MM-DD.json`, sin el nombre de la persona, porque queda en la lista de descargas. **C10:** el JSON empieza con un `aviso` fijo: es una copia para ejercer derechos y no la ficha para un relevo. **C11:** aviso en pantalla antes de descargar: el archivo queda en el teléfono, fuera de MATU, no vence y MATU no lo borra |
| P4 | **Qué se muestra de la auditoría de la ficha, de la cuenta y de los avisos** | Hoy **NO CUMPLE**: la cuenta no se puede leer (P2-2) y la ficha no se puede asociar a la persona (hallazgo). Con la 0024, la 0028 y las condiciones, **CUMPLE** | **C12:** de la ficha, quién (nombre), qué (texto de `lenguaje.md`) y cuándo, y el tipo de sección si es adicional. Nunca el texto. **C13:** cada rol ve lo que hoy le deja ver RLS (0005 y 0010): el admin ve todo, el cuidador ve lo suyo y las aperturas del relevo (D-54-6). **C14:** quien salió del grupo aparece según la D-42-10. **C15:** la cuenta se ve solo en «Tus datos», con la 0024. **C16:** los avisos enviados van en la copia de cada cuenta (`notificacion_propia` ya existe), con la fecha, el canal y si salió. Nunca el texto ni el destino. **C17:** en el piloto un aviso simulado queda como `enviada`, y la pantalla no puede decir que salió (D-54-11) |
| P5 | **Registro de cada descarga** | **CUMPLE** con condiciones. **No hace falta un `CHECK` nuevo** | **C18:** `persona.datos_descargar` (con grupo, entidad `persona_cuidada`) y `cuenta.datos_descargar` (sin grupo, en `ACCIONES_DE_CUENTA`), sin detalle. **C19:** una fila por cada GET que entrega datos, en la misma transacción. Si la inserción falla, no se entregan los datos. **C20:** no se registra si el archivo se guardó, porque el navegador no lo confirma (mismo criterio que MATU-60). **C21:** la fila de la persona aparece en «Quién abrió o editó la ficha» como «Pidió una copia de los datos». No se agrega un `plan.leer` aparte |
| P6 | **Límites: frecuencia, tamaño y plazo** | **CUMPLE** con condiciones. El plazo legal y si un límite es compatible con la gratuidad **REQUIEREN CONSULTA LEGAL** (CL-48 ampliada y CL-63) | **C22:** gratis y sin pasos extra. **C23:** 10 copias por hora por cuenta, con un contador por huella HMAC en Redis que dura 1 hora, y un 429 con texto. **C24:** la pantalla muestra 90 días de historial con «Ver más», y el archivo trae todo lo guardado (D-54-9). **C25:** la app entrega en el momento, y el correo sigue con su plazo (acuse en 2 días hábiles y respuesta en 30 días corridos) para lo que la app no da |
| P7 | **Política, registro y `lenguaje.md`** | **NO CUMPLE** hasta que se publique | §9 contradice la copia. §13 la lista como pendiente. §6 (línea 220) promete que la auditoría de la ficha se puede consultar, y hoy no hay pantalla. `lenguaje.md` 29 manda a pedir la copia por correo. El registro, entrada 5, dice «la API no expone las compras». Ver la sección 6 |
| P8 | **El cliente, los logs y la caché (DdT)** | **CUMPLE** con condiciones | **C26:** nada en `localStorage`, `sessionStorage`, `history.state`, URL ni `document.title`, y la ruta sin parámetros de datos. **C27:** `Cache-Control: no-store`, que ya ponen los middlewares de `/v1/personas-cuidadas/` y `/v1/cuenta` (`main.py:103-106`). Hoy no hay un service worker que guarde respuestas, y debe seguir así. **C28:** la ficha se descifra solo con la autorización `VIGENTE` según el `Reloj`, por la misma dependencia de la ficha (`care_plan/api/dependencias.py`), con su 404 si la clave está destruida. **C29:** ningún log lleva el cuerpo de la respuesta, nombres, teléfonos ni texto, con una prueba |
| P9 | **Accesibilidad (Ley 20.422)** | **CUMPLE** con condiciones | El JSON no es legible para una persona, así que **la pantalla es el formato accesible**. **C30:** encabezados por bloque, listas semánticas, fechas `DD/MM/AAAA` y hora de 24 horas, 17 px en rem, sin desplazamiento horizontal a 320 px con el texto al 200 %, botones de 48 px y el aviso antes de descargar en un diálogo que atrapa el foco y lo devuelve |

## 2. ¿Migración? Sí: la 0028, con `down_revision = "0027"`

**Por qué:** la copia tiene que decir quién abrió o editó la ficha de **esa** persona, también después de quitar una sección o de destruir la clave. Hoy eso no se puede, porque las filas apuntan a ids que se borran (hallazgo de la sección 0).

**Qué no depende de la 0028:** la acción nueva (texto sin `CHECK`), la lectura de la cuenta (0024 de MATU-55), las compras (`reposicion_leer`, 0011), los avisos propios (`notificacion_propia`) y la aceptación (`aceptacion_propia_leer`, 0021).

**Con la 0023 a la 0027 no hay choque:** no toca `auditoria_detalle_acotado` (0026) ni `acceso_relevo` (0027).

> **Nota (MATU-100, 13-11):** este borrador quedó reemplazado por la 0028 fusionada. Las diferencias son tres: la acción nueva sí lleva `CHECK` (`auditoria_cuenta_acotada` pasa a 15 acciones); la referencia es una FK compuesta `(persona_cuidada_id, grupo_id)` con `persona_cuidada_id_grupo_uq`, y se agrega `auditoria_persona_obligatoria` (NOT VALID); y el índice es `(persona_cuidada_id, ocurrido_en DESC, id DESC)`. La fuente es la migración y `docs/modelo-datos.md`.

**Borrador** (con D-54-7 (a). La forma la decide el backend):

```sql
-- upgrade
ALTER TABLE auditoria ADD COLUMN persona_cuidada_id uuid REFERENCES persona_cuidada(id);
ALTER TABLE auditoria ADD CONSTRAINT auditoria_persona_con_grupo
    CHECK (persona_cuidada_id IS NULL OR grupo_id IS NOT NULL);
CREATE INDEX auditoria_persona_ix ON auditoria (persona_cuidada_id, ocurrido_en DESC)
    WHERE persona_cuidada_id IS NOT NULL;
COMMENT ON COLUMN auditoria.persona_cuidada_id IS
    'MATU-54: la persona a quien se refiere la acción, para su copia de datos. Sin relleno de filas anteriores';

-- downgrade (en orden inverso). Nunca borra registros de auditoría
DO $$ BEGIN
    IF EXISTS (SELECT 1 FROM auditoria WHERE persona_cuidada_id IS NOT NULL) THEN
        RAISE EXCEPTION 'MATU-54: hay auditoría asociada a personas. El downgrade no borra registros';
    END IF;
END $$;
DROP INDEX auditoria_persona_ix;
ALTER TABLE auditoria DROP CONSTRAINT auditoria_persona_con_grupo;
ALTER TABLE auditoria DROP COLUMN persona_cuidada_id;
```

**Notas para quien implemente:**
- **Sin relleno de filas anteriores.** `auditoria_solo_insercion` rechaza todo UPDATE, y no se debe apagar ese trigger. Las filas anteriores se asocian por la entidad mientras exista, o por el grupo si cuida a una sola persona. Las que no se puedan asociar se omiten, y la copia lo dice. En el piloto solo hay datos sintéticos.
- La FK es segura: `persona_cuidada` no se borra, solo se anonimiza (MATU-72).
- Hay que verificar que el `INSERT` de `matu_app` sobre `auditoria` cubra la columna nueva, si el permiso es por columna.
- **Código:** `EntradaAuditoria` suma `persona_cuidada_id` (opcional, exige grupo), y lo llenan las acciones de la ficha, del relevo, de las autorizaciones, de los insumos, de las alertas, de las compras, `persona.borrar` y `persona.datos_descargar`.
- Una prueba comprueba que la persona de la fila es del mismo grupo. No se usa un trigger, porque el relevo no puede leer `persona_cuidada` con RLS.
- **Coordinación con la 0024:** MATU-54 la necesita en `main`. Si se invierte el orden, la política `auditoria_cuenta_propia` va en la migración de MATU-54 y sale de la de MATU-55.

**Si Jorge elige D-54-7 (b):** no hay migración, y la limitación se declara en la política y en el registro.

## 3. Qué lleva cada copia

**«Datos de {nombre_pila}»** (admin y cuidador):
- **La persona:** nombre, nombre de pila, nivel de apoyo, dirección (calle, número, depto, comuna, región y referencia) y fecha de alta.
- **Autorizaciones:** cada una con su finalidad, estado, calidad (que ya ven admin y cuidador), versión de la política, declaración y aviso vistos (identificador y versión), quién la registró (nombre), fecha, revisión de los 12 meses, retiro y motivo. **Sin** `referencia_documento`: la copia dice que existe y que se pide por correo (D-54-4).
- **Ficha:** los tres campos y las secciones adicionales, con su texto, quién escribió cada una (nombre) y cuándo. Solo con la autorización `VIGENTE` (C28). «A quién llamar» va tal como se escribió, con los nombres y teléfonos que tenga. **Si la autorización está retirada o en pausa:** el estado y la fecha de borrado, sin texto (D-54-5).
- **Enlaces de relevo:** nombre del relevo, motivo, secciones compartidas, creación, vencimiento, corte, quién lo creó (nombre de pila), veces que se abrió y último uso. Las aperturas van con la fecha, el tipo y las secciones vistas. **Sin el teléfono** (D-54-4).
- **Insumos**, solo con la autorización de insumos `VIGENTE`: nombre del producto o el nombre escrito, unidad, cuánto usa cada cuántos días, lo que quedaba y cuándo, días de aviso, unidades por envase y si se sigue. **Compras anotadas de los últimos 90 días:** cantidad, fecha y quién (nombre). **Avisos de insumos:** fecha prevista, estado y fechas. Es la primera ruta que lee las compras, y el registro, entrada 5, lo tiene que decir.
- **Quién abrió o editó la ficha**, más el historial de autorizaciones, enlaces e insumos: lo que el rol puede leer por RLS (C13).
- **No lleva:** los avisos enviados a otros miembros, que son datos de ellos, la lista de miembros, y los correos o celulares de nadie.

**«Tus datos»** (cualquier cuenta, también pagador y observador):
- nombre, correo, celular completo, si está confirmado y el canal de los códigos;
- la aceptación de la política: versión, fecha y huella;
- los grupos con su nombre y el rol en cada uno;
- los dispositivos: nombre general, creación y último uso, sin `push_token`;
- los ingresos y eventos de seguridad que fije la D1 de MATU-55, con la 0024;
- la preferencia de avisos;
- los avisos enviados, con fecha, canal y estado.

Nunca la contraseña transformada, el secreto del doble factor, la huella del email, los hashes de sesión ni nada de una persona cuidada.

**Formato del JSON:**
- `"formato": "matu-datos/1"` y la fecha en que se generó;
- fechas ISO 8601 con desfase de Chile;
- nombres de campo en español y sin ids internos;
- el `aviso` fijo de C10.

## 4. Decisiones para Jorge (con la recomendación del analista)

- **D-54-1 · Quién pide la copia de la persona.** (a) Admin y cuidador. (b) Además, el pagador con permiso de ver la ficha. (c) Solo el admin. (d) Solo quien dio la autorización. **Se recomienda (a):** son los que ya ven todo y los que retiran y borran. La (d) deja sin salida a la persona si quien autorizó salió del grupo.
- **D-54-2 · Dos copias separadas.** (a) «Datos de {nombre_pila}» en Grupo familiar, y «Tus datos» en Tu cuenta para toda cuenta. (b) Un solo archivo con la persona y la cuenta de quien descarga. **Se recomienda (a):** la copia de la persona no debe llevar el celular de quien la pidió, y el pagador y el observador también tienen derecho a la suya.
- **D-54-3 · Formato.** (a) Lo legible en pantalla y el JSON como archivo, con un solo GET y el archivo guardado desde la memoria. (b) Además, un archivo legible (HTML o texto). (c) PDF. **Se recomienda (a):** un archivo legible o un PDF es, en la práctica, la hoja imprimible que el ADR-029 quitó. La tarjeta dice «en un formato legible y en uno estructurado», y (a) lo cumple con la pantalla.
- **D-54-4 · Datos de terceros.** (a) Se incluyen los nombres (relevos, miembros, quien comparte) y «A quién llamar» tal cual. No van el teléfono del relevo, el correo ni el celular de otros, ni la referencia al documento. (b) Además, el teléfono del relevo mientras exista. (c) Sin ningún nombre de terceros. **Se recomienda (a):** el art. 12 de la Ley 19.628 incluye saber a quién se comunican los datos, y el teléfono no habla de la titular y se borra a los 30 días (MATU-46). Con CL-61.
- **D-54-5 · Autorización retirada o en pausa.** (a) La copia va sin el texto de la ficha ni los insumos, con su estado y la fecha de borrado. (b) Con el texto. **Se recomienda (a):** la política promete que en ese plazo «nadie lo puede leer». Si la titular lo pide, va a CL-62.
- **D-54-6 · La auditoría que ve cada rol.** (a) Como hoy, por RLS (admin todo, cuidador lo suyo y las aperturas). (b) Una política nueva para que el cuidador vea todo, lo que cambia §6 y la versión. **Se recomienda (a),** con el texto de C13.
- **D-54-7 · Asociar la auditoría a la persona.** (a) La 0028 con `persona_cuidada_id`, sin relleno. (b) Sin migración: unir por la entidad y declarar el límite. (c) Solo cambiar la entidad de `plan.editar` a `plan_cuidado`, que arregla la ficha y no los insumos. **Se recomienda (a).**
- **D-54-8 · Acción de auditoría.** (a) `persona.datos_descargar` y `cuenta.datos_descargar`, sin detalle. (b) Con el formato en el detalle, que obliga a cambiar el `CHECK` después de la 0026. **Se recomienda (a):** hay un solo formato.
- **D-54-9 · Cuánto trae.** (a) En pantalla, 90 días de historial con «Ver más», y el archivo con todo lo guardado. (b) Todo en pantalla. (c) 90 días en las dos. **Se recomienda (a):** el derecho alcanza a todo lo que se guarda.
- **D-54-10 · Límite.** (a) 10 copias por hora por cuenta, con 429. (b) Sin límite. **Se recomienda (a),** con CL-63.
- **D-54-11 · Avisos simulados del piloto.** (a) Se muestran con «En el piloto no salió». (b) Se ocultan. **Se recomienda (a):** decir «Salió» sería falso.
- **D-54-12 · La versión de la política.** La que toque según la pregunta abierta de la revisión de MATU-42 (una 0.12 compartida, o una versión por fusión). **No se pide aceptar de nuevo:** no agrega usos, datos ni destinatarios, porque la copia llega a quien ya ve esos datos. Queda con CL-24.
- **D-54-13 · El nombre en pantalla.** (a) «Datos de {nombre_pila}» y «Tus datos». (b) «Mis datos» para las dos. **Se recomienda (a):** «Mis datos» confunde cuando los datos son de otra persona.

## 5. Pruebas sugeridas

- **Aislamiento:**
  - pagador, observador, otro grupo, persona borrada y relevo reciben 404;
  - en `test_aislamiento.py`, A no lee la auditoría de una persona de B, ni con `persona_cuidada_id`;
  - la columna nueva no abre lecturas nuevas.
- **Contenido:**
  - la respuesta no trae teléfono del relevo, correos, celulares de otros, ids, `ip`, `request_id`, hashes, `evidencia` en bruto, `referencia_documento` ni `push_token` (`extra="forbid"`);
  - «Tus datos» no trae nada de una persona cuidada.
- **Autorización:**
  - retirada, en pausa o con la clave destruida, la copia va sin texto de la ficha y sin insumos (con `RelojFijo`);
  - vigente, el texto llega descifrado y completo.
- **Roles:** el cuidador ve solo sus filas y las aperturas del relevo, y el admin ve todas.
- **Asociación:**
  - con dos personas en el grupo, una sección quitada y una clave destruida se atribuyen a la persona correcta;
  - una fila con persona de otro grupo falla.
- **Auditoría:**
  - una fila por GET, sin detalle y en la misma transacción;
  - si falla, no hay datos (con el registro forzado a fallar).
- **Cabeceras y límite:** `Cache-Control: no-store` también en 404 y 429, y la copia 11 en una hora da 429.
- **Logs:** tras la descarga, sin nombres, teléfonos ni texto.
- **Piloto:** un aviso simulado no aparece como enviado.
- **Migración:** `upgrade`, `downgrade` y `upgrade` de la 0028, y el downgrade se detiene si hay filas con persona.
- **Frontend:**
  - nada en el almacenamiento, la URL ni `history.state`;
  - el nombre del archivo es genérico;
  - la impresión muestra «Esta pantalla no se imprime.».

## 6. Documentos que hay que actualizar (borradores)

### `politica-privacidad.md`, en la versión de D-54-12

- **Encabezado:** «MATU-54: se ajustan las secciones 4, 6, 9, 10 y 13 con la copia de los datos desde la aplicación. No agrega usos, datos ni destinatarios: la copia la reciben quienes ya ven esos datos. Cambia la versión porque cambia el texto (MATU-75). Nadie vuelve a aceptar.»
- **§4, «De ti», viñeta nueva:** «**Cuando pides una copia de los datos:** la fecha, la hora y quién la pidió. No guardamos la copia ni su contenido.»
- **§6, «Quién abrió o editó la ficha», al final:** «Lo ves en «Datos de» la persona, en «Grupo familiar».»
- **§9, reemplaza «MATU no imprime ni exporta la ficha. Solo se comparte con el enlace con PIN.»:** «MATU no imprime la ficha y no la exporta para compartirla: con un relevo se comparte solo con el enlace con PIN. La única copia que sale de MATU es la que pide quien administra el grupo o cuida a la persona, para ejercer sus derechos (sección 10). Es un archivo para otro programa, no una hoja para imprimir.» `<!-- ADR-029, MATU-54 -->`
- **§10, subsección nueva, «Ver y descargar los datos desde la aplicación»:**
  - «**Tus datos:** en «Tu cuenta», «Tus datos», ves y descargas lo que guardamos de tu cuenta: tu nombre, tu correo, tu celular, la versión de esta política que aceptaste, tus grupos y tu rol, tus dispositivos, tus últimos ingresos, tu elección de avisos y los avisos que te enviamos, sin su texto.»
  - «**Los datos de la persona que cuidas:** quien administra el grupo o quien la cuida los ve y los descarga en «Grupo familiar», «Datos de» la persona: sus datos, sus autorizaciones, su ficha con sus secciones, sus enlaces de relevo y quién los abrió, sus insumos, las compras anotadas de los últimos 90 días, sus avisos de insumos y quién abrió o editó la ficha. Si la persona o su representante legal te lo piden, muéstraselos o entrégales la copia.»
  - «Quien cuida ve en la copia solo lo que hizo él en la ficha. Quien administra ve todo.»
  - «La copia no trae el teléfono del relevo, el correo ni el celular de otras personas del grupo, ni la referencia al documento del representante legal. Si los necesitas, pídelos por correo.»
  - «Si la autorización de la ficha o de los insumos está retirada o en pausa, la copia no trae lo escrito ni lo anotado, porque nadie lo puede leer, y dice hasta cuándo se guarda.» `<!-- PENDIENTE: CL-62 -->`
  - «La copia se descarga en un archivo que otro programa puede leer (JSON). MATU la arma en ese momento y no la guarda. El archivo queda en tu teléfono, fuera de MATU: no vence, no se puede cortar y no se borra si después se borran los datos. No lo uses para compartir la ficha con un relevo.»
  - «Cada vez que alguien pide una copia, MATU registra quién y cuándo, sin el contenido. Es gratis.»
  - «Si la persona que cuidas o su representante no tienen a nadie en el grupo que la pida, o para lo que no está en la aplicación, escribe al correo de esta sección.» `<!-- PENDIENTE: CL-04, CL-30 y CL-61 -->`
- **§13:** se quita «Ver o descargar los datos desde la aplicación…». Si se elige D-54-7 (b), se agrega «La copia no puede asociar a la persona lo que se hizo en una sección ya quitada o en una ficha ya borrada, si el grupo cuida a más de una persona».

### `registro-tratamientos.md`

**Entrada 13 nueva, «Acceso y copia de los datos (MATU-54)»** (la 12 es de MATU-42):
- **Finalidad:** atender el derecho de acceso y de portabilidad de la persona cuidada y de cada cuenta.
- **Titulares:** la persona cuidada, cada persona usuaria y los terceros nombrados en la copia (relevos, miembros y quienes aparecen en «A quién llamar»).
- **Datos:** no se crea ningún dato nuevo. Se lee lo de las entradas 1, 3, 4, 5, 6, 7 y 10, con lo que dice la sección 3 de esta revisión. Se registra `persona.datos_descargar` o `cuenta.datos_descargar`, sin detalle, y `auditoria.persona_cuidada_id` (0028).
- **Base de licitud:** el cumplimiento del derecho de la titular (Ley 19.628, art. 12, y Ley 21.719). Que admin y cuidador lo ejerzan en su nombre: [PENDIENTE: CL-04 y CL-61].
- **Quién accede:**
  - a la copia de la persona, admin y cuidador. El cuidador ve solo sus filas de auditoría y las aperturas del relevo (0005 y 0010);
  - pagador, observador y otro grupo reciben 404;
  - a «Tus datos», cada cuenta, con la 0024 de MATU-55;
  - operación nunca.
- **Conservación:** la copia no se guarda en el servidor. El registro de cada descarga, 3 años, como la auditoría. El archivo que queda en el teléfono no lo alcanzan los plazos de MATU.
- **Medidas:**
  - `no-store`, nada en el almacenamiento del navegador ni en la URL, y nombre de archivo sin datos;
  - se descifra solo con la autorización `VIGENTE`;
  - transacción de lectura coherente y auditoría en la misma transacción;
  - 10 copias por hora por cuenta;
  - sin impresión;
  - logs sin contenido.
- **Comunicaciones a terceros:** ninguna desde MATU.
- **Decisiones automatizadas:** ninguna.

**Otras entradas:**
- **Entrada 3, Medidas:** «la ficha y sus secciones no se imprimen ni se exportan, salvo la copia de la entrada 13».
- **Entrada 5, Medidas:** en vez de «la API no expone las compras (sin ruta de lectura, MATU-51)», «las compras se leen solo en la copia de la entrada 13».
- **Entrada 6, Quién accede:** «la titular ve y descarga la auditoría de su cuenta en «Tus datos» (MATU-54)».

### `consulta-legal.md`
Las CL-61 a CL-63, las ampliaciones de la sección 9, «la próxima es CL-64» y la fila de MATU-54.

### Fuera de `docs/legal/`
- El ADR-029 y la arquitectura 11.1: el sprint de MATU-54.
- El modelo de datos: la columna `auditoria.persona_cuidada_id`.
- `docs/api/README.md`: las dos rutas propuestas y P2-2 cerrado por MATU-55.

## 7. Textos propuestos para `lenguaje.md` (sección 34, «Copia de los datos (MATU-54)»; se publicó como la **35**, porque la 34 quedó para MATU-42)

Sin «auditoría», «registro de accesos», «consentimiento», «sesión», «token», «usuario» ni «exportar». El número 34 sigue a las 31 a 33 de la fila.

| Dónde | Texto |
|---|---|
| Grupo familiar, bloque | Datos de {nombre_pila} · Todo lo que MATU guarda de {nombre_pila}. Si {nombre_pila} o su representante legal te lo pide, puedes mostrárselo o darle una copia. · [botón] Ver los datos de {nombre_pila} |
| Pagador y observador | Los puede ver quien administra el grupo o quien cuida a {nombre_pila}. |
| Pantalla, título y bajada | Datos de {nombre_pila} · Lo que MATU guarda hoy de {nombre_pila}, al {DD/MM/AAAA} a las {HH:MM}. |
| Bloques | Sus datos · Autorizaciones · Su ficha · Enlaces de relevo · Sus insumos · Compras anotadas (últimos 90 días) · Avisos de insumos · Quién abrió o editó la ficha |
| Ficha, autorización retirada | La autorización de la ficha está retirada. Lo escrito sigue guardado sin que nadie lo pueda leer, y se borra el {DD/MM/AAAA}. |
| Ficha, en pausa | La ficha está en pausa porque falta renovar la autorización. Cuando se renueve, vuelve a aparecer aquí. |
| Insumos, autorización retirada | La autorización de los insumos está retirada. Lo anotado se borra el {DD/MM/AAAA}. |
| Relevo | No incluimos su teléfono. |
| Representante legal | Hay una referencia al documento del representante legal. Si la necesitas, pídela a cuidaconmatu@gmail.com. |
| Cuidador, bajo «Quién abrió o editó la ficha» | Aquí ves solo lo que hiciste tú. La lista completa la ve quien administra el grupo. |
| Historial, líneas | Abrió la ficha · Editó «{sección}» · Quitó «{sección}» · Pidió una copia de los datos · {DD/MM/AAAA} a las {HH:MM} · {nombre} |
| Sin poder asociar (solo con D-54-7 b) | Hay cambios anteriores que no podemos mostrar aquí. Si los necesitas, pídelos a cuidaconmatu@gmail.com. |
| Historial largo | Ver más |
| Botón de descarga y ayuda | Descargar en un archivo · Es un archivo (JSON) que otro programa puede leer, para llevar estos datos a otro lugar. |
| Diálogo, título | Antes de descargar |
| Diálogo, texto | El archivo trae todo lo de esta pantalla, también lo escrito en la ficha y los nombres y teléfonos de «A quién llamar». Queda en tu teléfono, fuera de MATU: no vence, no se puede cortar y MATU no lo puede borrar. No lo uses para compartir la ficha con un relevo: para eso está el enlace con PIN. |
| Diálogo, botones | Descargar · No descargar |
| Hecho | Te entregamos el archivo. Búscalo en las descargas de tu teléfono. |
| Error de conexión | No pudimos traer los datos. Revisa tu conexión y vuelve a intentarlo. |
| 429 | Ya pediste los datos varias veces. Vuelve a intentarlo en una hora. |
| Tu cuenta, fila | Tus datos · Ver y descargar lo que MATU guarda de tu cuenta. |
| Tus datos, bloques | Tu cuenta · Política de privacidad · Tus grupos · Tus teléfonos y computadores · Últimos ingresos · Tus avisos · Avisos que te enviamos |
| Tus datos, nota | Lo que guardamos de las personas que cuidas lo ves en Grupo familiar. |
| Avisos enviados, línea | {DD/MM/AAAA} a las {HH:MM} · Por correo · Salió \| No salió |
| Avisos, en el piloto | En el piloto los avisos se prueban sin enviarse: aparecen aquí, pero no te llegaron. |
| Tus datos, diálogo | El archivo trae tu correo y tu celular completos. Queda en tu teléfono, fuera de MATU. |
| Ajuste de la sección 29, «Tu cuenta, cómo pedir» | Para cambiar tu nombre o tu correo, o eliminar tu cuenta, escribe a cuidaconmatu@gmail.com desde el correo de tu cuenta. Para ver o descargar tus datos, entra a «Tus datos». |

**Para el diseñador:** el aviso antes de descargar y el bloque que reemplaza a la ficha cuando la autorización no está vigente.

## 8. Faltantes y contradicciones

1. **La auditoría no se puede asociar a la persona** cuando se borra la entidad. Va en la 0028.
2. **La persona cuidada no puede ejercer sus derechos en la app:** no hay vínculo entre una cuenta y una persona cuidada. Por ahora, por correo (CL-30 ampliada). Quedó en la tarjeta **MATU-90**, en el Product Backlog.
3. **La rectificación no tiene pantalla:** no hay ruta para corregir el nombre, el nivel de apoyo o la dirección de la persona, ni el nombre o el correo propios (política §13). Mientras tanto, el correo. Quedó en la tarjeta **MATU-91**, en el Product Backlog.
4. **La política §9** contradice la historia (sección 6).
5. **La política §6, línea 220,** promete que la auditoría de la ficha se puede consultar, y no existe la pantalla hasta MATU-54.
6. **El ADR-029 y la arquitectura** dicen sprint 5, y la tarjeta sprint 4.
7. **El registro, entrada 5,** dice que las compras no tienen ruta de lectura.
8. **Los avisos simulados** quedan como `enviada` (D-54-11).
9. **El comentario de `consentimiento.evidencia`** en `db/01_esquema.sql:210` dice «texto aceptado, ip, agente», pero el dominio (`care_circle/domain/personas.py:9`) y la política dicen sin IP ni agente. Solo es el comentario. Se puede corregir con un `COMMENT ON COLUMN` en la 0028, si Jorge lo aprueba.
10. **Qué módulo arma la copia:** junta `care_circle`, `care_plan`, `consumption`, `iam` y `notifications`. Lo decide el orquestador con las reglas de la arquitectura 6.4, y `test_arquitectura.py` lo verifica. No puede ser `backoffice`, que no importa `care_plan` ni `consumption` (11.2).
11. **La copia trae 3 años de auditoría** mientras no exista el borrado a los 3 años (MATU-89).

## 9. Consulta legal (desde la CL-61)

- **CL-61 · Quién recibe la copia y qué lleva de terceros (nueva).** ¿Pueden el admin y el cuidador del grupo, también un cuidador de hecho, recibir en la aplicación una copia completa y portable de los datos de la persona cuidada, como ejercicio de sus derechos en su nombre? ¿O es una comunicación nueva que necesita su propia base? ¿Se pueden incluir los nombres de los relevos y de los miembros, y lo escrito en «A quién llamar», y excluir el teléfono del relevo y la referencia al documento? ¿La portabilidad alcanza a lo que escribió la familia y a la auditoría? Se relaciona con CL-04, CL-33 y CL-34. Bloquea los datos reales.
- **CL-62 · La copia con la autorización retirada o en pausa (nueva).** En los 90 días después de un retiro, o con la ficha en pausa, ¿hay que entregar a la titular, si la pide, el texto que nadie puede leer? ¿Quién lo entrega y cómo, si para hacerlo el equipo tendría que descifrarlo? Se relaciona con CL-25 y CL-06. Bloquea los datos reales.
- **CL-63 · El formato y el límite (nueva).** ¿Basta un JSON como formato estructurado y de uso común para la portabilidad, con la pantalla como formato legible? ¿Es compatible con la gratuidad un límite de 10 copias por hora, si el correo sigue disponible? Bloquea los datos reales.
- **CL-04 (ampliada):** suma el acceso y la portabilidad a la pregunta de quién ejerce los derechos de la persona cuidada.
- **CL-30 (ampliada):** la verificación de identidad vale también para pedir una copia por correo, si la persona no tiene cuenta.
- **CL-48 (ampliada):** la copia en la aplicación es inmediata. ¿Cuenta como respuesta dentro del plazo legal, o hay que responder igual por escrito?

Ninguna bloquea el semestre, que trabaja solo con datos sintéticos.

## Archivos revisados

- **Documentos** (main del repositorio MATU), en `docs/`:
  - en `legal/`: `politica-privacidad.md`, `registro-tratamientos.md` y `consulta-legal.md`;
  - `adr/ADR-029-ficha-no-se-imprime.md`;
  - `arquitectura.md`, 11.1 a 11.8;
  - `lenguaje.md`, 3, 24, 25 y 29;
  - `modelo-datos.md`.
- **Revisiones de esta noche:** `revision-previa-matu-55.md`, `revision-previa-matu-42-53.md`, `revision-previa-matu-46.md`, `revision-previa-matu-61.md` y `revision-previa-matu-62.md`, cada una en su rama `docs/matu-XX-revision-previa`.
- **Código** (MATU_PROYECTO, `backend/`):
  - el esquema: `db/01_esquema.sql`, `db/02_rls.sql` y `db/03_permisos.sql`;
  - las migraciones 0005, 0008, 0010, 0011, 0013, 0017, 0021 y 0022 en `alembic/versions/`;
  - `app/shared/auditoria.py`;
  - `app/modules/care_plan/infrastructure/auditoria_ficha.py`;
  - `app/main.py`, líneas 98 a 106.
- **Contrato:** `docs/api/README.md` (P2-2, línea 396) y `docs/api/openapi.json` (lista de rutas).

## Decisiones de Jorge (12 de noviembre de 2026)

Jorge decidió las primeras cinco de MATU-55 una por una y delegó el resto con «todas de acuerdo a tus recomendaciones». Se aplican las recomendaciones actualizadas del analista, que tienen en cuenta MATU-61, 62 y 94. Versión de la política según la D11, una por fusión. Fila de migraciones: 0024 MATU-62, 0025 MATU-55, 0026 MATU-42, 0027 MATU-46 y 0028 MATU-54. La próxima CL libre es la CL-68.

| Id | Decisión |
|---|---|
| D-54-1 | **a)** la copia de la persona la piden el admin y el cuidador |
| D-54-2 | **a)** dos copias: «Datos de {nombre}» y «Tus datos» |
| D-54-3 | **a)** la pantalla y un JSON |
| D-54-4 | **a)** nombres sí; teléfonos, correos y la referencia al documento no. Tampoco el teléfono de contacto del pedido ni los datos de la venta (token, orden, sesión, código de autorización). El nombre de quien pagó sí |
| D-54-5 | **a)** con una autorización retirada o en pausa, solo el estado y la fecha de borrado |
| D-54-6 | **a)** la auditoría como hoy, por RLS |
| D-54-7 | **a)** la **0028** agrega `persona_cuidada_id` a la auditoría; también la llenan `pedido.*`, `pago.*`, `direccion.cambiar` y la autorización de pedidos. Se verifica que las filas del sistema lleven `grupo_id` |
| D-54-8 | **a)** la descarga sin detalle |
| D-54-9 | **a)** 90 días en pantalla y todo en el archivo |
| D-54-10 | **a)** 10 copias por hora, con la CL-63 |
| D-54-11 | **a)** «En el piloto no salió» para los avisos simulados |
| D-54-12 | Ya no hace falta: la resolvió la D11 |
| D-54-13 | **a)** «Datos de {nombre}» y «Tus datos» |
| D-54-14 | Sí: la copia de la persona trae sus pedidos y pagos (productos, precios con IVA incluido, envío, total, estados, la dirección copiada, si se pagó y quién pagó, lo cobrado y lo devuelto, y la autorización de pedidos), sin el teléfono de contacto ni datos de la tarjeta |
| D-54-15 | **a)** se incluye igual con la autorización de pedidos retirada o la capa 3 apagada; con la capa quitada, el bloque se omite sin fallar |
| D-54-16 | **a)** «Tus datos» de quien pagó trae sus pagos (tipo de tarjeta, cuotas y últimos 4 dígitos) y las condiciones que aceptó; nunca el token, la orden ni la sesión |

**CL-68 nueva (Pedidos y pagos en la copia):** ¿se puede entregar al admin y al cuidador el historial de pedidos de la persona con el nombre de quien pagó? ¿Conserva quien pagó y salió del grupo el acceso a sus pagos? Se relaciona con CL-11, 12, 61 y 66. Bloquea los datos reales.

**Ajustes:** la migración es la 0028 (después de la 0025 de MATU-55, que hace la política de lectura de la auditoría si va primero); el JSON lleva los precios con IVA incluido, sin un campo `iva`; el módulo lee los pedidos por un puerto que devuelve vacío sin la capa 3; se borra «la próxima es CL-64».

## Revisión de cierre (12-11)

El analista normativo revisó lo construido en la rama de código de MATU-54 contra esta revisión previa y las decisiones D-54-1 a D-54-16.

- **El código CUMPLE.** Lo que se guarda, quién lo ve, lo que queda en el historial, lo que nunca sale y lo que se informa coinciden con las decisiones de Jorge y con la política 0.17.
- **F2 y F3 se corrigieron** en el código (decisiones 401 y 402 del contrato). «Tus datos» trae los grupos de los que la persona salió, con el rol y las fechas, sin el nombre del grupo, y a quien pagó le trae el código de autorización de sus pagos, solo ahí.
- **F1 y F7 se resuelven con texto** en la política 0.17 (§6 y §10, «Por el correo de esta sección») y con la CL-70: los intentos fallidos, los registros de quien paga u observa en un grupo y los cambios antiguos que no se pueden asociar a una persona se declaran y se entregan por correo.
- **C-E pasa a las condiciones antes de datos reales** de `consulta-legal.md`: marcar cada aviso y cada pago como simulado o de prueba en su propia fila, antes de enviar avisos reales o cobrar dinero real.
- **Quedan abiertas** para la consulta legal la CL-61, la CL-62, la CL-63, la CL-68 y la CL-70, y las CL-04, CL-30, CL-48 y CL-53 ampliadas. Todas bloquean los datos reales.

Los documentos quedan en el PR de documentos de MATU-54: la política 0.17, el registro de tratamientos (entradas 2 a 10 y la 13 nueva), la consulta legal, el modelo de datos, el ADR-029, la arquitectura 11.1 y `lenguaje.md`, sección 35.

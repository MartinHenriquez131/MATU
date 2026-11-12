# Revisión previa del analista normativo · MATU-46 · Borrar el teléfono del relevo y anonimizar el nombre de pila

**11 de noviembre de 2026, madrugada** · Agente analista normativo, a pedido de Jorge · Estado: **decisiones D-46-1 a D-46-7 pendientes de Jorge**

Esto no es asesoría legal: sirve para que Jorge decida. El analista leyó las cuatro revisiones de esta noche (MATU-61, 55, 62 y 42/53) y no contradice ninguna.

**Nota del orquestador:** el faltante D-46-5, el borrado a los 3 años de los accesos y de la auditoría, quedó como tarjeta propia en el Product Backlog: MATU-89.

## Resumen

- **La mitad de la tarjeta ya está hecha:** MATU-72 ya anonimiza el nombre de pila de la persona en sus accesos de relevo, y lo prueba. Lo único nuevo es borrar el teléfono.
- **Sí hace falta migración.** Se recomienda la **0027**, al final de la fila. No depende de la 0023 a la 0026.
- **`lenguaje.md` no necesita textos nuevos.** La pantalla ya tiene el texto para el teléfono vacío.

## Qué se verificó en el código

- **El nombre de pila ya se anonimiza:** `care_plan/infrastructure/efecto_retiro.py`, `borrar()` → `_ACCESOS_SIN_NOMBRE`, con `NOMBRE_BORRADO = "borrada"` (`care_circle/domain/borrado.py:21`), en todos los accesos del plan. Lo prueba `test_borrar_borra_todo_al_tiro_en_una_transaccion_y_un_instante` (`tests/modules/care_plan/test_borrado_persona_api.py:170-173`), y la 0020 ya da el `UPDATE` de esa columna.
- **Lo que falta probar:** que el borrado no toque los accesos de otra persona del mismo grupo. En `test_otras_personas_y_otros_grupos_no_se_tocan`, la hermana se crea sin accesos.
- **La 0020 se equivoca en un comentario:** dice que se anonimiza «al retirar o borrar», pero el retiro (MATU-44) no anonimiza. No se edita una migración publicada, pero no hay que guiarse por ese comentario.
- **Hoy nadie borra el teléfono:** `otorgado_a_telefono` sigue con `NOT NULL` (`db/01_esquema.sql:286`).
- **El contrato y la pantalla ya lo esperan vacío:** `AccesoListado.telefono_relevo` admite `null`, y `web/src/familia/textos.ts:513` ya dice «Ya no guardamos su teléfono.».
- **Hoy son promesas sin cumplir:** el aviso al relevo (`lenguaje.md` 7.5), la política (§8 y §10) y el registro (entrada 4). La política lo reconoce en §13.
- **El teléfono no está en la auditoría, en Redis ni en los eventos:** `relevo.compartir` lleva solo el motivo, y la sesión de Redis guarda solo `acceso_id`. Los campos tienen `repr=False`.
- **El patrón de la tarea:** `app/tareas.py` es un archivo. El modelo es `plan_destruir_claves` (0016): `SECURITY DEFINER`, dueño `matu_owner`, `search_path` fijo, exige `app.rol = 'operacion'`, `ahora <= now() + 5 min` y un `limite` mínimo. Desde la 0022 solo lo ejecuta `matu_scheduler`.
- **`token_vida_fija` no estorba.** Falta revisar que el trigger de la 0007 no rechace un `UPDATE` hecho por `matu_owner`.

## 1. Veredicto por punto

| # | Punto | Veredicto | Por qué y condiciones |
|---|---|---|---|
| P1 | **Plazo de 30 días para el teléfono** | **CUMPLE** | Lo decidió Jorge el 27-10 (decisión 25), y es corto y acotado a su finalidad. La base de licitud sigue en la CL-33. **C1:** se cuenta desde `LEAST(expira_en, COALESCE(revocado_en, expira_en))`. **C2:** un acceso bloqueado o en pausa cuenta desde `expira_en`. **C3:** se borra a más tardar la madrugada siguiente al día 30 |
| P2 | **Lo que hoy se promete** | **NO CUMPLE** hoy. Con MATU-46, **CUMPLE** | La política lo declara en §13. Bloquea los datos reales |
| P3 | **Que la auditoría y los logs no lleven el teléfono** | **CUMPLE** hoy, y debe seguir así | **C4:** la función devuelve solo un contador. **C5:** ningún `RAISE` lleva el valor. **C6:** una prueba de que el log de la corrida no trae el número |
| P4 | **Lo que se conserva 3 años** (nombre, motivo y fechas) | **CUMPLE** en el diseño. El plazo **REQUIERE CONSULTA LEGAL** (CL-34 y, después de un borrado, CL-27) | **Faltante:** nada borra a los 3 años, ni los accesos ni la auditoría (D-46-5, tarjeta MATU-89). **C7:** `otorgado_a_nombre` es texto libre; se recomienda un largo máximo y la ayuda «Solo su nombre» |
| P5 | **Anonimizar el nombre de pila al borrar a la persona** | **CUMPLE**: ya lo hace MATU-72 | **C8:** se agrega `test_borrar_persona_anonimiza_accesos` para lo que falta probar: un acceso cortado hace meses, el acceso de otra persona del grupo y un segundo borrado (409). Si es anonimización o seudonimización, va a la CL-60 |
| P6 | **El teléfono cuando se borra a la persona** | **CUMPLE** hoy (30 días). Hay una mejora posible | Después del borrado nadie ve la lista (404). Ver D-46-3 |
| P7 | **Tarea periódica, roles y RLS** | **CUMPLE** con condiciones | **C9:** `EXECUTE` solo para `matu_scheduler`, con una prueba de que a otro se le niega. **C10:** las políticas `TO matu_owner` exigen `operacion`, y no se agrega nada para `matu_app`. **C11:** se vacía solo el teléfono. **C12:** es idempotente. **C13:** la regla vive en `care_plan/domain`, con el `Reloj` |
| P8 | **Cruce con la D-42-7** | **CUMPLE** sin trabajo extra | Cortar fija `revocado_en`, y desde ahí corren los 30 días |
| P9 | **Copias de respaldo** | **REQUIERE CONSULTA LEGAL** (amplía la CL-29) | **C14:** al restaurar una copia, se corre `python -m app.tareas borrados` antes de reabrir la base |
| P10 | **Política y registro** | **NO CUMPLE** hasta que se publique la versión | Quitar la línea de §13 ya es una versión nueva. Ver D-46-6 |

## 2. ¿Migración? Sí: la 0027, con `down_revision = "0026"`

**De qué depende:** de la 0018, la 0020 y la 0022, que ya están en `main`.

**No depende de la 0023 a la 0026:**
- La 0023, la 0024 y la 0025 no tocan `acceso_relevo`.
- La 0026 toca `auditoria_detalle_acotado`. Con D-46-4 (c) no hay choque.

Adelantarla causaría solo conflictos de texto, pero obligaría a volver a encadenar las ramas (D-46-1).

**Borrador** (con D-46-3 (a) y D-46-4 (c); la forma la decide el backend):

```sql
-- upgrade
ALTER TABLE acceso_relevo ALTER COLUMN otorgado_a_telefono DROP NOT NULL;
ALTER TABLE acceso_relevo ADD COLUMN telefono_borrado_en timestamptz;
ALTER TABLE acceso_relevo ADD CONSTRAINT acceso_telefono_o_borrado
    CHECK ((otorgado_a_telefono IS NULL) = (telefono_borrado_en IS NOT NULL));
-- Un teléfono solo se vacía, una vez, y nunca cambia ni vuelve. Vale para todos los roles, también el dueño
CREATE FUNCTION acceso_telefono_solo_se_borra() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.otorgado_a_telefono IS DISTINCT FROM OLD.otorgado_a_telefono AND NEW.otorgado_a_telefono IS NOT NULL THEN
        RAISE EXCEPTION 'el teléfono del relevo solo se borra' USING ERRCODE = 'check_violation';
    END IF;
    IF OLD.telefono_borrado_en IS NOT NULL AND NEW.telefono_borrado_en IS DISTINCT FROM OLD.telefono_borrado_en THEN
        RAISE EXCEPTION 'el borrado del teléfono no cambia' USING ERRCODE = 'check_violation';
    END IF;
    RETURN NEW;
END $$;
CREATE TRIGGER acceso_relevo_telefono BEFORE UPDATE ON acceso_relevo
    FOR EACH ROW EXECUTE FUNCTION acceso_telefono_solo_se_borra();

-- La tarea (como 0016 y 0022)
CREATE POLICY acceso_conservacion_leer ON acceso_relevo FOR SELECT TO matu_owner USING (app_rol() = 'operacion');
CREATE POLICY acceso_conservacion ON acceso_relevo FOR UPDATE TO matu_owner
    USING (app_rol() = 'operacion') WITH CHECK (app_rol() = 'operacion' AND otorgado_a_telefono IS NULL);
CREATE FUNCTION relevo_conservar(limite timestamptz, ahora timestamptz) RETURNS integer
    LANGUAGE plpgsql VOLATILE SECURITY DEFINER SET search_path = pg_catalog, public, pg_temp AS $$
DECLARE n integer := 0;
BEGIN
    IF public.app_rol() IS DISTINCT FROM 'operacion' THEN
        RAISE EXCEPTION 'relevo_conservar exige app.rol = operacion' USING ERRCODE = 'insufficient_privilege';
    END IF;
    IF ahora IS NULL OR ahora > now() + interval '5 minutes' THEN
        RAISE EXCEPTION 'ahora no puede estar en el futuro' USING ERRCODE = 'invalid_parameter_value';
    END IF;
    IF limite IS NULL OR limite > ahora - interval '30 days' THEN
        RAISE EXCEPTION 'el teléfono se conserva 30 días' USING ERRCODE = 'invalid_parameter_value';
    END IF;
    UPDATE public.acceso_relevo SET otorgado_a_telefono = NULL, telefono_borrado_en = ahora
     WHERE otorgado_a_telefono IS NOT NULL
       AND LEAST(expira_en, COALESCE(revocado_en, expira_en)) <= limite;
    GET DIAGNOSTICS n = ROW_COUNT;
    RETURN n;
END $$;
REVOKE ALL ON FUNCTION relevo_conservar(timestamptz, timestamptz) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION relevo_conservar(timestamptz, timestamptz) TO matu_scheduler;

-- Solo con D-46-3 (a): el borrado de la persona vacía el teléfono en ese momento
GRANT UPDATE (otorgado_a_telefono, telefono_borrado_en) ON acceso_relevo TO matu_app;
```

**Downgrade, en orden inverso:**
1. Si quedó algún teléfono borrado, se detiene con un error claro, como la 0018. **Nunca inventa un teléfono.**
2. Quita el permiso, la función, las políticas, el trigger, el `CHECK` y la columna.
3. Vuelve a poner el `SET NOT NULL`.

**Código:**
- **Dominio:** `telefono_por_borrar(expira_en, revocado_en, ahora)` y `limite_telefono(ahora)`, en `care_plan/domain`.
- **Aplicación:** el caso de uso con su puerto.
- **Infraestructura:** `tarea_conservacion_relevo.py`, con `matu_scheduler`.
- **`tareas.py`:** la tarea `conservacion_relevo` en `TAREAS` y en `BORRADOS_DIARIOS`, sin cambiar los horarios. Se actualizan `test_tareas.py` y los README.
- **Con D-46-3 (a):** el `UPDATE` de `efecto_retiro.borrar()` vacía también el teléfono y fija `telefono_borrado_en`. Cambia lo que verifica `test_migraciones.py:940`.

**Pruebas:**
- **`test_telefono_relevo_se_borra_a_los_30_dias`,** con el `Reloj`:
  - a los 29 días y 23 horas no se borra, y a los 30 días sí;
  - el acceso vigente no se toca;
  - el cortado cuenta desde el corte y el bloqueado desde su vencimiento;
  - el nombre, el motivo y las fechas no cambian;
  - es idempotente;
  - a `matu_app` se le niega;
  - falla con otro rol, con `ahora` en el futuro y con un límite reciente;
  - la API devuelve `telefono_relevo: null`;
  - el log no trae el número.
- **El trigger:** nadie cambia el teléfono ni lo devuelve, tampoco el dueño.
- **`test_borrar_persona_anonimiza_accesos`:** lo de C8 y, con D-46-3 (a), el teléfono vacío al instante.
- **`test_aislamiento.py`:** la tarea no abre lecturas a `matu_app` ni a otro grupo.
- **`test_migraciones.py`:** el ciclo completo.

## 3. Decisiones para Jorge (con la recomendación del analista)

- **D-46-1 · Número y orden.** (a) La 0027, al final de la fila, o (b) adelantarla y volver a encadenar. **Se recomienda (a).**
- **D-46-2 · La anonimización ya hecha.** (a) Se da por hecha y se agrega la prueba enfocada, o (b) se da por hecha sin prueba nueva. **Se recomienda (a).**
- **D-46-3 · El teléfono al borrar a la persona.**
  - (a) Se borra en ese momento: `matu_app` recibe el `UPDATE` de las dos columnas, el trigger solo deja vaciarlo y la RLS lo limita al admin y al cuidador.
  - (b) Se borra a los 30 días, como dice hoy §10.

  **Se recomienda (a),** por minimización. Acorta un plazo, así que no exige una autorización nueva. Se aparta un poco de la nota de la 0020 (c), y lo decide Jorge.
- **D-46-4 · La constancia del borrado.**
  - (a) Solo el contador.
  - (b) Una fila de auditoría por acceso.
  - (c) `telefono_borrado_en` en la misma fila, con su `CHECK`, más el contador.

  **Se recomienda (c):** no agrega acciones de auditoría y no choca con la 0026.
- **D-46-5 · El borrado a los 3 años de los accesos y de la auditoría,** que hoy no existe. (a) Declararlo pendiente en §13, junto con la D3 de MATU-55, y crear una tarjeta. (b) Construirlo aquí. **Se recomienda (a).** **Faltante:** quedó en la tarjeta MATU-89.
- **D-46-6 · La versión de la política.** (a) La 0.12 que comparten MATU-61, 55, 62 y 42, si todavía no se publicó, o (b) una 0.13 propia. Depende de la pregunta abierta en la revisión de MATU-42. No se pide aceptar de nuevo, porque acorta plazos y no agrega usos, datos ni destinatarios.
- **D-46-7 · Faltante: `nombre_pila_comparte`.** Cuando exista la eliminación de la cuenta (CL-49), debería anonimizarse. Con la D-42-10 (a), la lista mostraría «Alguien que ya no está en el grupo». Se recomienda anotarlo en MATU-42 y en la tarjeta de eliminar la cuenta.

## 4. Borradores para `docs/legal/`

### `registro-tratamientos.md`, entrada 4

- **Datos:**
  - «el nombre y el teléfono del relevo, obligatorios al crear el acceso. Cuando el teléfono se borra queda vacío, y `telefono_borrado_en` guarda cuándo (MATU-46).»
  - «el nombre de pila de la persona cuidada, copiado al crear el acceso. Si se borra a la persona, se reemplaza por un valor fijo, sin datos, en todos los accesos de su plan, también en los vencidos y los cortados (MATU-72, D5) [PENDIENTE: CL-60].»
- **Conservación, el teléfono:** «se borra 30 días después de que el acceso vence o se corta, lo que ocurra primero. Lo hace la tarea diaria `conservacion_relevo` (MATU-46) con `relevo_conservar`, `SECURITY DEFINER`, que solo ejecuta `matu_scheduler`, vacía únicamente el teléfono y devuelve un contador. Un acceso bloqueado o en pausa cuenta desde su vencimiento. Si se borra a la persona, se borra en ese momento.» La última frase va con D-46-3 (a).
- **Conservación, el nombre, el motivo y las fechas:** se agrega «[PENDIENTE: la tarea que los borra a los 3 años; CL-34 y, después de un borrado, CL-27]».
- **Medidas:**
  - «La aplicación no puede cambiar el teléfono, solo vaciarlo al borrar a la persona. Un trigger impide, para todos los roles de la base, que un teléfono vaciado vuelva o cambie por otro (MATU-46, migración 0027).»
  - En la línea de MATU-72, con D-46-3 (a): «El plazo de 3 años corre desde el corte, y el teléfono se borra en ese momento».
  - Nueva: «Si se restaura una copia de respaldo, antes de reabrir la base se corren las tareas de borrado [PENDIENTE: CL-29].»

### `politica-privacidad.md`, en la 0.12 o la 0.13 según D-46-6

- **Encabezado:** «**MATU-46:** el teléfono del relevo se borra solo, 30 días después de que el acceso vence o se corta, y si pides borrar los datos de la persona, en ese mismo momento. Acorta plazos, no agrega usos, datos ni destinatarios, y no cambia las declaraciones.»
- **§8:** sin cambios, porque vale la regla general de «a más tardar el día siguiente».
- **§10, con D-46-3 (a):** «su teléfono, hasta 30 días» pasa a «su teléfono se borra en ese momento».
- **§13:** se quita «Borrar el teléfono del relevo 30 días después de que el acceso vence o se corta. Mientras no exista, MATU no trata datos reales.» Si MATU-55 agrega el borrado a los 3 años, se le suma «y de los accesos de relevo».
- **Backend:** `POLITICA_VERSION` y la copia del texto con su huella.

### `consulta-legal.md`

- Se quita el punto de MATU-46 en «antes de datos reales» cuando se fusione.
- Se agrega su fila, y la próxima pregunta pasa a ser la **CL-61**.

### Fuera de `docs/legal/`

- **Arquitectura 11.8:** se cierra el PENDIENTE del teléfono, y «Lo hace la historia de borrado» pasa a «Lo hace MATU-72».
- **`modelo-datos.md`:** se cierra el PENDIENTE y se agregan `telefono_borrado_en` y su `CHECK`.
- **`docs/api/README.md`, decisión 25:** se agregan la 0027 y MATU-46.

## 5. `lenguaje.md`

No hace falta ningún texto nuevo.
- «Ya no guardamos su teléfono.» ya existe (sección 9).
- El aviso 7.5 se vuelve cierto con esta historia.
- **Opcional (C7):** la ayuda del campo del nombre, «Solo su nombre, sin apellidos ni teléfono», que aprueba Jorge.

## 6. Consulta legal (desde la CL-60)

- **CL-60 (nueva) · ¿Anonimización o seudonimización?** Si se reemplaza el nombre de pila por un valor fijo y se conserva el número interno que une el acceso, la auditoría y el grupo, ¿es una anonimización según la Ley 21.719, o una seudonimización que sigue siendo dato personal? Mientras tanto se trata como dato personal, con los plazos de la CL-27. Bloquea los datos reales.
- **CL-34 (ampliar):** ¿puede el relevo, que no tiene cuenta, pedir que se borre su teléfono antes de los 30 días? ¿Por qué vía, y cómo se verifica que es él?
- **CL-29 (ampliar):** el teléfono queda en las copias de respaldo hasta que vencen. ¿Basta volver a correr los borrados antes de reabrir una copia restaurada?
- **Siguen abiertas:** la CL-33, la CL-27 y la CL-53.

Ninguna bloquea el semestre, que usa datos sintéticos.

## Certeza de las citas

No cita artículos: ninguna conclusión depende de uno. La WCAG y la Ley 20.422 no aplican, porque no hay pantallas nuevas.

## Decisiones de Jorge (12 de noviembre de 2026)

Jorge decidió las primeras cinco de MATU-55 una por una y delegó el resto con «todas de acuerdo a tus recomendaciones». Se aplican las recomendaciones actualizadas del analista, que tienen en cuenta MATU-61, 62 y 94. Versión de la política según la D11, una por fusión. Fila de migraciones: 0024 MATU-62, 0025 MATU-55, 0026 MATU-42, 0027 MATU-46 y 0028 MATU-54. La próxima CL libre es la CL-68.

| Id | Decisión |
|---|---|
| D-46-1 | Ya no hace falta: la migración es la **0027** (`down_revision = "0026"`) |
| D-46-2 | **a)** una prueba enfocada de que el borrado no toca los accesos de otra persona del grupo |
| D-46-3 | **a)** al borrar a la persona, el teléfono del relevo se borra al tiro |
| D-46-4 | **c)** `telefono_borrado_en` y un contador |
| D-46-5 | Ya no hace falta: el borrado a los 3 años va en MATU-89 |
| D-46-6 | Ya no hace falta: la resolvió la D11 |
| D-46-7 | Sí: se anota en MATU-42 y en la tarjeta de eliminar la cuenta que `nombre_pila_comparte` debe anonimizarse |

**Ajustes:** `conservacion_relevo` va en `BORRADOS_DIARIOS` y corre siempre; las pruebas corren solo contra una base de pruebas (MATU-94); se borra «la próxima pregunta pasa a ser la CL-61».

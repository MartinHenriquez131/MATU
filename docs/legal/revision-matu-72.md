# Revisión normativa de MATU-72 · Borrar los datos de la persona al tiro

**Analista normativo**, revisión previa del 8 de noviembre de 2026. No es asesoría legal: apoya las decisiones de Jorge Espinoza (Product Owner).

## Revisión previa (antes de implementar)

**Qué resuelve:** la política prometía borrar la ficha de inmediato a pedido, con un [PENDIENTE] sobre si una solicitud de borrado esperaba los 90 días del retiro. Con MATU-72 no espera: el borrado de los datos de la persona se hace en el acto, desde la aplicación. MATU-71 (escrituras que no esperan a un retiro en curso) se resuelve dentro de esta historia (condición C7).

**Decisiones de Jorge del 08-11, según la recomendación:**
- **D1 · Quién borra:** el admin y el cuidador, en la aplicación, con la misma regla y la misma barrera RLS que el retiro (`app_retira_autorizacion()`). El pagador, el observador, otro grupo o una persona que no existe reciben 404. La API no pregunta en qué calidad se pide. El borrado por correo, de una persona sin cuenta o de su representante, queda para antes de los datos reales (política, sección 13).
- **D2 · Autorizaciones:** en la misma transacción, las vigentes se retiran con `revocacion_motivo = 'borrado'`. Las ya retiradas conservan su motivo. La marca durable es `persona_cuidada.datos_borrados_en`, con `persona.borrar` en la auditoría. Después de un borrado nunca «vuelve lo que estaba escrito».
- **D3 · Copias de respaldo:** un plazo máximo antes de los datos reales (CL-6 ampliada). La auditoría `persona.borrar` sirve de lista para volver a borrar si se restaura una copia.
- **D4 · Lo que se conserva**, sin texto: la auditoría, el registro de autorizaciones, los accesos y las aperturas del relevo, por sus plazos (CL-8).
- **D5 · La persona sale de MATU (opción A):** `eliminado_en` queda en ahora, el nombre y el nombre de pila se reemplazan por un valor fijo sin datos, el nivel de apoyo y la dirección se borran, y se anonimiza `acceso_relevo.nombre_pila_persona`. La fila queda solo con su número interno, que une los registros conservados. Para volver hay que registrarla de nuevo (MATU-07), en blanco.
- **D6 · Confirmación:** casilla obligatoria «Entiendo que esto no se puede deshacer.» y botones «Borrar todo» y «No borrar». No se pide la contraseña.
- **D7 · `POLITICA_VERSION`** sigue en 0.10: no agrega usos, datos ni destinatarios, y acorta plazos (criterio del 06-11).
- **D8:** las condiciones C1 a C13, abajo.

**Qué se borra y qué se conserva:**
- La clave se destruye en el acto. La fila de la clave queda, sin la clave.
- Las secciones de la ficha se borran. El plan se conserva, porque borrarlo arrastraría los accesos del relevo.
- Los insumos se borran, y con ellos los avisos y las compras anotadas.
- Los avisos enviados y los eventos internos siguen sus plazos, porque solo llevan identificadores.
- Se cortan todos los accesos de relevo que todavía no vencían ni estaban cortados, también los bloqueados y los en pausa. Responden 410 `relevo-revocado` para siempre.

**Condiciones para implementar:**
1. **C1:** una sola transacción y un solo instante del `Reloj`, con un orden de bloqueo fijo: la persona, las autorizaciones vigentes, los accesos y la clave.
2. **C2:** borran solo el admin y el cuidador. Los demás reciben 404, nunca 403, con la barrera también en RLS. Otras personas y otros grupos no se tocan (`test_aislamiento.py`).
3. **C3:** si la persona ya se borró, 409 `ya-borrada`.
4. **C4:** la auditoría no lleva contenido: `persona.borrar`, un `consentimiento.revocar` por autorización vigente, un `relevo.revocar` por acceso cortado y `clave.destruir`, con el mismo `request_id` e instante. Los contadores van solo en la respuesta.
5. **C5:** los logs llevan a lo más el resultado. La pantalla saca de la memoria todo lo cargado de esa persona.
6. **C6:** primero se destruye la clave y después se borran las secciones, en otra sentencia, para que una sección confirmada a la vez no quede viva. Con prueba de concurrencia.
7. **C7 (absorbe MATU-71):** toda escritura de la ficha, de las secciones y del consumo lee la autorización con `FOR SHARE`. Si un retiro o un borrado la cambió mientras esperaba, responde 403 o 404 en vez de escribir. Una prueba de concurrencia por ruta.
8. **C8:** un retiro durante el borrado espera y recibe 404 o 409. Un borrado durante un retiro respeta el motivo `retiro`. Otorgar falla si la persona está borrada.
9. **C9:** el relevo recibe 410 en la siguiente petición, y el canje queda serializado con el corte.
10. **C10:** el estado de las autorizaciones reconoce el borrado. `tarea_destruccion` y `consumo_conservar` no fallan sobre una persona borrada.
11. **C11:** migración reversible (0018). El downgrade se detiene si hay personas borradas.
12. **C12:** no depende de los pedidos (capa 3). Si existiera un pedido, se conserva, y la dirección no se borra mientras la use.
13. **C13:** pruebas marcadas con su RF: camino feliz, 404, 409, concurrencia de C6 y C7, relevo 410, auditoría sin contenido y vuelta atrás si falla un efecto.

**Textos:** salen tal cual de `lenguaje.md` 24, aprobados por Jorge el 08-11, con los ajustes A1 y A2 del diseñador.

## Consulta legal

- **CL-6 ampliada:** si destruir la clave basta para la supresión, y qué plazo máximo corre para las copias de respaldo, que ahora también contienen los insumos y las compras anotadas de una persona borrada. Volver a borrar antes de usar una copia restaurada es la medida propuesta.
- **CL-7:** cómo verificar la identidad de la persona sin cuenta, o de su representante legal, que pide el borrado por correo, y si una cuidadora o un cuidador de hecho puede pedirlo por su cuenta.
- **CL-8:** por cuánto tiempo se conservan, después de un borrado, el registro de autorizaciones, la auditoría y los accesos y las aperturas del relevo, sin texto, para demostrar cómo se usaron los datos.

CL-1 a CL-5 siguen abiertas como en MATU-44. Las tres van a la tarjeta de consulta legal de Trello.

**Antes de operar con datos reales:**
- el borrado a pedido por correo, sin pasar por el grupo (política, sección 13);
- el plazo de las copias de respaldo (CL-6);
- el correo de contacto.

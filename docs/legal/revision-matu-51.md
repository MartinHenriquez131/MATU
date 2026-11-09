# Revisión normativa de MATU-51 · Anotar una compra o lo que queda

> **Nota del 9 de noviembre de 2026.** Las preguntas de esta revisión usan la numeración antigua. Su número actual está en la tabla de equivalencias de [`consulta-legal.md`](consulta-legal.md#tabla-de-equivalencias), que es la única lista vigente.

**Analista normativo**, revisión previa y revisión de cierre del 7 de noviembre de 2026. No es asesoría legal: apoya las decisiones de Jorge Espinoza (Product Owner).

## Revisión previa (antes de implementar)

**Veredicto:** CUMPLE en los puntos 1 a 5, con 12 condiciones. El punto 6 (capa 3) daba REQUIERE CONSULTA LEGAL si se hacía ahora, y Jorge lo sacó de la historia (decisión C).

**Decisiones de Jorge del 07-11, según la recomendación y con dos ajustes suyos:**
- **A:** las compras anotadas se guardan 90 días desde que se anotan, y no mientras exista el insumo.
- **A2:** «Ya lo resolví» acepta envases, igual que «Compré».
- **A3:** los insumos «Sin seguir» no muestran los botones, y la API responde 409 `perfil-inactivo`.
- **B:** anotan solo el admin y el cuidador. El pagador, el observador y otro grupo reciben 404.
- **C:** nada de capa 3. Un pedido entregado no suma al stock todavía (MATU-61 a 63, con versión nueva de la política).
- **D, con ajuste:** «Compré» acepta de 1 a 99 envases o de 1 a 10.000 en la unidad, y lo que queda no pasa de 100.000.
- La nota de los avisos cambia según el rol.

**Condiciones para implementar:**
1. «Me quedan N» reemplaza lo que queda y no guarda una compra.
2. «Compré» usa las mismas funciones de «Ya lo resolví» (MATU-37), en una sola transacción.
3. La fecha la pone el servidor con el `Reloj`, y la API no acepta una fecha.
4. No hay historial de compras en la API.
5. Anotan solo el admin y el cuidador. Los demás roles y otro grupo reciben 404.
6. Las compras anotadas se borran a los 90 días.
7. Una compra simultánea a un retiro espera (`FOR SHARE`) y responde 403 sin escribir nada.
8. La auditoría usa acciones que ya existen, sin cantidades, stock, nombre ni IP, y los logs y errores tampoco los llevan.
9. «Compré» nunca crea una alerta.
10. Si la alerta ya estaba cerrada, «Compré» funciona sin 409.
11. La cantidad viaja solo en el cuerpo.
12. Nada de capa 3.

## Revisión de cierre (lo implementado)

**Veredicto:** CUMPLE para el piloto con datos sintéticos. Las 12 condiciones se cumplen, con su evidencia en `test_reposicion_api.py`, `test_aislamiento.py`, `test_migraciones.py` y `test_capa3_desacoplable.py` de la rama `matu-51-registrar-reposicion`, y con la migración 0017. La política, el registro y `lenguaje.md` 23 dicen lo mismo que el código.

**Observaciones del cierre, corregidas en este PR:**
- **Política, sección 13:** la tarea que borra a los 90 días las compras, los avisos cerrados y el registro de avisos también se corre a mano.
- **Registro:** se precisa que la API no expone las compras y que la conservación las borra solo con el rol de operación.

**Lo que sigue:**
- **`POLITICA_VERSION`** sigue en 0.10, por el criterio del 06-11. «Compré» no agrega usos, datos ni destinatarios, y el plazo de 90 días es más corto que el de antes.
- **Derecho de acceso:** las compras no se ven en la aplicación (condición 4). Mientras no se puedan descargar desde la aplicación, se piden por el correo de la sección 10, y la descarga debe incluirlas.

**Consulta legal:** nada nuevo. CL-1 a CL-6 siguen abiertas como en MATU-44.

**Antes de operar con datos reales:**
- un programador de tareas para `quiebre_conservar`, además de `tarea_destruccion` y `consumo_conservar`;
- lo que ya listó MATU-44.

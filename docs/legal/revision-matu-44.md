# Revisión normativa de MATU-44 · Retirar una autorización

**Analista normativo**, revisión previa del 6 de noviembre de 2026 y revisión de cierre del 7 de noviembre de 2026. No es asesoría legal: apoya las decisiones de Jorge Espinoza (Product Owner).

## Revisión previa (antes de implementar)

**Veredicto:** dos NO CUMPLE de diseño en la tarjeta original:
- solo el admin podía retirar, y quien dio la autorización como cuidador no tenía cómo deshacerla por el mismo medio;
- la ficha no se podía volver a autorizar.

Jorge los resolvió con D1 y D2.

**Decisiones de Jorge del 06-11, según la recomendación:**
- **D1:** retiran el admin y el cuidador.
- **D2:** la ficha se puede volver a autorizar.
- **D3:** borrar la ficha a los 90 días, dentro de esta historia.
- **D4:** `revocacion_motivo` distingue el retiro de la renovación.
- **D5:** al retirar los insumos se descartan las alertas abiertas.
- **D6:** el botón va en Grupo familiar.
- **D7:** retirar algo ya retirado da 409.
- **D8:** la fecha de retiro va en el contrato.
- **P1 a P8:** Grupo familiar es una sección mínima. El pagador y el observador ven el estado sin la calidad. Se puede retirar con la revisión vencida. Se avisa que una lista ya compartida no se borra. Después del día 90, la ficha empieza en blanco con una clave nueva. Renovar pasa a MATU-69.

**Condiciones para implementar:**
1. El retiro solo fija `revocado_en` en la fila vigente.
2. Retiran el admin y el cuidador. El pagador, el observador y otro grupo reciben 404.
3. Se puede retirar con la revisión anual vencida.
4. El retiro va en una sola transacción, con el `Reloj`, `consentimiento.revocar`, el corte de todos los accesos que todavía abrían y un `relevo.revocar` por cada uno. Si algo falla, todo vuelve atrás.
5. Los accesos vencidos o ya cortados no se tocan.
6. Las otras personas y los otros grupos no se tocan.
7. La carrera con compartir queda cerrada (`FOR UPDATE` y `FOR SHARE`).
8. El relevo queda en 410 para siempre después del retiro.
9. La ficha responde 403, y la lista de enlaces y las aperturas siguen en 200.
10. Los insumos responden 403. No se crean alertas, y el aviso pendiente queda `omitida`. Retirar una finalidad no toca la otra.
11. Los logs no llevan nombres, teléfonos, tokens ni texto.
12. La pantalla saca de la memoria lo que ya estaba cargado.
13. Los textos salen tal cual de `lenguaje.md` 22.

## Revisión de cierre (lo implementado)

**Veredicto:** CUMPLE para el piloto con datos sintéticos. Las 13 condiciones se cumplen, con su evidencia en el código y en las pruebas de la rama `matu-44-revocar-consentimiento`.

Las observaciones del cierre se corrigieron en el mismo PR:
- **Condición 10:** se agregó la prueba de que retirar la ficha no toca los insumos.
- **Condición 4:** toda la auditoría del retiro usa el mismo instante.
- **Condición 13:** se quitó un texto de reserva que no estaba en la sección 22.
- **CL-6:** la tarea de los 90 días ahora también borra el texto cifrado y las filas de las secciones, y no solo la clave.
- **Documentos:** la política dice que la calidad se puede deducir de la revisión de 12 meses (P2) y que la tarea de los 90 días se corre a mano. El modelo de datos registra la excepción a MATU-11: una clave nueva solo tras una autorización nueva.

**Lo que sigue:**
- **P8 es coherente con el borrado:** la clave destruida nunca vuelve a tener DEK, y una clave nueva solo existe después de una autorización nueva y explícita.
- **P2 se acepta por minimización:** que el pagador y el observador puedan deducir la calidad de la revisión de 12 meses solo revela si quien autorizó es un cuidador de hecho, y la política lo informa.
- **`POLITICA_VERSION`** sigue en 0.10, por el criterio del 06-11.

**Consulta legal:** CL-1 a CL-5 siguen abiertas desde la revisión previa. CL-6, sobre si destruir la clave basta para la supresión y qué plazo corre para las copias de respaldo, queda abierta en lo que toca a las copias. Están en la tarjeta de consulta legal de Trello.

**Antes de operar con datos reales:**
- un programador de tareas para `tarea_destruccion` y `consumo_conservar`;
- MATU-46;
- el correo de contacto;
- MATU-69, para renovar la autorización.

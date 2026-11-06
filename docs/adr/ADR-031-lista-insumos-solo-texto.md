# ADR-031 · La lista de insumos se comparte como texto, sin enlace

**Estado:** Aceptado
**Fecha de decisión:** 6 de noviembre de 2026
**Decisor:** Jorge Espinoza (Product Owner). Martín Henríquez (Scrum Master) revisa en el PR
**Ajusta:** RF-15, la arquitectura 9.3 y 9.6, el almacenamiento de objetos para las exportaciones de la lista y el calendario del sprint 6 de la arquitectura. Se consolida en la v1.2 (MATU-43)

---

## Contexto

RF-15 dice que la familia exporta la lista de reposición «como documento o enlace compartible». La arquitectura 9.3 proponía `POST …/lista-reposicion/exportar`, que devolvía un PDF o un enlace, y guardaba las exportaciones en el almacenamiento de objetos. El ejemplo de la 9.6 traía el nombre de la persona cuidada y una acción `compartir_enlace`.

La lista muestra qué insumos usa la persona, y el diseño trata el consumo como un dato de salud (decisión de Jorge del 31-10, pendiente de consulta legal). Un enlace abierto lo puede abrir cualquiera que lo reciba, y obligaría a construir otro acceso con token, vencimiento y corte, como el del relevo. Un PDF hecho en el servidor obliga a guardar archivos con datos de consumo.

## Decisión

1. **En el semestre la lista se comparte como texto, sin enlace.** Se imprime o se guarda como PDF desde el navegador del teléfono, y se comparte con la hoja de compartir del teléfono (`navigator.share`, solo con texto) o con «Copiar la lista».
2. **MATU no genera archivos, no guarda exportaciones y no crea un acceso público.** No existe `POST …/exportar` ni una ruta pública para la lista.
3. **RF-15 se cumple con el documento.** «Enviarla a un miembro del grupo» (ADR-027, punto 2) se cumple porque todos los miembros ven la lista en la app.
4. **La lista no lleva el nombre de la persona cuidada** ni nada de la ficha (ADR-029). El texto que sale del teléfono tampoco lleva los días que quedan, para que no se pueda deducir el consumo diario.
5. **Quién la saca del teléfono:** administrador, cuidador y pagador. El observador la ve, sin esos botones.
6. **La cantidad sugerida va en envases** cuando el insumo tiene anotadas sus unidades por envase (dato opcional nuevo). Si no las tiene, va en la unidad del insumo.

## Consecuencias

- La v1.2 de la arquitectura (MATU-43) corrige RF-15, la 9.3, la 9.6, el almacenamiento de objetos y el calendario.
- Si después hace falta un enlace, va con un ADR nuevo, una revisión normativa y su propio acceso con token, vencimiento y corte.
- La política de privacidad lo informa (MATU-60), sin cambiar su versión.

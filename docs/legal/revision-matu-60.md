# Revisión normativa de MATU-60 · Lista de insumos

> **Nota del 9 de noviembre de 2026.** Las preguntas de esta revisión usan la numeración antigua. Su número actual está en la tabla de equivalencias de [`consulta-legal.md`](consulta-legal.md#tabla-de-equivalencias), que es la única lista vigente.

**Analista normativo**, revisión previa y revisión de cierre del 6 de noviembre de 2026. No es asesoría legal. Apoya las decisiones de Jorge Espinoza (Product Owner).

## Revisión previa (antes de implementar)

**Veredicto:** ningún NO CUMPLE. El diseño se puede implementar con las condiciones de abajo.

**Condiciones para implementar:**

*Backend*
1. El `GET` nuevo usa `consumo_para_leer`. Responde 403 `sin-consentimiento` sin autorización, 403 `revision-vencida` con la revisión vencida, y 403 `sin-consentimiento` con la autorización retirada.
2. Responde 404 a quien no es miembro, a otro grupo, a una persona inexistente y a un id que no es UUID, con su prueba en `test_aislamiento.py`. El rol de operación no lee nada.
3. La respuesta trae solo el perfil, el nombre del insumo, los días, la cantidad sugerida y la fecha. No trae la persona, la ficha, el grupo, la tasa, el stock, precios, comercios ni acciones. Una prueba verifica los campos exactos.
4. Entran solo los perfiles activos que hoy avisan (decisión 117, ajustada por Jorge el 06-11).
5. `Cache-Control: no-store` también en 403 y 404.
6. Sin tabla nueva para la lista, sin auditoría, sin eventos, sin archivos, sin almacenamiento de objetos, sin ruta pública ni token, y sin `POST …/exportar`.
7. `nombre_libre` nunca en logs, errores ni eventos. Lo agregado a mano nunca llega al servidor.

*Frontend*

8. La lista, lo agregado a mano y las cantidades cambiadas viven solo en el estado de la pantalla. Nada en `localStorage`, `sessionStorage`, la URL, `history.state` ni `document.title`. La lista se pide de nuevo cada vez que se abre la pantalla.
9. Sin autorización vigente, la pantalla muestra los textos de «Permiso» y no muestra la lista ni los botones.
10. `navigator.share` va solo con `text`. Sin `navigator.share`, queda «Copiar la lista».
11. La impresión muestra solo el título con la fecha, las líneas y el pie del piloto. Durante la impresión, `document.title` es «Lista de insumos».
12. Hay un aviso siempre visible sobre los botones, sin cuadro de confirmación.
13. El observador ve la lista sin botones ni campos (decisión de Jorge del 06-11).
14. El texto compartido y la impresión llevan «Piloto académico con datos de prueba».
15. Se cumple el checklist de accesibilidad, con botones de 48 px y el texto al 200% en 320 px.

*Documentos*

16. La política, el registro y `lenguaje.md` 21 entran en el mismo PR, aprobados por Jorge.
17. Jorge deja por escrito D1 frente a RF-15 y la arquitectura (ADR-031).

**Consulta legal:** CL-1 a CL-3, en la tarjeta de consulta legal de Trello.

## Revisión de cierre (lo implementado)

**Veredicto:** CUMPLE para el piloto con datos sintéticos. Las 17 condiciones se cumplen, con su evidencia en el código y en las pruebas de la rama `matu-60-lista-reposicion`.

- **Regla de impresión:** también cierra Ctrl+P en la ficha y en la página del relevo (ADR-029). Tiene su prueba en `web/pruebas/reglaImpresion.test.ts`.
- **`unidades_por_envase`:** queda bien declarado sin cambiar `POLITICA_VERSION`, porque cabe en «qué insumos usa» y ninguna persona real aceptó la versión 0.10.
- **Observaciones de documentos corregidas en este PR:** la política dice «imprimir o compartir» en vez de «exportar», el modelo de datos aclara que la lista no lee el envase del catálogo, el ADR-031 matiza lo que se puede deducir del consumo, y el registro dice que ninguna otra pantalla se imprime.
- **Consulta legal:** se suma CL-4, sobre cuándo un dato opcional o una función nueva dentro de la misma finalidad exige una versión nueva de la política.

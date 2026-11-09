# Herramientas de la documentación

## `generar_arquitectura_html.mjs`

Genera la versión navegable `docs/arquitectura.html` desde `docs/arquitectura.md`, para que las dos digan siempre lo mismo. **El HTML no se edita a mano:** se corrige el `.md` y se vuelve a generar.

Qué hace:

- Convierte el Markdown a HTML con `markdown-it`: tablas, enlaces y un id en cada encabezado, con el mismo algoritmo de anclas que usa GitHub (por ejemplo, `## 7. Modelo de datos` queda en `#7-modelo-de-datos`).
- Dibuja cada bloque ` ```mermaid ` como SVG con `@mermaid-js/mermaid-cli` y lo inserta dentro de la página, en `<figure class="chart">`.
- Arma el índice lateral con los títulos `##` y `###`, y marca la sección que se está leyendo.
- Usa la plantilla `arquitectura.plantilla.html` (estilos, índice y script de la versión 1.0, con los marcadores `{{TITULO}}`, `{{VERSION}}`, `{{INDICE}}` y `{{CONTENIDO}}`). La versión la toma de la línea `**Versión:**` de la cabecera del `.md`.
- Escribe el archivo en UTF-8 con fin de línea CRLF. La página no carga nada de internet: sin `<script src=`, hojas de estilo ni imágenes remotas.
- Se detiene con un mensaje claro si falta una dependencia, si un diagrama no se puede dibujar, si un enlace interno `#…` no tiene destino o si la salida tendría un recurso externo.

## Requisitos

- **Node 20 o superior** (`node --version`).
- Conexión a internet solo para el primer `npm install`.

## Comandos (Windows)

Desde la raíz del repositorio MATU, en PowerShell o en Git Bash (los comandos son los mismos):

```
cd docs/herramientas
npm install
node generar_arquitectura_html.mjs
```

- **`npm install` se corre una sola vez.** Instala las dos dependencias con versión fija (`package.json`) y **descarga un Chromium de unos 200 MB**, que `mermaid-cli` usa para dibujar los diagramas. Puppeteer lo guarda en `%USERPROFILE%\.cache\puppeteer`, fuera del repositorio. Crea también `package-lock.json`, que conviene subir junto con el cambio para que la instalación sea reproducible.
- **`node generar_arquitectura_html.mjs`** (o `npm run generar`) escribe `docs/arquitectura.html`. Muestra cada diagrama a medida que lo dibuja y termina con una línea `Listo: … · versión … · N entradas en el índice · N diagramas · N KB`. Tarda unos segundos por diagrama.

`node_modules/` no se sube: lo excluye el `.gitignore` de esta carpeta.

## Cómo revisar el resultado

1. Abre el archivo en el navegador. Desde la misma carpeta:
   - PowerShell: `start ..\arquitectura.html`
   - Git Bash: `start ../arquitectura.html`
2. Comprueba que:
   - el índice lateral lista todas las secciones y resalta la que estás leyendo al bajar;
   - cada diagrama aparece dibujado, sin etiquetas cortadas;
   - las tablas, los bloques de código y los enlaces a los ADR se ven bien;
   - la cabecera del índice dice la versión del `.md`.
3. Revisa el cambio antes del commit, desde la raíz del repositorio:

   ```
   git diff --stat docs/arquitectura.html
   git add docs/arquitectura.html docs/herramientas/package-lock.json
   ```

Si un diagrama falla, el mensaje dice en qué línea de `arquitectura.md` empieza. Se corrige ahí y se vuelve a correr el script.

#!/usr/bin/env node
// Genera docs/arquitectura.html desde docs/arquitectura.md (MATU-43).
//
// Uso, desde docs/herramientas:   node generar_arquitectura_html.mjs
//
// - Markdown a HTML con markdown-it (tablas, enlaces y un id estable en cada
//   encabezado, con el mismo algoritmo que usa GitHub para sus anclas).
// - Cada bloque ```mermaid se convierte en SVG con @mermaid-js/mermaid-cli y se
//   inserta inline en <figure class="chart">.
// - El índice lateral se arma con los h2 y h3, en el mismo orden en que el
//   script de la plantilla los observa para marcar la sección activa.
// - La salida es UTF-8 con CRLF y no carga ningún recurso externo.
//
// Requisitos: Node 20 o superior y `npm install` en esta carpeta.

import { mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));
const DOCS = path.resolve(AQUI, '..');
const ENTRADA = path.join(DOCS, 'arquitectura.md');
const SALIDA = path.join(DOCS, 'arquitectura.html');
const PLANTILLA = path.join(AQUI, 'arquitectura.plantilla.html');

// Configuración de Mermaid: la misma apariencia de la versión 1.0 (tema
// neutral, tipografía del sistema, líneas en gris cálido).
const FUENTE = "system-ui,-apple-system,'Segoe UI',Roboto,sans-serif";
const CONFIG_MERMAID = {
  theme: 'neutral',
  fontFamily: FUENTE,
  themeVariables: { fontFamily: FUENTE, fontSize: '13.5px', lineColor: '#898781' },
  flowchart: { htmlLabels: true, useMaxWidth: true },
};

class ErrorGeneracion extends Error {}

function fallar(mensaje) {
  throw new ErrorGeneracion(mensaje);
}

function comprobarNode() {
  const mayor = Number(process.versions.node.split('.')[0]);
  if (!(mayor >= 20)) {
    fallar(`Se necesita Node 20 o superior. Esta terminal tiene Node ${process.versions.node}.`);
  }
}

async function cargarDependencia(nombre) {
  try {
    return await import(nombre);
  } catch (e) {
    if (e && e.code === 'ERR_MODULE_NOT_FOUND') {
      fallar(
        `Falta la dependencia "${nombre}".\n` +
          `  Instálala con:  cd docs/herramientas  y luego  npm install\n` +
          `  (detalle: ${e.message})`,
      );
    }
    throw e;
  }
}

// Ancla al estilo de GitHub: minúsculas, se quitan los signos de puntuación
// (salvo guion y guion bajo), cada espacio pasa a guion y se conservan las
// letras con tilde. Los repetidos llevan -1, -2, etc.
function crearGeneradorDeAnclas() {
  const usadas = new Map();
  return (texto) => {
    const base = texto
      .trim()
      .toLowerCase()
      .replace(/[^\p{L}\p{M}\p{N}\p{Pc}\- ]/gu, '')
      .replace(/ /g, '-');
    let ancla = base;
    if (usadas.has(base)) {
      let n = usadas.get(base);
      do {
        n += 1;
        ancla = `${base}-${n}`;
      } while (usadas.has(ancla));
      usadas.set(base, n);
    }
    usadas.set(ancla, usadas.get(ancla) ?? 0);
    return ancla;
  };
}

// Texto plano de un encabezado, sin el marcado de negritas, código o enlaces.
function textoPlano(inline) {
  if (!inline || !inline.children) return inline ? inline.content : '';
  return inline.children
    .map((t) => {
      if (t.type === 'text' || t.type === 'code_inline') return t.content;
      if (t.type === 'softbreak' || t.type === 'hardbreak') return ' ';
      return '';
    })
    .join('');
}

function esMermaid(token) {
  return token.type === 'fence' && token.info.trim().split(/\s+/)[0] === 'mermaid';
}

async function renderizarMermaid(run, codigo, id, dirTemporal, linea) {
  const entrada = path.join(dirTemporal, `${id}.mmd`);
  const salida = path.join(dirTemporal, `${id}.svg`);
  await writeFile(entrada, codigo, 'utf8');
  try {
    await run(entrada, salida, {
      quiet: true,
      outputFormat: 'svg',
      parseMMDOptions: {
        svgId: id,
        backgroundColor: 'transparent',
        mermaidConfig: CONFIG_MERMAID,
      },
    });
  } catch (e) {
    fallar(`Mermaid no pudo dibujar el diagrama de la línea ${linea} de arquitectura.md:\n  ${e.message}`);
  }
  let svg = await readFile(salida, 'utf8');
  svg = svg
    .replace(/^\uFEFF/, '')
    .replace(/<\?xml[^>]*\?>\s*/g, '')
    .replace(/<!DOCTYPE[^>]*>\s*/gi, '')
    // Un @import dentro del <style> del SVG sería un recurso externo.
    .replace(/@import\s+url\([^)]*\)\s*;?/g, '')
    .trim();
  if (!svg.startsWith('<svg')) {
    fallar(`El diagrama de la línea ${linea} no produjo un SVG válido.`);
  }
  return svg;
}

// Nada de la página puede cargar un recurso de otro sitio.
function comprobarSinRecursosExternos(html) {
  const prohibidos = [
    [/<script\b[^>]*\bsrc\s*=/i, '<script src=…>'],
    [/<link\b/i, '<link>'],
    [/<iframe\b/i, '<iframe>'],
    [/@import\b/i, '@import'],
    [/url\(\s*['"]?\s*(?:https?:)?\/\//i, 'url(http…)'],
    [/<(?:img|image|source|video|audio|embed|object)\b[^>]*\b(?:src|href|xlink:href|data)\s*=\s*['"]?\s*(?:https?:)?\/\//i, 'imagen o medio remoto'],
  ];
  for (const [patron, nombre] of prohibidos) {
    const m = html.match(patron);
    if (m) {
      const i = m.index ?? 0;
      fallar(`La salida tendría un recurso externo (${nombre}) cerca de: ${html.slice(i, i + 120)}`);
    }
  }
}

// Todo enlace interno (#ancla) del documento debe tener su encabezado.
function comprobarAnclas(html) {
  const ids = new Set([...html.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1]));
  const rotas = [...html.matchAll(/href="#([^"]*)"/g)]
    .map((m) => {
      try {
        return decodeURIComponent(m[1]);
      } catch {
        return m[1];
      }
    })
    .filter((a) => !ids.has(a));
  if (rotas.length > 0) {
    fallar(`Hay enlaces internos sin destino: ${[...new Set(rotas)].map((a) => `#${a}`).join(', ')}`);
  }
}

function rellenar(plantilla, valores) {
  let salida = plantilla;
  for (const [clave, valor] of Object.entries(valores)) {
    const marcador = `{{${clave}}}`;
    if (!salida.includes(marcador)) fallar(`La plantilla no tiene el marcador ${marcador}.`);
    // split/join en vez de replace: el contenido puede traer "$&" u otros
    // patrones que replace interpretaría.
    salida = salida.split(marcador).join(valor);
  }
  const sobrante = salida.match(/\{\{[A-Z]+\}\}/);
  if (sobrante) fallar(`La plantilla tiene un marcador sin valor: ${sobrante[0]}`);
  return salida;
}

async function principal() {
  comprobarNode();
  const { default: MarkdownIt } = await cargarDependencia('markdown-it');
  const { run } = await cargarDependencia('@mermaid-js/mermaid-cli');
  if (typeof MarkdownIt !== 'function') fallar('markdown-it no exporta lo esperado. Revisa la versión de package.json.');
  if (typeof run !== 'function') fallar('@mermaid-js/mermaid-cli no exporta run. Revisa la versión de package.json.');

  const markdown = await readFile(ENTRADA, 'utf8').catch(() => fallar(`No se encontró ${ENTRADA}`));
  const plantilla = await readFile(PLANTILLA, 'utf8').catch(() => fallar(`No se encontró ${PLANTILLA}`));

  const versionEncontrada = markdown.match(/^\*\*Versión:\*\*\s*(.+?)\s*$/m);
  if (!versionEncontrada) fallar('arquitectura.md no tiene la línea "**Versión:** …" de la cabecera.');
  const version = versionEncontrada[1];

  const md = new MarkdownIt({ html: false, linkify: false, typographer: false });
  const env = {};
  const tokens = md.parse(markdown.replace(/^\uFEFF/, ''), env);

  // Anclas e índice.
  const anclar = crearGeneradorDeAnclas();
  const indice = [];
  let titulo = '';
  for (let i = 0; i < tokens.length; i += 1) {
    const t = tokens[i];
    if (t.type !== 'heading_open') continue;
    const texto = textoPlano(tokens[i + 1]).trim();
    const ancla = anclar(texto);
    t.attrSet('id', ancla);
    if (t.tag === 'h1' && !titulo) titulo = texto.replace(/\s+—\s+/g, ' · ');
    if (t.tag === 'h2' || t.tag === 'h3') {
      indice.push(`<a class="lvl${t.tag[1]}" href="#${ancla}">${md.utils.escapeHtml(texto)}</a>`);
    }
  }
  if (!titulo) fallar('arquitectura.md no tiene un título "# …".');
  if (indice.length === 0) fallar('arquitectura.md no tiene encabezados ## ni ###.');

  // Diagramas: se dibujan antes de renderizar, porque el renderer es síncrono.
  const diagramas = tokens.map((t, i) => [t, i]).filter(([t]) => esMermaid(t));
  const svgs = new Map();
  if (diagramas.length > 0) {
    const dirTemporal = await mkdtemp(path.join(os.tmpdir(), 'matu-arq-'));
    try {
      for (const [n, [t, i]] of diagramas.entries()) {
        const linea = t.map ? t.map[0] + 1 : '?';
        process.stdout.write(`Diagrama ${n + 1} de ${diagramas.length} (línea ${linea})… `);
        svgs.set(i, await renderizarMermaid(run, t.content, `dg${n}`, dirTemporal, linea));
        process.stdout.write('listo\n');
      }
    } finally {
      await rm(dirTemporal, { recursive: true, force: true });
    }
  }

  const fenceOriginal = md.renderer.rules.fence;
  md.renderer.rules.fence = (toks, idx, options, entorno, self) => {
    if (svgs.has(idx)) return `<figure class="chart">${svgs.get(idx)}</figure>\n`;
    return fenceOriginal(toks, idx, options, entorno, self);
  };
  const contenido = md.renderer.render(tokens, md.options, env);

  const figuras = (contenido.match(/<figure class="chart">/g) || []).length;
  if (figuras !== diagramas.length) {
    fallar(`Se esperaban ${diagramas.length} diagramas en la salida y hay ${figuras}.`);
  }

  const html = rellenar(plantilla, {
    TITULO: md.utils.escapeHtml(titulo),
    VERSION: md.utils.escapeHtml(version),
    INDICE: indice.join('\n'),
    CONTENIDO: contenido,
  });
  comprobarSinRecursosExternos(html);
  comprobarAnclas(html);

  const crlf = html.replace(/\r\n/g, '\n').replace(/\n/g, '\r\n');
  await writeFile(SALIDA, crlf, { encoding: 'utf8' });
  console.log(
    `Listo: ${path.relative(process.cwd(), SALIDA) || SALIDA} · versión ${version} · ` +
      `${indice.length} entradas en el índice · ${diagramas.length} diagramas · ` +
      `${Math.round(Buffer.byteLength(crlf, 'utf8') / 1024)} KB`,
  );
}

principal().catch((e) => {
  if (e instanceof ErrorGeneracion) {
    console.error(`\nError: ${e.message}`);
  } else {
    console.error('\nError inesperado al generar arquitectura.html:');
    console.error(e);
  }
  process.exitCode = 1;
});

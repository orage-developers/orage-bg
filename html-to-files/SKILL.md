---
name: html-to-files
description: >
  Crea archivos DOCX, PPTX, PDF, XLSX y CSV siempre a partir de un HTML fuente.
  Úsala cuando un agente deba entregar un documento Word, una presentación
  PowerPoint, un PDF, una hoja de cálculo Excel o un CSV, o convertir contenido
  a cualquiera de esos formatos. El agente escribe primero un HTML y luego lo
  convierte con scripts/html2file.py. Nunca genera el binario directamente.
  Todo archivo sigue siempre las brand guidelines de ORAGE AI AGENCY (brand/).
---

# HTML a archivos (DOCX, PPTX, PDF, XLSX, CSV)

Regla única: **todo archivo nace de un HTML**. El HTML es la fuente de verdad.
Para cambiar el archivo, edita el HTML y vuelve a convertir. No uses
python-docx, python-pptx, openpyxl, reportlab ni editores de binarios para
crear el contenido.

## Brand guidelines (obligatorio)

Todo archivo usa **siempre** la marca de ORAGE AI AGENCY, salvo que la
petición nombre otra marca de forma explícita. Antes de escribir el HTML:

1. Lee `brand/BRAND.md` (voz, color, tipografía, logo, documentos, decks).
2. Toma los hechos de la empresa solo de `brand/COMPANY.md`. Nunca inventes
   clientes, resultados, precios, direcciones ni teléfonos.
3. Parte siempre de una plantilla de `templates/`. Ya aplican la marca.

Reglas que todo archivo cumple:

- Colores solo de `brand/tokens.css`: Ink `#0A0A0A`, Storm Gold `#B68039`
  (único acento, nunca rellena una página), blanco y neutros. Ningún otro
  tono, tampoco en gráficos (usa oro, graphite y tintes muted).
- Tipos: Syne (Bold/ExtraBold, mayúsculas) en títulos; Space Grotesk en
  texto. Ninguna otra familia.
- Emblema `brand://logo/logo.png` en cada pieza, sin alterar.
- Documentos y PDF: páginas blancas, texto Ink, banda o portada Ink con el
  emblema, regla dorada bajo cada título, pie "ORAGE AGENCY LLC ·
  orage.agency".
- Presentaciones: portada y cierre en Ink con el emblema, diapositivas de
  contenido en blanco, oro solo para la cifra que importa.
- Hojas de datos: el PDF del mismo HTML lleva banda Ink con el emblema.
- Voz (§2 de `BRAND.md`): directa, frases cortas, resultado primero. En
  español, "usted". Sin promesas de resultados ni emojis en títulos.

### URLs `brand://`

En el HTML, `brand://<ruta>` apunta a la carpeta `brand/` de esta skill.
El script la resuelve en cada conversión. Ejemplos:

```html
<img src="brand://logo/logo.png" width="56" alt="ORAGE AI AGENCY">
<style>
  @font-face { font-family: "Syne"; src: url("brand://fonts/Syne.ttf"); font-weight: 400 800; }
</style>
```

Para DOCX el script incrusta las imágenes locales como `data:` URI. Para
DOCX y PPTX instala las fuentes de marca en la carpeta de fuentes del
usuario (`~/.local/share/fonts/orage-brand` en Linux, `~/Library/Fonts` en
macOS) si faltan, para que LibreOffice las use.

`brand/` contiene `BRAND.md`, `COMPANY.md`, `tokens.css`, `fonts/` y
`logo/logo.png`. Las variantes `logo-white.png` y `brandmark.png` que cita
`BRAND.md` son el mismo archivo: usa `logo.png`.

## Flujo

1. Lee `brand/BRAND.md`. Elige la plantilla según el formato (tabla abajo) y cópiala junto al
   entregable, por ejemplo `informe.html`.
2. Escribe el contenido en ese HTML. Respeta las reglas del formato.
3. Convierte:
   ```bash
   python3 <skill-dir>/scripts/html2file.py informe.html --to docx -o informe.docx
   ```
4. Verifica el resultado (sección "Verificación").
5. Entrega el archivo y conserva el HTML junto a él.

Si piden también el PDF de un DOCX, PPTX, XLSX o CSV, conviértelo desde el
**mismo HTML** con `--to pdf`. Nunca conviertas el binario a PDF para
entregarlo: la fuente siempre es el HTML.

| Formato | Plantilla | Motor | Requisitos |
|---|---|---|---|
| PDF | `templates/document.html` o `templates/slides.html` | Chrome headless (`--print-to-pdf`) | Chrome o Chromium |
| DOCX | `templates/document.html` | LibreOffice Writer (import HTML) | `soffice` |
| PPTX | `templates/slides.html` | Chrome a PDF, luego LibreOffice Impress (import PDF) | Chrome + `soffice` |
| XLSX | `templates/data.html` | Escritor propio en stdlib | Python 3 |
| CSV | `templates/data.html` | `csv` de stdlib | Python 3 |

Variables opcionales: `CHROME_BIN`, `SOFFICE_BIN` (rutas a los binarios),
`CHROME_NO_SANDBOX=1` (contenedores sin sandbox).

## Opciones del script

```
html2file.py INPUT.html --to pdf|docx|pptx|xlsx|csv [-o OUTPUT]
  --wait MS        tiempo para fuentes/JS en Chrome (por defecto 3000)
  --table N|NAME   csv: exporta solo esa tabla (índice desde 1 o nombre de hoja)
  --delimiter ;    csv: separador (por defecto ,)
  --bom            csv: añade BOM UTF-8 para que Excel detecte acentos
```

El script imprime la ruta de cada archivo creado. Sale con código distinto
de 0 y un mensaje `html2file: error:` si algo falla.

## Reglas por formato

### PDF

- Controla el tamaño con `@page { size: A4; margin: 20mm; }` (o `Letter`).
- Salto de página: `page-break-before: always` en el elemento.
- Colores de fondo: añade `print-color-adjust: exact` al `body`.
- Chrome renderiza todo el CSS moderno (flex, grid, fuentes web, SVG).

### DOCX

LibreOffice importa un subconjunto de HTML/CSS. Para un DOCX fiel:

- Estructura semántica: `h1`–`h3`, `p`, `ul`/`ol`, `table`, `strong`, `em`,
  `a`, `img`. Los encabezados se vuelven estilos de Word reales.
- Declara la fuente en cada selector (`body, h1, h2, h3, p, li, td, th`). El
  import no hereda la fuente de `body`.
- Tablas: usa atributos `border="1" cellspacing="0" cellpadding="6"
  width="100%"`. Fondo de celda con `bgcolor="#0A0A0A"` y alineación con
  `align`. El color de texto en `th` se pierde: envuélvelo en
  `<span class="on-ink">`.
- Colores en hex, no `var(--o-…)`: el import no lee variables CSS.
- Pie de página: `@page @bottom-center` solo existe en el PDF.
- Sin flex, grid ni `position`: se pierden. Usa tablas para maquetar
  columnas (como la banda de cabecera de la plantilla).
- Imágenes: rutas relativas al HTML o `data:` URI, con `width` explícito.

### PPTX

- Cada `<section class="slide">` es una diapositiva de 13.333 × 7.5 in (16:9).
- No cambies `@page` ni el tamaño de `.slide`. El contenido que desborde se
  corta (`overflow: hidden`).
- Todo CSS de Chrome vale (flex, grid, fuentes web, SVG).
- El PPTX resultante tiene texto y formas editables, colocados de forma
  absoluta. Para editar el diseño, edita el HTML y reconvierte.
- Syne es una fuente variable: en el PPTX los títulos pueden verse con peso
  normal en vez de Bold. El PDF del mismo HTML los muestra correctos.

### XLSX

- Cada `<table>` de nivel superior es una hoja. Nombre de hoja:
  `data-sheet="Nombre"`, si no, el `<caption>`, si no, `Sheet1`, `Sheet2`…
- Las filas cuyo contenido es solo `<th>` salen en negrita. Si la primera
  fila es de `<th>`, queda fija (freeze pane).
- Tipos: números como `12` o `19.90` se guardan como número. Fuerza texto
  con `data-type="text"` (códigos con ceros a la izquierda, fechas ISO,
  teléfonos). Fuerza número con `data-type="number"`. Booleano:
  `data-type="bool"`.
- Fórmulas: `<td data-formula="=SUM(B2:B3)">17</td>`. Excel recalcula al
  abrir. Pon el valor calculado como texto de la celda para que el HTML,
  el PDF y el CSV también lo muestren.
- Valor distinto del texto visible: `data-value="1234.5"`.
- `colspan` se respeta rellenando celdas vacías. `rowspan` no se admite:
  repite el valor en cada fila.
- `<br>` dentro de una celda crea salto de línea.

### CSV

- Misma fuente que XLSX (`templates/data.html`).
- Una tabla: un archivo. Varias tablas: un archivo por tabla con sufijo
  `-<hoja>`, salvo que elijas una con `--table`.
- Se exporta `data-value` si existe, si no, el texto visible. Las fórmulas
  no se exportan: el texto de la celda debe llevar el valor.
- Para Excel en español usa `--delimiter ";" --bom`.

## Verificación

Antes de entregar, comprueba siempre el resultado:

- PDF, DOCX, PPTX: convierte el archivo a PDF y rasteriza la primera página
  para revisarla a ojo:
  ```bash
  soffice --headless --convert-to pdf --outdir /tmp/check archivo.docx
  pdftoppm -r 50 -png -f 1 -l 1 /tmp/check/archivo.pdf /tmp/check/p
  ```
- PPTX: el número de diapositivas debe igualar el número de `.slide`:
  `unzip -l archivo.pptx | grep -c 'ppt/slides/slide'`.
- XLSX: reconvierte a CSV con `soffice --convert-to csv` y revisa valores y
  fórmulas calculadas.
- CSV: `head` del archivo; revisa acentos y separador.

## Errores comunes

- `LibreOffice produced no output`: el HTML no existe o tiene un error de
  codificación. Guarda siempre en UTF-8 con `<meta charset="utf-8">`.
- `Chrome/Chromium not found`: instala Chrome o define `CHROME_BIN`.
- Fuentes distintas en DOCX: la fuente no está instalada en el sistema o
  no se declaró en cada selector.
- Diapositivas de más en PPTX: algún `.slide` desborda o hay contenido
  fuera de las secciones.

---
name: html-to-files
description: >
  Crea archivos DOCX, PPTX, PDF, XLSX y CSV siempre a partir de un HTML fuente,
  con la marca de Orage AI Agency. Úsala cuando un agente deba entregar un
  documento Word, una presentación PowerPoint, un PDF, una hoja de cálculo
  Excel o un CSV, o convertir contenido a cualquiera de esos formatos. El agente
  escribe primero un HTML con las brand guidelines (brand/BRAND-GUIDELINES.md)
  y luego lo convierte con scripts/html2file.py. Nunca genera el binario
  directamente.
---

# HTML a archivos (DOCX, PPTX, PDF, XLSX, CSV)

Dos reglas, sin excepción:

1. **Todo archivo nace de un HTML.** El HTML es la fuente de verdad. Para
   cambiar el archivo, edita el HTML y vuelve a convertir. No uses
   python-docx, python-pptx, openpyxl, reportlab ni editores de binarios para
   crear el contenido.
2. **Todo archivo sigue las brand guidelines de Orage AI Agency**
   (`brand/BRAND-GUIDELINES.md`), salvo que la petición nombre otra marca de
   forma explícita.

`<skill-dir>` en este documento es la carpeta que contiene este `SKILL.md`.

## Brand guidelines (obligatorio)

Antes de escribir el HTML, lee `brand/BRAND-GUIDELINES.md` completo. Toma de
ahí la voz, los colores, la tipografía y los hechos de la empresa (oferta,
precios, productos, ubicación). Nunca inventes clientes, resultados, cifras,
precios ni datos de contacto que no estén en ese archivo.

Las plantillas de `templates/` ya aplican la marca. Resumen de lo que todo
archivo cumple:

- **Modo oscuro** en documentos, PDF y presentaciones: fondo `#000000`,
  superficies `#151515` y `#212121`, texto tan `#FFD69C` / `#FFE8C7`.
  Nunca blanco puro en modo oscuro. (El modo claro es solo para email, que
  esta skill no produce.)
- **Oro ancla `#B68039`** visible en cada pieza (títulos, reglas, cifra
  clave). Encabezados y énfasis en cobre `#E4AF7A`. Divisores e iconos en
  `#543C1C`. Ningún otro color: tokens en `brand/tokens.css`.
- **Dos fuentes, nunca una tercera**: Bebas Neue (solo peso 400, siempre
  MAYÚSCULAS y con letter-spacing) para títulos, eyebrows, precios y
  botones; Montserrat (500 texto, 600 entradilla, 700 énfasis) en
  sentence case para el resto.
- **Un family por peso**: Word y LibreOffice solo distinguen normal y bold.
  Pide Medium y SemiBold por nombre con `font-weight: normal`:
  `"Montserrat Medium"` (texto), `"Montserrat SemiBold"` (entradilla) y
  `"Montserrat"` con `font-weight: 700` (énfasis). Las plantillas ya
  declaran los `@font-face`. Nunca uses `font-weight: 500` o `600`: en
  DOCX salen en Bold.
- Bebas Neue no tiene `→` ni `×`. Escribe `3X` en vez de `3×` y pon la
  flecha en Montserrat: `<span class="arrow">→</span>`. Si no, aparece una
  tercera fuente de reserva.
- **Emblema** `brand://logo/logo.png` en cada pieza, sin alterar.
- **Voz**: confiada, directa, premium, orientada a la acción. Resultado
  primero, frases cortas, números en vez de adjetivos, "nosotros" para la
  empresa y "usted" para el comprador. Sin palabras hype
  ("revolucionario", "de vanguardia", "game-changing").
- Sin emojis en títulos, botones ni etiquetas; `→` es el único glifo
  permitido. Sin comillas para enfatizar: usa negrita o oro.
- Pie de documentos PDF: "© Orage AI Agency · Edmond, Oklahoma ·
  orage.agency" (ya está en las plantillas).

### URLs `brand://`

En el HTML, `brand://<ruta>` apunta a la carpeta `brand/` de esta skill. El
script la resuelve en cada conversión. Ejemplos:

```html
<img src="brand://logo/logo.png" width="56" alt="Orage AI Agency">
<style>
  @font-face { font-family: "Bebas Neue"; src: url("brand://fonts/BebasNeue-Regular.ttf"); }
</style>
```

Para DOCX el script incrusta las imágenes locales como `data:` URI. Para
DOCX y PPTX instala las fuentes de marca en la carpeta de fuentes del usuario
(`~/.local/share/fonts/orage-brand` en Linux, `~/Library/Fonts` en macOS)
si faltan, para que LibreOffice las use.

`brand/` contiene `BRAND-GUIDELINES.md`, `tokens.css`, `fonts/` (Bebas Neue,
Montserrat Medium/SemiBold/Bold, licencias OFL) y `logo/logo.png`.
`brand/BRAND-GUIDELINES.md` es copia de `BRAND-GUIDELINES.md` en la raíz del
repositorio: si cambia la raíz, actualiza la copia.

## Flujo

1. Lee `brand/BRAND-GUIDELINES.md`.
2. Copia la plantilla del formato junto al entregable:
   ```bash
   cp <skill-dir>/templates/document.html <salida>/informe.html
   ```
3. Escribe el contenido en ese HTML. Cambia el `<title>`. Conserva el
   bloque `<style>` y la cabecera con el emblema. Respeta las reglas del
   formato (abajo). `text-transform: uppercase` funciona en todos los
   formatos.
4. Convierte:
   ```bash
   python3 <skill-dir>/scripts/html2file.py <salida>/informe.html --to docx
   ```
   Sin `-o`, la salida es el HTML con la nueva extensión
   (`<salida>/informe.docx`).
5. Verifica el resultado (sección "Verificación").
6. Entrega el archivo y conserva el HTML junto a él.

Si piden también el PDF de un DOCX, PPTX, XLSX o CSV, conviértelo desde el
**mismo HTML** con `--to pdf`. Queda como `<nombre>.pdf` al lado del otro
archivo. Nunca conviertas el binario a PDF para entregarlo: la fuente siempre
es el HTML.

| Formato | Plantilla | Motor | Requisitos |
|---|---|---|---|
| PDF | la del formato hermano, o `document.html` | Chrome headless (`--print-to-pdf`) | Chrome o Chromium |
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

- Tamaño y fondo de página con `@page { size: Letter; margin: …;
  background: #000000; }`. El fondo de `@page` cubre también los márgenes.
- Pie repetido: `@page { @bottom-center { content: "…"; } }`.
- Salto de página: `page-break-before: always` en el elemento.
- Chrome renderiza todo el CSS moderno (flex, grid, fuentes web, SVG).

### DOCX

LibreOffice importa un subconjunto de HTML/CSS. Para un DOCX fiel:

- Estructura semántica: `h1`–`h3`, `p`, `ul`/`ol`, `table`, `strong`, `em`,
  `a`, `img`. Los encabezados se vuelven estilos de Word reales.
- Fondo de página: `<body bgcolor="#000000">`. El script lo aplica como
  color de página del DOCX.
- Declara la fuente y el color en cada selector (`body, p, li, td, th,
  span`). El import no hereda de `body`.
- Colores en hex, no `var(--o-…)`: el import no lee variables CSS.
- Tablas: atributos `border="1" cellspacing="0" cellpadding="6"
  width="100%"`. Fondo de celda con `bgcolor` y alineación con `align`. El
  color de texto en `th` se pierde: envuélvelo en `<span class="th">`.
- Sin flex, grid ni `position`: se pierden. Maqueta columnas con tablas
  (como la banda de cabecera de la plantilla).
- El DOCX no tiene pie de página: `@page` solo existe en el PDF.
- La paginación del DOCX difiere del PDF: LibreOffice ocupa más alto que
  Chrome. Si piden un número de páginas, cuenta las páginas del DOCX
  (Verificación) y recorta texto o tamaños hasta cumplirlo.
- Imágenes: rutas relativas al HTML, `brand://` o `data:` URI, con `width`
  explícito.

### PPTX

- Cada `<section class="slide">` es una diapositiva de 13.333 × 7.5 in (16:9).
- No cambies `@page` ni el tamaño de `.slide`. El contenido que desborde se
  corta (`overflow: hidden`).
- Todo CSS de Chrome vale (flex, grid, fuentes web, SVG).
- Portada y cierre con clase `cover` y emblema; contenido sobre negro.
- El PPTX tiene texto y formas editables, colocados de forma absoluta. Para
  cambiar el diseño, edita el HTML y reconvierte.
- El script corrige el PPTX tras el import: nombres de fuente reales y
  letter-spacing de Bebas Neue. El espaciado del PPTX es aproximado; el
  PDF del mismo HTML es la referencia exacta.
- Tamaño de texto que cabe: título 54–88pt, texto 20–24pt, máximo 5
  viñetas o unas 40 palabras por diapositiva.

### XLSX

- Cada `<table>` de nivel superior es una hoja. Nombre de hoja:
  `data-sheet="Nombre"`, si no, el `<caption>`, si no, `Sheet1`, `Sheet2`…
- El script aplica el estilo de marca: Montserrat en todas las celdas y
  `<th>` en Montserrat Bold cobre sobre `#151515`. El CSS del HTML no
  afecta al XLSX. Si la primera fila es de `<th>`, queda fija.
- Tipos: números como `12` o `19.90` se guardan como número. Fuerza texto
  con `data-type="text"` (códigos con ceros a la izquierda, fechas ISO,
  teléfonos). Fuerza número con `data-type="number"`. Booleano:
  `data-type="bool"`.
- Fórmulas: `<td data-formula="=SUM(B2:B3)">17</td>`. Excel recalcula al
  abrir. Pon el valor calculado como texto de la celda para que el PDF y
  el CSV también lo muestren.
- Valor distinto del texto visible: `data-value="1234.5"`.
- `colspan` se respeta rellenando celdas vacías. `rowspan` no se admite:
  repite el valor en cada fila.
- `<br>` dentro de una celda crea salto de línea.
- El contenido fuera de `<table>` (cabecera, notas `.note`) solo aparece en
  el PDF.

### CSV

- Misma fuente que XLSX (`templates/data.html`).
- Una tabla: un archivo. Varias tablas: un archivo por tabla con sufijo
  `-<hoja>`, salvo que elijas una con `--table`.
- Se exporta `data-value` si existe, si no, el texto visible. Las fórmulas
  no se exportan: el texto de la celda debe llevar el valor.
- Por defecto: UTF-8, separador `,`. Solo si el destino es Excel en
  español, usa `--delimiter ";" --bom`.

## Verificación

Usa un directorio de trabajo temporal propio (`$CHECK`), por ejemplo el
scratchpad de la sesión o `mktemp -d`. Nunca uses la carpeta de salida: el
PDF de revisión sobrescribiría el PDF entregado. Revisa todas las páginas,
no solo la primera (ajusta `-l`). Comprueba siempre:

- PDF: `head -c 4 archivo.pdf` imprime `%PDF`. Rasteriza y mira las
  páginas:
  ```bash
  pdfinfo archivo.pdf | grep Pages
  pdftoppm -r 40 -png -f 1 -l 2 archivo.pdf "$CHECK/p"
  ```
- DOCX y PPTX: conviértelos a PDF solo para revisarlos y mira las páginas:
  ```bash
  soffice --headless --convert-to pdf --outdir "$CHECK" archivo.docx
  pdfinfo "$CHECK/archivo.pdf" | grep Pages
  pdftoppm -r 40 -png -f 1 -l 2 "$CHECK/archivo.pdf" "$CHECK/p"
  ```
- Fuentes: en cada PDF (entregado o de revisión), `pdffonts` solo debe
  listar BebasNeue y Montserrat (más OpenSymbol para viñetas de DOCX).
  Cualquier otra fuente es un glifo sin cobertura o un nombre mal escrito.
- PPTX: el número de diapositivas debe igualar el número de `.slide`:
  `unzip -l archivo.pptx | grep -c 'ppt/slides/slide[0-9]*.xml'`.
- XLSX: exporta todas las hojas a CSV (una por hoja) y revisa valores y
  fórmulas calculadas:
  ```bash
  soffice --headless --convert-to 'csv:Text - txt - csv (StarCalc):44,34,76,1,,0,false,true,false,false,false,-1' \
    --outdir "$CHECK" archivo.xlsx
  ```
- CSV: `head` del archivo; revisa acentos y separador.

## Errores comunes

- `LibreOffice produced no output`: el HTML no existe o tiene un error de
  codificación. Guarda siempre en UTF-8 con `<meta charset="utf-8">`.
- `Chrome/Chromium not found`: instala Chrome o define `CHROME_BIN`.
- Fuentes distintas en DOCX: la fuente no se declaró en cada selector.
- Texto en Bold en DOCX: se usó `font-weight: 500/600` en vez del family
  por peso.
- Página blanca en DOCX: falta `bgcolor` en `<body>`.
- Diapositivas de más en PPTX: algún `.slide` desborda o hay contenido
  fuera de las secciones.

---
name: html-to-files
description: >
  Crea archivos DOCX, PPTX, PDF, XLSX y CSV siempre a partir de un HTML fuente.
  Úsala cuando un agente deba entregar un documento Word, una presentación
  PowerPoint, un PDF, una hoja de cálculo Excel o un CSV, o convertir contenido
  a cualquiera de esos formatos. El agente escribe primero un HTML y luego lo
  convierte con scripts/html2file.py. Nunca genera el binario directamente.
---

# HTML a archivos (DOCX, PPTX, PDF, XLSX, CSV)

Regla única: **todo archivo nace de un HTML**. El HTML es la fuente de verdad.
Para cambiar el archivo, edita el HTML y vuelve a convertir. No uses
python-docx, python-pptx, openpyxl, reportlab ni editores de binarios para
crear el contenido.

## Flujo

1. Elige la plantilla según el formato (tabla abajo) y cópiala junto al
   entregable, por ejemplo `informe.html`.
2. Escribe el contenido en ese HTML. Respeta las reglas del formato.
3. Convierte:
   ```bash
   python3 <skill-dir>/scripts/html2file.py informe.html --to docx -o informe.docx
   ```
4. Verifica el resultado (sección "Verificación").
5. Entrega el archivo y conserva el HTML junto a él.

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
  width="100%"`. Bordes y fondo en `td`/`th` por CSS sí funcionan.
- Sin flex, grid, `position`, variables CSS ni fuentes web: se pierden.
  Usa colores en hex y tablas para maquetar columnas.
- Imágenes: rutas relativas al HTML o `data:` URI, con `width` explícito.

### PPTX

- Cada `<section class="slide">` es una diapositiva de 13.333 × 7.5 in (16:9).
- No cambies `@page` ni el tamaño de `.slide`. El contenido que desborde se
  corta (`overflow: hidden`).
- Todo CSS de Chrome vale (flex, grid, fuentes web, SVG).
- El PPTX resultante tiene texto y formas editables, colocados de forma
  absoluta. Para editar el diseño, edita el HTML y reconvierte.

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

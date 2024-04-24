import pdfplumber
import re

pdf = pdfplumber.open('/Users/josecalatayud/UAB/2_quadrimestre/Obtencio_i_emmagatzematge_de_dades/Web_scrapping/pdfextract còpia/productos.pdf')
page = pdf.pages[2]
text=page.extract_text()

linies = text.split('\n')
i = 0
express_reg = re.compile('^\d\.\d (.*)')
for lin in linies:
    if express_reg.match(lin):
        print(lin[5:])

print('end')


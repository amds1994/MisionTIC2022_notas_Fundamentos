# Importar librerias para leer pdf
import fitz
import unidecode

# carga el archivo
pdf_prueba = 'C:\\Users\Mauricio\\Desktop\\prueba.pdf'
documento = fitz.open(pdf_prueba)

# obtener texto de todas las paginas y transformar el texto de todas las paginas
texto = ''
for pagina in documento:
    texto += unidecode.unidecode(pagina.get_text())
# transformar el texto de todas las paginas
texto = unidecode.unidecode(texto)
# quitar las comas del texto de todas las paginas
texto = texto.replace(',','')
print(texto)
# Guardar el texto de todas las paginas en un archivo
with open('C:\\Users\Mauricio\\Desktop\\prueba2.txt', 'w') as archivo:
    archivo.write(texto)
# cerrar el archivo
archivo.close()
# cerrar el documento
documento.close()

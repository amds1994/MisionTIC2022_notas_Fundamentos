# Manejo de archivos
import pandas as pd
import numpy as np
print('\x1Bc')

#Crear dataframe apartir de un diccionario
# listado de atletas
dict_datos = {
    'Nombre': ['Juan', 'Pedro', 'Maria', 'Pablo'],
    'Apellido': ['Perez', 'Gonzalez', 'Lopez', 'Garcia'],
    'Edad': [20, 21, 22, 23],
    'Partido_1': [7.4, 4.2, 10, 0],
    'Partido_2': [6.4, 7.2, 15, 9]
}
print(dict_datos)

datos_deportistas = pd.DataFrame(dict_datos)
print(datos_deportistas)

# Exportar como archivo csv
# datos_deportistas.to_csv('datos_deportistas.csv')
# print('Archivo exportado con exito')
# leer archivos csc
df = pd.read_csv('datos_deportistas.csv', index_col=0)
print(df)

# manejo de archivos de excel
#datos_deportistas.to_excel('datos_deportistas.csv')
# tener cuidado que con los archivos de excel no se reescriben y saldra error
#print('Archivo exportado con exito')
# try:
#     datos_deportistas.to_excel('datos_deportistas.csv')
#     print('Archivo exportado con exito')
# except:
#     print('Error al exportar el archivo')


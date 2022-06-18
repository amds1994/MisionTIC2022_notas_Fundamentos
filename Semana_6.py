import pandas as pd
import numpy as np
print('\x1Bc') # Formatea la consola

# Seleccionar informacion de la serie
notas = pd.Series({'Matematicas': 4.9, 'Iingles': 4.5, 'Habilidades': 3, 'Programacion': 5})
print(notas)
print('Nota de matematicas: ',notas[0])

print('\nNotas por rango Ingles, Habilidades')
print(notas[1:3])

print('\nindex y por el valor')
print(notas[[3,1]])

print('\nFuncion get')
print(notas.get('Matematicas'))
print(notas.get(0))

# Metodo loc e iloc
asignaturas = pd.Series(['Matemáticas', 'Ingles', 'Programacion', 'Habilidades'], index=['M1', 'I2', 'P3', 'H4'])
print(asignaturas)
print('\nIndice explicito o etiquetas: ',asignaturas.loc['M1'])
print('\nIndice implicito: \n',asignaturas.iloc[0:3])

print('\nPor indice implicito')
print(asignaturas.iloc[[0,2]]) # Recordar la doble llave

print('\n Aleatorios ----> sample')
print(asignaturas.sample(1, random_state=0))

print('\n Eliminar asignaturas')
print(asignaturas.drop('M1'))
print(asignaturas.pop('M1'))
print(asignaturas.drop(asignaturas.index[0]))

# Cuales edades son mayores a 5

x = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(x > 5)
print('\nSolo los numeros: \n')
print(x[x > 5])

print(x.axes)
print('La dimension o tamaño de mi serie es: ',x.shape)

# Edicion de series 
print(asignaturas)
asignaturas[1] = 'Programacion II'
print(asignaturas)

asignaturas[0:2] = ['Sociales', 'Historia']
print(asignaturas)

asignaturas['I2'] = 'Estadistica'
print(asignaturas)

# Buscar / reemplazar
numeros = pd.Series([1,2,3,4,5,6,7,8,9,10])

# Numeros pares
resultado = numeros.where(numeros % 2 == 0)
print(resultado)
## limpiar los valores nulos
print('\nLimpiar resultado\n')
a=[]
for i in range(resultado.shape[0]): # se puede hacer con len(resultado)
    if not(pd.isna(resultado[i])):
        a.append(resultado[i])
print(a)

# Los impares
resultado = numeros.where(numeros % 2 != 0)
print(resultado)
## limpiar los valores nulos
print('\nLimpiar resultado\n')
a=[]
for i in range(resultado.shape[0]):
    if not(pd.isna(resultado[i])):
        a.append(resultado[i])
print(a)

# Dataframes
# 1. Creamos un diccionario

ventas = {'Manzanas': [10,20,30,50,60], 'Peras': [20,30,40,70,80]}

# 2. Creamos un dataframe
frutas_vendidas = pd.DataFrame(ventas, index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'])
print(frutas_vendidas)

# Atributos
print('\n Atributos de index y colums\n')
print('Index: ',frutas_vendidas.index)
print('Columns: ',frutas_vendidas.columns)

print('\n Axes ---- brindar informacion\n')
print(frutas_vendidas.axes)
print('\n Tamaño de mi dataframe: ',frutas_vendidas.shape)

# nombres a mis filas y columnas de
print('\n Nombres de mis filas y columnas\n')
frutas_vendidas.index.name = 'Dia'
frutas_vendidas.columns.name = 'Frutas'
print(frutas_vendidas)

print('Los valores de mi dataframe')
print(frutas_vendidas.values)

# Crear dataframe de array
print('\n Crear dataframe de array\n')
x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # 3x4
print(x)

df = pd.DataFrame(x)
print(df)

# Crear dataframe de varios diccionarios
print('\n Crear dataframe de varios diccionarios\n')
unidades_2020 = {'Hierro': 5.2, 'Fosforo': 7.2, 'Potasio': 6.3}
unidades_2021 = {'Hierro': 4.2, 'Fosforo': 3.2, 'Potasio': 6.4}
unidades_2022 = {'Hierro': 5.4, 'Fosforo': 7.8, 'Potasio': 6.8}

elementos = pd.DataFrame([unidades_2020, unidades_2021, unidades_2022], index=['2020', '2021', '2022'])
print(elementos)

# Inspeccionar la informacion
# Crear dataframe apartir de series
print('\n Crear dataframe apartir de series\n')
# Invetario de un alamcen 
entran = pd.Series([10,15,24,28,10,14,18,19,10,20,13,14],
 index=['Enero', 'Febrero', 'Marzo', 'Abril','Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'] )
salen = pd.Series([8,12,10,8,5,8,11,9,1,2,4,6], 
index=['Enero', 'Febrero', 'Marzo', 'Abril','Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])

# Creando el DataFrame
inventario = pd.DataFrame({'Entrada': entran, 'Salida': salen})
print(inventario)

# Agragar una columna
print('\n Agregar una columna\n')
inventario['Total'] = inventario['Entrada'] - inventario['Salida']
inventario['Saldo'] = inventario.Entrada - inventario.Salida
print(inventario)

# mostrar datos
print('\n Mostrar datos\n')
print('Los 10 iniciales')
print(inventario.head(10))
print('Los 10 finales')
print(inventario.tail(10))
print('Mostrar 5 ramdoms')
print(inventario.sample(5))
print('Informacion estadistica')
print(inventario.describe() )
print('Informacion basica')
print(inventario.info())


# Conteo de lista de datos
print('\n Conteo de lista de datos\n')
salen = pd.Series([8,12,10,8,5,8,11,9,1,2,4,6])
print('Conteo de valores')
print(salen.value_counts())

# Selecion de informacion de un dataframe
print('\n Selecion de informacion de un dataframe\n')
ventas = pd.DataFrame({
    'Entradas': [41,25,36,47],
    'Salidas': [40,20,35,42],
    'Valoracion': [66,54,70,14],
    'Limite': ['No','Si','No','No'],
    'Cambio': [1.43,1.16,-0.5,1.0]
}, index = ['Enero', 'Febrero', 'Marzo', 'Abril'])
print(ventas)
print('Por medio de la Key ---- Columns')
print(ventas['Entradas'])
print('\nPor medio del Index\n')
print(ventas['Entradas']['Enero'])

# Metodos iloc, iloc y get
print('\n Por el metodo loc\n')
print(ventas.loc['Enero']) # Etiquetas
print('\n Por el metodo iloc\n')
print(ventas.iloc[1])
print('\n Por el metodo get\n')
print(ventas.index.get_loc('Abril')) 
print('\n Por el metodo get por columnas\n')
print(ventas.columns.get_indexer(['Cambio']))
print(ventas.columns.get_loc('Cambio'))

# Por rangos 'Fila inicial:Fila final'
print('\n Por rangos\n')
print(ventas.iloc[:2,:2]) # de 0:2, de 0:2
print(ventas.iloc[1:3,2:4]) 

# dataframe con rangos
print('\n Dataframe con rangos\n')
df = pd.DataFrame(np.arange(1,19).reshape([6,3]),
                index=['a','b','c','d','e','f'],
                columns=['A','B','C'])
print(df)

# Edicion de dataframe
print('\n Edicion de dataframe\n')
print('Por los indices --- metodo iloc')
df.iloc[1,2] = -1
print(df)
print('Modificar el numero 8 por -8')
df.iloc[2,1] = -8
print(df)
print('Por columna')
df['A'] = [-1,-3,-9,-4,-7,-8]
print(df)

print('\nPor fila\n')
df.loc['f'] = [0,0,0]
print(df)

print('\n por rangos\n')
df.iloc[:2,:2] = -8
print(df)

df.iloc[3:6,1:] = -1
print(df)

# metodo where
print('\n metodo where\n')
df = pd.DataFrame(np.arange(1,13).reshape([4,3]),
                index=['a','b','c','d'],
                columns=['A','B','C'])
print(df)

respuesta = df.where(df % 2 == 0)
print(respuesta)

# Recorrido por el df 
print('Dimension de respuesta: ', respuesta.shape)
print('Filas: ', respuesta.shape[0])
print('Columnas: ', respuesta.shape[1])

rf =[]
for i in range(respuesta.shape[0]):
    for j in range(respuesta.shape[1]):
        if not(pd.isna(respuesta.iloc[i,j])):
            print(respuesta.iloc[i,j], end=' ')
            rf.append(respuesta.iloc[i,j])
print('\n',rf)

# Eliminar por metodo drop
print('\n Eliminar por metodo drop\n')
df = pd.DataFrame(np.arange(1,13).reshape([4,3]),
                index=['a','b','c','d'],
                columns=['A','B','C'])
print(df)
print(df.drop('c'))
print('Eliminar varias filas')
print(df.drop(['a','b']))
print('Eliminar por columnas')
print(df.drop(columns = 'C'))

# Funcion concatenar
print('\n Funcion concatenar\n')
df1 = pd.DataFrame(np.arange(1,13).reshape([4,3]),
                index=['a','b','c','d'],
                columns=['A','B','C'])
df2 = pd.DataFrame(np.arange(1,5).reshape([2,2]),
                index=['a','b'],
                columns=['A','B'])
dfr = pd.concat([df1,df2])
print(dfr)
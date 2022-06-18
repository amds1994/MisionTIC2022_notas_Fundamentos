# Pandas
from numpy import int16, int256
import pandas as pd
print('\x1Bc') # Formatea la consola

# Asignaturas de un estudiante 
# Lista
asignaturas = pd.Series(['Matemáticas', 'Ingles', 'programacion', 'Habilidades'], index=['M1', 'I2', 'P3', 'H4'])
print(asignaturas)

# Diccionario
asignaturas = ({'Matemáticas': 4.9, 'Ingles': 4.5, 'programacion': 5, 'Habilidades': 3})
print(asignaturas)

# Tuplas 
asignaturas = pd.Series(('Matemáticas', 'Ingles', 'programacion', 'Habilidades'), index=['M1', 'I2', 'P3', 'H4'])
print(asignaturas)



# Seleccionar informacion de la serie
notas = pd.Series({'M1': 4.9, 'I2': 4.5, 'P3': 5, 'H4': 3})
print(notas)
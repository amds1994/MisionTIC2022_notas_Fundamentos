# Numpy

from traceback import print_tb
import numpy as np
print('\x1Bc')

# Crear matrices
m1d = np.array([1, 2, 3, 4, 5])
print(m1d)
print(type(m1d))

print('Matriz bidimencional (2x3)')
m2d = np.array([[1, 2, 3], [4, 5, 6]])
print(m2d)
print(type(m2d))

print('Matriz tridimencional (3x3)')
m3d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m3d)
print(m3d.shape) # la dimension de la matriz

# llegar a los elementos de la matriz
print(m3d[0,0]) # 1
print(m3d[0,1]) # 2
print(m3d[0,2]) # 3
print(m3d[1,0]) # 4
print(m3d[1,1]) # 5
print(m3d[1,2]) # 6
print(m3d[2,0]) # 7
print(m3d[2,1]) # 8
print(m3d[2,2]) # 9

print('Matriz de 2x4')
m2x4d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(m2x4d)
print(m2x4d[-1, -1]) # 8
print(m2x4d[-1, -3]) # 6

# Crear matriz con datos aleatorios
print("Matriz con datos aleatorios")
matriz_aleatoria = np.random.rand(3,3)
print(matriz_aleatoria)

matriz_aleatoria_redondeada = np.round(np.random.rand(3,3), 2)
print('\nmatriz redondeada\n',matriz_aleatoria_redondeada)

# Matriz ramdon de enteros 3x3
matriz_enteros = np.random.randint(100,201,(3,3))
print('\nmatriz enteros\n',matriz_enteros)

#### Funciones para usar matrices ####
# Matriz de ceros 2x3
Matriz_ceros = np.zeros((2,3))
print('\nMatriz de ceros\n',Matriz_ceros)

# Matriz de unos
Matriz_unos = np.ones((2,3))
print('\nMatriz de unos\n',Matriz_unos)

# Matriz de una constante
Matriz_constante = np.full((2,3), 5)
print('\nMatriz de una constante\n',Matriz_constante)


# Matriz identidad
Matriz_identidad = np.eye(4)
print('\nMatriz identidad\n',Matriz_identidad)

# Rebanada de mateices o submatrices
a = np.array([[1,'Carlos',3],[4,'Andres',6],[7,'Juan',9]])
print('\nMatriz a\n',a)
#print('\nRebanada de la matriz a\n',a[0:2,1:3]) # recordar que es excluyente por lo cual se coloca el numero siguiente
print('\nRebanada de la matriz a\n', a[1:,0:2])

# Invertir las filas y las columnas
print('\nInvertir las filas y las columnas forma 1\n', np.fliplr(a))
print('\nInvertir las filas y las columnas forma 2\n', np.flip(a))

#Tasnpuesta de una matriz
print('\nTasnpuesta de una matriz\n', np.transpose(a))


# idexacion de Matrices (sacar los datos que necesito de ella)
a = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print('\nMatriz a\n',a)
b = np.array([0,2,0,1])
print(a[np.arange(4),b])

# Indexacion de matrices booleanas
a = np.array([[1,2],[4,5],[7,8]])
matrizb = (a > 2)
print('\nMatriz a numeros mayores que 2\n',a)
print(a[matrizb])

x = np.array([1,2], dtype = np.float64) # para darle el tipo de dato que se necesita
print('\n',x.dtype)

# Suma de Matrices 
a = np.array([[1,2],[3,4]]) # de 2x2
b = np.array([[5,6],[7,8]]) # de 2x2
print('\nSuma de matrices forma 1\n', a+b)
print('\nSuma de matrices forma 2\n', np.add(a,b))

# resta de Matrices
print('\nResta de matrices forma 1\n', a-b)
print('\nResta de matrices forma 2\n', np.subtract(a,b))

# Productos de elementos
print('\nProducto de elementos forma 1\n', a*b)
print('\nProducto de elementos forma 2\n', np.multiply(a,b))

# Division de elementos
print('\nDivision de elementos forma 1\n', np.round(a/b,2))
print('\nDivision de elementos forma 2\n', np.round(np.divide(a,b),2))

# Raiz cuadrada de los numeros de una matriz
print('\nRaiz cuadrada de los numeros de una matriz\n', np.round(np.sqrt(a),2))

# Multiplicacion entre matrices
print('\nMultiplicacion entre matrices\n', np.round(np.dot(a,b),2))
print('\nMultiplicacion entre matrices\n', np.round(np.matmul(a,b)))


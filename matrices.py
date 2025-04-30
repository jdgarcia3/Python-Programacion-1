#Definir una matriz
Matriz_A = [
    [1 ,2, 3],
    [0 ,5, 4],
]
#Imprimir la matriz
print(f"Matriz A:{Matriz_A}")
#Datos por posición
print(Matriz_A[0][0])
print(Matriz_A[1][1])
print(Matriz_A[0][2])

#Tamaño de la matriz
longitud = len(Matriz_A)
print(f"Longitud de la matriz: {longitud}")
#Recorrer la matriz
for filas in Matriz_A:
    print(f"Fila: {filas}")
    for columnas in filas:
        print(f"Columna: {columnas}")

#Iimprimir posicion y datos de la matriz 
for fila in range(longitud):
    for columna in range(len(Matriz_A[fila])):
        print(f"Posicion: {fila},{columna} = {Matriz_A[fila][columna]}")

#Libreria numpy
import numpy as np
#Nombrar matriz
Matriz_B = np.array([[1,2,3],[0,5,4]])
print(f"Matriz B: {Matriz_B}")
#Sumar matrices
Matriz_Suma = Matriz_A + Matriz_B
print(f"Matriz suma: {Matriz_Suma}")
#multiplicar matrices
Matriz_Multiplicacion = Matriz_A * Matriz_B
print(f"Matriz multiplicacion: {Matriz_Multiplicacion}")
#Resta de matrices
Matriz_Resta = Matriz_A - Matriz_B
print(f"Matriz resta: {Matriz_Resta}")

#Propiedades de la matriz
#Shape
print(f"Filas*Columnas: {Matriz_B.shape}")
#Size
print(f"Numero de datos: {Matriz_B.size}")
#Dtype
print(f"Tipo de datos: {Matriz_B.dtype}")
#ndim
print(f"Numero de dimensiones: {Matriz_B.ndim}")

        

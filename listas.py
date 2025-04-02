#crear lista
lista = [2, "a", "David", 3.14, True, 100, "@"]
print(type(lista))#tipo de dato
print(lista)#imprimir lista

#Individual elementos
numero = lista[0]#primer elemento
print(numero)#imprimir primer elemento
decimal = lista[3]#cuarto elemento
print(decimal)#imprimir cuarto elemento
#Tamaño de la lista
tamaño = len(lista)
print(f"Tamaño lista: {tamaño}")
Estado = lista[4]
print(Estado)#imprimir sexto elemento
dato = lista[-4]
print(dato)
print(lista[-7])
#Recorrer una lista
print(lista[2:6])#imprimir del 0 al 3
print(lista[:])
print(lista[2:])
print(lista[:4])
print(lista[-5:-1])
#Lista vacia
Numeros = []
print(Numeros)#tipo de dato
#Añador valores a la lista
Numeros.append(10)
Numeros.append(1)
Numeros.append(5)
Numeros.append(False)
print(Numeros)
tamaño_numeros = len(Numeros)
print(f"Tamaño lista: {tamaño_numeros}")
#Agregar datos a una lista
Numeros.insert(0, "Jesús")#pos, dato
print(Numeros)
Numeros.insert(2, "Unisangil")#pos, dato
print(Numeros)
Numeros.insert(-1, 6)#pos, dato
print(Numeros)
tamaño_numeros = len(Numeros)
print(f"Tamaño lista: {tamaño_numeros}")
#Eliminar datos de la lista
Numeros.remove("Unisangil")
print(Numeros)
Numeros.remove(1)
print(Numeros)
tamaño_numeros = len(Numeros)
print(f"Tamaño lista: {tamaño_numeros}")
#Eliminar el último elemento
Numeros.pop()
print(Numeros)
Numeros[1:3] = []#eliminar del 2 al 3
print(Numeros)
#Seperar datos de la lista con for
for dato in Numeros:
    print(f"Dato: {dato}")

Lista1 = [10, 2, 30, 4, 5, 1]
print(Lista1)
#Invertir datos de una lista
Lista1.reverse()
print(Lista1)
#Ordenar datos de una lista
Lista1.sort()#de menor a mayor
print(Lista1)
#Ordenar datos descendente
Lista1.sort(reverse=True)#de mayor a menor
print(Lista1)

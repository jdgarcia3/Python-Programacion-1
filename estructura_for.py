#Estructura for
for i in range(10):#muestra un estado anterior 
    print(i)

#Estructura for con range
for i in range(5, 10):#muestra un estado anterior 
    print(i)

#Estructura for con range
for i in range(3, 10, 2):#inicio, fin-1, incremento
    print(i)

#Variable
x = "Python"
#Separar los caracteres con for
for letra in x:
    if letra == "h":
        break
    else:
        print(letra)

#Ejemplo 1: tabla de multiplicar
for mul in range(1,11):
    print(f"2 x {mul} = {2 * mul}")
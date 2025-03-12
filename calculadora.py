#Calculadora con while y elif
#Libreria
import math
#While True
while True:
    #Menu
    print("Calculadora de operaciones básicas")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Salir")
    #Opcion
    opcion = int(input("Ingrese una opción: "))
    if opcion == 7:
        print("Saliendo de la Calculadora...")
        break
    elif opcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        suma = num1 + num2
        print(f"Suma = {suma}")
    elif opcion == 2:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resta = num1 - num2
        print(f"Resta = {resta}")
    elif opcion == 3:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        mul = num1 * num2
        print(f"Multiplicación = {mul}")
    elif opcion == 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        div = num1 / num2
        print(f"División = {div}")
    elif opcion == 5:
        num1 = float(input("Ingrese la base: "))
        num2 = float(input("Ingrese la potencia: "))
        po = num1 ** num2
        print(f"Potencia = {po}")
    elif opcion == 6:
        num1 = float(input("Ingrese la base para la raiz: "))
        raiz = math.sqrt(num1)
        print(f"Raiz cuadrada = {raiz}") 
    else:
        print("Opción Erronea!!!")
print("Gracias por utilizar la Calculadora!!!")
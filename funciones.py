#Funcion simple
def mensaje():
    """
    Muestra un mesaje en pantalla
    """
    print("Unisangil")

#Llamada a la funcion
mensaje()

#Funcion con parametros
def suma(a, b):
    """
    Suma dos numeros: int a, int b
    imprime el resultado
    """
    rta = a + b
    print(rta)
#LLamada a la funcion
suma(10,5)

#Funcion con retorno
def multiplicacion(a,b):
    """
    Multiplica dos numeros: int a, int b
    Devuelve el resultado de la multiplicacion
    Devuelve: int
    """
    rta = a * b
    return rta

#Llamada a la funcion
rta = multiplicacion(10,5)
print(rta * 2)

#Funcion con retorno y sin parametros
def solicitar_datos():
    """
    Solicitar 2 numeros int
    y los retorna num1 y num2
    """
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    return num1, num2

#Llamada a la funcion
a,b = solicitar_datos()
print(f"primer numero = {a} y segundo numero = {b}")
#Llamar suma
suma(a,b)
#Llamar multiplicacion
mul = multiplicacion(a,b)
print(f"Multiplicacion = {mul}")


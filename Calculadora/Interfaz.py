#Solicita y muestra informacion
#Menu
def menu():
    """
    Muestra el menu de opciones
    """
    print("Bienvenido a la calculadora de figuras geometricas")
    print("Seleccione una figura para calcular su area:")
    print("1. Cuadrado")
    print("2. Circulo")
    print("3. Triangulo")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))
    return opcion
#Solicitar datos cuadrado
def solicitar_datos_cuadrado():
    """
    Solicita el lado de un cuadrado
    :return: float
    """
    lado = float(input("Ingrese el lado del cuadrado: "))
    return lado
#Solicitar datos circulo
def solicitar_datos_circulo():
    """
    Solicita el radio de un circulo
    :return: float
    """
    radio = float(input("Ingrese el radio del circulo: "))
    return radio
#Solicitar datos triangulo
def solicitar_datos_triangulo():
    """
    Solicita la base y altura de un triangulo
    :return: float, float
    """
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    return base, altura
#Mostrar area del cuadrado
def mostrar_area_cuadrado(area):
    """
    Muestra el area de un cuadrado
    :param area: float
    """
    print(f"El area del cuadrado es: {area}")
#Mostrar area del circulo
def mostrar_area_circulo(area):
    """
    Muestra el area de un circulo
    :param area: float
    """
    print(f"El area del circulo es: {area}")
#Mostrar area del triangulo
def mostrar_area_triangulo(area):
    """
    Muestra el area de un triangulo
    :param area: float
    """
    print(f"El area del triangulo es: {area}")
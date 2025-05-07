#Importar funciones de script
from Interfaz import (
    menu,
    solicitar_datos_cuadrado,
    solicitar_datos_circulo,
    solicitar_datos_triangulo,
    mostrar_area_cuadrado,
    mostrar_area_circulo,
    mostrar_area_triangulo
)
from Figuras import (
    area_cuadrado,
    area_circulo,
    area_triangulo
)
#Variables
CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
SALIR = 4
#Inicializar variable de opcion
op = 0
#Estructura while
while op != SALIR:
    #Mostrar menu
    op = menu()
    #Seleccionar figura
    if op == CUADRADO:
        #Solicitar datos
        lado = solicitar_datos_cuadrado()
        #Calcular area
        area = area_cuadrado(lado)
        #Mostrar resultado
        mostrar_area_cuadrado(area)
    elif op == CIRCULO:
        #Solicitar datos
        radio = solicitar_datos_circulo()
        #Calcular area
        area = area_circulo(radio)
        #Mostrar resultado
        mostrar_area_circulo(area)
    elif op == TRIANGULO:
        #Solicitar datos
        base, altura = solicitar_datos_triangulo()
        #Calcular area
        area = area_triangulo(base, altura)
        #Mostrar resultado
        mostrar_area_triangulo(area)
    elif op == SALIR:
        print("Gracias por utilizar la calculadora de figuras geometricas!!!")
    else:
        print("Opcion no valida!!!")
    
    
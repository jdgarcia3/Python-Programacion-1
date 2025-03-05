import math

#solicitar al usuario
base = float(input("Ingrese la base del terreno - Triangulo: "))
altura = float(input("Ingrese la altura del terreno - Triangulo: "))
altura_rectangulo = float(input("Ingrese la altura del terreno - Rectangulo: "))
#Calcular el area del triangulo
triangulo = (base*altura)/2
#Calcular el area del rectangulo
rectangulo = base*altura_rectangulo
#Calcular el area total
area_total = triangulo + rectangulo

#Terreno circular
radio = float(input("Ingrese el radio del terreno - Circular: "))
#Calcular el area del circulo
circulo = math.pi * (math.pow(radio,2))



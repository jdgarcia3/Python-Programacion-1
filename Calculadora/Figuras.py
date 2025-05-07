#Calcular el areas de figuras geometricas
import math
# 1. Cuadrado
def area_cuadrado(lado):
    """
    Calcula el area de un cuadrado
    area = lado * lado
    :param lado: float
    :return: float
    """
    area = lado ** 2
    return area
#2. Circulo
def area_circulo(radio):
    """
    Calcula el area de un circulo
    area = pi * radio^2
    :param radio: float
    :return: float
    """
    area = math.pi * (radio ** 2)
    return area
#3. Triangulo
def area_triangulo(base, altura):
    """
    Calcula el area de un triangulo
    area = (base * altura) / 2
    :param base: float
    :param altura: float
    :return: float
    """
    area = (base * altura) / 2
    return area
#Definir clase persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
    
    #metodo para saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

#Llamar a la clase persona
Juan = Persona("Juan", 30)
Juan.mostrar_informacion()
Pedro = Persona("Pedro", 25)
Pedro.mostrar_informacion()
Juan.saludar()

#Definir clase conche
class Conche:
    def __init__(self, marca, modelo, placa, color):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.color = color

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Placa: {self.placa}, Color: {self.color}")
    
    #metodo para encender el coche
    def encender(self):
        print(f"El coche {self.marca} {self.modelo} está encendido.")

#Llamar a la clase coche
Toyota = Conche("Toyota", "Corolla", "ABC123", "Rojo")
BMW = Conche("BMW", "X5", "XYZ789", "Blanco")
#Llamar a los metodos de la clase coche
BMW.mostrar_informacion()
Toyota.encender()

#Definir clase estudiante
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")
    
    #metodo para estudiar
    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")

#Llamar a la clase estudiante
Juan = Estudiante("Juan", 20, "Ingeniería")
Pedro = Estudiante("Pedro", 22, "Medicina")
#Llamar a los metodos de la clase estudiante
Juan.mostrar_informacion()
Pedro.estudiar()
#Fin de ejecución

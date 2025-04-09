#Diccionario de datos
diccionario ={
    "Nombre": "Jesús David Garcia Caro",
    "Celular": 2345678654,
    "Universidad": "Unisangil",
    "Estado": True,
    "Estatura": 1.73,
    "Edad": 32,
    "lista": ["Python", "Java", "C++"]
}
#Imprimir el diccionario
print(diccionario)

#Diccionario 2
programacion1 = {
    "docente" : {
        "nombre" : "Carlos",
        "apellido" : "Gonzalez",
        "telefono" : 4536748,
        "correo" : "ftgyug@gmail.com"
    },
    "estudiantes" : [
        {
            "nombre" : "Juan",
            "apellido" : "Pérez",
            "cedula" : 1234567890,
            "correo" : "ftuyg@gmai.com"
        },
        {
            "nombre" : "Camila",
            "apellido" : "Rosas",
            "cedula" : 1234545690,
            "correo" : "huhgjrkl@gmai.com"
        }
    ],
    "codigo" : "PROG-101",
    "creditos" : 3,
    "estado" : True
}
#Tipo de dato
print(type(programacion1))
#Imprimir informacion docente
print(programacion1["docente"])
print(programacion1["estado"])
print(programacion1["creditos"])
#Nombre docente
print(programacion1["docente"]["nombre"])
print(programacion1["docente"]["correo"])
#Lista de los estudiantes
for estudiante in programacion1["estudiantes"]:
    print(estudiante["nombre"])

#Items dentro de los diccionario
print(programacion1["docente"].items())
#Kkeys dentro de los diccionarios
print(programacion1.keys())
print(programacion1["docente"].keys())

#Lista de los estudiantes
for estudiante in programacion1["estudiantes"]:
    print(estudiante.keys())

#valores dentro de los diccionarios
print(programacion1["docente"].values())
#Lista de los estudiantes
for estudiante in programacion1["estudiantes"]:
    print(estudiante.values())
#Get dentro de los diccionarios
print(programacion1.get("creditos"))
#cambiar inrformacion dentro de los diccionarios
programacion1["docente"]["nombre"] = "Jesus caro"
print(programacion1["docente"]["nombre"])
#Agregar un atrubutio dentro de los diccionarios
programacion1["programa"] = "Ingenieria de sistemas"
print(programacion1)
#Agregar estuciente al diccionario
#Eliminar atributo
del programacion1["programa"]
print(programacion1)

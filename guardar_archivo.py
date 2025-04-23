#Guardar archivo en formato JSON
#Libreria JSON
import json
#Guardar archivo en formato JSON
datos = {
        "nombre" : "Carlos",
        "apellido" : "Gonzalez",
        "telefono" : 4536748,
        "correo" : "carlos_gonzalez@gmail.com",
        "usuario": "jdgarcia3"
}
#Variable para guardar el archivo
archivo = open("informacion.json", "w")
#Guardar el archivo en formato JSON
json.dump(datos, archivo)
#Cerrar el archivo
archivo.close()
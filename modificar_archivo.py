#Importar libreria
import json
from datetime import datetime

#Leer archivo en formato JSON
archivo = open("informacion.json", "r")
#guardar json
contenido = json.load(archivo)
#Cerrar el archivo
archivo.close()

#Modificar el contenido
username = input("Ingrese el nuevo nombre de usuario: ")
contenido["usuario"] = username
contenido["fecha_modificacion"] = str(datetime.now())
#Guardar el json
#Variable para guardar el archivo
archivo = open("informacion_v1.json", "w")
#Guardar el archivo en formato JSON
json.dump(contenido, archivo)
#Cerrar el archivo
archivo.close()
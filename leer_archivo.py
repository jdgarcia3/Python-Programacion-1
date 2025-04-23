#Libreria Json
import json
#Leer archivo en formato JSON
archivo = open("informacion.json", "r")
#guardar json
contenido = json.load(archivo)
#imprimir el contenido
print(contenido)
#Cerrar el archivo
archivo.close()
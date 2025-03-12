#Datos inicio de sesion
david = "jgarciac"
password = 1234
print(type(password))
#Solicitud datos
usuario = input("Usuario: ")
contrasena = int(input("Contraseña: "))
print(type(contrasena))
#Validacion
#Operadores de comparación
if (david == usuario and password == contrasena):
    print("Bienvenido Sistema")
else:
    print("Usuario o contraseña incorrectos")
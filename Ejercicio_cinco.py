#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha
#introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
nombre_usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
if nombre_usuario == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema.")
else:
    print("Error: nos se puede ingresar")
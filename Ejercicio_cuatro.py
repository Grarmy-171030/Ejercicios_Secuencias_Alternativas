#Crea un programa que pida al usuario dos números y muestre su división si 
# el segundo no es cero, o un mensaje de aviso en caso contrario.
numero_uno=float(input("Ingrese el primer numero:"))
numero_dos=float(input("Ingrese el segundo numero:"))
if numero_dos != 0:
    resultado = numero_uno / numero_dos
    print("El resultado de la división es:", resultado)
else:
    print("Error: no se puede dividir entre cero.")
print("Programa finalizado.")

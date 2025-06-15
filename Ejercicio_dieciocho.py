#Escribe un programa que pida un número entero entre uno y doce e imprima 
# el número de días que tiene el mes correspondiente.
numero=int(input("Ingrese un numero entre uno y doce:"))
if numero == 1:
    print("Enero tiene 31 días.")
elif numero == 2:
    print("Febrero tiene 28 días.")
elif numero == 3:
    print("Marzo tiene 31 días.")
elif numero == 4:
    print("Abril tiene 30 días.")
elif numero == 5:
    print("Mayo tiene 31 días.")
elif numero == 6:
    print("Junio tiene 30 días.")
elif numero == 7:
    print("Julio tiene 31 días.")
elif numero == 8:
    print("Agosto tiene 31 días.")
elif numero == 9:
    print("Septiembre tiene 30 días.")
elif numero == 10:
    print("Octubre tiene 31 días.")
elif numero == 11:
    print("Noviembre tiene 30 días.")
elif numero == 12:
    print("Diciembre tiene 31 días.")
else:
    print("ERROR: número incorrecto. ")
print("Programa finalizado.")
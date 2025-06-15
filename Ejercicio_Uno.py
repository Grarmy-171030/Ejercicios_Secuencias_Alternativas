#Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no
numero_uno=int(input("Ingrese el primer numero: "))
numero_dos=int(input("Ingrese el  segundo numero: "))
if numero_uno>numero_dos :
    print("El numero ", numero_uno,"es mayor")
elif numero_uno < numero_dos:
    print("El número", numero_uno, "es menor que", numero_dos)
else:
    print("Ambos números son iguales.")
print("Programa finalizado.")
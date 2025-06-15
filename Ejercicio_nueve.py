# Algoritmo que pide tres números y los muestra ordenados de mayor a menor
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))
if numero_uno >= numero_dos and numero_uno >= numero_tres:
    if numero_dos >= numero_tres:
        print("Orden:", numero_uno, numero_dos, numero_tres)
    else:
        print("Orden:", numero_uno, numero_tres, numero_dos)
elif numero_dos >= numero_uno and numero_dos >= numero_tres:
    if numero_uno >= numero_tres:
        print("Orden:", numero_dos, numero_uno, numero_tres)
    else:
        print("Orden:", numero_dos, numero_tres, numero_uno)
else:
    if numero_uno >= numero_dos:
        print("Orden:", numero_tres, numero_uno, numero_dos)
    else:
        print("Orden:", numero_tres, numero_dos, numero_uno)
print("Programa finalizado.")

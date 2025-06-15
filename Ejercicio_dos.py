#Algoritmo que pida un número y diga si es positivo, negativo o 0.
numero=int(input("Ingrese un numero: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
print("Programa finalizado.")
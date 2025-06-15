#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcto
dia=int(input("Ingrese el dia:"))
mes=int(input("Ingrese el mes:  "))
anio=int(input("Ingrese el año: "))
if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and anio > 0:
    print("La fecha es correcta ")
else:
    print("La fecha es incorrecta")
print("Programa finalizado.")
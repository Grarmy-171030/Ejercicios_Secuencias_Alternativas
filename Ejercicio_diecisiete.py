#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. 
# Si introducimos otro número nos da un error.
dia_de_la_semana=int(input("Ingrese el dia de la semana:"))
if dia_de_la_semana == 1:
    print("Lunes")
elif dia_de_la_semana == 2:
    print("Martes")
elif dia_de_la_semana == 3:
    print("Miércoles")
elif dia_de_la_semana == 4:
    print("Jueves")
elif dia_de_la_semana == 5:
    print("Viernes")
elif dia_de_la_semana == 6:
    print("Sábado")
elif dia_de_la_semana == 7:
    print("Domingo")
else:
    print("Error:  Debe ser del 1 al 7.")
print("Programa finalizado.")

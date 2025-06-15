#El director de una escuela está organizando un viaje de estudios, y requiere determinar
#  cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
#  La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de
#  65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos
#  de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
#  Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que
#  debe pagar cada alumno por el viaje.
# Programa para calcular el costo del viaje escolar

numero_de_alumnos = int(input("Ingrese el numero de alumnos  "))
if numero_de_alumnos > 0:
    if numero_de_alumnos >= 100:
        coste_por_alumno = 65
    elif numero_de_alumnos >= 50:
        coste_por_alumno = 70
    elif numero_de_alumnos >= 30:
        coste_por_alumno = 95
    else:  
        coste_por_alumno = 4000 / numero_de_alumnos
    coste_autobus = numero_de_alumnos * coste_por_alumno
    print("El costo a cobrar por alumno es ", round(coste_por_alumno, 2), "euros.")
    print("El costo de la renta del autobús es  ", round(coste_autobus, 2), "euros.")
else:
    print("El número de alumnos debe ser un valor positivo.")

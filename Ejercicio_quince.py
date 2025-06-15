#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, 
# el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos
#  cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, 
# y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es
#  domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice 
# un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza
#  una llamada.
minutos = int(input("Ingrese los minutos  de la llamada: "))
dia = input("¿Fue domingo? (sí/no): ")
if minutos <= 5:
    costo = 1
elif minutos <= 8:
    costo = 1 + (minutos - 5) * 0.8
elif minutos <= 10:
    costo = 1 + 3 * 0.8 + (minutos - 8) * 0.7
else:
    costo = 1 + 3 * 0.8 + 2 * 0.7 + (minutos - 10) * 0.5
if dia.lower() == "sí":
    impuesto = costo * 0.03
else:
    impuesto = costo * 0.10  
total = costo + impuesto

print("Total a pagar: €", round(total, 2))
print("Programa finalizado.")

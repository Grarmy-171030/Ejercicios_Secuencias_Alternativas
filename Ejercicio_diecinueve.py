#Una compañía de transporte internacional tiene servicio en algunos países de América del Norte,
#  América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se
#  basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados,
#  esto por cuestiones de logística y de seguridad. Realice un algoritmo para determinar el 
# cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
print("Zonas de envío:")
print("1 - América del Norte (24.00 €/gramo)")
print("2 - América Central (20.00 €/gramo)")
print("3 - América del Sur (21.00 €/gramo)")
print("4 - Europa (10.00 €/gramo)")
print("5 - Asia (18.00 €/gramo)")
zona_de_envio = int(input("Ingrese el número de zona 1 al 5: "))
peso_gramos = float(input("Ingrese el peso del paquete en gramos: "))
if peso_gramos > 5000:
    print("No se puede transportar el paquete. Excede 5 kg permitidos.")
elif zona_de_envio < 1 or zona_de_envio > 5:
    print("Zona no válida. Ingrese un número del 1 al 5.")
else:
    if zona_de_envio == 1:
        costo_gramo = 24.00
    elif zona_de_envio == 2:
        costo_gramo = 20.00
    elif zona_de_envio == 3:
        costo_gramo = 21.00
    elif zona_de_envio == 4:
        costo_gramo = 10.00
    else:  # zona_de_envio == 5
        costo_gramo = 18.00
    total = peso_gramos * costo_gramo
    print("El costo total por enviar el paquete es:","€",round(total, 2))
print("Programa finalizado.")

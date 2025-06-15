#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva,
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta
#  del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
#  productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
#  se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de 
# tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando
# es de tamaño 2. 
#Realice un algoritmo para determinar la ganancia obtenida.
tipo_de_uva = input("Ingresa el tipo de uva (A o B): ").upper()
if tipo_de_uva == "A" or tipo_de_uva == "B":
    tamano_de_uva = int(input("Ingresa el tamaño de la uva (1 o 2): "))
    if tamano_de_uva == 1 or tamano_de_uva == 2:
        precio_inicial = float(input("Ingresa el precio inicial por kilo: "))
        kilos = float(input("Ingresa cuántos kilos entregaste: "))
        if tipo_de_uva == "A":
            if tamano_de_uva == 1:
                precio_final = precio_inicial + 0.20
            else:  # tamaño 2
                precio_final = precio_inicial + 0.30
        else:  # tipo B
            if tamano_de_uva == 1:
                precio_final = precio_inicial - 0.30
            else:  # tamaño 2
                precio_final = precio_inicial - 0.50

        ganancia = precio_final * kilos
        print("El productor recibirá: $", round(ganancia, 2))
    else:
        print("Tamaño inválido. Solo se acepta 1 o 2.")
else:
    print("Tipo inválido. Solo se acepta A o B.")

print("Programa finalizado.")

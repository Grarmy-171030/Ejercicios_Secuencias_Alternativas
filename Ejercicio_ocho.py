#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje 
# ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y
#  el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir
#  ‘POSIBLE’.Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
nota = float(input("Ingrese su nota: "))
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (F o M): ")

if nota >= 5 and edad >= 18:
    if sexo.upper() == "F":
        print("ACEPTADA")
    elif sexo.upper() == "M":
        print("POSIBLE")
    else:
        print("Error: Ingrese un carácter válido (F o M)")
else:
    print("NO ACEPTADA")

print("Programa finalizado.")

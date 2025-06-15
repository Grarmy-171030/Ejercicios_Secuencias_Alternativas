#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los 
# lados de un triángulo. El programa debe determinar qué tipo de triangulo es, teniendo en
#  cuenta los siguiente:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno
valor_a=int(input("Ingrese el primer valor: "))
valor_b=int(input("Ingrese el segundo valor: "))
valor_c=int(input("Ingrese el tercer valor: "))
if (pow(valor_a, 2) + pow(valor_b, 2) == pow(valor_c, 2)) or \
   (pow(valor_a, 2) + pow(valor_c, 2) == pow(valor_b, 2)) or \
   (pow(valor_b, 2) + pow(valor_c, 2) == pow(valor_a, 2)):
    print("Es un triángulo rectángulo")
elif valor_a == valor_b == valor_c:
    print("Es un triángulo equilátero")
elif valor_a == valor_b or valor_a == valor_c or valor_b == valor_c:
    print("Es un triángulo isósceles")
else:
    print("Es un triángulo escaleno")
print("Programa finalizado.")
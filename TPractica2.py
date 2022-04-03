lista = list(range(1,11))
tupla = tuple(lista)
indice = int(input("Ingrese un indice para buscar el valor: "))
while indice<0 and indice>10:
    print("El indice ingresado no existe")
    indice = int(input("Ingrese un indice para buscar el valor: "))
print(f"El indice apunta al valor: {tupla.index(indice)}")
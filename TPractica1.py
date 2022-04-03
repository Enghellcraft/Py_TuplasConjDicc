cant =  int(input("Ingrese la cantidad de numeros a ingresar:"))
lista = []
for i in range(1, cant+1):
    num = int(input(f"Ingrese el {i}° numero: "))
    lista.append(num)
tupla = tuple(lista)
find = int(input("Ingrese el numero a buscar en la tupla:"))
print(f"El numero ingresado aparece: {tupla.count(find)} vez/veces")
conj1 = set()
conj2 = set()
lim1 = int(input("Ingrese la cantidad de elementos del Primer Conjunto: "))
for i in range (1, lim1+1):
    num=int(input(f"Ingrese el {i}° numero: "))
    conj1.add(num)
lim2 = int(input("Ingrese la cantidad de elementos del Segundo Conjunto: "))
for i in range (1, lim2+1):
    num=int(input(f"Ingrese el {i}° numero: "))
    conj2.add(num)
print(f"Los elementos comunes son: {conj1.difference(conj2)}")
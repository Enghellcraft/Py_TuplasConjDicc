op = 'y'
dict = {}
while op == 'y':
    nombre = str(input("Ingrese el Nombre de la Fruta: "))
    nom = nombre.lower()
    while nom in dict:
        print("Esta Fruta ya se encuentra en el diccionario. ")
        nombre = str(input("Ingrese el Nombre de la Fruta: "))
        nom = nombre.lower()         
    precio = int(input("Ingrese el Precio por kilo: "))
    dict[nombre]=precio
    op=str(input("Ingrese 'y' para continuar o 'n' para salir: "))
print(f"El diccionario se compone de: {dict}")
while op == 'n':
    fruta = str(input("Ingrese el nombre de la Fruta: "))
    frut = fruta.lower()
    cant = int(input(f"Ingrese la cantidad vendida de {fruta}: "))
    precio_fru = dict.get(frut)
    print(f"La ganancia es de: {precio_fru * cant}")
    op=str(input("Ingrese 'n' para continuar o 'r' para salir: "))
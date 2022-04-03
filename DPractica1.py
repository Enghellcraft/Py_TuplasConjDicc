op = 'y'
dict = {}
while op == 'y':
    nombre = str(input("Ingrese el Nombre: "))
    nom = nombre.lower()
    while nom in dict:
        print("Este nombre ya se encuentra en el diccionario. ")
        nombre = str(input("Ingrese el Nombre: "))
        nom = nombre.lower()         
    tel = int(input("Ingrese el numero telefonico: "))
    dict[nombre]=tel
    op=str(input("Ingrese 'y' para continuar o 'n' para salir: "))
print(f"El diccionario se compone de: {dict}")
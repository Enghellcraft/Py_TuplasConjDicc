lista_pasajeros = []
lista_ciudades = []
op = 0
while op == 0 or 1 or 2 or 3 or 4:
    op = int(input("Seleccione la Opcion: \n\
    1) Agregar pasajeros a la lista de viajeros. \n\
    2) Agregar ciudades a la lista de ciudades. \n\
    3) Dado el DNI de un pasajero, emitir a qué ciudad y país viaja. \n\
    4) Dado un país, mostrar cuántos pasajeros viajan a ese país. \n\
    5) Salir del programa.  \n"))
    if op == 1:
        lista_pasajero=[]
        nombre=str(input("Ingrese el nombre del pasajero: "))
        nombr = nombre.lower()
        lista_pasajero.append(nombr)
        dni=int(input("Ingrese el DNI del pasajero: "))
        lista_pasajero.append(dni)
        destino=str(input("Ingrese la ciudad destino del pasajero:"))
        dest = destino.lower()
        lista_pasajero.append(dest)
        tupla_pasajero = (tuple(lista_pasajero))
        lista_pasajeros.append(tupla_pasajero)
        print(f"{lista_pasajeros}")
    elif op == 2:
        lista_ciudad=[]
        ciudad=str(input("Ingrese la ciudad: "))
        ciud = ciudad.lower()
        lista_ciudad.append(ciud) 
        pais=str(input(f"Ingrese el pais de la ciudad {ciud}: "))
        pai = pais.lower()
        lista_ciudad.append(pai)
        tupla_ciudad=tuple(lista_ciudad)
        lista_ciudades.append(tupla_ciudad)
        print(f"{lista_ciudades}")
    elif op == 3:
        dni_pasajero=int(input("Ingrese el dni del pasajero para buscar su ciudad-destino y pais: "))
        for nombre, dni, destino in lista_pasajeros:
            if dni_pasajero == dni:
                ciudad_pasajero = destino
        for ciudad, pais in lista_ciudades:
            if ciudad_pasajero == ciudad:
                print(f"La ciudad destino es {ciudad} en {pais}")
    elif op == 4:
        cont=0
        pais_pasajero=str(input("Ingrese un pais para saber la cantidad de pasajeros que viajan: "))
        pais_pasa = pais_pasajero.lower()
        for ciudad, pais in lista_ciudades:
            if pais_pasa == pais:
                ciudad_buscada = ciudad
        for nombre, dni, destino in lista_pasajeros:
            if destino == ciudad_buscada:
                cont += 1
        print(f"La cantidad de pasajeros que viajan a {pais_pasa} es: {cont}")
    elif op == 5:
        break
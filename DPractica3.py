alumnado = {}
cant = int(input("Ingrese la cantidad de Alumnos: "))
i = 0
for i in range(1, cant+1):
    notas = []
    alumno = str(input(f"Ingrese el nombre del {i}° Alumno: "))
    alum = alumno.lower()
    while alum in alumnado:
        print("El Alumno {alumno} ya ha sido ingresado")
        alumno = str(input(f"Ingrese el nombre del {i}° Alumno: "))
        alum = alumno.lower()
    else:
        nota = float(input("Ingrese la Primer nota: "))
        while nota > 0:
            notas.append(nota)
            nota = float(input("Ingrese la Siguiente nota: "))
        alumnado[alum] = notas
for alumno,notas in alumnado.items():
    prom = sum(notas)/len(notas)
    print(f"El promedio de {alumno} es: {prom}")
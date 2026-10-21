estudiantes = {
    "Juan": [70, 80, 90],
    "Ana": [100, 95, 90]
}

def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip().capitalize()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    if nombre in estudiantes:
        print("El estudiante ya existe.")
        return
    notas_str = input("Ingrese las notas separadas por espacio: ")
    try:
        notas = [float(n) for n in notas_str.split()]
        if not notas:
            print("Debe ingresar al menos una nota.")
            return
        estudiantes[nombre] = notas
        print("Estudiante agregado con éxito.")
    except ValueError:
        print("Error: las notas deben ser valores numéricos.")

def mostrar_promedios():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)
        print(f"{nombre}: Promedio = {promedio:.2f}")

def mejor_estudiante():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    nombre_mejor = None
    mejor_promedio = -1
    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            nombre_mejor = nombre
    print(f"Mejor estudiante: {nombre_mejor} ({mejor_promedio:.2f})")

while True:
    print("\n1. Agregar estudiante")
    print("2. Mostrar promedios")
    print("3. Mostrar mejor estudiante")
    print("4. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_promedios()
    elif opcion == "3":
        mejor_estudiante()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")

agenda = {
    "Juan": "098111111",
    "Ana": "098222222"
}

def agregar_contacto():
    nombre = input("Ingrese el nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    if nombre in agenda:
        print("El contacto ya existe.")
        return
    telefono = input("Ingrese el teléfono: ").strip()
    agenda[nombre] = telefono
    print("Contacto agregado con éxito.")

def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ").strip()
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print("Contacto no encontrado.")

def mostrar_contactos():
    if not agenda:
        print("La agenda está vacía.")
        return
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")

while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")

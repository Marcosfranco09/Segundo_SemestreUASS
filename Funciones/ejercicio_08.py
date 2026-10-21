inventario = {
    "Teclado": 10,
    "Mouse": 5,
    "Monitor": 2
}

def agregar_stock():
    producto = input("Ingrese el producto: ").strip().capitalize()
    cantidad = int(input("Ingrese la cantidad a agregar: "))
    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return
    inventario[producto] = inventario.get(producto, 0) + cantidad
    print(f"Stock de {producto}: {inventario[producto]}")

def vender_producto():
    producto = input("Ingrese el producto a vender: ").strip().capitalize()
    if producto not in inventario:
        print("El producto no existe.")
        return
    cantidad = int(input("Ingrese la cantidad a vender: "))
    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return
    if inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        print(f"Venta realizada. Stock restante: {inventario[producto]}")
    else:
        print(f"Stock insuficiente. Stock actual: {inventario[producto]}")

def consultar_stock():
    producto = input("Ingrese el producto a consultar: ").strip().capitalize()
    if producto in inventario:
        print(f"Stock disponible de {producto}: {inventario[producto]}")
    else:
        print("El producto no existe en el inventario.")

while True:
    print("\n1. Agregar stock")
    print("2. Vender producto")
    print("3. Consultar stock")
    print("4. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_stock()
    elif opcion == "2":
        vender_producto()
    elif opcion == "3":
        consultar_stock()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")

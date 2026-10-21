with open("productos.txt", "w", encoding="utf-8") as archivo:
    for i in range(5):
        nombre = input(f"Ingrese el nombre del producto {i + 1}: ").strip()
        precio = input(f"Ingrese el precio del producto {i + 1}: ").strip()
        archivo.write(f"{nombre} - {precio}\n")

def producto_mas_caro(productos):
    mas_caro = productos[0]
    for producto in productos:
        if producto[1] > mas_caro[1]:
            mas_caro = producto
    return mas_caro

productos = [
    ("Teclado", 150000),
    ("Mouse", 80000),
    ("Monitor", 1200000)
]

nombre, precio = producto_mas_caro(productos)

print(f"Producto: {nombre}")
print(f"Precio: {precio}")

cantidad = 0
total = 0
precio = int(input())

while precio != 0:
    cantidad += 1
    total += precio
    precio = int(input())

print(f"Productos comprados: {cantidad}")
print(f"Total a pagar: {total}")

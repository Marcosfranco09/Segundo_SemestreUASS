monto_compra = int(input("Ingrese el monto de su compra: "))

if monto_compra > 500000:
    descuento = monto_compra * 0.20
elif monto_compra > 200000:
    descuento = monto_compra * 0.10
else:
    descuento = 0

total = monto_compra - descuento

print("Monto Original:", monto_compra)
print("El descuento aplicado es de:", descuento)
print("Total a Pagar:", total)

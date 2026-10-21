color = input("Por favor, ingrese el color del semáforo (Verde, Amarillo, Rojo): ").strip().capitalize()

if color == "Verde":
    print("AVANCE")
elif color == "Amarillo":
    print("Reduzca la velocidad.")
elif color == "Rojo":
    print("DETENGASE")
else:
    print("ERROR (el color ingresado no es válido)")

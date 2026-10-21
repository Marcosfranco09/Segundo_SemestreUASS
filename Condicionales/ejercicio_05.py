temperatura = int(input("Ingrese la temperatura actual: "))

if temperatura < 10:
    print("Hace Mucho Frío")
elif 10 <= temperatura <= 24:
    print("El clima está templado")
elif 25 <= temperatura <= 34:
    print("El clima está caluroso")
else:
    print("El clima está MUY caluroso")

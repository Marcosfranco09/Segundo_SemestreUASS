porcentaje = int(input("Ingrese el porcentaje de batería: "))

if 0 <= porcentaje <= 10:
    print("Su nivel de batería es Crítico")
elif 11 <= porcentaje <= 30:
    print("Su nivel de batería es Bajo")
elif 31 <= porcentaje <= 80:
    print("Su nivel de batería es Normal")
elif 81 <= porcentaje <= 100:
    print("Su nivel de batería es Alto")
else:
    print("El nivel de batería ingresado está fuera del rango (0-100)")

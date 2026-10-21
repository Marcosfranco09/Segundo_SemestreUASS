edad = int(input("Ingrese su edad: "))
ci = input("¿Posee CI? (S/N): ").strip().upper()

if edad >= 18 and ci == "S":
    print("Ingreso permitido.")
elif edad < 18:
    print("Ingreso denegado: Es menor de edad.")
else:
    print("Ingreso denegado: No presentó CI.")

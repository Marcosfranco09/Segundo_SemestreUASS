frase = input("Ingrese una palabra o frase: ")

cantidad_vocales = 0

for letra in frase:
    if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
        cantidad_vocales += 1

print("La cantidad de vocales:", cantidad_vocales)

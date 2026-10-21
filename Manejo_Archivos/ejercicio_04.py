numeros = []

with open("numeros.txt", "r", encoding="utf-8") as archivo_lectura:
    for linea in archivo_lectura:
        texto = linea.strip()
        if texto:
            numeros.append(float(texto))

if numeros:
    promedio = sum(numeros) / len(numeros)
else:
    promedio = 0

with open("resultado.txt", "w", encoding="utf-8") as archivo_escritura:
    archivo_escritura.write(f"Promedio: {promedio:g}\n")

def estadisticas(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    promedio = sum(numeros) / len(numeros)
    return mayor, menor, promedio

numeros = [10, 20, 30, 40, 50]
mayor, menor, promedio = estadisticas(numeros)

print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Promedio: {promedio:g}")

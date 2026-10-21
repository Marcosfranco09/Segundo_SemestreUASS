def calcular_promedio(notas):
    return sum(notas) / len(notas)

def estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    return "Reprobado"

notas = [70, 80, 90, 60]
prom = calcular_promedio(notas)

print(f"Promedio: {prom:g}")
print(f"Estado: {estado(prom)}")

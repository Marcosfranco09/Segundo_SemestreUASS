def mejor_alumno(alumnos):
    mejor = alumnos[0]
    for alumno in alumnos:
        if alumno[1] > mejor[1]:
            mejor = alumno
    return mejor

def peor_alumno(alumnos):
    peor = alumnos[0]
    for alumno in alumnos:
        if alumno[1] < peor[1]:
            peor = alumno
    return peor

def promedio_general(alumnos):
    total = 0
    for alumno in alumnos:
        total += alumno[1]
    return total / len(alumnos)

alumnos = [
    ("Juan", 85),
    ("Ana", 95),
    ("Pedro", 70)
]

mejor = mejor_alumno(alumnos)
peor = peor_alumno(alumnos)
promedio = promedio_general(alumnos)

print(f"Mejor alumno: {mejor[0]} ({mejor[1]})")
print(f"Peor alumno: {peor[0]} ({peor[1]})")
print(f"Promedio general: {promedio:.2f}")

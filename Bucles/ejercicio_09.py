total_asistencias = 0
clases = 0
asistencia = int(input())

while asistencia != -1:
    total_asistencias += asistencia
    clases += 1
    asistencia = int(input())

if clases > 0:
    promedio = total_asistencias / clases
else:
    promedio = 0

print(f"Total de asistencias: {total_asistencias}")
print(f"Cantidad de clases: {clases}")
print(f"Promedio de asistencia: {promedio}")

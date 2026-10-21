def contar_frecuencia(lista):
    frecuencia = {}
    for elemento in lista:
        frecuencia[elemento] = frecuencia.get(elemento, 0) + 1
    return frecuencia

elementos = ["a", "b", "a", "c", "a", "b"]
print(contar_frecuencia(elementos))

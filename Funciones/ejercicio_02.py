def buscar(lista, valor):
    return valor in lista

alumnos = ["Ana", "Luis", "Carlos"]
resultado = buscar(alumnos, "Luis")
print(resultado)

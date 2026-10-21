nombre = input("Ingrese su nombre: ").strip()
edad = input("Ingrese su edad: ").strip()

with open("registro.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre} - {edad}\n")

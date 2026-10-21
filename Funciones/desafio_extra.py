votos = {}

def registrar_voto(candidato):
    votos[candidato] = votos.get(candidato, 0) + 1

def obtener_ganador():
    if not votos:
        return None
    return max(votos, key=votos.get)

def total_votos():
    return sum(votos.values())

def mostrar_resultados():
    if not votos:
        print("No se registraron votos.")
        return
    print("\n--- Resultados ---")
    for candidato, cantidad in votos.items():
        print(f"{candidato}: {cantidad} voto(s)")
    print(f"Total de votos registrados: {total_votos()}")
    print(f"Candidato ganador: {obtener_ganador()}")

while True:
    entrada = input("Ingrese el nombre del candidato (o 'FIN' para terminar): ").strip().capitalize()
    if entrada == "Fin":
        break
    if not entrada:
        continue
    registrar_voto(entrada)
    print(f"Voto registrado para {entrada}.")

mostrar_resultados()

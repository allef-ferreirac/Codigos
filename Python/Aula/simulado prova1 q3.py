qtd = int(input("Informe a quantidade de votantes: "))

a = 0
b = 0
c = 0

for i in range(1, qtd + 1):
    print(f"Votante {i}:")
    
    voto1 = input(". Informe o voto 1: ")
    voto2 = input(". Informe o voto 2: ")

    if voto1 == "a":
        a += 1.5
    elif voto1 == "b":
        b += 1.5
    elif voto1 == "c":
        c += 1.5

    if voto2 == "a":
        a += 0.5
    elif voto2 == "b":
        b += 0.5
    elif voto2 == "c":
        c += 0.5

print()
print("Pontuações:")
print(f'. Participante "a": {a:.1f}')
print(f'. Participante "b": {b:.1f}')
print(f'. Participante "c": {c:.1f}')
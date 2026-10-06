m1 = float(input("Informe a Moeda 1: "))
m2 = float(input("Informe a Moeda 2: "))
m3 = float(input("Informe a Moeda 3: "))

nome = input("Informe o nome do produto: ")

total = m1 + m2 + m3

if nome == "cafe" or nome == "café":
    preco = 1.50
elif nome == "suco":
    preco = 1.25
elif nome == "agua" or nome == "água":
    preco = 1.10

if total >= preco:
    troco = total - preco
    print(f"Retire o produto: {nome}")
    print(f"Troco: {troco:.2f}")
else:
    print("ERRO: valor insuficiente!")
    print(f"Devolução: {m1:.2f}, {m2:.2f}, {m3:.2f}")
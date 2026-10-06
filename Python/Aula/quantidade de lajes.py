tipo = str(input("Forneça o tipo de ladrilho (g ou p): "))
area = float(input("Forneça a área da sala: "))
if tipo == "g":
    lad = float(80)
elif tipo == "p":
    lad = float(60)
qnt = float(area / lad)
qnt = qnt + 0.4
qnt = int(round(qnt))
print(f"Quantidade de ladrilhos: {qnt}")



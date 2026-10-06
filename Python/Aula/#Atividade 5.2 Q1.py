qnt = int(input("Informe a quantidade de copos: "))
while qnt <= 0:
    qnt = int(input("Quantidade inválida, informe novamente: "))
print(f"Total de água consumida: {qnt * 0.250:.2f} litros")
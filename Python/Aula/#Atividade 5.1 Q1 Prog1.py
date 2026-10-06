#Atividade 5.1 Q1 Prog1
venda = float(1)
totalvendas = float(0)
while venda > 0:
    venda = float(input("Digite o valor da venda: "))
    if venda > 0:
        totalvendas = totalvendas + venda
print(f"Total de vendas: R$ {totalvendas:.2f}")



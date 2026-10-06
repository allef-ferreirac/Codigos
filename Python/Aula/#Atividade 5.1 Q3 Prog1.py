#Atividade 5.1 Q1 Prog1
produto = str("a")
produtomenosvendido = str
qntproduto = int(0)
qntmenosvendido = int(999999999999999999)
while produto != "":
    produto = str(input("Digite o nome do produto: "))
    if produto != "":
        qntproduto = int(input("Digite a quantidade de unidades vendidas: "))
        if qntproduto < qntmenosvendido:
            produtomenosvendido = produto
            qntmenosvendido = qntproduto
print(f"Produto com menor venda: {produtomenosvendido} ({qntmenosvendido} unidades)")



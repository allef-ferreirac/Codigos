#Atividade 5.4 Q3
t = int(input("Digite o tempo para a evacuação: "))
c = int(input("Digite a capacidade de evacuação: "))
qnt = int(input("Digite a quantidade de pessoas: "))
for i in range(t):
    evacuados = c + c*i
    if evacuados >= qnt:
        evacuados = qnt
    print(f"Explosão em {t - i} segundos. Pessoas evacuadas: {evacuados}")
print("Explosão! Sucesso: evacuação completa!")
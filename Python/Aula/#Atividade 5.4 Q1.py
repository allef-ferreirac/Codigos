n = int(input("Digite o valor de N: "))
while n <= 0:
    n = int(input("Digite o valor de N: "))
q = 2
resul = 0
for i in range(n):
    em = q / (n - i)
    resul += em
    q += 2
print(f"Métrica de estabilidade = {resul:.4f}")
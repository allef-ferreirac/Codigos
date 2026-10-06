V = float(input("Digite o valor base do investimento: "))

while V <= 0:
    V = float(input("Digite o valor base do investimento: "))

N = int(input("Digite a quantidade de períodos: "))

while N <= 0:
    N = int(input("Digite a quantidade de períodos: "))

R = 0

for i in range(N, 0, -1):
    R += V / i

print(f"Índice acumulado = {R:.4f}")
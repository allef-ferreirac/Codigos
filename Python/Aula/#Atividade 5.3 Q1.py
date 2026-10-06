n = int(input("Digite um número inteiro positivo: "))
while n <= 0:
    n = int(input("Digite um número inteiro positivo: "))
h = float(0)
for i in range(1,n + 1):
    h += 1 / i
result = n / h
print(f"Média harmônica = {result:.5f}")
n = int(input("Escreva um numero!: "))
x = int(input(f"Deseja ver quantos fatores de {n}: "))
for i in range(x):
    print(n * i,f"    {i + 1}")
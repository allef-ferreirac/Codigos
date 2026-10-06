ci = float(input("Informe o capital inicial: "))
ja = float(input("Informe a taxa de juros anual (em %): "))
years = float(input("Informe o número de anos: "))

mf = ci * (1 + ja / 100) ** years

print(f"O montante final é: {mf:.2f}")
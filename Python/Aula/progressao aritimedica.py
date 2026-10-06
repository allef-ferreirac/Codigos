n1 = float(input("Informe o primeiro termo: "))
q = float(input("Informe a razão: "))
a = float(input("Informe o número do termo: "))

n = n1 * q ** (a - 1)

print(f"O termo a({a}) é {n:.2f}")

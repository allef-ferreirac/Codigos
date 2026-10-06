terrestre = 0
maritimo = 0
aereo = 0

codigo = int(input("Digite um código: "))

while codigo != 0:
    if codigo % 3 == 0:
        terrestre += 1
    elif codigo % 5 == 0:
        maritimo += 1
    else:
        aereo += 1

    codigo = int(input("Digite um código: "))

print()
print(f"Enviados por transporte terrestre: {terrestre}")
print(f"Enviados por transporte marítimo: {maritimo}")
print(f"Enviados por transporte aéreo: {aereo}")
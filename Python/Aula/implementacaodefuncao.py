def impostoRenda(salario):
    if salario <= 1500:
        imposto = 0
    elif salario <= 2500:
        imposto = 0.05 * salario
    elif salario <= 4500:
        imposto = 0.10 * salario
    else:
        imposto = 0.20 * salario
    return imposto
sb = float(input("Digite o salário bruto: "))
while sb > 0:
    ir = impostoRenda(sb)
    print(f"Dedução de IR: {ir}")
    print("")
    sb = float(input("Digite o salário bruto: "))
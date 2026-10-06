m = float(input("Digite seu peso (em kg): "))
h = float(input("Digite sua altura (em metros): "))
c = float(input("Digite a circunferência do seu quadril (em cm): "))

imc = float(m / (h ** 2))
iac = float((c / (h ** 1.5)) - 18)

print(f"IMC = {imc:.3f}")
print(f"IAC = {iac:.3f}")
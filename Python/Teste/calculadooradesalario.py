hrs = float(input("Quantas horas foram trabalhadas?: "))
v_hr = float(input("Qual valor das horas trabalhadas?: "))
inss = 0.065
salario_b = hrs * v_hr
v_inss = salario_b * inss
salario_l = salario_b - v_inss

print(f"Entre com a quantidade de horas trabalhadas (h): {hrs:.1f}")
print(f"Entre com o valor da hora de trabalho (R$): {v_hr:.2f}")
print(f"Entre o com valor do percentual do INSS (%): {inss:.2f}")
print("")
print(f"Salário Bruto........R${salario_b:.2f}")
print(f"Desconto INSS........R${v_inss:.2f}")
print(f"Salário Liquido......R${salario_l:.2f}")
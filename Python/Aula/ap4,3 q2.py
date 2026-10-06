h = float(input("Entre com a altura do reservatório (cm): "))
l = float(input("Entre com a largura do reservatório (cm): "))
comprimento = float(input("Entre com o comprimento do reservatório (cm): "))
consumo = float(input("Entre com o consumo médio diário (litros): "))

capacidade = h * l * comprimento / 1000
autonomia = capacidade / consumo

print(f"Capacidade: R${capacidade:.2f} litros.")
print(f"Autonomia: {autonomia:.2f} dias.")

if autonomia < 1:
    print("Consumo extremo")
elif autonomia > 1 and autonomia <= 3:
    print("Consumo elevado")
elif autonomia > 3 and autonomia <= 7:
    print("Consumo moderado")
elif autonomia > 7:
    print("Consumo reduzido")

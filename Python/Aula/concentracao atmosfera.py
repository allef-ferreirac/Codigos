import math
ci = float(input("Informe a concentração inicial (em ppm): "))
t = float(input("Informe o tempo decorrido (em horas): "))

ct = ci / (1 + math.log(t + math.e, 10))

print(f"A concentração atual de poluentes é: {ct:.4f}")
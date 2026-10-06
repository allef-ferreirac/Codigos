import math
cf = float(input("Forneça o comprimento do fio: "))
p = float(input("Forneça a força peso: "))
m = float(input("Forneça a massa: "))
g = float(p / m)
t = float((2 * 3.14) * ((cf / g) ** (1 / 2)))

print(f"A aceleração da gravidade é {g:.3f}")
print(f"O período do pêndulo é {t:.3f}")

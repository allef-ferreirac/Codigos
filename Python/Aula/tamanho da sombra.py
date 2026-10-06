import math
h = float(input("Informe a altura da torre (em metros): "))
a = float(input("Informe o ângulo de elevação do Sol (em graus): "))
teta = a * math.pi / 180
s = h / math.tan(teta)

print(f"A sombra projetada no solo mede {s:.3f} metros.")

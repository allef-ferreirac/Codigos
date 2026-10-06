n = int(input("Digite o número de termos: "))
pi = 0
for i in range(n):
    n1 = (-1)**i * 4 / (2*i + 1)
    pi += n1
r = int(input("Digite o raio da esfera: "))
v = (4/3) * pi * r**3
print(f"pi = {pi:.5f}")
print(f"Volume da esfera = {v:.5f}")

import random
numeros = []
qnt = int(input("Quantos numeros deseja sortear?"))
for i in range(qnt):
    numeros.insert(i, int(random.randint(1, 100)))
print(tuple(numeros))
menorn = int(numeros[1])
maiorn = int(numeros[1])
for i in range(len(numeros)):
    if numeros[i] > maiorn:
        maiorn = numeros[i]
print(f"O maior numero é {maiorn}")
for i in range(len(numeros)):
    if numeros[i] < menorn:
        menorn = numeros[i]
print(f"O menor numero é {menorn}")
print(max(numeros)) #nao sabia que existia saporra!!!!!!!!!!!!!!
print(min(numeros))
import random 
print("================================")
print("Leitor de mentes pro max")
print("================================")
print()
print("Pense em um numero de 1 a 100.")
r = str(input("Pensou? "))
n = (random.randint(1, 100))
while r == "s":
    acertou = str(input(f"seu numero é {n}? [maior/sim/menor]"))
    if acertou == "maior":
        d = 100 - n
        n = n + (d/2)
        n = round(n)
    elif acertou == "menor":
        d = 100 - n
        n = n - (d/2)
        n = round(n)
    else:
        r == "n"

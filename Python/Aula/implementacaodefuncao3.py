def Somatorio(ntermos):
    somatorio = 1.0
    for i in range(2,ntermos+1):
        somatorio += 1/i
    return somatorio
def Produtorio(ntermos):
    produtorio = 2
    for i in range(2,ntermos+1):
        produtorio = produtorio * (2 ** (1/i))
    return produtorio
n = int(input("Defina a quantidade de termos (N): "))
while n > 0:
    s = Somatorio(n)
    p = Produtorio(n)
    print(". O valor de S é ",round(s, 3))
    print(". O valor de P é ",round(p, 3))
    n = int(input("Defina a quantidade de termos (N): "))


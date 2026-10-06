no1 = int(input("Qual o numero 1?: "))
no2 = int(input("Qual o numero 2?: "))
numero1 = no1
numero2 = no2
p = 2
resultado = 1
def  Primo(pp):
    d = 0
    pp = p
    for i in range(1, pp + 1):
        if pp % i == 0:
            d = d + 1
    if d == 2:
        return True
    else:
        return False
def MMC(n1,n2,r):   
    while n1 % p == 0 and n2 % p == 0:
        n1 = n1 / p
        n2 = n2 / p
        r = r * p
        print(f"{n1:^5.0f} , {n2:^5.0f}     /{p}")
    while n1 % p == 0 or n2 % p == 0:
        while n1 % p == 0:
            n1 = n1 / p
            r = r * p
            print(f"{n1:^5.0f} , {n2:^5.0f}     /{p}")
        while n2 % p == 0:
            n2 = n2 / p
            r = r * p
            print(f"{n1:^5.0f} , {n2:^5.0f}     /{p}")
    return n1,n2,r
print(f"{numero1:^5.0f} , {numero2:^5.0f}     /{p}")
numero1,numero2,resultado = MMC(numero1,numero2,resultado)
while numero1 != 1 or numero2 != 1:
    p = p + 1
    while Primo(p) == False:
        p = p + 1
    numero1,numero2,resultado = MMC(numero1,numero2,resultado)
print("=====================================")
print(f"O MMC de {no1} e {no2} é {resultado}")
print("=====================================")


q = int(input("Quantos primos deseja exibir?: "))
p = 2
def  Primo(pp):
    d = 0
    for i in range(1, pp + 1):
        if pp % i == 0:
            d = d + 1
    if d == 2:
        return True
    else:
        return False
for i in range(q):
    if Primo(p):
        print(p)
        p = p + 1
    else:
        while Primo(p) == False:
            p = p + 1
        print(p)
        p = p + 1

        



        


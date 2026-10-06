
x = float(input("Entre com o valor de x: "))
y = float(input("Entre com o valor de y: "))
z = float(input("Entre com o valor de z: "))
media = str(input("Entre com a média desejada (G,P,H,A): "))

def Geometrica(x, y, z):
    mf = (x * y * z) ** (1/3)
    return mf
def Ponderada(x, y, z):
    mf = (x + (2*y) + (3*z)) / 6
    return mf
def Harmonica(x, y, z):
    mf = 3 / ((1/x) + (1/y) + (1/z))
    return mf
def Aritmetica(x,y,z):
    mf = (x + y + z) / 3
    return mf

if media == "G":
    mediaf = Geometrica(x,y,z)
elif media == "P":
    mediaf = Ponderada(x,y,z)
elif media == "H":
    mediaf = Harmonica(x,y,z)
elif media == "A":
    mediaf = Aritmetica(x,y,z)
else:
    print("A media escolhida não foi encontrada!")
print(f"O valor da média escolhida é {mediaf:.2f}")


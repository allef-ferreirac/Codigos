from biblioteca import *
def selecionarRobo(pcaixa):
    if pcaixa <= 20:
        print("Robô 1")
    elif pcaixa <= 50:
        print("Robô 2")
    elif pcaixa <= 100:
        print("Robô 3")
    else:
        print("excede a capacidade maxima")
pcaixa = int(input("Informe o peso da caixa: "))
while pcaixa > 0:
    selecionarRobo(pcaixa)
    pcaixa = int(input("Informe o peso da caixa: "))
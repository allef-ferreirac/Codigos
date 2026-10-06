from biblioteca import *
def eEmergencia(vetor):
    qnt = 0
    for i in range(len(vetor)):
        if vetor[i] < 12:
            qnt += 1
    return qnt
def eAlerta(vetor):
    qnt = 0
    for i in range(len(vetor)):
        if vetor[i] >= 12 and vetor[i] <= 20:
            qnt += 1
    return qnt
def eAtencao(vetor):
    qnt = 0
    for i in range(len(vetor)):
        if vetor[i] > 20 and vetor[i] <= 30:
            qnt += 1
    return qnt
def eNaoCritico(vetor):
    qnt = 0
    for i in range(len(vetor)):
        if vetor[i] > 30:
            qnt += 1
    return qnt
umi = inputVetor("Informe os valores da umidade relativa ao ar: ",int)
print("Quantidade de estados:")
print(". Estados de emergência:", eEmergencia(umi))
print(". Estados de alerta:", eAlerta(umi))
print(". Estados de atenção:", eAtencao(umi))
print(". Estados de não criticos:", eNaoCritico(umi))
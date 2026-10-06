from biblioteca import *
mat = inputMatriz("Informe a matriz de produção: ",int)
l,c = dimMatriz(mat)
print(f"Você definiu {l} unidades e {c} meses.")
maiormedia = 0
total = 0
for i in range(l):
    for j in range(c):
        total += mat[i][j] 
    mediaatual = total / c
    print(f". Média de produção da unidade {i+1}: {mediaatual:.2f}")
    if mediaatual > maiormedia:
        maiormedia = mediaatual
        maiorunidade = i+1
    total = 0
print(f"A unidade {maiorunidade} teve a maior média de produção.")
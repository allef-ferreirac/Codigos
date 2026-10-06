from biblioteca import *
mg = inputMatriz("Informe a matriz de energia gerada: ",int)
mc = inputMatriz("Informe a matriz de energia consumida: ",int)
lg,cg = dimMatriz(mg)
lc,cc = dimMatriz(mc)
if lg != lc or cg != cc:
    print("Erro: Matrizes com dimensões diferentes.")
else:
    m = criarMatriz(lg,cg,0)
    for i in range(lg):
        for j in range(cg):
            m[i][j] = mg[i][j] - mc[i][j]
    print(f"Energia excedente: {m}")
    te = 0
    for i in range(lg):
            for j in range(cg):
                te = te + m[i][j]
    print(f"Total excedente: {te}")

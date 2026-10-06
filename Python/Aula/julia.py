from biblioteca import *

# Entrada das matrizes
receitas = inputMatriz("Informe a matriz de receitas: ", int)
despesas = inputMatriz("Informe a matriz de despesas: ", int)

# Verifica se possuem mesmas dimensões
if len(receitas) != len(despesas) or len(receitas[0]) != len(despesas[0]):
    print("Erro: Matrizes com dimensões diferentes.")

else:

    # Cria matriz saldo
    saldo = criarMatriz(len(receitas), len(receitas[0]), 0)

    # Calcula saldo
    for i in range(len(receitas)):
        for j in range(len(receitas[0])):
            saldo[i][j] = receitas[i][j] - despesas[i][j]

    # Exibe resultado
    print("Saldo disponivel:", end=" ")

    for linha in saldo:
        print(linha, end=" ")
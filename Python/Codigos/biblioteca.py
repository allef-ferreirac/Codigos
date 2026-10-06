'''
Biblioteca fornecida pelos professores de BCC701/BCC104
Este arquivo não deve ser modificado.
'''

def criarVetor(qtdElementos, valorPadrao):
    vetor = [ ]
    for i in range(qtdElementos):
        vetor.append(valorPadrao)
    return vetor

def inputVetor(mensagem, conversao):
    valores = input(mensagem)
    resultado = [ ]
    if valores == '':
        return resultado
    valores = valores.split(',')
    for i in range(len(valores)):
        valor = conversao(valores[i].strip())
        resultado.append(valor)
    return resultado

def criarMatriz(qtdLinhas, qtdColunas, valorPadrao):
    matriz = [ ]
    for lin in range(qtdLinhas):
        linha = criarVetor(qtdColunas, valorPadrao)
        matriz.append(linha)
    return matriz

def inputMatriz(mensagem, conversao):
    valores = input(mensagem)
    resultado = [ ]
    if valores == '':
        return resultado
    valoresLin = valores.split(';')
    for lin in range(len(valoresLin)):
        linha = []
        valoresCol = valoresLin[lin].split(',')
        for col in range(len(valoresCol)):
            valor = conversao(valoresCol[col].strip())
            linha.append(valor)
        resultado.append(linha)
    return resultado

def dimMatriz(matriz):
    qtdLins = len(matriz)
    if qtdLins == 0:
        return 0, 0
    else:
        qtdCols = len(matriz[0])
        return qtdLins, qtdCols







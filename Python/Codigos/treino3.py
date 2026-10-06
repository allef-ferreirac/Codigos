from biblioteca import *
dist = inputMatriz("Digite as distâncias percorridas: ",float)
jogadores,jogos = dimMatriz(dist)
print(f"Analise de desemprenho de {jogadores} jogadores em {jogos} jogos.")
for j in range(jogadores):
    kmtotal = 0
    for i in range(jogos):
        kmtotal += dist[j][i]
    kmmedio = kmtotal / jogos
    print(f"Jogador {j+1}: Média de {round(kmmedio,2):.2f} km por jogo.")



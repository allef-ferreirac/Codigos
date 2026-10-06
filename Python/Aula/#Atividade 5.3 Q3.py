nome = input("Informe o nome do juiz: ")
partidas = int(input("Informe a quantidade de partidas: "))

soma_impedimentos = 0
soma_faltas = 0

for i in range(1, partidas + 1):
    print()
    print(f"Partida {i}:")
    
    impedimentos = int(input(". Informe impedimentos.: "))
    faltas = int(input(". Informe faltas........: "))
    
    soma_impedimentos += impedimentos
    soma_faltas += faltas

media_impedimentos = soma_impedimentos / partidas
media_faltas = soma_faltas / partidas

print()
print(f"Estatísticas do juiz {nome}:")
print(f". Impedimentos.........: {media_impedimentos:.2f}")
print(f". Faltas...............: {media_faltas:.2f}")
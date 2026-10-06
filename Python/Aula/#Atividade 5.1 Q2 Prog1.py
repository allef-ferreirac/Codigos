#Atividade 5.1 Q1 Prog1
duracao = int(1)
maiordura = int(0)
while duracao > 0:
    duracao = int(input("Digite a duração da chamada: "))
    if duracao > maiordura:
        maiordura = duracao
print(f"Maior duração de chamada: {maiordura} minutos")



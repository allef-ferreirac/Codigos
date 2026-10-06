nome = str(input("Entre com o nome: "))
idade = float(input("Entre com a idade: "))
sexo = str(input("Entre com o sexo (m ou f): "))
if sexo  == "m":
    if idade < 18:
        mi = 18 - idade
        mi = round(mi, 1)
        print(f"Faltam {mi} anos para {nome} atingir a maioridade")
    else:
        print(f"{nome} tem maioridade civil")
if sexo  == "f":
    if idade < 21:
        mi = 21 - idade
        mi = round(mi, 1)
        print(f"Faltam {mi} anos para {nome} atingir a maioridade")
    else:
        print(f"{nome} tem maioridade civil")



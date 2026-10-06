nome = input("Qual seu nome completo?: ")
email = input("Qual seu email?: ")
idade = input("Quantos anos voce tem?: ")
idade = int(idade)
servidor_p= email.find("@")
servidor = email[servidor_p:(len(email))]
nome1 = (nome[0:(nome.find(" "))]).title()

print(f"O usuario {nome1} foi cadastrado com o email final {servidor}")
if idade < 18 :
    print(f"{nome1} é menor de idade!")
else :
    print(f"{nome1} é maior de idade!")




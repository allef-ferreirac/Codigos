senha = str(input("Qual a senha?"))
print(senha.isdigit)
def medidordeforca(forca):
    forca = int(0)
    if len(senha) < 8:
        print("Senha possui boa quantia de caracteres.")
        forca = forca + 1
    else:
        print("Senha possui pequena quantia de caracteres.")
    if senha.upper() != senha and senha.lower() != senha:
        forca = forca + 1
        print("Senha possui letras maisculas e minusculas.")
    else:
        print("Senha não possui letras minusculas e maiusculas")
    if senha.find("@") != -1 or senha.find("!") != -1 or senha.find("#") != -1 or senha.find("*") != -1:
        forca = forca + 1
        print("Senha possui caracteres especiais.")
    else:
        print("Senha nao possui caracteres especiais")
        return forca
f = medidordeforca(senha)
if f == 1:
    print("Senha fraca.")
if f == 2:
    print("Senha razoavel.")
if f == 3:
    print("Senha forte.")
if f == 4:
    print("Senha ideal!")    



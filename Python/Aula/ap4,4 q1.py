
yo = float(input("Informe a idade do cliente: "))
if yo < 0:
    print("Idade inválida!")
if yo <= 11:
    price = float(0)
    print(f"Preço do ingresso: R${price:.2f}")
elif yo <= 17:
    price = float(12.50)
    print(f"Preço do ingresso: R${price:.2f}")
elif yo <= 59:
    price = float(25)
    print(f"Preço do ingresso: R${price:.2f}")
elif yo > 59:
    price = float(15)
    print(f"Preço do ingresso: R${price:.2f}")




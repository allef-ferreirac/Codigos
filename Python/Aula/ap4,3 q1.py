v = float(input("Informe o valor da compra: "))
frete = float(20)
if v > 100 and v <= 200:
    frete = frete - (5/100 * frete)
elif v > 200 and v <= 300:
    frete = frete - (10/100 * frete)
elif v > 300:
    frete = 0
vt = v + frete
print(f"Valor do frete é R${frete:.2f}")
print(f"Valor total da compra: R${vt:.2f}")

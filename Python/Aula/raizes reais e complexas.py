a = float(input("Entre com o coeficiente a: "))
b = float(input("Entre com o coeficiente b: "))
c = float(input("Entre com o coeficiente c: "))

if b**2 - 4*a*c >= 0:
    print(f"As raízes são reais")
else:
    print(f"As raízes são complexas")
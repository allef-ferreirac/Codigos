n = int(input("Informe o número que deseja calcular o Fatorial: "))
while n <= 0:
    n = int(input("Número inválido, defina outro: "))
numero = n
fn = n
while n > 1:
    n = (n-1)
    fn = fn * n
print(f"O Fatorial de {numero} é: {fn}")
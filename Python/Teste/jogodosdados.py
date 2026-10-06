import random
dado = {
     "___________
     |           |
     |           |
     |     o     | 
     |           |
     |___________|"
}
qnt = int(input("Quantos dados voce quer roletar? "))
for i in range(qnt):
    print(random.choice(dado))
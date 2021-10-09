import random

number_user = int(input("Advinhe o numero correto (este número está entre 0 e 10): "))
numero_sorteado = random.randint(0,10)

print(numero_sorteado)
if number_user == numero_sorteado:
    print('You guessed!')
elif number_user > numero_sorteado:
    print('Reduce your guess')
else:
    print('Increase your guess')

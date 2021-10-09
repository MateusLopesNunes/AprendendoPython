tupla = (1,2,3,4,5)

tuplaDobro = tuple(map(lambda x: x*2, tupla))
tuplaPar = tuple(filter(lambda x: x%2 == 0, tupla))
tuplaImpar = tuple(filter(lambda x: not x%2 == 0, tupla))
tuplaParcial1 = tupla[1:3]
tuplaParcial2 = tupla[1::]

print(f'Numeros originais: {tupla}')
print(f'Numero em dobro: {tuplaDobro}')
print(f'Numeros pares: {tuplaPar}')
print(f'Numeros impares: {tuplaImpar}')
print(f'Numeros entre as posições >= 1 e < 3: {tuplaParcial1}')
print(f'Numeros entre as posições >= 1: {tuplaParcial2}')
lista = []
for i in range(0,5):
    n = int(input('Informe um numero: '))
    lista.append(n)

listaDobro = list(map(lambda x: x*2, lista))
listaPar = list(filter(lambda x: x%2 == 0, lista))
listaImpar = list(filter(lambda x: not x % 2 == 0, lista))
listaParcial1 = lista[1:3]
listaParcial2 = lista[1::]

print(f'Numeros originais: {lista}')
print(f'Numero em dobro: {listaDobro}')
print(f'Numeros pares: {listaPar}')
print(f'Numeros impares: {listaImpar}')
print(f'Numeros entre as posições >= 1 e < 3{listaParcial1}')
print(f'Numeros entre as posições >= 1 {listaParcial2}')
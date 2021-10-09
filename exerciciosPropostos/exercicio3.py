valor = int(input("Informe uma valor a ser decomposto: "))

nota_de_100 = 0
nota_de_50 = 0
nota_de_20 = 0
nota_de_10 = 0
nota_de_5 = 0
nota_de_2 = 0

if (valor / 100 >= 1):
    result = valor // 100
    nota_de_100 = result
    valor = valor - result * 100

if (valor / 50 >= 1):
    result = valor // 50
    nota_de_50 = result
    valor = valor - result * 50

if (valor / 20 >= 1):
    result = valor // 20
    nota_de_20 = result
    valor = valor -  result * 20

if (valor / 10 >= 1):
    result = valor // 10
    nota_de_10 = result
    valor = valor - result * 10

if (valor / 5 >= 1):
    result = valor // 5
    nota_de_5 = result
    valor = valor - result * 5
    
if (valor / 2 >= 1):
    result = valor // 2
    nota_de_2 = result
    valor = valor - result * 2

print(f'{nota_de_100} notas de 100')
print(f'{nota_de_50} notas de 50')
print(f'{nota_de_20} notas de 20')
print(f'{nota_de_10} notas de 10')
print(f'{nota_de_5} notas de 5')
print(f'{nota_de_2} notas de 2')

#for i in range(1, 101):
#    if (i % 2 == 0):
#        print(i, end=', ')

#------------------------------------------------------------

def divi(n1, n2):
    print(n1 // n2) #divisão inteira

#divi(20, 3)

#------------------------------------------------------------

def expo(n1,n2):
    print(n1**n2) #exponenciação

#expo(int(input("Enter a number: ")), int(input('Enter a number: ')))

#------------------------------------------------------------

def encadeamento(n1, n2, n3):
    if (n1 < n2 < n3): #encadeamento
        print('O segundo numero é maior que o primeiro e menor que o terceiro')
    else:
        print("O segundo numero não está entre o primeiro e o segundo numero")

#numberOne = int(input('Enter the first number: '))
#numberTwo = int(input('Enter the second number: '))
#numberTree = int(input('Enter the third number: '))

#encadeamento(numberOne, numberTwo, numberTree)

#------------------------------------------------------------

hello = "Hello"
world = "World"
print(f"{hello} {world}!!!")
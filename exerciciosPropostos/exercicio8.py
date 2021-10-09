import random

def fib(n):
    a, b = 0, 1
    print('')
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

lista = [random.randrange(1000), random.randrange(700), random.randrange(800)]
list(map(lambda x: fib(x), lista))
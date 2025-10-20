from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        n = randint(0, 5)
        lista.append(n)
        print(n, end=' ')
        sleep(0.5)
    print('PRONTO!')


def soma(lista):
    s = 0
    for d in lista:
        if d % 2 == 0:
            s += d
    print(f'Somando os valores pares de {lista}, temos {s}.')


num = list()
sorteio(num)
soma(num)


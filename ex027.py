from random import randint
from time import sleep
print('-='*30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar... ')
print('-='*30)
n = int(input('Em que numero eu pensei? '))
s = randint(0, 5)
print('PROCESSANDO...')
sleep(3)
if n == s:
    print('PARABENS! Voce conseguiu me vencer! ')
else:
    print(f'GANHEI! Eu pensei no numero {s} e nao no {n}!')

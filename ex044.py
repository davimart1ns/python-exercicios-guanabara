from time import sleep
from random import randint
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
op = int(input('Qual é a sua jogada? '))
if op != 0 and op != 1 and op != 2:
    print('JOGADA INVÁLIDA')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    itens = ['PEDRA', 'PAPEL', 'TESOURA']
    pc = randint(0, 2)
    jg = itens[op]
    print('-='*12)
    print(f'Computador jogou {itens[pc]}')
    print(f'Jogador jogou {jg}')
    print('-='*12)
    if op == 0 and pc == 2:
        print('JOGADOR VENCE')
    elif op == 1 and pc == 0:
        print('JOGADOR VENCE')
    elif op == 2 and pc == 1:
        print('JOGADOR VENCE')
    elif pc == 0 and op == 2:
        print('COMPUTADOR VENCE')
    elif pc == 1 and op == 0:
        print('COMPUTADOR VENCE')
    elif pc == 2 and op == 1:
        print('COMPUTADOR VENCE')
    elif pc == op:
        print('EMPATE')

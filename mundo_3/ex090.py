from time import sleep
from random import randint
from operator import itemgetter
jogadores = dict()
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
resultado = dict()
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('-='*25)
print('== RANKING DOS JOGADORES ==')
resultado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for j, v in enumerate(resultado):
    print(f'    {j+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
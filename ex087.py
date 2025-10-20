from random import randint
from time import sleep
lista = list()
games = list()
print('-'*38)
print('JOGUE NA MEGA SENA'.center(38))
print('-'*38)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('=-'*5, f'SORTEANDO {jogos} JOGOS', '=-'*5)
tot = 1
while tot <= jogos:
    cont = 0
    while True:
        nums = randint(1, 60)
        if nums not in lista:
            lista.append(nums)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    games.append(lista[:])
    lista.clear()
    tot += 1
for c, i in enumerate(games):
    print(f'Jogo {c+1}: {i}')
    sleep(1)
print('Boa sorte CHEFE')
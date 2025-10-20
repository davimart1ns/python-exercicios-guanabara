jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for j, v in enumerate(jogador['gols']):
    print(f'    => Na partida {j}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
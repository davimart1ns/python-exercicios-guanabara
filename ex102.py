def info(nom='<desconhecido>', gols=0):
    print('__'*20)
    print(f'O jogador {nom} fez {gols} gols no campeonato')


nome = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    info(gols=g)
else:
    info(nome, g)
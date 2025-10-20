lista = list()
parte = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    if 5 in lista:
        parte = 'faz parte'
    else:
        parte = 'não foi encontrado dentro'
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {sorted(lista, key=int, reverse=True)}')
print(f'O valor 5 {parte} da lista!')

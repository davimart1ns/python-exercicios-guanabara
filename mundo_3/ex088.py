ficha = list()
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)
for c, i in enumerate(ficha):
    print(f'{c:<4}{i[0]:<10}{i[2]:>8}')
print('-'*30)
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas <= len(ficha) - 1:
        print(f'A notas de {ficha[notas][0]} sao {ficha[notas][1]}.')
    print('-' * 30)
    if notas == 999:
        print('FINALIZANDO...')
        break
print('<<< VOLTE SEMPRE CHEFE >>>')

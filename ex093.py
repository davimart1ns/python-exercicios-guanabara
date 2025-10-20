lista = list()
pessoas = dict()
resp = ''
soma = 0
while resp != 'N':
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]
    while pessoas['sexo'] != 'M' and pessoas['sexo'] != 'F':
        print('ERRO! Responda apenas S ou N.')
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    resp = str(input('Que continuar? [S/N] ')).upper().split()[0]
    while resp != 'N' and resp != 'S':
        print('ERRO! Responda apenas com S ou N')
        resp = str(input('Quer continuar ? [S/N] ')).upper().split()[0]
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma/len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres codastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print(f'    ')
        for k, v in p.items():
            print(f'{k} = {v} ;', end='')
        print()
print('<< ENCERRADO >>')
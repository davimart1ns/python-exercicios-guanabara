from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 35) - datetime.now().year
print('-='*30)
for c, v in pessoa.items():
    print(f'    - {c} tem o valor {v}')

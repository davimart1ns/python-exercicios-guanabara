from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print(f'Quem nasceu em {ano} tem {idade} em {date.today().year}.')
if idade < 18:
    n = 18 - idade
    print(f'Ainda faltam {n} anos para o alistamento.')
    print(f'Seu alistamento será em {date.today().year + n}.')
elif idade > 18:
    n = idade - 18
    print(f'Você já deveria ter se alistado há {n} anos.')
    print(f'Seu alistamento foi em {date.today().year - n}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')

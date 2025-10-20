def votacao(ano):
    from datetime import date
    atual = date.today().year
    idade = (atual - ano)
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    if 16 <= idade < 18 or idade > 60:
        print(f'Com {idade} anos: VOTO OPCIONAL ')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


y = int(input('Digite o ano em que você nasceu: '))
print(votacao(y))

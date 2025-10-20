from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
win = 0
res = ''
while True:
    jg = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I]')).upper().strip()
    jgcomp = randint(1, 10)
    soma = jg + jgcomp
    if soma % 2 == 0:
        res = 'PAR'
    else:
        res = 'ÍMPAR'
    print(f'Você jogou {jg} e o computador {jgcomp}. Total de {soma} DEU {res}')
    if pi == 'P' and res == 'PAR':
        win += 1
        print('Você GANHOU!')
    elif pi == 'I' and res == 'ÍMPAR':
        win += 1
        print('Você GANHOU!')
    else:
        print('Você PERDEU')
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {win} vezes')

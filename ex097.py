from time import sleep


def contagem(i, f, p):
    if p < 1:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} ate {f} de {p} em {p}.')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while f <= cont:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')


contagem(1, 10, 1)
contagem(10, 1, 1)
print('-=' * 20)
print('Agora é a sua vez de contar')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
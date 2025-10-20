from time import sleep


def valores(* num):
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados... ')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores()

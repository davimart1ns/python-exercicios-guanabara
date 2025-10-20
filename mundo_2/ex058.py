from time import sleep
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    op = int(input('>>>>Qual é a sua opção? '))
    if op == 1:
        print(f'A soma entra {p1} e {p2} é igual a {p1+p2}')
    elif op == 2:
        print(f'O resultado de {p1} x {p2} é {p1*p2}')
    elif op == 3:
        maior = [p1, p2]
        print(f'Entre {p1} e {p2} o maior valor é {max(maior)}')
    elif op == 4:
        print('Informe os números novamente: ')
        p1 = int(input('Primeiro valor: '))
        p2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(1.5)
print('Fim do programa ! Volte sempre!')

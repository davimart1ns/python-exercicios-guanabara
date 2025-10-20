def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


def leiareal(msg):
    while True:
        try:
            r = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return r


n = leiaint('Digite um número inteiro: ')
r = leiareal('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r}')
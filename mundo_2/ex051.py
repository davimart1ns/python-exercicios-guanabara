num: int = int(input('Digite um número: '))
div = 0
ff = num + 1
for c in range(1, ff):
    if num % c == 0:
        print('\033[33m', end=' ')
        div += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print(f'\n\033[mO número {num} foi divisível {div} vezes')
if div == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')

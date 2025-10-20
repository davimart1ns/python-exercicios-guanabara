print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
t1 = 0
t2 = 1
termo = int(input('Quantos termos você quer mostrar? '))
c = 3
print('~'*30)
print(f'{t1} ➔ {t2}', end=' ➔ ')
while c <= termo:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t3}', end=' ➔ ')
    c += 1
print('FIM')
print('~'*30)

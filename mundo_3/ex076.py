words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
         'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in words:
    print('\nNa palavra ', c, f'temos', end=' ')
    for i in c:
        if i.lower() in 'aeiou':
            print(i, end='')

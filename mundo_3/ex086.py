lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
num = ter = 0
for c in range(0, 3):
    for i in range(0, 3):
        lista[c][i] = int(input(f'Digite um valor para [{c}, {i}]: '))
print('-='*30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{lista[c][i]:^5}]', end='')
        if lista[c][i] % 2 == 0:
            num += lista[c][i]
    ter += lista[c][2]
    print()
print(f'A soma dos valores pares é {num}')
print(f'A soma dos valores da terceira coluna é {ter}')
print(f'O maior valor da segunda linha é {max(lista[1])}')

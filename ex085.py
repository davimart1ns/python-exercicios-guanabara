lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for i in range(0, 3):
        lista[c][i] = int(input(f'Digite um valor para [{c}, {i}]: '))
print('=-'*30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{lista[c][i]:^5}]', end='')
    print()

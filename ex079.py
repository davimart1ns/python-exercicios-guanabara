valor = list()
p = 0
for c in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n > valor[-1]:
        valor.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {valor}')

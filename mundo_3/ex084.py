valores = [[], []]
num = 0
for c in range(1, 8):
    num = (int(input(f'Digite o {c}o. valor: ')))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print('=-'*30)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')

lista = list()
pares = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impar.append(valor)
print('-='*30)
print(f'A lista completa é {lista}')
print(f"A lista de pares é {pares}")
print(f'A lista de ímpares é {impar}')

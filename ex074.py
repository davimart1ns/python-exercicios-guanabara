n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
lista = (n1, n2, n3, n4)
print(f'Voce digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3) + 1} posicao')
else:
    print('0 valor 3 nao apareceu em lugar nenhum')
print('Os valores pares digitados foram ', end='')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')

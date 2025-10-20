import random
sort = 0
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
escolha = random.choices(numeros, k=5)
print(f'Os valores sorteados foram: {escolha}')
print(f'O maior valor sorteado foi {max(escolha)}')
print(f'O menor valor sorteado foi {min(escolha)}')
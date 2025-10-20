maior = 0
menor = 0
for peso in range(1, 6):
    massa = float(input(f'Peso da {peso}ª pessoa: '))
    if peso == 1:
        maior = massa
        menor = massa
    else:
        if massa > maior:
            maior = massa
        if massa < menor:
            menor = massa
print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')
#jeito simples de fazer o programa
#massa = [float(input(f'Peso da {peso}ª pessoa: ')) for peso in range(1, 6)]
#print(f'O maior peso lido foi de {max(massa)}kg')
#print(f'O menor peso lido foi de {min(massa)}kg')

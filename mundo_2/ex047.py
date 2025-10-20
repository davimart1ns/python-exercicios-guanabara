soma = 0
valores = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        soma = soma + cont
        valores = valores + 1
print(f'A soma de todos os {valores} valores solicitados é {soma}')
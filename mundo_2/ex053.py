from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    calculo = date.today().year - ano
    if calculo >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')

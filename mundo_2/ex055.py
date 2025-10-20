menina = 0
velho = ''
maior = 0
soma = 0
for p in range(1, 5):
    print('{:-^20}'.format(f' {p}ª PESSOA '))
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sex = str(input('[M/F]: ')).upper()
    soma += idade
    if p == 1 and sex == 'M':
        maior = idade
        velho = nome
    if idade > maior and sex == 'M':
        maior = idade
        velho = nome
    if sex == 'F' and idade < 20:
        menina += 1
media = soma / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maior} anos e se chama {velho}.')
print(f'Ao todo são {menina} mulheres com menos de 20 anos')

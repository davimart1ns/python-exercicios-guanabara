c = ''
cont = num2 = maior = menor = 0
while c != 'N':
    num = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N]')).upper().strip()
    cont += 1
    num2 += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
md = num2 / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, md))
print(f'O maior valor foi {maior} e o menor foi {menor}')

print('-'*45)
print('LOJA SUPER BARATÃO'.center(45))
print('-'*45)
soma = mil = cont = menor = 0
barato = ''
while True:
    pd = str(input('Nome do Produto: '))
    pre = float(input('Preço: R$'))
    con = ' '
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    soma += pre
    cont += 1
    if pre > 1000:
        mil += 1
    if cont == 1 or pre < menor:
        menor = pre
        barato = pd
    if con == 'N':
        break
print('-'*14, 'FIM DO PROGRAMA'.center(14), '-'*14)
print('O total da compra foi R${:.2f}'.format(soma))
print(f'Temos {mil} produtos custando mais de R$1000.00')
print('O produto mais barato foi {} que custa R${:.2f}'.format(barato, menor))
#hahahhahahahahahah
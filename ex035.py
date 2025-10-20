casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
por = sal * 30 / 100
pre = casa / (anos * 12)
print('Para pagar uma casa se R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, pre))
if pre <= por:
    print('Empréstimos pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

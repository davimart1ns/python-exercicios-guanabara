print('='*15, 'LOJAS MARTINS',  '='*15)
print('{:=^45}'.format('A LOJA MAIS PIKA DO MUNDO'))
comp = float(input('Preços das compraa: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    pr = comp - (comp * 10 / 100)
elif op == 2:
    pr = comp - (comp * 5 / 100)
elif op == 3:
    pr = comp / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(pr))
elif op == 4:
    par = int(input('Quantas parcelas? '))
    pr = comp + (comp * 20 / 100)
    parcelas = pr / par
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(par, parcelas))
else:
    pr = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(comp, pr))

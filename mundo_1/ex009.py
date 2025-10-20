n = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = n / 5.60
print('Com R${:.2f} você pode comprar US${:.2f}'.format(n, dol))
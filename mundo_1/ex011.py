p = float(input('Qual o preço do produto? R$'))
prom = (p * 95) / 100
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, prom))
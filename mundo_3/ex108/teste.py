from ex108 import moeda
preco = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(preco, 13, True)}')

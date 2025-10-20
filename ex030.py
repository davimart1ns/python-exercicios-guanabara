dis = float(input('Qual e a distancia da sua viagem? '))
r = dis * 0.5 if dis <= 200 else dis * 0.45
print(f'Voce esta prestes a começar uma viagem de {dis}km.')
print('E o preço da sua passagem sera de R${:.2f} reais'.format(r))


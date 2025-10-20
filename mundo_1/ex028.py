from termcolor import colored
v = float(input('Qual a velocidade atual do carro? '))
if v <= 80:
    print(colored('Tenha um bom dia! Dirija com segurança! ', 'yellow'))
else:
    r = (v - 80) * 7
    print(colored('MULTADO! Voce excedeu o limite permitido que e de 80km/h', 'red'))
    print(colored('Voce deve pagar uma multa de R${:.2f}!'.format(r), 'red'))
    print(colored('Tenha um bom dia! Dirija com segurança!', 'yellow'))

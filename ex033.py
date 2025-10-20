sal = float(input('Qual é o salario do funcionario? R$'))
if sal <= 1420:
    am = sal + (15 * sal) / 100
else:
    am = sal + (10 * sal) / 100
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, am))


print('='*30)
print('BANCO DAV'.center(30))
print('='*30)
valor = float(input('Que valor você quer sacar? R$'))
total = valor
nota = 50
totnota = 0
while True:
    if total >= nota:
        total -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f'Total de {totnota} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnota = 0
        if total == 0:
            break


#while True:
#    if valor >= 50:
#        valor -= 50
#       n2 += 1
#    else:
#        if valor >= 20:
#            valor -= 20
#            n3 += 1
#        else:
#            if valor >= 10:
#                valor -= 10
#                n4 += 1
#            else:
#                if valor >= 1:
#                    valor -= 1
#                    n5 += 1
#    if valor == 0:
#        break
#print(f'Total de {n2} cédulas de R$50')
#print(f'Total de {n3} cédulas de R$50')
#print(f'Total de {n4} cédulas de R$10')
#print(f'Total de {n5} cédulas de R$1')
#print('Volte sempre ao BANCO DAV! Tenha um bom dia!')

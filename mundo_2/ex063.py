n = v = c = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c += 1
    v += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {c} números e a soma entre eles é {v}.')
#jeito de preguiçoso
#n = v = c = 0
#while n != 999:
#    n = int(input('Digite um número [999 para parar]: '))
#    c += 1
#    v += n
#print(f'Você digitou {c - 1} números e a soma entre eles é {v - 999}.')

num = int(input('Digite um número para calcular o seu Fatorial: '))
c = num
f = 1
print(f'Calculando {num}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
#gambiarra que funcionou hahahahahahahahahahaha
#from math import factorial
#print('Digite um número para')
#num = int(input('calcular seu Fatorial: '))
#print(f'Calculando {num}! {num}', end=' ')
#for c in range(num - 1, 0, -1):
#    print(f'x {c}', end=' ')
#print(f'= {factorial(num)}')

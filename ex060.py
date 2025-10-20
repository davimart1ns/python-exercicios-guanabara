print('Gerador de PA')
print('-=' * 11)
t1 = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
decimo = t1 + (10 - 1) * rz
c = 1
while c <= 10:
    print(f'{t1}', end=' ⮕ ')
    t1 += rz
    c += 1
print('FIM')

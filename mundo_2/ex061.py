print('Gerador de PA')
print('-='*11)
termo = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
c = 1
pa = 0
ad = 10
while ad != 0:
    pa += ad
    while c <= pa:
        print(f'{termo}', end=' → ')
        termo += rz
        c += 1
    print('PAUSA')
    ad = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {pa} termos mostrados.')

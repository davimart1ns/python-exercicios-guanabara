print('='*30)
print("CADASTRE UMA PESSOA".center(30))
print('='*30)
maior = man = girl = 0
while True:
    age = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('='*30)
    if age >= 18:
        maior += 1
    if sex == 'M':
        man += 1
    if age < 20 and sex == 'F':
        girl += 1
    con = ' '
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N]')).strip().upper()
    if con == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {man} homens cadastrados')
print(f'E temos {girl} mulheres com menos de 20 anos')
#primeiramente eu fiz sem o while 'var' not ir 'SN' ou 'MF'
#fiz so com os if e deu certo, mas agora dei uma ajeitada e ficou midia
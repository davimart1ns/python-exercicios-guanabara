sex = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sex not in 'MF':
    print('Dados inválidos. ', end='')
    sex = str(input('Por favor, informe seu sexo: ')).upper()
print(f'Sexo {sex} registrado com sucesso')

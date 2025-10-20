nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome te ao todo {len(nome) - nome.count(" ")} letras')
p1 = nome.split()
print(f'Seu primeiro nome é {p1[0]} e ele tem {len(p1[0])} letras')



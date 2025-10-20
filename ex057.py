from random import randint
print('Sou seu computador... ')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
palpite = int(input('Qual é seu palpite? '))
sort = randint(1, 11)
tent = 1
while palpite != sort:
    if palpite < sort:
        print('Mais... Tente mais uma vez.')
        tent += 1
    else:
        print('Menos... Tente mais uma vez.')
        tent += 1
    palpite = int(input('Qual o seu palpite? '))
print(f'Acertou com {tent} tentativas. Parabéns!')


frase = str(input('Digite uma frase: ')).strip().upper()
words = frase.split()
join = ''.join(words)
inverso = ''
for c in range(len(join)-1 , -1, -1):
    inverso += join[c]
print(f'O inverso de {join} é {inverso}')
if join == inverso:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é palíndromo!')
#jeito mais simples de fazer esse programa
#frase = str(input('Digite uma frase: ')).upper()
#palavras = frase.split()
#certo = ''.join(palavras)
#print(f'O inverso de {certo} é {certo[::-1]}')
#if certo == certo[::-1]:
#    print('Temos um palíndromo!')
#else:
    #print('A frase digitada não é um palíndromo!')

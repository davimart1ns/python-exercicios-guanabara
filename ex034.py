print('-='*20)
print('Analisador de triangulos')
print('-='*20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
    print('Os segmentos acima PODEM FORMAR triangulo')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo')
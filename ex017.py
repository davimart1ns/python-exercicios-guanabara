import math
an = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(an)
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, math.sin(rad)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, math.cos(rad)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, math.tan(rad)))



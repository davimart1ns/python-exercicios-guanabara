import math
from math import sqrt
op = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
cat = (op**2) + (ad**2)
print('A hipotenusa vai medir {:.2f}'.format(sqrt(cat)))
#um jeito bem mais simples
#import math
#hi = math.hypot(op, ad)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

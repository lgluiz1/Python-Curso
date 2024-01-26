import math

catop = float(input('Comprimento do Cateto Oposto'))
catad = float(input('Comprimento do cateto adjacente'))
res = math.hypot(catop,catad)

print ('A hipotenusa vai medi {:.2f}'.format(res))
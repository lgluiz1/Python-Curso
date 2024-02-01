# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE O SEU FATORIAL
# EX 5!=5X4X3X2X1 =120
from time import sleep
from math import factorial

n1 = int(input('DIGITE UM VALOR!  '))
n2 = n1
fatorial = factorial(n1)
print('FATORIAL DE {}! = '.format(n1),end='')
while n2 > 1:
    print('{}'.format(n2), end='')
    n2 -= 1
    if n2 > 1:
        print(' x ', end='')
        
print(' = {}'.format(fatorial))
# FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E MOSTRE O SEU FATORIAL
# EX 5!=5X4X3X2X1 =120
from time import sleep
from math import factorial

n1 = int(input('DIGITE UM VALOR!  '))
n2 = n1
while n2 != 2:
    n2 -= 1
    calculo = n1 * n2
    calculo += calculo
    sleep(1)
print(calculo)
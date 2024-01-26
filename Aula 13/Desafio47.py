#CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NUMEROS PARES QUE ESTAO NO INTERVALO ENTRE 1 E 50

from time import sleep
print ('=_'*20)
n1 = int(input('Digite um valor para ter a sequencia de numeros PAR'))
print ('=_'*20)
for c in range(0,n1,2):
    print(c+2)
    sleep(1)
    print('='*4)
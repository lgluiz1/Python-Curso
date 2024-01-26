from random import randint
n1 = int(input('Digite a quantidade de numero para da tabela: '))
numero = randint(0,n1)
if numero % 2 == 0 :
    print('Numero Sorteado foi {} e Par'.format(numero))
else: 
    print('Numero Sorteado foi {} e e Impar'.format(numero))
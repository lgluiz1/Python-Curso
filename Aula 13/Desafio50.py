
#SE O VALOR DIGITADO FOR IMPAR. DESCONSIDERE-O
from time import sleep
from random import randint

lista = []
soma = 0
cont = 0
#DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS  INTEIROS
for numeros in range (6):  
    print('*=' * 15)
    n1 = int(input('DIGITE UM NUMERO:  '))
    lista += (str(n1).split(','))
    
print('+=+' * 16)
print('ESTAMOS CALCULANDO SEUS NUMEROS')
print('+=+' * 16)
sleep(5)
#MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES.
print('ESSES NUMEROS SAO OS NUMEROS PARES ')
sleep(3)
print('IMPRIMINDO OS NUMEROS ')
sleep(2)
for numero in lista :
    if int(numero) % 2 == 0 :
        print('+=+' * 10)
        print('O NUMERO {} E PAR'.format(numero))
        sleep(2)
        cont += 1
        soma += n1
print('+=+' * 15)
print('VOCE DIGITOU {} NUMERO PARES TOTAL DELES FOI {}'.format(cont,soma))
print('+=+' * 15)
sleep(5)
print('ESSES NUMEROS SAO OS NUMEROS IMPAR "DESCONSIDERADOS" ')
sleep(3)
print('IMPRIMINDO OS NUMEROS ')
print('+=+' * 15)
sleep(2)
for numero in lista :
    if int(numero) % 2 != 0 :
        print('-=-' * 10)
        print('O NUMERO {} ESTA DESCONSIDERADO'.format(numero))
        cont =+ 1
        sleep(2)
print('VOCE DIGITOU {} NUMEROS IMPARES'.format(cont))

'''
for _ in range(6):
    n1 = int(input('Digite um número: '))
    numeros = (n1, n1, n1, n1, n1, n1)
    lista.append(numeros)

for numeros in lista:
    for num in numeros:
        if num % 2 == 0:
            print('O número {} é par'.format(num))
        else:
            print('O número {} é ímpar'.format(num))



'''

'''for auto in range(randint(0,100)):
    if auto % 2 == 0 :
        par = auto % 2 == 0
        print('ESSES NUMEROS SAO PAR {}'.format(auto))
    elif auto % 2 != 0:
        impar = auto % 2 != 0 
        print('ESSES NUMEROS SAO IMPAR {}'.format(auto))'''
from random import randint

n1 = int(input('Digite a quantidade de numero da rifa: '))
sorteio = randint(0,n1)

print('Numero Sorteado dentre os {} foi {}'.format(n1,sorteio))
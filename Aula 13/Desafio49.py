#REFORÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NUMERO
#QUE O USUARIO ESCOLHER, SO QUE AGORA UTILIZANDO UM LAÇO FOR

from time import sleep

n1 = int(input('QUAL TABUADA VOCÊ QUE CALCULA?  '))

print('=' * 40)
print('TABUADA {}'.format(n1))
print('=' * 40 )

print('ESTOU CALCULANDO SEU NUMERO')
print('=' * 40)
sleep(5)

for c in range (1,11):
    ca = n1 * c
    sleep(1)
    
    print('{} X {} = {}'.format(n1,c,ca))
    print('=' * 13)
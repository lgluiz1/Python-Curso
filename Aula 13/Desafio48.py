#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES
#QUE SÃO MULTIPLOS DE TRES E QUE SE ENCONTRAM NO INTERVALO DE 1 ATE 500

from time import sleep
n1= int(input('DIGITE UM NUMERO PARA ANALISA LISTA:   '))
print('=' *40)
print('''ESTOU ANALISANDO TODOS OS NUMEROS QUE 
  SAO DIVIDIDOS POR 3 NA SUA TABELA''')
print('=' *40)
sleep(5)
print ('SEGUE ANALISE DE {} NUMEROS'.format(n1))
print('=' *40)

soma = 0
cont = 0
for c in range(1,n1,2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('SAO {} NUMEROS IMPARES E A SOMA DELE E {}'.format(cont,soma))
        
        

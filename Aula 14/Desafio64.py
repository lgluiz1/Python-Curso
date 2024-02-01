#Crie um programa que leia vários números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos 
#números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
soma = 0
n1 = 0

while n1 != 999 :
    n1 = int(input('DIGITE UM VALOR: '))
    soma += n1
    cont += 1
print('VOCE DIGITOU {} NÚMEROS EA SOMA ENTRE ELES E {}'.format(cont-1, soma-999))
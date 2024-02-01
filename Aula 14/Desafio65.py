#Crie um programa que leia vários números inteiros pelo teclado. No final da
#execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
sair = ''
cont = 0
soma = 0
maior = 0
menor = 0
while sair != 'n':
    numero = int(input('DIGITE UM NUMERO:  '))
    sair = str(input('DESEJA CONTINUA? S/N:  ')).lower()[0].strip()
    soma += numero
    cont +=1


    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma/cont
    
print('VOCE DIGITOU {} NUMEROS E A MEDIA FOI {}'.format(cont,media))
print('E O MAIOR NUMERO FOI {} EO MENOR {}'.format(maior,menor))


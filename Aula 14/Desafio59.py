# CRIE UM PROGRAMA QUE LEIA 2 VALORES E MOSTRE NA TELA
# 1 - PARA SOMAR
# 2 - MULTIPLICAR
# 3 - MAIOR
# 4 - NOVOS NUMEROS
# 5 - SAIR
# SEU PROGRAMA DEVERA REALIZA OPERAÇÕES SOLICITADA EM CADA CASO

opções = 1,2,3,4,5
print('**'*10)
print('LEIA ATENTAMENTE O MENU')
print('**'*10)
n1 = int(input('DIGITE UM VALOR!  '))
n2 = int(input('DIGITE OUTRO VALOR !  '))

while opções != 5:
    print('=='*10)
    print('ESCOLHA UMA OPÇÃO')
    print('=='*10)
    print ('DIGITE 1 PARA SOMAR')
    print ('DIGITE 2 PARA MULTIPLICAR')
    print ('DIGITE 3 PARA MAIOR')
    print ('DIGITE 4 PARA NOVOS NUMEROS')
    print ('DIGITE 5 PARA SAIR')
    print('=='*10)
    opções = int(input('QUAL OPÇÃO VOCE ESCOLHE? '))

    if opções == 1:
       soma = n1 + n2
       print('A SOMA DOS NUMERO {} + {} = {}'.format(n1,n2,soma))

    if opções == 2 :
        m = n1 * n2
        print('OS VALORES MULTIPLICADOS {}X{}={}'.format(n1,n2,m))

    if opções == 3:
        if n1 > n2 :
            print('O MAIOR VALOR ENTRE {} E {} E {}'.format(n1,n2,n1))
        else:
            print('O MAIOR VALOR ENTRE {} E {} E {}'.format(n1,n2,n2))
        
    if opções == 4 :
        n1 = int(input('DIGITE UM VALOR!  '))
        n2 = int(input('DIGITE OUTRO VALOR !  '))
        
print('VOCE SAIU DO MENU')
    
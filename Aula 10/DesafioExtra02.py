from random import randint

a = input('Você acha que o número será PAR ou IMPAR: ').lower()
numero = randint(0, 9999)

if numero % 2 == 0 and 'par' in a:
    print('O Número Escolhido Foi {} e Ele é PAR. Você Acertou! PARABÉNS!'.format(numero))

elif numero % 2 != 0 and 'impar' in a:
    print('O Número Escolhido Foi {} e Ele é ÍMPAR. Você Acertou!'.format(numero))

else:
    print('O número escolhido foi {} e não corresponde à sua escolha. Tente novamente.'.format(numero))

# MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR ''PENSA'' EM UM NUMERO ENTRE 0 A 10 
# SO QUE AGORA O JOGADOR VAI TENTA ADIVINHA ATE ACERTA, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER

from random import randint

computador = randint(0,10)
contado = 0
jogador = 0,1,2,3,4,5,6,7,8,9,10
while jogador != computador:
    contado += 1
    jogador = int(input('DIGITE SEU PALPITE DE 0 A 10!  '))
    if jogador < computador:
        print('MAS... VOCE ESTA PROXIMO')
    if jogador > computador:
        print('MENOS... VOCE ESTA PERTO')
 

print('=='*22)
print('VOCE ACERTOU O NUMERO ERA {}'.format(computador))
print('FOI NECESSARIO {} JOGADAS PARA VOCÊ VENCER'.format(contado-1))
print('=='*22)
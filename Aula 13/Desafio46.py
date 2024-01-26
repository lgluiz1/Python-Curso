#FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA
#PARA O ESTOURO DE FOGOS DE ARTIFICIO, INDO DE 10 ATÉ 0, 
#COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES

from time import sleep
contagem = int(input('DIGITE O INICIO DA CONTAGEM!  '))
print('*=' * 4)
for c in range (contagem , -1, -1):
    print (c)
    print('*=' * 4)
    sleep(1)

print('!!FOGO!!')
print('*=' * 4)
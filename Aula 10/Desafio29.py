veloc = int(input('Qual Velocidade do Carro?  '))
if veloc <= 80 :
    print (' Muito Bem voce esta no Limite permitido!')
else: 
    multa = (veloc-80) * 7
    print ('Voce foi multado em R${:.2f}'.format(multa))

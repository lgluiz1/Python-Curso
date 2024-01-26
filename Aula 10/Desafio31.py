v = int(input('Qual Distancia da sua viagem? '))
a = v * 0.50
n = v * 0.45
if v <= 200:
    print ('Valor da sua viagem e R${:.2f}'.format(a))
else:
    print('Sua viagem e Maior que 200KM por isso valor dela e R${:.2f}'.format(n))
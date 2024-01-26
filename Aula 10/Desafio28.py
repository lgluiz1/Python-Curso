from random import randint

numero = int(input('Digite um Numero de 0 a 5!'))
auto = randint(0,5)
if numero == auto:
    print('Voce Acertou o numero era {}'.format(auto))
else:
    print('Voce errou Tente Novamente numero era {}'.format(auto))

    
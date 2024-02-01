from random import randint

while True:
    numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
    crescente = tuple(sorted(numeros))
    print(f'OS VALORES SORTEADOS FORAM {numeros[0:]}')
    print(f'O MAIOR VALOR SORTEADO FOI {crescente[-1]}')
    print(f'O MENOR VALOR SORTEADO FOI {crescente[0]}')
    break
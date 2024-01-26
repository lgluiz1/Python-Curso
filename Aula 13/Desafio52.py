# FAÇA UM PROGRAMA Q LEIA UM NUMERO INTEIRO E DIGA SE ELE E OU NAO UM NUMERO PRIMO

n1 = int(input('DIGITE UM NUMERO:  ')) 

total = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[34m',end='')
        total += 1
    else:
        print('\033[33m', end='')

    print('{}'.format(c),end=' ')
print('\n O NUMERO {} FOI DIVIDIDO {}'.format(n1, total))

if total == 2:
    print('O NUMERO {} E PRIMO POIS ELE FOI DIVIDIDO {}x SOMENTE'.format(n1,total))
else:
    print('O NUMERO {} NÃO E PRIMO POIS ELE FOI DIVIDIVO {} NUMEROS'.format(n1,total))
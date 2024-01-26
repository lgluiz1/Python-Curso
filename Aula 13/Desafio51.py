# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO EA RAZAO
# DE UMA PA . NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

print('=='*15)
print('10 TERMOS DE UMA PA')
print('=='*15)

n1 = int(input('DIGITE O PRIMEIRO TERMO:  '))
n2 = int(input('RAZÃO'))
n3 = n1 + (10-1) * n2

for c in range(n1,n3 + n2 ,n2):
    print('{}'.format(c),end=' => ')
print('ACABOU!')
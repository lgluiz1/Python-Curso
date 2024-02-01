
print('=='*15)
print('TERMOS DE UMA PA')
print('=='*15)

primeiro = int(input('PRIMEIRO TERMO:  '))
razão = int(input('DIGITE A RAZÃO:  '))
cont = 1
termo = primeiro
while cont <= 10:    
    termo += razão
    print('{} ==> '.format(termo) , end='')
    cont += 1
    
print('FIM!')
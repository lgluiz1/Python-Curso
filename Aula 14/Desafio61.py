#REFAÇA O DESAFIO 51 , LENDO O PRIMEIRO TERMO EA RAZÃO DE UMA PA
#MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO ESTRUTURA WHILE.

print('=='*15)
print('10 TERMOS DE UMA PA')
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
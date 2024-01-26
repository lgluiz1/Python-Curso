
#FAÇA UM PROGRAMA Q LEIA O PESO DE CINCO PESSOAS
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('QUAL SEU PESO?  '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR PESO LIDO FOI {}Kg'.format(maior))
print('O MENOR PESO LIDO FOI {}Kg'.format(menor))
    

#NO FINAL MOSTRE QUAL FOI O MAIOR EO MENOR PESO LIDOS

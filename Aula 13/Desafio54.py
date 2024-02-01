#CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS
#NO FINAL MOSTRE QUANTAS PESSOAS AINDA NAO ATINGIRAM A MAIORIDADE
#E QUANTAS JA SAO MAIORES

from datetime import date

ano = date.today().year
contado_maior = 0
contado_menor = 0
for c in range (1,80):
    idade = int(input('Qual Ano Da {}º Pessoa?  '.format(c)))
    if ano - idade < 18:
        contado_maior += 1
    else: 
        contado_menor += 1
print('AO TODO TIVEMOS {} MENOR DE IDADE'.format(contado_maior))
print('E TAMBEM TIVEMOS UM TOTAL DE {} MAIOR DE IDADE.'.format(contado_menor))    

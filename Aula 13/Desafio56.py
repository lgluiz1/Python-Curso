
from time import sleep

print ('='*40)
print('''
VAMOS PRECISA DE ALGUMAS INFORMAÇÕES
    PARA VALIDARMOS SEU ACESSO
''')
print ('='*40)
sleep(3)
print('ATENÇÃO NAS PERGUNTAS A SEGUIR')
print ('='*40)
sleep(3)

dados = []
#DESENVOLVA UM PROGAMA QUE LEIA O NOME IDADE E SEXO DE 4 PESSOAS
for n in range(0,4):
    nome = str(input('Qual Seu Nome?  ')).lower()
    idade = int(input('Qual Sua Idade?  '))
    print('DIGITE F PARA FEMININO E M PARA MASCULINO')
    sexo = str(input('Voce e do sexo MASCULINO(M) ou FEMININO(F)?  ')).lower()

    pessoa = {'nome':nome , 'idade':idade , 'sexo':sexo}
    dados.append(pessoa)

soma_idades = 0
#A MEIDIA DE IDADE DO GRUPO
for pessoas in dados:
    soma_idades += pessoa['idade']

media_idades = soma_idades / len(dados)
print('A média de idade do grupo é {:.0f}.'.format(media_idades))

#QUAL EO NOME DO HOMEM MAIS VELHO
homem_mais_velho = None
idade_homem_mais_velho = 0

for pessoa in dados:
    if pessoa['sexo'] == 'm' and pessoa['idade'] > idade_homem_mais_velho:
        homem_mais_velho = pessoa['nome']
        idade_homem_mais_velho = pessoa['idade']

if homem_mais_velho is not None:
    print('O homem mais velho é:', homem_mais_velho)
else:
    print('Não há homens na lista ou nenhum homem tem idade registrada.')

#QUANTAS MULHERES TEM MENOS DE 20 ANOS
mulheres_menos_20 = sum(1 for pessoa in dados if pessoa['sexo'] == 'f' and pessoa['idade'] < 20)
print('Há {} mulheres com menos de 20 anos.'.format(mulheres_menos_20))
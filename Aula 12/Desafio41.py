# A CONFEDERAÇÃO NACIONAL DE NATAÇAO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO
# DE UM ATLETA E MOSTRE SUA CATEGORIA DE ACORDO COM A IDADE

# ATE 9 ANOS: MIRIM
# ATE 14 ANOS: INFANTIL
# ATE 19 ANOS: JUNIOR
# ATE 20 ANOS: SENIOR
# ACIMA : MASTER

from datetime import date

idade = int(input('Qual ano de nascimento do atleta? '))
ano = date.today().year
categoria = ano - idade

if categoria <= 9 :
    print('Seu atleta tem {} e Categoria dele e MIRIN'.format(categoria))
elif categoria <= 14 :
    print('Seu Atleta Tem {} e Categoria Dele e INFANTIL'.format(categoria))
elif categoria <= 19 :
    print('Seu Atleta tem {} e Categoria Dele e JUNIOR'.format(categoria))
elif categoria <= 20 :
    print('Seu Atleta Tem {} e Categoria Dele e SENIOR'.format(categoria))
elif idade > ano :
    print('Não e possivel ter nascido no ano digitado')
else:
    print('Seu Atleta tem {} e Categoria Dele e MASTER'.format(categoria))
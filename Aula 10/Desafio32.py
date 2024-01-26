from datetime import date

ano = int(input('Que Ano voce quer analisar? Digite 0 caso queira analisa ano atual: '))

if ano == 0 :

    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :

    print('{} e ano Bissexto'.format(ano))

else: 

    print('{} Não e um ano Bissexto'.format(ano))
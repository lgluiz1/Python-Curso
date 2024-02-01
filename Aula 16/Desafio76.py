print('=='*20)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('=='*20)

produtos = ('lapis', 1.75 , 'borracha' , 2.00, 'caderno',15.90,'estojo', 25.00,'mochila' ,120 ,'livro',34.90)
for nome in range(0 , len(produtos),2):
    print(f'{produtos[nome].capitalize():.<30}R${produtos[nome+1]:>.2f}')

print('=='*20)


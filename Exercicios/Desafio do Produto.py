nome = input('Qual nome do Produto?')
valor = float(input('Qual valor do Produto?R$'))
desconto = float(input('Valor do desconto?%'))

calcu = (desconto / 100 * valor)
res = valor-calcu


print('{} custa R${:.2f} com {:.0f}% ela sai a R${:.2f}'.format(nome,valor,desconto,res))
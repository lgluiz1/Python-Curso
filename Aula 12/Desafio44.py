# ELABORE UM PROGRAMA QUE CALCULE VALOR A SER PAGO POR UM PRODUTO
# CONSIDERANDO SEU PREÇO NORMAL E CONDIÇAO DE PAGAMENTO

# AVISTA DINHEIR/CHEQUE:10% DE DESCONTO
# A VISTA NO CARTÃO:5% DE DESCONTO
# EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# 3X OU MAIS NO CARTÃO: 20% DE JUROS

valor = float(input('Qual Valor Do Produto? '))
print('=' * 35)

if valor != 0 or '' :
    print('O PRODUTO CUSTA R${:.2f} '.format(valor))
    print('=' * 35)

    print('ESCOLHA UMA OPÇÃO DE PAGAMENTO')
    print('=' * 35)

    print('1 - Pagamento A Vista/Cheque')
    print('2 - Pagamento Debito a Vista')
    print('3 - Pagamento no Credito 1x a 2x')
    print('4 - Pagamento Credito 3x a 12x')

    print('=' * 35)
    opção = int(input('QUAL A FORMA DE PAGAMENTO? '))    

    if opção == 1:
        avista = valor - (valor * 0.1)
        print('=' * 85)
        print('AVISTA o Produto Ganha 10% de desconto com isso valor dele fica R${:.2f}'.format(avista))
        print('=' * 85)

    elif opção == 2:
        cartao_avista = valor - (valor * 0.05) 
        print('=' * 85)
        print('No DEBITO AVISTA o produto ganha 5% de desconto com isso valor dele fica R${:.2f}'.format(cartao_avista))
        print('=' * 85)

    elif opção == 3:
        print('=' * 60)
        print('Em 2x no Cartão Credito o Produto Fica no Valor De R${:.2f}'.format(valor))
        print('=' * 60)

    elif opção == 4:
        valor3x = valor + (valor * 0.2) 
        print('=' * 60)
        print('No CREDITO de 3x a 12x o produto fica no valor de R${:.2f}'.format(valor3x))
        print('=' * 60)

    else: 
        print('=' * 35)
        print('Opção Invalida')
        print('=' * 35)

else:
    print('Por Favor Digite Valor do Produto!')
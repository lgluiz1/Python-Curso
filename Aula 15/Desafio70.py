soma = acima = 0
mas_barato = float('inf')
nome_produto = None

while True:
    nome = str(input('NOME DO PRODUTO:  ')).upper().strip()
    preço = float(input('DIGITE VALOR DO PRODUTO!  R$'))
    soma += preço
    if preço > 1000:
        acima +=1

    if preço < mas_barato:
        nome_produto = nome
        mas_barato = preço

    continua = ''
    while continua != 's' and continua != 'n':
        continua = str(input('VOCE DESEJA CONTINUA? [S/N]  '))

    if continua == 'n':
        break
print('=='*30)
print(f'O TOTAL QUE VOCÊ GASTOU FOI R${soma:.2f}')
print(f'VOCÊ COMPROU {acima} ACIMA DE R$1000,00')
print(f'E O PRODUTO MAIS BARATO FOI {nome_produto} NO VALOR DE R${mas_barato:.2f} ')
print('=='*30)
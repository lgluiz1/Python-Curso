#ESCREVA UMA PROGRAMA QUE APROVA O EMPRESTIMO BANCARIO PARA COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTA
#O VALOR DA CASA, O SALRIO DO COMPRADOR EM QUANTOS ANOS ELE VAI PAGAR

#CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NAO PODE EXECER 30% DO SALARIO
#OU ENTAO O EMPRESTIMO SERA NEGADO

casa = float(input('Qual Valor da Casa? R$'))
salario = float(input('Qual Seu Salario Mensal? R$'))
quantidade = int(input('Em quantos anos deseja paga? '))

meses = quantidade * 12
mensalidade = casa / meses
limite_porcentagem = 30


if mensalidade <= salario * (limite_porcentagem / 100):
    print('Para paga uma casa de R${:.0f} em {} anos a prestação sera de R${:.2f}'.format(casa,quantidade,mensalidade))
    print('Seu Emprestimo Foi APROVADO!')

else:
    print('Para Pega uma casa de R${:.0f} em {} anos a prestação sera de R${:.2f}'.format(casa,quantidade,mensalidade))
    print('Seu Emprestimo Foi REPROVADO!')
    

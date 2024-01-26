salario = float(input('Qual seu Salario? '))
aumento = 1250 * 0.1 + salario
maior = salario * 0.15 + salario
if salario >= 1250 :
    print(' Seu Salario e R${:.2f} então voce vai receber {:.2f}'.format(salario , aumento))
else: print(' Seu salario e menor que R$1250.00 e por isso ira receber R${:.2f}'.format(maior))
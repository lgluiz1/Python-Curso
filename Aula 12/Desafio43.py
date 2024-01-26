# DESENVOLVA UMA LOGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA,
# CALCULE SEU ICM E MOSTRE SEU STATUS, DE ACORDOD COM A TABELA ABAIXO

# ABAIXO DE 18.5: ABAIXO DO PESO
# ENTRE 18.5 E 25: PESO IDEAL
# 25 ATÉ 30: SOBREPESO
# 30 ATÉ 40: OBESIDADE
# ACIMA DE 40: OBESIDADE MÓRBIDA

peso = int(input('Qual Seu Peso? '))
altura = float(input('Qual Sua Altura? ')) / 100
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC e {:.2f}'.format(imc))
    print ('Voce Esta ABaixo do PESO!')
elif 18.5 <= imc < 25:
    print('Seu IMC e {:.2f}'.format(imc))
    print('Voce Esta No PESO IDEAL')
elif 25 <= imc < 30:
    print('Seu IMC e {:.2f}'.format(imc))
    print('Voce Esta Com SOBREPESO')
elif 30 <= imc < 40:
    print('Seu IMC e {:.2f}'.format(imc))
    print('Voce Esta Com OBESIDADE')
else:
    print('Seu IMC e {:.2f}'.format(imc))
    print('Voce Esta Com OBESIDADE MÓRBIDA')
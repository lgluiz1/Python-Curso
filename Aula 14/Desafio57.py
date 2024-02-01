# FAÇA UM PROGRAMA Q LEIA SEXO DE UMA PESSOA MAIS SO ACEITE SE RESPOSTA FOR 'M' OU 'F'

sexo = str(input('QUAL SEU SEXO? ')).strip().lower()[0]

while sexo not in 'mf':
    sexo = str(input('DADOS INVALIDO. QUAL SEU SEXO? ')).strip().lower()[0]
    
print('OBRIGADO POR NOS INFORMA SEUS DADOS!')

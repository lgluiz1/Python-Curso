nome = str(input('Qual Seu Nome Completo?')).strip()
fat = nome.split()
pri = fat[0]
ult = fat[-1]

print ('Seu nome e {}'.format(nome))
print ('Seu Primeiro Nome e {}'.format(pri))
print ('Seu Ultimo Nome e {}'.format(ult))
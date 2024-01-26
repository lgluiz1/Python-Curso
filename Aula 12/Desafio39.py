# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORMA,DE ACORDO COM SUA IDADE

# SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
# SE E A HORA DE SE ALISTA.
# SE JA PASSOU DO TEMPO DO ALISTAMENTO

# SEU PROGRAMA TAMBEM DEVERA MOSTRA O TEMPO Q FALTA OU Q PASSOU DO PRAZO

from datetime import date
idade = int(input('Qual Sua Idade? '))
ano = date.today().year
na = ano - idade
passou = idade - 18
alistamento = ano - passou

if idade < 18:    
    falta = (18 - idade) + ano
    print ('Seu ano de nascimente foi {} e voce tem {} e precisa se alista no ano {} '.format(na,idade,falta))
elif idade == 18 :
    print(' Voce Nasceu em {} e Voce tem {} Anos precisa ir ate uma junta milita para se alista o mais rapido possivel'.format(na,idade))
else:
    print('Voce Nasceu em {} e tem {} Voce deveria ter se alistado no ano de {} se nao foi va a uma junta mais rapido possivel'.format(na,idade,alistamento))
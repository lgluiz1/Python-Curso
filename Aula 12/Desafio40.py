# CRIE UM PROGRAMA Q LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA 
#MOSTRANDO UMA MENSAGEM NO FINAL DE ACORDO COM A MEDIA ATINGIDA 

#MEDIA ABAIXO DE 5.0 : REPROVADO
#MEDIA ENTRE 5.0 E 6.9 : RECUPERAÇAO
#MEDIA 7.0 OU SUPERIOR : APROVADO

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua outra nota: '))
media = (n1 + n2 ) / 2

if media < 5:
    print('Sua nota Foi {} Voce Esta REPROVADO!'.format(media))

elif media > 5 and media < 6.9:
    print('Sua nota Foi {} Voce Esta RECUPERAÇÃO'.format(media))

else:    
    print('Sua nota Foi {} Voce Esta APROVADO!'.format(media))


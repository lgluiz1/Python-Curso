from random import randint
itens = ('PEDRA' , 'PAPEL' , 'TESOURA')
computador = randint(0,2)
print('-=' * 15)
print('ESCOLHA UMA OPÇÃO')
print('-=' * 15)
print(''' 
      DIGITE 0 PARA PEDRA
      DIGITE 1 PARA PAPEL
      DIGITE 2 PARA TESOURA
      ''')
print('-=' * 15)
jogador = int(input('DIGITE SUA OPÇÃO  '))

print('-=*' * 10)
print('''
      COMPUTADOR JOGOU {}
      JOGADOR JOGOU {}
      '''.format(itens[computador], itens[jogador]))

print('-=*' * 10)

if computador == 0 : #computador jogou pedra
    if jogador == 0 :
        print('EMPATOU!')
    elif jogador == 1 :
        print ('JOGADO VENCEU!')
    elif jogador == 2 :
        print ('COMPUTADOR VENCEU!')

elif computador == 1 : #computador jogou papel
    if jogador == 0 :
        print('COMPUTADOR VENCEU!')
    elif jogador == 1 :
        print ('EMPATE!')
    elif jogador == 2 :
        print ('JOGADOR VENCEU!')

elif computador == 2 : #computador jogou tesoura
    if jogador == 0 :
        print('JOGADOR VENCEU!')
    elif jogador == 1 :
        print ('COMPUTADOR VENCEU!')
    elif jogador == 2 :
        print ('EMPATOU!')  
else : 
    print ('OPÇÃO INVALIDA TENTE NOVAMENTE!')
#ESCREVA UM PROGRAMA Q LEIA DOIS NUMEROS INTEIROS E COMPARE-OS 
#MOSTRANDO NA TELA UMA MENSAGEM

#O PRIMEIRO VALOR É MAIOR
#O SEGUNDO VALOR É MAIOR
#NÃO EXISTE VALOR MAIOR, OS DOIS SAO IGUAIS

n1 = int(input('Digite um Numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2 :
    print('O Numero {} e maior que {}'.format(n1,n2))
elif n1 < n2 :
    print('O Numero {} e maior que {}'.format(n2,n1))
else:
    print('Não existe Valor Maior, Os dois São Iguais')
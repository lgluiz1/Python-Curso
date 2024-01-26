# ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E PEÇA PARA O
# USUARIO ESCOLHE QUAL SERA A BASE DE CONVERSÃO

#-1 PARA BINARIO
#-2 PARA OCTAL
#-3 PARA HEXADECIMAL

from bitstring import BitArray

n1 = int(input('Digite numeros para fazer conversão'))
print ('-'*35)
print ('DIGITE 1 PARA BINARIO')
print ('DIGITE 2 PARA OCTAL')
print ('DIGITE 3 PARA HEXADECIMAL')
print ('-'*35)
escolha = int(input('QUAL SERA CONVERÇÃO? 1 , 2 , 3 ?  '))
print ('='*35)

if escolha == 1 :
    conversao_binaria = BitArray(uint=n1, length=8)
    print('A CONVERSÃO DO NUMERO {} EM BINARIO E {}'.format(n1,conversao_binaria.bin))

elif escolha == 2:
    conversão_octal = oct(n1)
    print('A CONVERSÃO DO NUMERO {} EM OCTAL E {} '.format(n1,conversão_octal[2:] ))

elif escolha == 3 :
    conversão_hexa = hex(n1)
    print('A CONVERSÃO DO NUMERO {} EM HEXADECIMAL E {}'.format(n1,conversão_hexa[2:]))

else:
    print('DIGITE UMA OPÇÃO VALIDA POR FAVOR')
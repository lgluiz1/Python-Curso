# REFAÇA O DESADIO 35 DOS TRIANGULOS , ACRECENTANDO O RECURSO DE MOSTRA QUE TIPO DE TRIANGULO SERA FORMADO

# EQUILATERO: TODOS LADOS IGUAIS
# ISOSCELES: DOIS LADOS IGUAIS
# ESCALENO: TODOS OS LADOS DIFERENTES

n1 = int(input('Digite Uma Medida '))
n2 = int(input('Digite Outra Medida '))
n3 = int(input('Digite Outra Medida '))

a = n1 + n2 > n3
b = n2 + n3 > n1
c = n3 + n1 > n2

if all ([a ,b,c]) == True:
    print ('Voce consegue monta um triangulo com essas medidas')
    if n1 > n2 or n1 > n3 :
        print('VOCE VAI FROMA UM TRINGULO ISOSCELES COM 2 LADOS IGUAIS')
    elif n1 == n2 or n1 == n3:
        print('VOCE VAI FORMA UM TRINGANGULO EQUILATERO TODOS OS LADOS IGUAIS')
    elif n1 != n2 or n2 != n3:
        print('VOCE VAI FORMA UM TRIANGULO ESCALENO TODOS OS LADOS DIFERENTES')
else:
    print('VOCE NAO FORMA UM TRIANGULO COM ESSAS MEDIDAS')


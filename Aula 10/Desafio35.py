pri = int(input('Digite um numero: '))
seg = int(input('Digite outro Numero: '))
ter = int(input('Digite ultimo Numero: '))

a = pri + seg > ter 
b = pri + ter > seg
c = seg + pri > pri

if all ([a , b , c]) == True:
    print('Voce pode forma um triangulo com as medidas')
else: 
    print('Com as medidas voce nao pode forma um triangulo')
numero = int(input('Digite numero de 0 a 9999: '))
#und = numero[0]
#dez = numero[1]
#cen = numero[2]
#mil = numero[3]
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade {} \n Dezena {} \n Centena {} \n Milhar {}'.format(u , d , c , m))
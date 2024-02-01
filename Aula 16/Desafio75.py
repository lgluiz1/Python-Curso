numero =( int(input('DIGITE UM NUMERO: ')),
int(input('DIGITE MAIS UM NUMERO: ')),
int(input('DIGITE NOVAMENTE UM NUMERO: ')),
int(input('DIGITE ULTIMO NUMERO: ')))

print(f'VOCÊ DIGITOU OS VALORES {numero}')
print(f'VALOR 9 APARECEU {numero.count(9)} VEZES')
if 3 in numero:
    posição_3 = numero.index(3)
    print(f'O VALOR 3 APARECEU PELA PRIMEIVEZ NA PROSIÇÃO {posição_3+1}º')
else:
    print('O NÚMERO 3 NÃO FOI DIGITADO.')

print('OS VALORES PARES DIGITADOS FORAM ',end='')
for n in numero:
    if n % 2 == 0:
        print( n ,end=' ')

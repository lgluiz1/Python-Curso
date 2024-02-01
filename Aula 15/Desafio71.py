print('=='*15)
print('{:^30}'.format('BANCO DO LG'))
print('=='*15)

valor = int(input('QUANTO DESEJA SACAR? R$'))

cinquenta = valor // 50
resto_cin = valor % 50

vinte = resto_cin // 20
resto_vin = resto_cin % 20

dez = resto_vin // 10
resto_dez = resto_vin % 10

um = resto_dez // 1
resto_um = resto_dez % 1


if cinquenta > 0 :
    print(f'TOTAL DE {cinquenta} CÉDULAS DE R$50.00')
if vinte > 0 :
    print(f'TOTAL DE {vinte} CÉDULAS DE R$20.00')
if dez > 0:
    print(f'TOTAL DE {dez} CÉDULAS DE R$10.00')
if um > 0:
    print(f'TOTAL DE {um} CÉDULAS DE R$1.00')

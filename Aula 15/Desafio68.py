from random import randint

print('='*40)
print('VAMOS BRINDA DE PAR OU IMPAR')
print('='*40)

while True:
    escolha = str(input('VOCE ESCOLHE PAR OU IMPAR?:  ')).lower()[0].strip()
    numero = int(input('DIGITE UM NUMERO:  '))
    computador = randint(0,10)
    soma = numero + computador
    if soma % 2 == 0:
        print('=='*30)
        print(f'VOCE JOGOU {numero} E O COMPUTADOR JOGOU {computador} RESULTADO FOI {soma} E PAR')
        print('=='*30)
    else:
        print('=='*30)
        print(f'VOCE JOGOU {numero} E O COMPUTADOR JOGOU {computador} RESULTADO FOI {soma} E IMPAR')
        print('=='*30)    

    if escolha == 'p' and soma % 2 == 0:
        print('VOCE VENCEU')
        print('=='*6)
    elif escolha == 'i' and soma % 2 != 0:
        print('VOCE VENCEU')
        print('=='*6)
    else:
        print('VOCE PERDEU')
        print('=='*20)
        break
print('GAMER OVER PARA VOCE! TENTE NOVAMENTE!')
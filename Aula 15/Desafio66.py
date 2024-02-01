soma= cont= 0
while True:
    numero = int(input('DIGITE UM NUMERO OU DIGITE [999] PARA FINALIZA:  '))     
    if numero == 999:
        break
    cont +=1
    soma += numero
print(f'VOCE DIGITOU {cont} NUMEROS E A SOMA DOS VALORES DIGITADOS FOI {soma}')

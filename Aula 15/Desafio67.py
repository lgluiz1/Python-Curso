from time import sleep

while True:
    numero = int(input('DIGITE UM VALOR A PARA CALCULAR:  '))
    if numero <= 0 :
        break
    
    for n in range(1,11):
        tabuada = numero * n
        print(f'{numero} X {n} = {tabuada}')
print('FINALIZANDO...')
sleep(2)
print('CALCULADORA FECHADA')
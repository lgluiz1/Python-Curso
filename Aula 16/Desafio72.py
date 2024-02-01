numeros = ('zero','um','dois','trez','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte') 
# Criando uma nova tupla com strings em maiúsculas
tupla_maiuscula = tuple(s.upper() for s in numeros)
valor = None
while valor not in range(0, 20):
    valor = int(input('DIGITE UM VALOR ENTRE 0 A 20: '))    
    if valor in range(0,21):
        print(f'VOCÊ DIGITOU O VALOR {tupla_maiuscula[valor]}')
        break
    else:
        print('VALOR FORA DA FAIXA PERMITIDA TENTE NOVAMENTE! ')
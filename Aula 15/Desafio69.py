contador_idade = homens = mulher = 0

while True:
    idade = int(input('DIGITE A IDADE: '))
    if idade > 18 :
        contador_idade += 1

    sexo = ''
    while sexo != 'f' and sexo != 'm':
        sexo = str(input('DIGITE SEXO F/M: ')).lower()[0].strip()
        if sexo == 'm':
            homens +=1

        if sexo == 'f' and idade < 20:
            mulher += 1

    continua = ''
    while continua != 'n' and continua != 's':
        continua = str(input('DESEJA CONTINUAR? S/N: ')).lower()[0].strip()    

    if continua == 'n':
        break


print(f'O TOTAL DE PESSOAS COM MAIS DE 18 ANOS E {contador_idade}')
print(f'AO TODOS TIVEMOS {homens} HOMENS CADASTRADOS')
print(f'E TEMOS {mulher} MULHERES COM MENOS DE 20 ANOS')    
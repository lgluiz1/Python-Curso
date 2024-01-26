#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELE E UM PALINDROMO
#DESCONSIDERANDO OS ESPAÇOS
frase = str(input('Frase ')).upper()
rfrase = frase.replace(' ' , '')
palavra = ''.join(rfrase[::-1])

print (palavra)

if rfrase == palavra :
    print('A FRASE {} LIDA DE TRAZ PRA FRENTE E {}'.format(frase,palavra))
    print('A FRASE E PALINDROMO ')
else:
    print('A FRASE {} LIDA DE TRAZ PARA FRENTE E {}'.format(frase,palavra))
    print('A FRASE NAO E PALINDROMO ')
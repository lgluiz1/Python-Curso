import random

a1 = input('Primeiro Aluno')
a2 = input('Segundo aluno')
a3 = input('Terceiro Aluno')
a4 = input('Quarto Aluno')
lista = [ a1,a2,a3,a4]


print ('Aluno escolhido Foi {}'.format(random.choice(lista)))
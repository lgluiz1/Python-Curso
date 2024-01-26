frase = str(input('Digite Uma Frase!')).strip()

a = frase.lower().count('a')
p = frase.lower().find('a')+1
u = frase.lower().rfind('a')+1

print('A letra A Aparece {} No Seu Texto a Primeira Fez e Na Posição {} e a Ultima Vez e na Posição {}'.format(a , p , u))
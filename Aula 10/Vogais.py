#Contar a quantidade de vogais em uma palavra: Desenvolva uma função que 
#receba uma palavra como entrada e retorne a quantidade de vogais presentes na palavra.

pa = str(input('Digite Palavra')).lower()

a = pa.count('a')
e = pa.count('e')
i = pa.count('i')
o = pa.count('o')
u = pa.count('u')

print ('A Palavra {} Tem {} Letas A'.format(pa,a))
print ('A Palavra {} Tem {} Letas E'.format(pa,e))
print ('A Palavra {} Tem {} Letas I'.format(pa,i))
print ('A Palavra {} Tem {} Letas O'.format(pa,o))
print ('A Palavra {} Tem {} Letas U'.format(pa,u))
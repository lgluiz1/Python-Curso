import math

angulo = float(input('Digite o angulo'))

se = math.sin(math.radians(angulo))
co = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print ('o Angulo {} \n Seno de {:.2f} \n Cosseno de {:.2f} \n e Tangente de {:.2f}'.format(angulo , se , co ,tan))
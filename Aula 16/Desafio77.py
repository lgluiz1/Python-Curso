palavras = ('aprender','jogar','apanha','bater','correr','capina','varrer','lavar','estudar','python','javascript','programar')
for c in palavras:
    print (f'\nNa {c.upper()} Temos',end=' ')
    for vogais in c:
        if vogais.lower() in 'aeiou':
            print(vogais,end=' ')

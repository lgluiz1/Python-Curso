km = int(input('Quantos KM Foi rodado?'))
dia = int(input('Quantos dias foram Alugado?'))
r1=km*0.15
r2=dia*60

print('O total a paga e de R${:.2f}'.format(r1+r2))
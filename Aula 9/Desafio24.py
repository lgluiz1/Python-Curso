cidade = str(input('Qual Sua cidade?')).strip()
primeiro = cidade.split()[0]
res = 'santos' in primeiro.lower()

print (res)
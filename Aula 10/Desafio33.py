nu = input('Digite 3 Numeros ').split()
res = [int(num) for num in nu]
es = ' '.join(str(num) for num in res)
maior = max(es)
menor = min(es)

print (maior)
print (menor)

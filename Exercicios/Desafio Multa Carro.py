veloc = int(input('A quanto Kmh o veiculo passou?'))
multa = float(input('Qual valor da multa por Km?R$'))
calcu = veloc * multa

print ('O Carro Passou a {}kmh por isso vai recebe uma multa de R${:.2f}'.format(veloc, calcu))
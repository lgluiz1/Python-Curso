medida = float(input('Digite uma medida'))
cm= medida*100
mm= medida*1000
km= medida/1000
hm= medida/100
dam= medida/10

print('{:.0f}m Tem {:.0f}cm, {:.0f}mm, {:.0f}dm, {}hm, {}km'.format(medida,cm,mm,dam,hm,km))
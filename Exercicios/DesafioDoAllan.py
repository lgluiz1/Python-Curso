from time import localtime , sleep

while True:
    data = localtime()
    hora = data.tm_hour
    minuto = data.tm_min
    segundos = data.tm_sec
    dia = data.tm_mday
    mes = data.tm_mon
    ano = data.tm_year

    if hora < 6 :
        print('BOA NOITE ALLAN AGORA SÃO {}:{}:{} DO DIA {}/{}/{}'.format(hora,minuto,segundos,dia,mes,ano))
    elif hora < 12:
        print(' BOM DIA ALLAN SÃO {}:{}:{} DO DIA {}/{}/{}'.format(hora,minuto,segundos,dia,mes,ano))
    elif hora < 18:
        print('BOA TARDE ALLAN SÃO {}:{}:{} DO DIA {}/{}/{}'.format(hora,minuto,segundos,dia,mes,ano))
    else:
        print('BOA NOITE ALLAN SÃO {}:{}:{} DO DIA {}/{}/{}'.format(hora,minuto,segundos,dia,mes,ano))

    sleep(60)
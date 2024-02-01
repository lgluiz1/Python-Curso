times = ('Athletico','Atlético-GO','Atlético-MG','Bahia','Botafogo','Bragantino','Corinthians','Criciúma' ,'Cruzeiro','Cuiabá',
'Flamengo','Fluminense','Fortaleza','Grêmio','Internacional','Juventude' ,'Palmeiras','São Paulo','Vasco','Vitória',)
alfabetica = tuple(sorted(times))
while True:
    print('=='*20)
    print(f'Lista de times Brasileiro 2024: {times}')
    print('=='*20)
    print(f'Os 5º Primeiros São {times[:5]}')
    print('=='*20)
    print(f'Os Ultimos 4º São {times[-4:]}')
    print('=='*20)
    print(f'Em Ordem Alfabetica {alfabetica}')
    print('=='*20)
    if 'Criciúma' in times:
        posição = times.index('Criciúma')
        print(f'O Criciúma esta na {posição}º da tabela')
        print('=='*20)
    break
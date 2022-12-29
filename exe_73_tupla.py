'''
crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

a) os 05 primeiros ok
b)os ultimos 04 colocados ok
c) time em ordem alfabetica ok
d) Em que posição está o time do Fortaleza ok
'''
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias', 'Flamengo', 'Atletico - PR', 'Atletico MG', 'Fortaleza', 'São Paulo','América mineiro', 'Botafogo', 'Santos', 'Góias', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico - GO ', 'Avaí', 'Juventude')

fortaleza = times.index('Fortaleza')
print('-='*15)
print(f'Os times em ordem alfabetica são {sorted(times)}')
print('-='*15)
print(f'Os 05 Primeiros colocados são: {times[0:5]}',)
print('-='*15)
print(f'Os últimos 04 colocados são {times[-4:]}')
print('-='*15)
print(f'O time do Fortaleza Ficou na {fortaleza}')
print('-='*15)

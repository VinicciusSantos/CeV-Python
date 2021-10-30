# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# A) Os 5 primeiros.
# B) Os últimos 4 colocados.
# C) Times em ordem alfabética.
# D) Em que posição está o time da Chapecoense.

times = ("Flamengo", "Palmeiras", "Atletico Mineiro", "Grêmio", "São Paulo", "Corinthians", "Bragantino", "Internacional", "Santos", 
"Atletico Paranaense", "Fluminense", "Bahia", "Fortaleza", "Atletico Goianiense", "Cuiabá", "Ceará", "Atletico Mineiro", "Sport",
"Juventude", "Chapecoense")

print('-=-' * 20)
print('Lista de times do Brasileirão')
print('-=-' * 20)
print(f'Os 5 primeiros são {times[0:5]}')
print('-' * 60)
print(f'Os 4 últimos são {times[-4:]}')
print('-' * 60)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-' * 60)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-' * 60)

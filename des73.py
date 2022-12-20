#Crie uma tupla preenchida com os 20 primeiros colocados da tabela
#do campeonato brasileiro de futebol na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados
#B) Os últimos 4 colocados da tabela
#C) Uma lista com os times em ordem alfabética
#D) Em que posição na tabela está o time da chapecoense.

time = ('Palmeiras', "Internacional", 'Flamengo', 'Fluminese', 'Corínthians', 'Athletico-PR', 'Athletico-MG', 'Chapecoense')
print(f'lista de times: {time}')
print(f'os cinco primeiros são {time[0:5]}')
print(f'os 4 últimos colocaasddos são {time[2:6]}')
print(f'os times em ordem alfabética são {sorted(time)}')
print(f'o time da chapecó está em {time}')
print(f'a chapeco ta na {time.index("Chapecoense")} posição')
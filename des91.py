#um programa onde 4 jogadores jogam um dado e têm resultados aleatórios
#guardar resultados em um dicionário
#colocar dicionário em ordem
#o vencedor é quem tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter
resultados = {'jogador1': randint(1,6),
              'jogador2': randint(1,6),
              'jogador3': randint(1,6),
              'jogador4': randint(1,6)}
ranking = list()

print('Valores sorteados:')
for chave, valor in resultados.items():
    print(f'o {chave} sorteou {valor} no dado')
    sleep(0.5)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('-='*30)
for i,v in enumerate(ranking):
    print(f'{i+1}o lugar: {v[0]} com {v[1]}')
    sleep(0.5)


dicionario = {}


dicionario['jogador'] = str(input('Digite o nome do jogador: ')).title()
partidas = int(input(f'Quantas partidas {dicionario["jogador"]} jogou? '))
total = 0
lista = []
for gols in range(0,partidas):
    gols  = int(input(f'Quantos gols na partida {gols}? '))
    lista += [gols]
    total += gols
    dicionario['gols'] = lista[:]
    dicionario['total'] = total
print("-="*30)
print(dicionario)
print('-='*30)

for k, v in dicionario.items():
    print(f'O campo {k} tem valor {v}')

print('-='*30)

print(f'O jogador {dicionario["jogador"]} jogou {partidas} partidas.')
for a,z in enumerate(lista):
    print(f' => Na partida {a}, fez {z} gols')
print(f'Foi um total de {total} gols.')




#ler nome do jogador e quantas partidas ele jogou
#ler quantidade de gols feitos em cada partida
#guardar tudo em um dicionario
#incluindo total de gols

dicionario = {}
lista_dados = []
r = 'S'
while True:
    dicionario['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input('Número de partidas jogadas: '))

    lista = []
    total_gols = 0
    for gols in range(0,partidas):
        gols = int(input(f'  Quantos gols na partida {gols}? '))
        total_gols += gols
        lista += [gols]
        dicionario['gols'] = lista[:]
        dicionario['total'] = total_gols
    lista_dados += [dicionario.copy()]
    r = str(input('Quer continuar? [S/N] ')).upper()
    while r not in 'SN':
        r = str(input('Comando inválido! Digite [S/N]: '))
    if r == 'N':
        break


print('-='*40)
print()
print('cod', end=' ')
for i in dicionario.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k,v in enumerate(lista_dados):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end =' ')
    print()
print('-'*40)

while True:
    busca = int(input('Digite o codigo do jogador que você esá buscando (999 para parar) : '))
    if busca == 999:
        break
    if busca >= len(lista_dados):
        print('ERRO! O jogador buscado não existe!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista_dados[busca]["nome"]}:')
        for jogo,gol in enumerate(lista_dados[busca]['gols']):
            print(f'No jogo {jogo} fez {gol} gols.')


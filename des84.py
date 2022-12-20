#um programa que leia nome e peso de varias pessoas
#guardando tudo em uma lista. No fim mostre:
# A) Quantas pessoas foram cadastradas
# B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS
# C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES

lista = []
dados = []
total_de_pessoas = 0
maior_peso = menor_peso = 0
r = 'S'

while r == 'S':
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(int(input('Digite o peso da pessoa: ')))
    total_de_pessoas += 1
    if len(lista) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados [1] < menor_peso:
            menor_peso = dados[1]

    r = str(input('Gostaria de adicionar mais dados? [S/N]: ')).upper()
    lista.append(dados[:])
    dados.clear()

    while r not in 'SN':
        r = str(input('Comando inválido. Por favor, digite [S/N]: ')).upper()
        if r == 'N':
            break

print('-='*30)
for pessoa in lista:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]} é a pessoa mais pesada com {maior_peso} Kg')
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]} é a pessoa mais leve com {menor_peso} Kg')

print(f'{total_de_pessoas} pessoas foram cadastradas')




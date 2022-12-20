#um programa que leia nome e peso de varias pessoas
#guardando tudo em uma lista. No fim mostre:
# A) Quantas pessoas foram cadastradas
# B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS
# C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES

lista =[]
dados = []
r = 'S'
maior_peso = menor_peso = 0

while True:
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))
    if len(lista) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            dados[1] == maior_peso
        if dados[1] < menor_peso:
            dados[1] = menor_peso
    lista.append(dados[:])
    dados.clear()

    r = str(input('você gostaria de continuar adicionando dados? [S/N]: ')).upper()
    while r not in 'SN':
        r = str(input('Comando inválido! Por favor, digite S ou N: ')).upper()
        if r == 'N':
            break

print('-='*30)
for pessoa in lista:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]} é a pessoa mais pesada, pesando {maior_peso} Kg')
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]} é a pessoa mais leve, pesando {menor_peso} Kg')
print(f'{len(lista)} pessoas foram cadastradas.')
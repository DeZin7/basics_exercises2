#um programa q digite varios valores numericos e cadastre-os em lista.
#caso o numero ja exista la dentro, nao sera adicionado. no final serao
#exibidos todos os valores unicos digitados em ordem crescente

lista =[]
d = "S"

while d == 'S':
    r = int(input('digite um valor: '))
    d = str(input('gostaria de digitar outro valor? [S/N]: ')).upper()
    if r not in lista:
        lista += [r]
    while d not in 'SN':
        d = str(input('nao entendi, digite [S/N]: ')).upper()
        if d == 'N':
            break

print(sorted(lista))

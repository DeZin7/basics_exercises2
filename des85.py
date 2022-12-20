#digitar 7 valores
#cdastrar em uma lista unica
#manter separado os valores pares e impares
#no final mostrar valores pares e impares em ordem crescente

lista = [[],[]]
valor = 0

for c in range (0,7):
    valor = int(input('digite um valor: '))
    if valor %2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f'os valores pares foram: {sorted(lista[0])}')
print(f'os valores ímpares foram: {sorted(lista[1])}')

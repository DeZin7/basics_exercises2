#um programa que leia 5 valores numericos e guarde-os
#em uma lista. No final, mostre qual foi o maior e o menor
#valor digitado e as suas respectivas posições na lista

lista = []

for r in range(0,5):
    r = int(input('digite um número: '))
    lista += [r]

print(lista)
print(f'o maior valor foi {max(lista)}')
print(f'o menor valor foi {min(lista)}')

for pos, num in enumerate (lista):
    print(f'o numero {num} está na posição {pos}')


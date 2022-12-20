#programa q leia 5 valores e guarde-os em uma lista.
#no final mostre qual foi o maior e o menor valor digitado
#e suas respectivas posições na lista

lista = []
for valor in range(0,5):
    lista.append(int(input('digite o valor: ')))


a = max(lista)
b = min(lista)
print(lista)
print(f'o maior elemento {a} está na posição {lista.index(a)}')
print(f'o menor elemento {b} está na posição {lista.index(b)}')

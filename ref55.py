#programa que leia o peso de cinco pessoas
#no final mostre qual foi o maior e o menor peso lido
lista = []
for pessoa in range(1,6):
    peso = float(input(f'digite o peso da pessoa {pessoa}: '))
    lista += [peso]
print(f'o maior peso lido foi {max(lista)}')
print(f'o menor peso lido foi {min(lista)}')


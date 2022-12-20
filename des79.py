#um programa onde o usuario possa digitar varios valores
#numericos e cadastre-os em uma lista. Caso o numero ja exista
#la dentro, ele nao sera adicionado. No fina, serao exibidos
#todos os valores unicos digitados em ordem crescente.

lista = []

for r in range(0,5):
    r = int(input('digite um numero: '))
    if r not in lista:
        lista += [r]
print(lista)
print(f'valores em ordem crescente: {sorted(lista)}')
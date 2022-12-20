#um programa que vai ler varios numeros e coloca-los em uma lista
#criar duas listas extras que irão conter apenas os valores pares
#e os valores ímpares
#ao final mostre o conteudo das três listas geradas

lista = []
lista_pares = []
lista_impares = []
r = 'S'

while r == 'S':
    numeros = int(input('digite o valor a ser adicionado na lista: '))
    r = str(input('deseja adicionar mais numeros? [S/N]: ')).upper()
    lista += [numeros]
    if numeros %2 == 0:
        lista_pares += [numeros]
    else:
        lista_impares += [numeros]

    while r not in 'SN':
        r = str(input('por favor digite [S/N]: ')).upper()
        if r == 'N':
            break

print('-='*40)
print(f'os valores pares digitados foram {lista_pares}')
print(f'os valores ìmpares digitados foram {lista_impares}')
print(f'ao todo os valores digitados foram {lista}')
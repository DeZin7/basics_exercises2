#um programa q leia varios numeros e coloque-os em uma lista
#dps criar duas listas q vao armazenar apaenas valores pares ou aenas valores impares
#ao final mostrar as 3 listas

lista = []
lista_impares = []
lista_pares = []

while True:
    numeros = int(input('digite o numero: '))
    lista +=[numeros]
    if numeros == 0:
        break
    if numeros % 2 != 0:
        lista_impares += [numeros]
    elif numeros % 2 == 0:
        lista_pares += [numeros]

print(lista)
print(lista_pares)
print(lista_impares)
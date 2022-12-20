#um programa q vai ler varios numeros e colocar em uma lista.
#MOSTRE:
#A) QUANTOS NUMEROS FORAM DIGITADOS.
#B) A LISTA DE VALORES ORDENADA DE FORMA DECRESCENTE
#C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA

lista = []

while True:
    r = int(input('digite um numero: '))
    if r != -1:
        lista += [r]
    if r == -1:
        break

print(f' a lista possui {len(lista)} elementos')
print(lista[::-1])
if 5 in lista:
    print('o 5 foi digitado')
elif 5 not in lista:
    print('o 5 não foi digitado')

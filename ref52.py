#um programa que leia um numero inteiro e diga se ele é
#ou não um número primo
a = int(input('digite um numero: '))
cont = 0
for c in range (1, a+1):
    if a%c == 0:
        cont += 1
if cont == 2:
    print(f'{a} é um número primo. foi dividido {cont} vezes')
else:
    print(f'{a} não é um número primo. foi dividido {cont} vezes')

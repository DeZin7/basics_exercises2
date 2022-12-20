#um programa que leia quatro valores pelo teclado
#guarde os valores em uma tupla. No final mostre:
# A) quantas vzs apareceu o valor 9
# B) em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares.

x = (int(input('numero 1:')),int(input('numero 1:')),int(input('numero 1:')),int(input('numero 1:')),int(input('numero 1:')))
print(f'números digitados: ({x})')
print(f'o nove apareceu {x.count(9)} vezes')
if 3 in x:
    print(f'o primeiro valor 3 foi digitado na posição {x.index(3)}')
else:
    print(f'o 3 não apareceu')
print('os numeros pares digitados foram ' ,end='')
for n in x:
    if n % 2 ==0:
        print(n, end =' ')

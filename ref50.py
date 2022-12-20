#um programa que leia seis números inteiros e mostre a soma
#apenas daqueles que forem pares. Se o valor digitado for ímpar
#desconsidere-o
soma = 0
for n in range (1,7):
    n = int(input('digite um número: '))
    if n%2 == 0:
        soma += n
print(f'a soma dos números pares é {soma}')

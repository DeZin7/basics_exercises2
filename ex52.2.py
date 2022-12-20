#faça um programa q leia um numero inteiro e diga se ele é primo

num = int(input('digite um numero: '))
cont = 0
for n in range(1, num+1):
    if num % n == 0:
        cont = cont + 1
if cont == 2:
    print(f'o numero é primo. foi divido apenas {cont} vzs')
else:
    print(f'o numero não é primo. foi dividido {cont} vzs')

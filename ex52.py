n = int(input('digite um numero: '))
cont = 0
for c in range (1 , n+1):
    if n % c == 0:
        cont = cont + 1
if cont == 2:
    print(f'o numero é primo. foi divido {cont} vezes')
else:
    print(f'o numero nao é primo. foi dividido {cont} vezes')

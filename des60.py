#um programa que leia um número qualquer e mostre seu fatorial

n = int(input('digite um numero: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1
print(f'{f}')



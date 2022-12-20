#um programa que simule o funcionamento de um caixa eletroônico
#pergunte o valor a ser sacado e o programa informará quantas
#cédulas de cada valor serão entregues

c = int(input('quanto vc quer sacar? '))
total = c
n50 = n20 = n10 = n1 = 0
while True:
    while total >= 50:
        total -= 50
        n50 += 1
    while total >= 20:
        total -= 20
        n20 += 1
    while total >= 10:
        total -= 10
        n10 += 1
    while total >= 1:
        total -= 1
        n1 += 1
    if total == 0:
        if n50 > 0:
            print(f'{n50} notas de 50')
        if n20 > 0:
            print(f'{n20} notas de 20')
        if n10 > 0:
            print(f'{n10} nota de 10')
        if n1 > 0:
            print(f'{n1} notas de 1')
        break
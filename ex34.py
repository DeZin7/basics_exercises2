n = float(input('qual seu salário? '))
n1 = n + (0.1 * n)
n2 = n + (0.15 * n)

if n>1250:
    print(f'o salario será {n1:.2f}. o aumento sera de {(0.1*n):.2f}')

if n<=1250:
    print(f'o salario sera {n2:.2}. o aumento sera de {(0.15*n):.2f}')

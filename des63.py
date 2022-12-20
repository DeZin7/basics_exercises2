#um programa que leia um numero N inteiro qualquer e mostre na tela os n primeiros
#elementos de uma sequência de Fibonacci

# 0 → 1 → 1 → 2 → 3 → 5 → 8 → (...)
#         t1+t2=t3

n = int(input('digite quantos termos quer mostrar na sequencia de Fibonacci: '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end =' → ')
cont = 3
while cont <= n:
    t3 =(t2 + t1)
    t1 = t2
    t2 = t3
    cont += 1
    print(f'{t3}', end =' → ')
print('fim')
#desenvola um programa que leia o primeiro termo e a razão de uma PA
#No final, mostre os 10 primeiros termos dessa progressão.

a = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razão da PA: '))
n = a + (10*r)

for p in range (a,n,r):
    print(p,end=' → ')
print('PEEEIII!!!')
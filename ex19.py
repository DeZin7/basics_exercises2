n = str(input('digite um numero de 0 a 9999: '))
n1 = n[0:4]
print(f'como é de 0 a 9999, os digitos a mais serão desconsiderados e portando consideraremos somente os 4 primeiros digitos {n1}')
p = ' '.join(n1)
d = p.split()

a = d[3]
b = d[2]
c = d[1]
d = d[0]

print(f'unidade: {a}')
print(f'dezena: {b}')
print(f'centena: {c}')
print(f'milhar: {d}')

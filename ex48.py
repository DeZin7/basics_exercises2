soma = 0
for n in range(1,500):
    if (n%3) == 0 and (n%2) != 0:
        soma = soma + n
print(f'a soma dos valores é {soma}')
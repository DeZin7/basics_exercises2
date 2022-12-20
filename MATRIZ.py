import numpy as np

nl = int(input('Informe o número de linhas: '))
nc = int(input('Informe o número de colunas: '))

A = np.empty((nl,nc))

for i in range(0, nl):
    for j in range(0, nc):
        s = float(input(f'Informe o elemento {A[i][j]}:  '))
        A[i][j] = s

print("Imprime matriz...")
for i in range(0,nl):
    for j in range(0,nc):
        print(f'{A[i][j]:5.1f}', end='')
    print()
print()
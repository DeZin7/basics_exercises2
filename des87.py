#uma matriz 3x3 preenchida com valores lidos pelo teclado.
#mostrar matriz na tela com formatação correta
# A) A soma de todos os valores pares digitados
# B) A soma de todos os valores da terceira coluna
# C) O maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_valores_pares = 0
soma_valores_terceira_coluna = 0
valores_linha2 =[]



for linha in range (0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] %2 == 0:
            soma_valores_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_valores_terceira_coluna += matriz[linha][coluna]
        if linha == 2:
            valores_linha2 += [matriz[2][coluna]]


print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^4}]', end='')
    print()

print('-='*30)
print(f'a soma dos valores pares digitados é {soma_valores_pares}')
print(f'a soma dos valores da terceira coluna é {soma_valores_terceira_coluna}')
print(f'o maior valor da segunda linha é {max(valores_linha2)}')


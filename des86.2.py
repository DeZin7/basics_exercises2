#uma matriz 3x3 preenchida com valores lidos pelo teclado.
#mostrar matriz na tela com formatação correta

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha][coluna] = int(input(f'digite um valor para [{linha}, {coluna}]: '))
print("="*40)
for linha in range (0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
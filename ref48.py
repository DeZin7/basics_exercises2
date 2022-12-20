#calcule a soma entre todos os numeros impares que são
#multiplos de 3 e se encontram no intervalo de 1 até 500
soma = 0
for c in range (1, 501):
    if c%2 != 0 and c%3 == 0:
        soma += c
        print(c, end =' → ')
print(f'a soma dos números é {soma}')
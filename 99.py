def maior(*num):
    contador = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                valor = maior
        contador += 1

    print(f'\n{contador} valores foram passados. ')
    print(f'O maior valor passado foi {maior}')
    print('-='*40)


#programa principal
maior(9, 8, 5, 2, 1)
maior(50, 42, 13)
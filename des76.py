print('-'*50)
print(f'{"TABACARIA DO DEZIN":^50}')
print('-'*50)

lista = ('Tabaco de vea', 2.50,
        'Tabaco do buda', 3.75,
        'Tabaco de fresco', 1.99,
        'Piroca comestível', 4.50,
         'Caneco do Bacon', 3.00)
for pos in range(0, len(lista)):
    if pos %2 == 0:
        print(f'{lista[pos]:.<30}',end = '')
    else:
        print(f'R${lista[pos]:>5.2f}')
print('-'*50)


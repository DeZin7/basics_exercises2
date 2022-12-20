#um programa que vai ler vários números e colocar em uma lista.
# A) Quantos números foram digitados
# B) A lista de valores ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista


r = 'S'
lista =[]
while r == 'S':
    d = int(input('digite um valor: '))
    r = str(input('gostaria de continuar adicionando valores? [S/N]: ')).upper()
    lista += [d]
    while r not in 'SN':
        r = str(input('por favor, digite [S/N]: ')).upper()
        if r == 'N':
            break


print('-='*30)
print(f'{len(lista)} números foram digitados')
print(f'{sorted(lista, reverse=True)} é a lista em ordem decrescente')

if 5 in lista:
    print('o valor 5 foi digitado')
else:
    print('o valor 5 não foi digitado')
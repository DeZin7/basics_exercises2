#crie um programa que leia o nome e o preço de vários produtos. O
#programa deverá perguntas se o usuário vai continuar. No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000
# C) Qual é o nome do produto mais barato

cont = 0
soma = 0
menor_preço = 0
barato = ''
lista_mais_mil = []
lista_preço = []

while True:
    n = str(input('digite o nome do produto: '))
    p = float(input('digite o preço do produto: '))
    op = str(input('vc deseja continuar [S/N]: ')).strip().upper()
    cont += 1
    if cont == 1:
        menor_preço = p
        barato = n
    else:
        if p < menor_preço:
            menor_preço = p
            barato = n
    if p > 1000:
        lista_mais_mil += [p]
    soma += p
    if op == 'N':
        break
    print('='*40)
print(f'{len(lista_mais_mil)} produtos custam mais de 1000 reais')
print(f'{soma:.2f} reais é o total gasto na compra')
print(f'{barato} é o mais barato')
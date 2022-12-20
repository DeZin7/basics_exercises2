#crie um programa que leia vários números inteiros pelo teclado. No final
#da execução mostre a MÉDIA entre todos os valors e qual foi o maior e o menor
#valores lidos. O programa deve perguntar ao usuário se quer ou não continuar
#a digitar valores

soma = 0
cont = 0
r = 'S'
lista = []
while r == 'S':
    n = int(input('digite um número: '))
    cont += 1
    soma += n
    lista += [n]
    r = str(input('você quer continuar a digitar valores [S/N]: ')).strip().upper()
print(f'você digitou {cont} números')
print(f'a média entre todos os valores é {soma / cont}')
print(f'o maior valor digitado foi {(max(lista))}')
print(f'o menor valor digitado foi {(min(lista))}')
#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
#quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos
#números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

cont = -1
soma = 0
n = 0
while n != 999:
    n = int(input('digite um numero para somar com o anterior: '))
    cont += 1
    soma = soma + n
print(f'a soma entre os numeros é {soma - 999}. Foram digitados {cont} números.')
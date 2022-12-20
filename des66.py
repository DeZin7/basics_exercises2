#um programa que leia vários números inteiros pelo teclado. O programa só
#vai parar quando o usuário digitar 999 (condição final de parada). No final
#mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

soma = 0
cont = 0
while True:
    n = int(input('digite um numero inteiro [999 caso vc queira parar o processo]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'a soma dos {cont} números digitados foi {soma}')

#Um programa que jogue par ou ímpar com o computador. O jogo só será
#interrompido quando o jogador perder, mostrando o total de vitórias
#consecutivas que ele conquistou no final do jogo.

import random


cont = 0
while True:

    n = str(input('PAR ou ÍMPAR? ')).strip().upper()
    computador = random.randrange(0,11)
    pessoa = int(input('digite o número: '))
    soma = computador + pessoa
    print(f'{computador} + {pessoa} = {soma}')
    cont +=1

    if n == 'PAR' and soma%2 == 0:
        print('show vc acertou')
    elif n == 'PAR' and soma%2 !=0:
        print('vc errou')
        break
    elif n == 'IMPAR' and soma%2 ==0:
        print('vc errou')
        break
    else:
        print('vc acertou')
print('='*40)
print(f'vc obteve {cont} vitórias consecutivas')

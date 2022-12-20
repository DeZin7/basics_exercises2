#computador vai pensar em um numero entre 0 e 10
#jogador vai tentar adivinhar até acertar
#mostrando no final quantos palpites foram necessários

import random
pc = random.randrange(0,10)
jogador = int(input('digite um número aleatório entre 0 e 10: '))

cont = 1
while jogador != pc:
    jogador = int(input('você errou, tente novamente: '))
    cont += 1
print('='*20)
print(f'finalmente você acertou após {cont} tentativas.')

from random import randint
from time import sleep
opt = ['pedra', 'papel', 'tesoura']
pc = randint(0,2)
print('''faça sua escolha:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] tesoura''')

player = int(input('qual sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')


if player == 1 and pc == 0:
    print('empate')
elif player == 1 and pc == 1:
    print('vc perdeu e o pc venceu')
elif player == 1 and pc == 2:
    print('vc venceu')
elif player == 2 and pc == 0:
    print('vc venceu')
elif player == 2 and pc == 1:
    print('empate')
elif player == 2 and pc == 2:
    print('vc perdeu')
elif player == 3 and pc == 0:
    print('vc perdeu')
elif player == 3 and pc == 1:
    print('vc ganhou')
elif player == 3 and pc == 2:
    print('empate')
print('='*40)
print('flw, otário')
print(f'o pc escolheu {opt[pc]}')


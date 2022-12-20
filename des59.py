#um programa que leia dois valores e mostre um meno na tela
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
from time import sleep
n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
print('-'*40)

cmd = 0
while  cmd != 5:
    cmd = int(input('''Qual operação deseja realizar:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    >>>>>> Digite aqui a opção escolhida: '''))
    if cmd == 1:
        print(f'a soma é {n1} + {n2} = {n1+n2}')

    elif cmd == 2:
        print(f'o produto é {n1} x {n2} = {n1*n2}')

    elif cmd == 3:
        if n1 > n2:
            print(f'{n1} > {n2}')
        else:
            print(f'{n2} > {n1}')

    elif cmd == 4:
        n1 = int(input('digite o primeiro numero: '))
        n2 = int(input('digite o segundo numero: '))

    elif cmd == 5:
        print('finalizando...')

    print('='*50)
    sleep(2)

#um programa que tenha a função contador() e receba 3 parametros
#início, fim e passo.
#realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo =1
    if inicio < fim:
        cont = inicio-passo
        while cont <= fim-passo:
            cont += passo
            print(f'{cont}', end=' → ')
            sleep(0.5)
        print('fim!')

    if inicio > fim:
        cont = inicio+passo
        while cont >= fim+passo:
            cont -= passo
            print(f'{cont}', end=' → ')
            sleep(0.5)
        print('fim!')

print(f' A) ', end='')
{contador(1, 10, 1)}
print(f' B) ', end='')
{contador(10, 0, 2)}
print('-'*50)
print(' C) AGORA É SUA VEZ: ')
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
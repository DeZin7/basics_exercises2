#melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns
#termos. O programa encerra quando ele disser que mostrar 0 termos.

#criando programa que mostre os 10 primeiros termos de uma PA

p = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razão da PA:'))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end = ' → ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Gostaria de mostrar mais quantos termos? '))
print(f'{total} termos mostrados')
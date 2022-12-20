#refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando
#os 10 primeiros termos da progressão usando a estrutrura while

p = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razãp da pa: '))

termo = p
cont = 0
while cont < 10:
    print(f'{termo}', end = ' → ')
    termo += r
    cont += 1
print('pausa')


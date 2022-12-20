#crie um programa que vai gerar cinco números aleatórios e colocar em
#um tupla.
#Mostre a listagem de números gerados e também indique o menor e maior
#valor que estão na tupla

from random import randint
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(tupla)
c = sorted(tupla)
print(f'o menor valor é {c[0]}')
print(f'o maior valor é {c[-1]}')

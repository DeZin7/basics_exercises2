#Quantos jogos serão gerados
#Sortear 6 números entre 1 e 60
#guardar tudo em uma lista composta

from time import sleep
from random import randint
lista_temporaria = []
jogos =[]

quantidade_de_jogos = int(input('Digite quantos jogos deseja sortear: '))
contador_qtd_jogos = 1
while contador_qtd_jogos <= quantidade_de_jogos:
    contador_numeros = 0
    while True:
        palpites = randint(1,61)
        if palpites not in lista_temporaria:
            lista_temporaria.append(palpites)
            contador_numeros += 1
        if contador_numeros >= 6:
            break
    lista_temporaria.sort()

    jogos.append(lista_temporaria[:])
    lista_temporaria.clear()
    contador_qtd_jogos += 1

print('-='*20)
print('     BOA SORTE!     ')
print('-='*20)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)





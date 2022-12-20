from random import randint

def sorteia(numeros):

    for n in range(0,5):
        valores = randint(0,20)
        numeros += [valores]
    print(numeros)

def somaPar(numeros):

    somador = 0
    for par in numeros:
        if par%2 == 0:
            somador += par
    print(f'a soma dos valores pares de ({numeros}) é {somador}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)








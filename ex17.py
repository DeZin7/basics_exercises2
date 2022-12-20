import random
n1 = str(input('digite um nome: '))
n2 = str(input('digite outro nome: '))
n3 = str (input('mais oto: '))
n4 = str(input('mais oto please: '))
lista = [n1, n2, n3, n4]
f = random.choice(lista)
print(f'o escolhido foi {f}')



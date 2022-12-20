import random
a1 = str(input('digite o nome do aluno 1: '))
a2 = str(input('digite o nome do aluno 2: '))
a3 = str(input('digite o nome do aluno 3: '))
a4 = str(input('digite o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
f = random.sample(lista, k=4)
print(f'a ordem dos lixo escolhido foi {f}!')

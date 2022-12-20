n = str(input('digite um nome e vejamos se tem Silva no nome: ')).strip().title()
d = n.split()
print(d)
print('Silva' in d)
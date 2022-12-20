n = str(input('digite uma frase: ')).replace('à','a').replace('á','a').replace('ã','a').replace('â','a').strip().upper()
h = (n.count('A'))
p = (n.find('A'))
u = (n.rfind('A'))
print(f'a frase possui {(n.__len__())} caracteres')

print(f'a letra A aparece {h} vezes')
print(f'a letra A é encontrada pela primeira vez na posição {p}')
print(f'a letra A é encontrada pela última vez na posição {u}')
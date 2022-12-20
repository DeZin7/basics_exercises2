n = float(input('digite um numero: '))
n1 = float(input('digite outro numero: '))
n2 = float(input('digite outro numero: '))

if n<n1 and n<n2:
    print(f'{n} é o menor numero')
if n1<n and n1<n2:
    print(f'{n1} é o menor numero')
if n2<n and n2<n1:
    print(f'{n2} é o menor numero')

if n>n1 and n>n2:
    print(f'{n} é o maior numero')
if n1>n2 and n1>n:
    print(f'{n1} é o maior numero')
if n2>n1 and n2>n:
    print(f'{n2} é o maior numero')
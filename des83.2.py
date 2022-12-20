#um programa onde o usuario digite uma expressao qualquer que use parenteses.
#o aplicativo deverá analisar se a expressão está com os parênteses abertos
#e fechados na ordem correta

expressao = str(input('digite a expressao: '))
lista_parenteses_abertos = []
lista_parenteses_fechados = []

for parenteses in expressao:
    if parenteses == '(':
        lista_parenteses_abertos += [parenteses]
    elif parenteses == ')':
        lista_parenteses_fechados += [parenteses]

a = len(lista_parenteses_fechados)
b = len(lista_parenteses_abertos)
if a == b:
    print('expressão válida')
else:
    print('a expressão não é válida')

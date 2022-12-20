#Um programa onde o usuário digite uma expressão qualquer que use
#parênteses. Seu aplicativo deverá analisar se a expressão passada
#está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('digite a expressao: '))
lista = []

for parenteses in expressao:
    if parenteses == '(':
        lista.append('(')
    elif parenteses == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('expressao valida')
else:
    print('expressao errada')
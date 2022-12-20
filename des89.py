#um programa q leia NOME e duas notas de varios alunos
#guarde tudo em uma lista composta
#mostrar boletim contendo a média de cada um
#mostrar notas de cada aluno individualmente se o aluno pedir

lista =[]
lista_temporaria = []
r = 'S'

while True:
    nome_aluno = str(input('Digite o nome do aluno: ')).title()
    nota1 = float(input('Digite a nota 1 do aluno: '))
    nota2 = float(input('Digite a nota 2 do aluno: '))
    lista_temporaria.append(nome_aluno)
    lista_temporaria.append(nota1)
    lista_temporaria.append(nota2)
    lista.append(lista_temporaria[:])
    lista_temporaria.clear()


    r = str(input('Deseja adicionar mais alunos? [S/N]: ')).upper()
    if r == 'N':
        break

    while r not in 'SN':
        r = str(input('Comando inválido! Por favor digite [S/N]: ')).upper()
        if r == 'N':
            break

print('-='*30)
print('BOLETIM'.center(50))
print('-='*30)

for posicao, pessoa in enumerate(lista):
    media = ((pessoa[1]) + (pessoa[2])) / 2
    print(f'Aluno {posicao} → {pessoa[0]} → média: {media}')

print('-='*30)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        print('FINALIZANDO...')
        break
    if mostrar <= len(lista) - 1:
        print(f'Notas de {lista[mostrar][0]} foram {lista[mostrar][1]} e {lista[mostrar][2]}')
        print('-='*30)



    #print(f'{pessoa[0]} tirou {pessoa[1]} na primeira nota e {pessoa[2]} na segunda nota e obteve média {media}')


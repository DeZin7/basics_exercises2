#leia nome e média
#guarde a situação em um dicionário
#mostrar conteúdo da estrutura na tela

aluno = dict()
lista = []

for a in range(0,1):
    aluno['nome'] = str(input('Digite o nome do aluno: '))
    aluno['média'] = float(input('Digite a média do aluno: '))
    if aluno['média'] > 7:
        aluno['situacao'] = 'Aprovado'
    elif 5 <= aluno['média'] < 7:
        aluno['situacao'] = 'Recuperacao'
    elif aluno['média'] < 5:
        aluno['situacao'] = 'Reprovado'
    lista.append(aluno.copy())
print('-='*20)
for a in lista:
    for k,v in aluno.items():
        print(f'- {k} é igual a  {v}')


#função notas()
#a função recebe várias notas e retorna um dicionario
#dic = qtde de notas, maior nota, menor nota, média da turma, situação
#como variável opcional
#adicionar docstrings da função

def notas(*num, sit=False):
    """
    → Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.


    """

    dicionario = dict()
    lista = list(num)
    dicionario['total'] = len(lista)
    dicionario['maior'] = max(lista)
    dicionario['menor'] = min(lista)
    dicionario['média'] = sum(lista)/len(lista)
    if sit==True:
        if dicionario['média'] >= 7:
            dicionario['situação'] = 'BOA'
        elif 6<= dicionario['média'] <7:
            dicionario['situação'] = 'REGULAR'
        elif dicionario['média'] < 6:
            dicionario['situação'] = 'Ruim'

    return dicionario






#Programa Principal
resp = notas(8.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
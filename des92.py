#um programa que leia nome, ano de nascimento e carteira de trabalho
#cadastre nome, idade e carteiro de trabalho
#caso CTPS diferente de zero, dicionario recebe ano de contratação
#e salario.
#Mostrar com quantos anos a pessoa vai se aposentar

from datetime import datetime
dados = dict()
dados['nome'] = str(input('digite o nome do funcionario: '))
nascimento = int(input('Digite o ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('digite o ctps: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = int(input('Digite o salário: '))
    dados['aposentadoria'] = (35 - (datetime.now().year - dados['contratacao'])) + dados['idade']

print('-='*30)
for k,v in dados.items():
    print(f'{k} → {v}')
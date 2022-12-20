#Ler nome, sexo e idade de várias pessoas
#Guardar os dados de cada pessoa em um dicionário
#Guardar todos os dicionários em uma lista
#Mostrar:
# A) quantas pessoas foram cadastradas
# B) A média de idade de idade
# C) Uma lista com mulheres
# D) Uma lista com idade acima da média

dados_pessoas = {}
lista_dados = []
r = 'S'
soma_idade = 0
lista_mulheres = []
lista_idade_acima = []

while True:
    dados_pessoas['nome'] = str(input('Digite o nome: ')).title()
    dados_pessoas['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()
    while dados_pessoas['sexo'] not in 'MF' or dados_pessoas == '':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados_pessoas['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()
    dados_pessoas['idade'] = int(input('Digite a idade: '))
    soma_idade += dados_pessoas['idade']
    r = str(input('Quer continuar? [S/N]: ')).upper()
    lista_dados += [dados_pessoas.copy()]
    if dados_pessoas['sexo'] == 'F':
        lista_mulheres += [dados_pessoas['nome']]


    while r not in 'SN' or r == '':
        print('ERRO! Responda apenas S ou N.')
        r = str(input('Quer continuar? ')).upper()
    if r == 'N':
        break
media_idade = soma_idade/len(lista_dados)
print('-='*30)
print(f'A) {len(lista_dados)} pessoas foram cadastradas.')
print(f'B) a média de idade é de {soma_idade/len(lista_dados)}')
print(f'C) As mulheres cadastradas foram: ', end ='')
for mulheres in lista_mulheres:
    print(f'{mulheres}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média de idade: ')
for dados_pessoas in lista_dados:
    if dados_pessoas['idade'] >= media_idade:
        for k,v in dados_pessoas.items():
            print(f'{k} = {v}; ', end = '')
        print()
print()
print('-='*30)
print(lista_dados)





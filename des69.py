#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o
#usuário quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos


lista_idade = []
lista_sexo_masculino = []
lista_mulher_under20 = []
while True:
    i = int(input('digite a idade: '))
    s = str(input('digite o sexo [M/F]: ')).strip().upper()

    if i > 18:
        lista_idade += [i]
    if s == 'M':
        lista_sexo_masculino += [s]
    if i <20 and s == 'F':
        lista_mulher_under20 += [s]

    op = str(input('deseja continuar [S/N]?: ')).strip().upper()
    if op == 'N':
        break
    print('='*40)

print(f'{len(lista_idade)} pessoas possuem mais de 18 anos')
print(f'{len(lista_sexo_masculino)} pessoas são homens')
print(f'{len(lista_mulher_under20)} pessoas são mulheres com menos de 20 anos')



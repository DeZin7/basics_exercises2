#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
#M ou F. Caso esteja errado, peça a digitação novamente até ter
#um valor correto

n = str(input('digite o sexo [M/F]: ')).strip().upper()
while n not in 'MF':
    n = str(input('você digitou errado. por favor digite novamente: ')).strip().upper()
print(f'informação registrada com sucesso: {n}.')
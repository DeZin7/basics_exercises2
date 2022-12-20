#programa que leia ano de nascimento de 7 pessoas
#no final mostre quantas pessoas ainda não atingiram maioridade
#quantas já são maiores
cont = 0
cont1 = 0
for ano in range(1,8):
    ano = int(input('digite o ano de nascimento do indivíduo: '))
    idade = 2022 - ano
    if 0 < idade < 18:
        cont += 1
    elif idade >= 18:
        cont1 += 1
    else:
        print('o sujeito nem nasceu')
print(f'{cont} pessoas são maiores de idade')
print(f'{cont1} pessoas são menores de idade')

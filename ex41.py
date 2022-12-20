import datetime

n = int(input('Digite o ano de nascimento do atleta: '))
x = datetime.datetime.now()
ano_atual = (x.year)
idade = ano_atual - n

if 0 < idade <= 9:
    print('O atleta é mirim.')
elif 9 < idade <= 14:
    print('O atleta é infantil.')
elif 14 < idade <= 19:
    print('O atleta é junior.')
elif 19 < idade <= 20:
    print('O atleta é sênior.')
elif idade > 20:
    print('O atleta é master.')

elif idade < 0:
    print('O atleta nem nasceu ainda')

print('boa sorte, galerinha!')

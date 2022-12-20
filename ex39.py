ano = int(input('informe o ano de nascimento do jovem: '))
idade = 2022 - ano
tempo_atraso = idade - 18
tempo_falta = 18 - idade


if 0 < idade < 18:
    print(f'tem apenas {idade} anos, ainda vai se alistar')
    print(f'faltam {tempo_falta} anos pra se alistar')
elif idade == 18:
    print(f'ta na hora de se alistar, bro!')
elif idade <= 0:
    print(f'ainda nem nasceu man kkk fds')
else:
    print(f'vá se alistar, seu maconheiro')
    print(f'vc está {tempo_atraso} anos atrasado!')

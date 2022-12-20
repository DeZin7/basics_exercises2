def voto(ano_nascimento):
    from datetime import date #COLOCA A BIBLIOTECA DENTRO DA FUNÇÃO P ECONOMIZAR MEMORIA
    p = date.today().year
    idade = p - ano_nascimento
    if 16 <= idade < 18:
        return print(f'com {idade} anos: VOTO OPCIONAL')
    elif idade >= 18:
        return print(f"com {idade} anos: VOTO OBRIGATÓRIO!")
    elif idade < 16:
        return print(f'com {idade} anos: VOTO NEGADO!')
    elif idade > 65:
        return print(f'com {idade} anos: VOTO OPCIONAL')


#PROGRAMA PRINCIPAL
ano_nascimento = int(input('Digite o ano de nascimento: '))
voto(ano_nascimento)





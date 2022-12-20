from datetime import date
n = int(input('digite um ano. digite 0 para analisar o ano atual: '))
if n == 0:
    ano = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('é bissexto')
else:
    print('nao é bissexto')
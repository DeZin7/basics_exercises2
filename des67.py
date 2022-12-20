#um programa que mostre a tabuada de vários números, um de cada vez, para
#cada valor digitado pelo usuário. O programa será interrompido quando o
#número solicitado for negativo.


while True:
    n = int(input('digite o número para ver a tabuada: '))
    if n < 0:
        break
    for m in range (0, 11):
        y = n * m
        print(f'{n} x {m} = {y}')
    print('='*30)

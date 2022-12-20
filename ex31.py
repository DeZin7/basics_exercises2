n = float(input('digite a distancia da viagem em km: '))
l = 0.5 * n
p = 0.45 * n
if n > 200:
    print(f'a viagem custará {p:.2f} reais!')
else:
    print(f'a viagem custará {l:.2f} reais!')
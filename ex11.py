n = int(input('o carro foi alugado por quantos dias? '))
k = float(input('quantos km foram rodados?' ))
p = (60*n) + (0.15*k)
print(f'o preço total a ser pago é {p:.2f} reais')
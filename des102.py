def fatorial(num, show=False):
    """
    → Calcule o fatorial de um número.
    :param num: o número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor do fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f




num = int(input('Digite o numero: '))
print(fatorial(num, show=False))
help(fatorial)


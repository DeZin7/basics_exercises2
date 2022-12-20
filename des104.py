def leiaInt(n):
    n = str(input('Digite um número: ')).strip()
    if n.isnumeric():
        int(n)
        return n
    else:
        while n.isnumeric() == False or n == '':
            print('\033[0;31mERRO! Digite um número válido.\033[m')
            n = str(input('Digite um número: ')).strip()
            if n.isnumeric():
                int(n)
                return n




#programa principal
n =leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
print('='*40)
print('Bom dia liso!')
print('='*40)

valor = float(input('Qual valor da casa?'))
salario = float(input('Digite o valor do salário do comprador: '))
anos = int(input('Em quantos anos o liso vai querer pagar a casa? '))
qt_prestacao = anos * 12

prestacao = valor/(qt_prestacao)

if prestacao <= (0.3*salario):
    print(f'emprestimo aprovado com prestação de R${prestacao:.2f}!')
elif prestacao > (0.3*salario):
    print(f'infelizmente nao dá, pois vc é muito liso!')
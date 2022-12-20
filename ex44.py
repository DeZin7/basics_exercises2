print(f'{"Lojas DezinDelas":=^40}')
preço = float(input('digite o preço, liso: R$ '))
parcela = preço/2

print('''formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão 
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')

forma = int(input('Qual a forma de pagamento? '))

if forma == 1:
    print(f'o valor será {(preço - (preço*0.1)):.2f} ')

elif forma == 2:
        print(f'o valor será {(preço - (preço*0.05)):.2f}')

elif forma == 3:
        print(f'o valor será {(preço):.2f} reais em duas parcelas de {parcela}!')

elif forma == 4:
        print(f'o valor será {(preço + (preço*0.2)):.2f}')
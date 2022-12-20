#DESAFIO: IMPLEMENTAR UM BANCO
# DEPÓSITO, SAQUE E EXTRATO

menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    ==> '''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opçao = input(menu).lower()

    if opçao == "d":
        deposito = float(input('qual valor vc deseja depositar: '))
        saldo += deposito
        extrato += f'deposito realizado no valor de R$ {deposito:.2f} \n'

    if opçao == "s":
        saque = float(input('qual valor vc deseja sacar: '))
        saldo -= saque
        extrato += f'saque no valor de R$ {saque:.2f} \n'
        numero_saques += 1
        LIMITE_SAQUES -= 1
        if saque > saldo:
            print('você não possui saldo suficiente! ')
        if LIMITE_SAQUES < 0:
            print('vc ultrapassou o limite diário de 3 saques')

    if opçao == "e":
        print(extrato)

    if opçao == "q":
        break
print('Obrigado por utilizar nosso sistema, foi um prazer!!')
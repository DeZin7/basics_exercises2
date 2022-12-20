#crie um programa que tenha uma tupla com várias palavras.
#depois disso, você deve mostrar para cada palavra, quis são suas vogais

tupla = ('leitao', 'banha','bacon', 'porca', 'berg',)

for palavra in tupla:
    print(f'\n A palavra {palavra.upper()} possui a vogal: ', end='')
    for vogal in 'aeiou':
        if vogal in palavra:
            print(f'{vogal.upper()}', end='')

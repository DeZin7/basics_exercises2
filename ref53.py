#programa que leia uma frase e diga se ela é um palíndromo

frase = str(input('digite uma frase: ')).upper().strip().split()
frase_junta = ''.join(frase)
frase_contrario = frase_junta[::-1]

if frase_junta == frase_contrario:
    print('é palindromo')
else:
    print('não é palíndromo')
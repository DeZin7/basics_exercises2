print('='*40)
print('analisador de triangulos')
print('='*40)

r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))

print('='*40)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('formam um triangulo')
else:
    print('nao formam um triangulo')
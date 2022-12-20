p = float(input('digite o peso: '))
h = float(input('digite a altura: '))
imc = p/(h*h)

if imc < 18.5:
    print('abaixo do peso')

elif 18.5 <= imc <= 25:
    print('peso ideal')
elif 25 < imc <= 30:
    print('sobrepeso')
elif 30 < imc <= 40:
    print('obesidade')
elif imc > 40:
    print('obesidade mórbida')
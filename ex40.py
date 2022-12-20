nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2)/2

if media < 5:
    print('Aluno reprovado!')

elif 5<= media < 6.9:
    print ('Ta de recuperação fion!')

elif media >=7:
    print('Aluno aprovado!')
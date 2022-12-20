def área(largura, comprimento):
    área = largura * comprimento
    print(f'A área do terreno é {área} m^2.')



print('     CONTROLE DE TERRENOS     ')
print('-'*30)
largura = int(input('Digite a largura: '))
comprimento = int(input('Digite o comprimento: '))
área(largura, comprimento)

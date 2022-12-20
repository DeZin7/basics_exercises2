#um programa q tenha uma função escreva()
#recebe um parametro qualquer e mostra uma msg com tamanho adaptavel

def escreva(msg):
    print('-'*(len(msg)+4))
    print(f'{msg:^{(len(msg)+4)}}')
    print('-'*(len(msg)+4))

escreva(' dezin ')
escreva(' Berg Bacon ')
escreva(' Hidelbrando ')
escreva(' ROBIN IRMÃO RICO FOREVER ')
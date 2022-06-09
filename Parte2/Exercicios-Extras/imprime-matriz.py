'''
Escreva uma função que recebe e imprime uma matriz de inteiros.
Exercicio 11.2
'''

def imprima_matriz(matriz):
    print('Matriz:', len(matriz), 'x', len(matriz[0]))
    for linha in matriz:
        for item in linha:
            print(item, end = '  ')
        print()

    return

#matriz = [[1,2,3],[2,1,4],[3,4,1]]
#matriz = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 91, 92, 93]]
matriz = [[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]]
imprima_matriz(matriz)

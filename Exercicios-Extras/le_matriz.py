'''
Funcao que le do teclado o numero n_linhas de linhas e o numero n_colunas de
colunas e os elementos de uma matriz de inteiros dimensao n_linha x n_colunas.
Exercicio 11.1
'''


def leia_matriz():
    n_linhas = int(input('Digite o número de linha(s): '))
    n_colunas = int(input('Digite o número de coluna(s): '))
    
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            c = int(input('Digite o elemento [' + str(i) + '][' + str(j) + ']: '))
            linha.append(c)
        matriz.append(linha)

    return matriz

matriz = leia_matriz()
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(matriz[linha][coluna], end = "  ")
    print()


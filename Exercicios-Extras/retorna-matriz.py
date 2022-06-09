'''
A funcao le do teclado o numero n_linhas de linhas e o numero n_colunas de
colunas e os elementos de uma matriz de inteiros dimensao n_linha x n_colunas.
A funcao cria e retorna a matriz lida.
Exercicio 11.1
'''

def leia_matriz():
    n_linhas = int(input('Digite o número de linhas da matriz: '))
    n_colunas = int(input('Digite o número de colunas da matriz: '))
    matriz = []
    for c in range(n_linhas):
        linha = []
        for l in range(n_colunas):
            print('Digite o elemento [' +str(c)+ '][' +str(l)+ '] da matriz: ')
            n = int(input())
            linha.append(n)
            print('Linha ' + str(c) + ' =', linha)
        matriz.append(linha)
    return matriz

print('Matriz =', leia_matriz())

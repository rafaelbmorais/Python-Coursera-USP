'''
Escreva um programa que leia inteiros positivos m e n e os elementos de uma
matriz A de números inteiros de dimensão m x n e conta o número de linhas e
colunas que tem apenas zeros.
Exercicio 11.5
'''

m = int(input('Digite o número de linhas: '))
n = int(input('Digite o número de colunas: '))

matriz = []
for linha in range(m):
    linha_matriz = []
    for coluna in range(n):
        x = int(input('Digite 0 ou um número inteiro positivo: '))
        linha_matriz.append(x)
    matriz.append(linha_matriz)


print('Matriz: ', m, 'x', n)
cont_linhas = 0
for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        print(matriz[l][c], end='  ') # imprime a matriz
    print()
    if not (c != 0) in matriz[l]:    #verifica se a linha contém somente zeros
        cont_linhas += 1
print('Linhas nulas = ', cont_linhas)



cont_colunas = 0
for c in range(len(matriz[0])):
    aux = []
    for l in range(len(matriz)):
        aux.append(matriz[l][c])
    if not (l != 0) in aux:    #verifica se a coluna contém somente zeros
        cont_colunas += 1
print('Colunas nulas = ', cont_colunas)


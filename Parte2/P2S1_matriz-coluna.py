def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz

def le_matriz():
    linhas = int(input('Digite o número de linhas da matriz: '))
    colunas = int(input('Digite o número de colunas da matriz: '))
    return cria_matriz(linhas, colunas)

print(le_matriz())
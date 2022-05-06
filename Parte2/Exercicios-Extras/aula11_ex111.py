
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

a_mat = leia_matriz()
print(a_mat)
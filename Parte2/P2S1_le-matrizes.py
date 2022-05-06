def cria_matriz(num_linhas, num_colunas):
    ''' (int, int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemneto é igual ao valor digitado pelo usuario.
    '''

    matriz = []    #cria a matriz vazia
    for i in range(num_linhas):    #cria a cada linha i
        linha = []    #lista vazia

        for j in range(num_colunas):
            valor = int(input('Digite o elemento [' + str(i) + ']['+ str(j) + ']: '))
            linha.append(valor)

        matriz.append(linha)    # adiciona linha a matriz
 
    return matriz


def le_matriz():
    linhas = int(input('Digite o número de linhas da matriz: '))
    colunas = int(input('Digite o número de colunas da matriz: '))
    return cria_matriz(linhas, colunas)


matriz = le_matriz()
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()



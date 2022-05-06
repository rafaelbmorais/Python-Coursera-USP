def cria_matriz(num_linhas, num_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemneto é igual ao valor dado.
    '''

    matriz = []    #cria a matriz vazia
    for i in range(num_linhas):    #cria a cada linha i
        linha = []    #lista vazia

        for j in range(num_colunas):
            linha.append(valor)

        matriz.append(linha)    # adiciona linha a matriz
 

    return matriz

linhas = int(input('Digite o número de linhas da matriz: '))
colunas = int(input('Digite o número de colunas da matriz: '))
valor = int(input('Digite o valor para a matriz: '))

matriz = cria_matriz(linhas, colunas, valor)
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()
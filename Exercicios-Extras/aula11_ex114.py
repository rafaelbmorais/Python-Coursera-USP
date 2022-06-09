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


def simetrica(matriz):
    l = 0
    c = 0
    for linha in matriz:
        l += 1
        for coluna in linha:
            c += 1
    
    if (c / l) == l:
        #return True
        return print('A matriz é simétrica!')
    else:
        #return False
        return print('A matriz não é simétrica!')    



def imprima_matriz(matriz):
    for linha in matriz:
        for i in linha:
            print(i, end = '  ')
        print()

    return


def main():
    matriz = leia_matriz()
    simetrica(matriz)
    imprima_matriz(matriz)

main()
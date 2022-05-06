
def imprime_matriz(matriz):

    for linha in matriz:
        for i in linha:
            if i == linha[-1]:
                print(i, end = '')
            else:
                print(i, end = ' ')
        print(end='\n')

    return


def main():
    matriz = [[1, 2, 3], [4, 5, 6]]
    imprime_matriz(matriz)

main()
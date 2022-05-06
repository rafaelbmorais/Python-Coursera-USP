def imprima_matriz(matriz):
    for linha in matriz:
        for i in linha:
            print(i, end = '  ')
        print()

    return

a = [[1,2,3],[2,1,4],[3,4,1]]
imprima_matriz(a)
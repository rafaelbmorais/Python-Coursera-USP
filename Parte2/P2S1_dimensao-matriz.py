# a função recebe uma matriz como parametro e devolve as dimensões no formato iXj.

def dimensoes(matriz):
    l = 0
    for linha in matriz:
        l += 1
        c = len(linha)
    
    print(str(l)+'X'+str(c))

#minha_matriz = [[1], [2], [3]]
minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)
# a função recebe 2 matrizes e devolve a soma das matrizes, caso tenham dimensões iguais.

def soma_matrizes(m1, m2):

    l1 = len(m1)
    c1 = len(m1[0])
    l2 = len(m2)
    c2 = len(m2[0])

    if (l1 == l2) and (c1 == c2):
        num_linhas = len(m1)
        num_colunas = len(m1[0])
        m3 = []
        for linha in range(num_linhas):
            linha_m3 = []
            for coluna in range(num_colunas):
                linha_m3.append(m1[linha][coluna] + m2[linha][coluna])
            m3.append(linha_m3)

        return m3

    else:
        return False    


def main():
    #m1 = [[1]]
    #m2 = [[1,2,3],[1,2,3], [1,2,3]]
    m1 = [[1, 1, 1], [2, 2, 1]]
    m2 = [[1, 2, 3], [1, 2, 3]]

    print(soma_matrizes(m1, m2))

main()
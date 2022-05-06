def sao_multiplicaveis(m1, m2):

    l1 = len(m1)
    c1 = len(m1[0])
    l2 = len(m2)
    c2 = len(m2[0])

    if (c1 == l2):
        return True

    else:
        return False    


def main():
    #m1 = [[1], [2], [3]]
    #m2 = [[1, 2, 3]]
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]

    print(sao_multiplicaveis(m1, m2))

main()
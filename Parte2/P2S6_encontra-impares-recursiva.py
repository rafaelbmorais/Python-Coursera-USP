'''
Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números
inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista.
Utilizando recursão.
'''
impar = []
def encontra_impares(lista):

    if len(lista) == 1:
        if (lista[0] % 2) != 0:
            impar.extend([lista[0]])
        return impar
    else:
        if (lista[0] % 2) != 0:
            impar.append(lista[0])
        encontra_impares(lista[1:])

    return impar
 



a = [9, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]
print(encontra_impares(a))


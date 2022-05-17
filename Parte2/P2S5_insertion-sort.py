'''
Implemente a função insertion_sort(lista), que recebe uma lista com números inteiros
como parâmetro e devolve esta lista ordenada. Utilize o algoritmo insertion sort.
'''

def insertion_sort(lista):
    final = len(lista)

    for i in range(final):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
                if j != 0:
                    for k in range(final-2, 0, -1):
                        if lista[k] > lista[k+1]:
                            lista[k], lista[k+1] = lista[k+1], lista[k]
                            print(lista)
    return lista

#print(insertion_sort([5, 1, 4, 2]))
print(insertion_sort([1, 5, 3, 4, 2, 0]))

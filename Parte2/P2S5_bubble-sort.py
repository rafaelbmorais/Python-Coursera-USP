'''
Implemente a função bubble_sort(lista), que recebe uma lista com números inteiros
como parâmetro e devolve esta lista ordenada. Utilize o algoritmo bubble sort.
'''

def bubble_sort(lista):

    for i in range(len(lista) - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
    return lista

#print(bubble_sort([5, 1, 4, 2]))
#print(bubble_sort([1, 5, 3, 4, 2, 0]))

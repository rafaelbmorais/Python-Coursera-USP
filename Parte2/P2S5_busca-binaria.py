'''
Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e
devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca binária.
Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.
'''



def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(meio)
        if lista[meio] == elemento:
            return meio
        elif elemento < lista[meio]:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
    return False

    
#print(busca(['a', 'e', 'i'], 'e'))
#print(busca([1, 2, 3, 4, 5], 6))
#print(busca([1, 2, 3, 4, 5, 6], 4))
#print(busca([-100, 0, 20, 30, 50, 100, 3000, 5000], 5000))

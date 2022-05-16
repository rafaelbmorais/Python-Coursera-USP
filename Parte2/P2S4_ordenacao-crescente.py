'''
Implemente a função ordena(lista), que recebe uma lista com números inteiros como parâmetro e
devolve esta lista ordenada em ordem crescente. Utilize o algoritmo selection sort.
'''

def ordena(lista):
    tamanho = len(lista)
    for i in range(tamanho-1):
        menor = i
        for j in range(i+1, tamanho):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista
                
print(ordena([9 , -1, -30, 98, 202, 1, -3, 4]))

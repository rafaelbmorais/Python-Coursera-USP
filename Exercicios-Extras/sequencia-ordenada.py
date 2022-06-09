'''
Dados dois números naturais m e n e duas sequências ordenadas com m e n
números inteiros, obter uma única sequência ordenada contendo todos os
elementos das sequências originais sem repetição.
Exercicio 9.3
'''

def ordenado(lista1, lista2):
    lista_ordenada = []
    for m in lista1:
        if m not in lista_ordenada:
            lista_ordenada.append(m)
    for n in lista2:
        if n not in lista_ordenada:
            lista_ordenada.append(n)

    lista_ordenada.sort()
    return lista_ordenada



lista1 = []
lista2 = []
m = int(input('Digite a quantidade de elementos da sequência 1: '))
for i in range(m):
    x = int(input('Digite um número: '))
    lista1.append(x)

n = int(input('Digite a quantidade de elementos da sequência 2: '))
for j in range(n):
    y = int(input('Digite um número: '))
    lista2.append(y)

print(ordenado(lista1, lista2))

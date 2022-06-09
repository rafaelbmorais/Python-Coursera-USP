'''
Escreva um programa que dados um número inteiro n e uma sequência com n números
inteiros, conta e imprime o número de vezes que cada número ocorre na sequência.
Exercicio 10.4
'''


lista = [1, 2, 1, 1, 3, 4, 5, 2, 3, 5, 1, 3, 6, 7, 8, 1, 2]

for i in range(len(lista)):
    if lista[i] not in lista[:i]:
        cont = 0
        for j in range(len(lista)):
            if lista[i] == lista [j]:
                cont += 1        
        print(lista[i], 'apareceu', cont, 'vez(es)')




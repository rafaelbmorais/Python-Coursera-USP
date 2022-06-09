
#imprime a lista na ordem inversa
#Exercicio 9.1


lista = [17, 123, 87, 34, 66, 8398, 44]

#usando while
'''
cont = -1
while cont >= -len(lista):
    print(lista[cont])
    cont -= 1
'''


#usando for
'''
for i in range(-1, (-len(lista) - 1), -1):
    print(lista[i])
'''


#usando slice + for
lista_inversa = lista[::-1]
for i in lista_inversa:
    print(i)

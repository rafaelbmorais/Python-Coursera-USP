'''
Escreva um programa que dados um número inteiro n e uma sequência com n números
inteiros, imprimi-los eliminando as repetições. Escreva uma solução que usa a
função pertence() do exercício anterior.
Exercicio 10.2
'''

def pertence(item, lista):
    contem = 0
    for i in lista:
        if item == i:
            contem = 1
    if contem == 1:
        return True
    else:
        return False



n = int(input('Informe a quantidade de elementos da lista: '))
lista = []
for i in range(n):
    x = int(input('Digite um número: '))
    if not pertence(x, lista):
        lista.append(x)
print(lista)




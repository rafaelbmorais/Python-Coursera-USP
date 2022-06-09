'''
Dada uma sequência de n > 0 números reais, imprimi-los eliminando as repetições.
Exercicio 9.2
'''

def removendo(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

lista = []
x = int(input('Digite a quantidade da lista: '))
for i in range(x):
    n = input('Digite um número: ')
    lista.append(n)
print(removendo(lista))

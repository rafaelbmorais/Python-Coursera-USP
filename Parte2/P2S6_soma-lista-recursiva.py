'''
Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números
inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista.
Utilizando recursão.
'''

def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])



a = [-10, -2, 0, 5, 66, 77, 99, 102, 239, 567, 875, 934]
print(soma_lista(a))


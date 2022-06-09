'''
Recebe uma lista `lista` de numero e dois indices ini e fim, retorna a soma da
sublista (= fatia) formada pelos elementos de indices ini, ini+1,...,fim-1.
Exercicio 10.5
'''


def soma_elementos(ini, fim, lista):
    soma = 0
    lista2 = lista[ini:fim]
    for i in range(len(lista2)):
        soma = soma + lista2[i]
    return soma

# testes
lista  = [1, 2, 3, 4, 5]

# teste 1
if soma_elementos(0,len(lista),lista) == 15:
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")

# teste 2
if soma_elementos(1,4,lista) == 9:
    print("Passou no segundo teste! :-)")
else:
    print("Nao passou no segundo teste! :-(")

# teste 3
if soma_elementos(2,2,lista) == 0:
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")

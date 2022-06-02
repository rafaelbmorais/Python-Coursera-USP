'''
Recebe um objeto 'item' e uma lista 'lista' e retorna o indice da posicao em
que item ocorre na lista. Caso item nao ocorra na lista a funcao retorna None.
Exercicio 10.3
'''

def indice(item, lista):
    for i in range(len(lista)):
        if item is lista[i]:
            return i
    else:
        return None



# testes
lista  = [1, "oi", 3.14, 7, True]

# teste 1
if indice("oi",lista) == 1:
    print("Passou no primeiro teste! :-)")
else:
    print("Nao passou no primeiro teste! :-(")

# teste 2
if indice(True,lista) == 4:
    print("Passou no segundo teste! :-)")
else:
    print("Nao passou no segundo teste! :-(")

# teste 3
if indice(False,lista) == None:
    print("Passou no terceiro teste! :-)")
else:
    print("Nao passou no terceiro teste! :-(")

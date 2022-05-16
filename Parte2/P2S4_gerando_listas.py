'''
Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n
e devolve uma lista contendo n números inteiros aleatórios.
'''
import random

def lista_grande(n):
    nova_lista = []
    for i in range(n):
        x = random.randint(-100, 100)
        nova_lista.append(x)
    return nova_lista

print(lista_grande(10))
    

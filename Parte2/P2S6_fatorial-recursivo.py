'''
Implemente a função fatorial(x), que recebe como parâmetro um número inteiro
e devolve um número inteiro correspondente ao fatorial de x.
'''

def fatorial(x):

    if (x == 0) or (x == 1):
        return 1
    else:
        return x * fatorial(x-1)

#print(fatorial(7))
    

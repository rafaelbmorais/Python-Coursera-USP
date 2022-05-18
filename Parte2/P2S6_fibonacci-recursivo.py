'''
Implemente a função fibonacci(n), que recebe como parâmetro um número inteiro e devolve
um número inteiro correspondente ao n-ésimo elemento da sequência de Fibonacci.
'''

def fibonacci(n):

    if (n == 1) or (n == 2):
        return 1
    else:
        return  fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(11))


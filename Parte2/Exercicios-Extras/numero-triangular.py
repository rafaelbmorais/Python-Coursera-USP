'''
Dizemos que um número inteiro positivo é triangular se ele é o produto de três numeros inteiros consecutivos.
Dado um número inteiro positivo n, verificar se n é triangular.
Exercicio 3.3
'''

def triangular(n):
    a = 1
    b = 2
    c = 3
    if n <= 5:
        return n+1
    else:
        while a * b * c < n:
            a += 1
            b += 1
            c += 1
        return a*b*c

n = 120

if n == triangular(n):
    print('É triangular!')
else:
    print('Não é triangular!')
        



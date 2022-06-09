'''
Dados um número inteiro n, n > 0, e um dígito d. 0 <= d <= 9,
determinar quantas vezes d ocorre em n.
Exercicio 3.2
'''


n = int(input('Digite o valor de n: '))
d = int(input('Digite o valor de d: '))
cont = 0
if (d == 0 and n >= d) or (d >= 0 and d <= 9):
    while (n >= d) and ( n != 0):
        if (n % 10 == d):
            cont += 1
        n //= 10
print(cont)
    


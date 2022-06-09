'''
Dado um número inteiro n >= 0, calcular n!.
Exercício 2.4
'''


n = int(input('Digite um número para o fatorial:'))

cont = 1
if n == 0 or n == 1:
    fatorial = 1
else:
    fatorial = 1
    while n >= cont:
        fatorial *= cont
        cont += 1

print('O fatorial de', n, 'é', fatorial)

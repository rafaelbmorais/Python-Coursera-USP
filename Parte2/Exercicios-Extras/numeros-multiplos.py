'''
Dados números inteiros n, i e j, todos maiores do que zero, imprimir em ordem
crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
Exercicio 8.2
'''

n = int(input('Digite a quantidade de números para imprimir:'))
i = int(input('Digite um numero maior que zero e inteiro para i: '))
j = int(input('Digite um numero maior que zero e inteiro para j: '))
cont1 = 0
cont2 = 0
while cont1 < n:
    if ((cont2 % i) == 0) or ((cont2 % j) == 0):
        print(cont2)
        cont1 += 1
    cont2 += 1
        

#Dados números inteiros n e k, com k >= 0, calcular n elevado a k.
#Exercício 2.3

n = int(input('Digite um número:'))
k = int(input('Digite um número que será a potência:'))

p = 1
cont = k
while cont > 0:
    p *= n
    cont -= 1
    

print('A potência de', n, 'elevado a', k, 'é', p)

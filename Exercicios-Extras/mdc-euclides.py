'''
Dados dois inteiros positivos calcular o máximo divisor comum entre eles usando o algoritmo de Euclides.
Exercício 08.3
'''

x1 = int(input('Digite o primeiro número: '))
x2 = int(input('Digite o segundo número: '))
resto = 0

if x1 < x2:
    x1, x2 = x2, x1

while x2 != 0:
    resto = x1 % x2
    x1, x2 = x2, resto

print("O MDC dos números informados é: ", x1)

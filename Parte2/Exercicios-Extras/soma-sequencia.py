'''
Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma.
Exercício 2.2
'''

def main():
    x = int(input('Digite um número inteiro ou zero para sair: '))
    soma = 0
    while x != 0:
        soma += x
        x = int(input('Digite um número inteiro ou zero para sair: '))
    
    print('A soma dos números informados é', soma)

main()

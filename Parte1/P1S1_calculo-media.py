#cálculo da média de 4 notas

n1 = int(input("Digite a primeira nota: "))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))
n4 = int(input('Digite a quarta nota: '))

soma = n1+n2+n3+n4
media = float(soma/4)

print('A média aritmética é', media)
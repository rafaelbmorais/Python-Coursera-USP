#verifica se os números de entrada foram digitados em ordem crescente

x1 = int(input('Digite o primero número: '))
x2 = int(input('Digite o segundo número: '))
x3 = int(input('Digite o terceiro número: '))

if (x1 < x2) and (x2 < x3):
	print('crescente')
else:
	print('não está em ordem crescente')

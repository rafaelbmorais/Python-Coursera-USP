#verifica se o número de entrada é divisivel por 3 e 5.

x = int(input('Digite um número: '))

if (x % 3 == 0) and (x % 5 == 0):
	print('FizzBuzz')
else:
	print(x)

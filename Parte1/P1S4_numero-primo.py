#verifica se o número é primo

n = int(input('Digite um númro inteiro: '))

if n == 2:
	print('primo')
else:
	if (n // 1 == n) and (n // n == 1) and (n % 2 != 0):
		print('primo')
	else:
		print('não primo')





		

#verifica se o numero digitado tem números adjacentes iguais

x = int(input('Digite um número inteiro: '))

iguais = False
anterior = -1

while x > 0:
	y = x % 10
	x = x // 10
	if y == anterior:
		iguais = True
		print('sim')
	anterior = y
if iguais == False:
	print('não')
	


	

		
 
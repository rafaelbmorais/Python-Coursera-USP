#recebe um número e imprime essa quantidade de números ímpares

n = int(input('Digite o valor de n: '))
count = 0
p = 1

while count < n:
	if p % 2 != 0:
		print(p)
		p = p + 1
		count = count + 1

	else:
		p = p + 1
		

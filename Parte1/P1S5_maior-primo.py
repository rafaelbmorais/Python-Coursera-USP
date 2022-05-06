#devolve o maior número primo a partir de um número recebido

def maior_primo(n):
	count2 = n
	nprimo2 = True
	while nprimo2 == True and count2 <= n:
		nprimo = True
		count = count2
		while count <= count2 and count != 0:
			if (count2 % count == 0) and (count != 1) and (count != count2):
				nprimo = False
				count = count - 1
			else:
				count = count - 1
		if nprimo == True:
			nprimo2 = False
		else:
			count2 = count2 - 1	
	return count2
	
	

x = int(input('Digite um número inteiro: '))
if x >= 2:
	print(maior_primo(x))	
else:
	print('Digite um número maior ou igual a 2!')

	


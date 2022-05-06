# descobrir quantos números primos tem dentro de um número dado

def n_primos(n):
	fator = 2
	p = 0
	cont = 2
	while cont <= n:
		while cont % fator != 0 and fator <= cont/2: #verifica se um numero é dividido por mais de um numero, tirando o um e ele mesmo
			fator = fator + 1
		if cont % fator == 0 and cont != 2:
			cont = cont + 1
		else:
			p = p + 1
			cont = cont + 1
		fator = 2
	return p

n = int(input('Digite um número inteiro: '))
print(n_primos(n))

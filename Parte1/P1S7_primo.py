# descobrir se o número é primo

def primo(n):
	fator = 2
	while n % fator != 0 and fator <= n/2: #verifica se um numero é dividido por mais de um numero, tirando o um e ele mesmo
		fator = fator + 1
	if n % fator == 0 and n != 2:
		return False
	else:
		return True


n = int(input('Digite um número inteiro: '))

while n > 0:
	if primo(n):
		print(n, ' é primo! :)')
	else:
		print(n,' não é primo! :(')
	n = int(input('Digite um número inteiro: '))


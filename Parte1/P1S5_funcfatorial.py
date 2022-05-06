
x = int(input('Digite um número para o fatorial: '))


def fatorial(x):
	y = 1
	cont = 1
	while cont <= x:
		y = y * cont
		cont = cont + 1
	return y

print(fatorial(x))
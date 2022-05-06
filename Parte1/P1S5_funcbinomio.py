
x = int(input('Digite um número para x: '))
k = int(input('Digite um valor para k: '))


def fatorial(x):
	y = 1
	cont = 1
	while cont <= x:
		y = y * cont
		cont = cont + 1
	return y


n = fatorial(x)
d = fatorial(x-k)*fatorial(k)
print(int(n/d))
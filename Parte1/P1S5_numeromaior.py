#Devolve maior número

def maximo(x, y, z):
	if x > y and x > z:
		return x
	elif y > x and y > z:
		return y
	else:
		return z

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))


print(maximo(n1, n2, n3))
#imprime uma lista em ordem inversa

lista = []
x = 1

while x != 0:
	x = int(input('Digite um número inteiro: '))
	if x != 0:
		lista.append(x)

cont = len(lista) - 1
while cont >= 0:
	print(lista[cont])
	cont = cont - 1
#removendo elementos repetidos

def remove_repetidos(lista):
	aux = []
	for item in lista:
		if item not in aux:
			aux.append(item)
	aux.sort()
	return aux


lista = []
x = 1
while x != 0:
	x = int(input('Digite um número diferente de zero ou zero para sair: '))
	if x != 0:	
		lista.append(x)
print(lista)
print(remove_repetidos(lista))
	
			
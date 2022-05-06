#devolve o maior elemento

def maior_elemento(lista):
	aux = 0
	for item in lista:
		if aux == 0:
			aux = item
		else:
			if item >= aux:
				aux = item
	return aux


lista = []
x = 1
while x != 0:
	x = int(input('Digite um número diferente de zero ou zero para sair: '))
	if x != 0:	
		lista.append(x)
print(lista)
print(maior_elemento(lista))
	
			
#devolve a soma dos elementos

def soma_elementos(lista):
	aux = 0 
	for item in lista:
		aux = aux + item
	return aux


lista = []
x = 1
while x != 0:
	x = int(input('Digite um número diferente de zero ou zero para sair: '))
	if x != 0:	
		lista.append(x)
print(lista)
print(soma_elementos(lista))
	
			
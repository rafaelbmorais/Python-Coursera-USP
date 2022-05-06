#soma hipotenusas

def soma_hipotenusas(n):
	soma = 0
	cont = 1
	while cont <= n:
		if é_hipotenusa(cont) == True:
			soma = soma + cont
		cont = cont + 1

	return soma 


def é_hipotenusa(n):
	i = j = 1
	while i <= n:
		while j <= n:
			if n**2 == i**2 + j**2:
				return True
			j = j + 1
		j = 1
		i = i + 1
	i = 1


n = int(input('Informe um valor para a hipotenusa: '))
print(soma_hipotenusas(n))
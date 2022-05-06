#fatorial de um número inserido pelo usuário

print ('Atenção!!! Para sair digite um número negativo!')
f = int(input('Digite um número inteiro para o fatorial: '))

while f >= 0:
	fat = 1
	while f > 1:
		fat = fat * f
		f = f - 1		
	print('O fatorial do número informado é: ', fat)
	f = int(input('Digite um número inteiro para o fatorial: '))


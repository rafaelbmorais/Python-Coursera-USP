#soma os digitos de um número

x = int(input('Digite um número: '))
soma = 0

while x > 0:
	y = x % 10
	x = x // 10
	soma = soma + y

print('a soma dos algarismos do número digitado é: ', soma)
 
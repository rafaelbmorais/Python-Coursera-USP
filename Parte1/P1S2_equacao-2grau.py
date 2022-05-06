import math
a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))


delta = ((b**2) - (((4*a)*c)))

if delta > 0:
	if a == 0:
		print('a = 0, não existe divisão por zero!')
	else:
		x1 = ((-1*b) + (math.sqrt(delta))) / (2*a)
		x2 = ((-1*b) - (math.sqrt(delta))) / (2*a)
		print('As raízes são: ', x1, 'e ', x2)

elif delta == 0:
	if a == 0:
		print('a = 0, não existe divisão por zero!')
	else:
		x3 = (-1*b) / (2*a)
		print('A raiz é: ', x3)

else: 
	print('Não existe raiz!')


	 
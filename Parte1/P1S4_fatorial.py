#fatorial

x = int(input('Digite o valor de n: '))
fat = 1

while x > 0:
	fat = fat * x
	x = x - 1
print(fat)

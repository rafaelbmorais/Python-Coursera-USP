# lê dois numeros (largura e altura) e imprime um retangulo


largura = int(input('Informe a largura: '))
altura = int(input('Informe a altura: '))

cont_alt = 1
while cont_alt <= altura:
	cont_larg = 1
	while cont_larg <= largura:
		print('#', end='')
		cont_larg = cont_larg + 1
	cont_alt = cont_alt + 1
	print()

# lê dois numeros (largura e altura) e imprime um retangulo oco


largura = int(input('Informe a largura: '))
altura = int(input('Informe a altura: '))

cont_alt = 1
while cont_alt <= altura:
	cont_larg = 1
	if altura == 2:
		while cont_larg <= largura:
			print('#', end='')
			cont_larg = cont_larg + 1
	elif cont_alt == 1 or cont_alt == altura:
		while cont_larg <= largura:
			print('#', end='')
			cont_larg = cont_larg + 1
	else:
		while cont_larg <= largura:
			if cont_larg == 1 or cont_larg == largura:
				print('#', end='')
			else:
				print(' ', end='')
			cont_larg = cont_larg + 1

	cont_alt = cont_alt + 1
	print()

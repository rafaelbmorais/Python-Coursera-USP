#jogo do NIM

def main():
	print('Seja bem vindo ao Jogo do NIM! Escolha: ')
	print('1 - para jogar uma partida isolada')
	print('2 - para jogar um campeonato')
	escolha = int(input())
	if escolha == 1:
		partida()
	elif escolha == 2:
		campeonato()
	else:
		print('Esolha 1 para Partida, 2 para Campeonato!')	



def computador_escolhe_jogada(n, m):

	if n < m:
		peca = n

	elif n == m:
		peca = n

	elif n > m:
		cont = 0
		while n % (m+1) != 0:
			n = n - 1
			cont = cont + 1
		if cont == 0:
			while (n - cont) != (m + 1):
				cont = cont + 1
			if cont > m:
				peca = m
			else:
				peca = cont
		elif cont > m:
			peca = m
		else:
			peca = cont	

	print('O computador tirou', peca,' peças.')
	return peca



def usuario_escolhe_jogada(n, m):

	peca = int(input('Quantas peças você vai tirar? '))

	while peca > m or peca <= 0 or peca > n:
		print('Oops! Jogada inválida! Tente de novo!')
		peca = int(input('Quantas peças você vai tirar? '))


	print('Você tirou ', peca, ' peça(s).')
	
	return peca


def partida():
	n = int(input('Quantas peças?'))
	m = int(input('Limite de peças por jogada?'))
			
	if (n % (m+1)) == 0:
		print('Você começa!')
		while n > 0:
			jogada = usuario_escolhe_jogada(n, m)
			n = n - jogada	
			if n == 0:
				print('Fim do jogo! O jogador ganhou!')
				
			else:
				print('Agora resta(m) ', n,' peça(s) no tabuleiro.')
				jogada = computador_escolhe_jogada(n, m)
				n = n - jogada
				if n == 0:
					print('Fim do jogo! O computador ganhou!')
					return 'computador'
				else:
					print('Agora resta(m) ', n,' peça(s) no tabuleiro.')
	else:
		print('Computador começa!')
		while n > 0:
			jogada = computador_escolhe_jogada(n, m)
			n = n - jogada
			if n == 0:
				print('Fim do jogo! O computador ganhou!')
				return 'computador'
			else:
				print('Agora resta(m) ', n,' peça(s) no tabuleiro.')
				jogada = usuario_escolhe_jogada(n, m)
				n = n - jogada
				if n == 0:
					print('Fim do jogo! O jogador ganhou!')
					
				else:
					print('Agora resta(m) ', n,' peça(s) no tabuleiro.')
	
	
	

def campeonato():
	cont = 1
	pc = 0
	pu = 0

	while cont <= 3:
		print('**** Rodada', cont,' ****')
		placar = partida()
		cont = cont + 1
		if placar == 'computador':
			pc = pc + 1
		else:
			pu = pu + 1
			
	print('**** Final do campeonato! ****')

	print('Placar: Você ', pu,' X ', pc,' Computador')
	


main()


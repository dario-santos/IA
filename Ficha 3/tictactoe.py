import copy
import random


def mostra_tabuleiro(T):
	print(T[0], ' | ', T[1], ' | ', T[2])
	print('--------------')
	print(T[3], ' | ', T[4], ' | ', T[5])
	print('--------------')
	print(T[6], ' | ', T[7], ' | ', T[8])
	print('\n')


def acoes(T):
	a = []

	for i, value in enumerate(T):
		if value == 0:
			a.append(i)
	
	return a


def resultado(T, a, jog):
	aux = copy.copy(T)
	
	if jog == 'MAX':
		aux[a] = 1
	else: 
		aux[a] = -1
	
	return aux


def utilidade(T):

	# linhas
	for i in range(0, 3, 6):
		if T[i] == T[i + 1] and T[i] == T[i + 2] and T[i] != 0:
			return T[i]

	# colunas
	for i in range(0, 3):
		if T[i] == T[i + 3] and T[i] == T[i + 6] and T[i] != 0:
			return T[i]

	# diagonais
	if T[0] == T[4] and T[0] == T[8] and T[2] != 0:
		return T[0]

	if T[2] == T[4] and T[2] == T[6] and T[2] != 0:
		return T[2]

	return 0


def estado_terminal(T):
	if utilidade(T) != 0:
		return True

	if 0 in T:
		return False
	
	return True


def alfabeta(T, alfa, beta, jog):
	if estado_terminal(T):
		return utilidade(T), -1, -1

	if jog:
		v = -10
		bestAction = -1
		for action in acoes(T):
			v1, ac, es = alfabeta(resultado(T, action, 'MAX'), alfa, beta, False)

			if v1 > v: # guardo a melhor acção para o Min
				v = v1
				bestAction = action

			alfa = max(alfa, v)

			if beta <= alfa:
				break

		return v, bestAction, resultado(T, bestAction, 'MAX')
	else:
		v = 10
		bestAction = 1
		for action in acoes(T):
			v1, ac, es = alfabeta(resultado(T, action, 'MIN'), alfa, beta, True)

			if v1 < v: # guardo a pior ação para o Max
				v = v1
				bestAction = action

			beta = min(beta, v)

			if beta <= alfa:
				break

		return v, bestAction, resultado(T, bestAction, 'MIN')


def joga_max(T):
	v, a, e = alfabeta(T, -10, 10, True)
	print('MAX joga para ', a)
	return e


def joga_min(T):
	v, a, e = alfabeta(T, -10, 10, False)
	print('MIN joga para ', a)
	return e


def joga_rand(T):
	x = random.choice(acoes(T))
	T[x] = -1
	print('RAND joga para ', x)
	
	return T


def joga_real(T):
	a = acoes(T)
	
	while True:
		jogada = int(input("Insira um elemento das ações: "))

		if jogada in a:
			T[jogada] = -1
			break

	print('REAL joga para ', jogada)
	
	return T


def jogo(p1, p2):
	# cria tabuleiro vazio
	T = [0] * 9
	
	mostra_tabuleiro(T)

	while acoes(T) != [] and not estado_terminal(T):
		T = p1(T)

		mostra_tabuleiro(T)
		
		if acoes(T) != [] and not estado_terminal(T):
			T = p2(T)
			mostra_tabuleiro(T)
	
	# fim
	if utilidade(T) == 1:
		print('Venceu o jog1')
	elif utilidade(T) == -1:
		print('Venceu o jog2')
	else:
		print('Empate')


jogo(joga_max, joga_min)
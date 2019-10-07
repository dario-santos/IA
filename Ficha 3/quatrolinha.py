import copy
import time
import random

def board_show(T):
	for i in range(0, len(T) - 3, 4):
		print(T[i], ' | ', T[i + 1], ' | ', T[i + 2], ' | ', T[i + 3])

	print('\n')


def board_actions(T):
	a = []

	for i in range(len(T)):
		if T[i] == 0:
			a.append(i)

	return a


def board_state(T):
	# lines
	for i in range(0, 9, 4):
		for j in range(i, i + 2):
			if T[j] == T[j + 1] and T[j] == T[j + 2] and T[j] != 0:
				return T[j]

	# columns
	for i in range(4):
		if T[i] == T[i + 4] and T[i] == T[i + 8] and T[i] != 0:
			return T[i]

	# diagonals
	for i in range(2):
		if T[i] == T[i + 5] and T[i] == T[i + 10] and T[i] != 0:
			return T[i]

	for i in range(2, 4):
		if T[i] == T[i + 3] and T[i] == T[i + 6] and T[i] != 0:
			return T[i]

	return 0


def is_terminal_state(T):
	if board_state(T) != 0:
		return True
	elif 0 in T:
		return False
	return True


def alfabeta_result(T, action, player):
	aux = copy.copy(T)
	
	if player == 'MAX':
		aux[action] = 1
	else: 
		aux[action] = -1
	
	return aux


def alfabeta(T, alfa, beta, player):
	if is_terminal_state(T):
		return board_state(T), -1, -1

	if player:
		v = -10
		bestAction = -1
		for action in board_actions(T):
			v1, ac, es = alfabeta(alfabeta_result(T, action, 'MAX'), alfa, beta, False)

			if v1 > v: # guardo a melhor acção para o Min
				v = v1
				bestAction = action

			alfa = max(alfa, v)

			if beta <= alfa:
				break
			
		return v, bestAction, alfabeta_result(T, bestAction, 'MAX')
	else:
		v = 10
		bestAction = 1
		for action in board_actions(T):
			v1, ac, es = alfabeta(alfabeta_result(T, action, 'MIN'), alfa, beta, True)

			if v1 < v: # guardo a pior ação para o Max
				v = v1
				bestAction = action

			beta = min(beta, v)

			if beta <= alfa:
				break

		return v, bestAction, alfabeta_result(T, bestAction, 'MIN')


def joga_max(board, value):
	v, a, e = alfabeta(board, -10, 10, True)
	# print('MAX plays to ', a)
	return e


def joga_min(board, value):
	v, a, e = alfabeta(board, -10, 10, False)
	# print('MIN plays to ', a)
	return e


def joga_rand(board, value):
	x = random.choice(board_actions(board))
	board[x] = value	
	return board


def joga_real(board, value):
	a = board_actions(board)
	
	while True:
		jogada = int(input("Insira um elemento das ações: "))

		if jogada in a:
			T[jogada] = value
			break

	print('JOGADOR joga para ', jogada)
	
	return board


def jogo(p1, p2):
	T = [0] * 12
	
	# board_show(T)

	while board_actions(T) != [] and not is_terminal_state(T):
		T = p1(T, 1)

		# board_show(T)
		
		if board_actions(T) != [] and not is_terminal_state(T):
			T = p2(T, -1)
			# board_show(T)
	
	return board_state(T)


def print_game_details(game_info):
	print("Wins")
	print("Player 1 ", game_info[0])
	print("Player 2 ", game_info[2])
	print("Draw ", game_info[1])


def main():	

	time_start = time.time()

	print("P1 = RAND, P2 = MIN")
	game_info = [0, 0, 0]
	for i in range(500):
		game_info[jogo(joga_rand, joga_min) + 1] +=1
		
	time_end = time.time()

	print_game_details(game_info)
	
	print("A seção demorou", int((time_end - time_start) / 60))




main()
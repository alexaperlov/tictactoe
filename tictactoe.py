class Player:
	def __init__(self, hasWon, tie):
		self.hasWon=hasWon
		self.tie = tie
	
	def move(self, board):
		moveInvalid = True
		
		#keep prompting player for a move until they enter valid coordinates
		while(moveInvalid):
			outOfRange = False
			move = input("please enter the coordinates of where you want to move")	
			try:
				move_list = move.split(',')
				for i in move_list:
					if int(i) < 0 or int(i) > 2:
						print("Invalid move, please enter coordinates within the range of 0 and 2")
						outOfRange = True
						break
				
				if(not outOfRange):
					if(board[int(move_list[0])][int(move_list[1])] == 0):
						moveInvalid = False
						board[int(move_list[0])][int(move_list[1])] = 2
					else:
						print("Invalid move, please enter a spot that's not already taken")
			except:
				print("Invalid move, please enter coma seperated coordinates")
			
		
		return(board)


class Computer(Player):

	def move(self, board):

		#check each row and see if there is 2 in a row --> computer wins 
		index1 = 0
		index2 = 0
		counter = 0
		one_counter = 0

		for i in board:
			for elements in i:
				if elements == 1:
					one_counter += 1
				if elements == 0 or elements == 2:
					index2 = counter
				counter += 1
			if one_counter == 2 and board[index1][index2] == 0:
				board[index1][index2] = 1
				self.hasWon = True
				return board

			counter = 0
			index1 +=1
			one_counter = 0


		#check each column and see if there is a 2 in a row --> computer wins
		index1 = 0
		index2 = 0
		one_counter = 0

		for i in range (0,3): 
			for j in range (0,3):
				if board[j][i] == 1:
					one_counter += 1
				if board[j][i] == 0 or board[j][i] == 2:
					index1 = j
					index2 = i
			if one_counter == 2 and board[index1][index2] == 0:
				board[index1][index2] = 1
				self.hasWon = True
				return(board)

			one_counter = 0



		#check each diagonal and see if there is a 2 in a row --> computer wins
		one_counter = 0
		index = 0
		for i in range(3):
			if board[i][i] == 1:
				one_counter += 1
			if board[i][i] == 0 or board[i][i] == 2:
				index = i

		if one_counter == 2:
			if board[index][index] == 0:
				board[index][index] = 1
				self.hasWon = True
				return board

		one_counter = 0
		index = 0
		index2 = 2
		for i in range(0, 3):
			if board[i][index2] == 1:
				one_counter += 1
			if board[i][index2] == 0 or board[i][index2] == 2:
				index1 = i
				index = index2
			index2 -= 1
		if one_counter == 2 and board[index1][index] == 0:
			board[index1][index] = 1
			self.hasWon = True
			return board


		#check each row and see if opponent has 2 in a row --> block
		index1 = 0
		index2 = 0
		two_counter = 0

		for i in board:
			for elements in i:
				if elements == 2:
					two_counter += 1
				if elements == 0:
					index2 = counter
				counter += 1
			if two_counter == 2 and board[index1][index2] == 0:
				board[index1][index2] = 1
				return board

			counter = 0
			index1 +=1
			two_counter = 0

		#check each column and see if opponent has 2 in a row --> block
		index1 = 0
		index2 = 0
		two_counter = 0

		for i in range (0,3): 
			for j in range (0,3):
				if board[j][i] == 2:
					two_counter += 1
				if board[j][i] == 0:
					index1 = j
					index2 = i
			if two_counter == 2 and board[index1][index2] == 0:
				board[index1][index2] = 1
				return(board)

			two_counter = 0

		#check each diagonal and see if opponent has 2 in a row --> block
		two_counter = 0
		index = 0
		
		for i in range(3):
			if board[i][i] == 2:
				two_counter += 1
			if board[i][i] == 0:
				index = i

		if two_counter == 2:
			if board[index][index] == 0:
				board[index][index] = 1
				return board

		two_counter = 0
		index = 0
		index2 = 2
		for i in range(3):
			if board[i][index2] == 2:
				two_counter += 1
			if board[i][index2] == 0:
				index1 = i
				index = index2
			index2 -= 1
		if two_counter == 2 and board[index1][index] == 0:
			board[index1][index] = 1

			return board

		#check if computer can make a fork
		for i in [0,2]:
			if board[0][i] == 1 and board[2][(i+2)%4] == 1:
				if board[2][i] == 0:
					board[2][i] = 1
					return board
				elif board[0][(i+2)%4] == 0:
					board[0][(i+2)%4] = 1
					return board
		
		#check if center is open
		if board[1][1] == 0:
			board [1][1] = 1
			return board

		#block opponent's fork
		for i in [0,2]:
			if board[0][i] == 2:
				if board[0][1] == 0:
					board[0][1] = 1
					return board
				elif board[2][i] == 0:
					board[2][1] = 1
					return board



		#if opponent is in a corner, check if opposite corner is open
		if board[0][2] == 2:
			if board[2][0] == 0:
				board[2][0] = 1
				return board
		if board[2][0] == 2:
			if board[0][2] == 0:
				board[0][2] = 1
				return board

		if board[0][0] == 2:
			if board[2][2] == 0:
				board[2][2] = 1
				return board

		if board[2][2] == 2:
			if board[0][0] == 0:
				board[0][0] = 1
				return board


		#else just check if any corner is free
		for i in [0,2]:
			for j in [0,2]:
				if board[i][j] == 0:
					board[i][j] = 1
					return board

		#else move on the side
		for i in [0,2]:
			if board[i][1] == 0:
				board[i][1] = 1
				return board
			elif board[1][i] == 0:
				board[1][i] = 1

		#else there are no more moves and the game is a tie
		self.tie = True
		return board

def replay():
	playAgain = input("Play again? (Y/N)")
	if(playAgain == "Y"):
		play()
	else:
		print("Thanks for playing!")

def play():
	print("Welcome to Tic Tac Toe!")
	print("You are '2' and the computer is '1'")
	board = [[0,0,0], [0,0,0], [0,0,0]]
	for i in board:
			print(i)
	computer = Computer(False, False)
	player = Player(False, False)

	playing = True

	while(playing):

		#player goes first
		board = player.move(board)
		print("Player's Move: ")
		for i in board:
			print(i)

		#computer goes next
		board = computer.move(board)
		
		#check if the game is a tie
		if computer.tie:
			print("Tie!")
			replay()
			break 
		#print the new board
		print("Computer's Move: ")
		for i in board:
			print(i)

		#check if the computer has won
		if computer.hasWon:
			playing = False
			print("The computer won")
			replay()
			break

if __name__ == "__main__":
	play()




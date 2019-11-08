from gameFunctions import gameVars

#need a function to run to compare the choices
#figure out what to pass into the functuin - hint => what are tou comparing?

##always check a breaking condiiton first
def compareChoices(player):
	if player == gameVars.computer:
#we have a tie! the game ends here
		print("tie, no one wins! Try again")
	
	elif player == "quit":
		print("Go on and quit then, quitter.")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("You Lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("You Lose!", gameVars.computer, "slices", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "scissors":
		if gameVars.computer == "rock":
			print("You Lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "slices", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

from random import randint
from gameFunctions import gameVars

# #These are our choices
# choices=["rock", "paper", "scissors"]

# #adding lives
# player_lives = 5
# computer_lives = 5

# #let the ai make a choice
# computer=choices[randint(0,2)]

# #set up a game loop here so we dont have to keep restarting
# player = False

def winorlose(status):
	#print("called win or lose function", status, "\n")
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False
		gameVars.computer= gameVars.choices[randint(0,2)]
#reset the game
	elif choice == "N" or choice == "n":
		print("You Decide to Leave... Come back Soon!")
		exit()
	else:
		print("Make a valid choice. Yes or no!")
		#recursive -> calling a function from inside itself
		winorlose(status)
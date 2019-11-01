#import the randomizer package to generate an ai choice
from random import randint

#These are our choices
choices=["rock", "paper", "scissors"]

#adding lives
player_lives = 5
computer_lives = 5

#let the ai make a choice
computer=choices[randint(0,2)]

#set up a game loop here so we dont have to keep restarting
player = False

def winorlose(status):
	print("called win or lose function", status, "\n")
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
		#reset the game
		player_lives = 1
		computer_lives = 1
		player = False
		computer = choices[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You Decide to Leave... Come back Soon!")
		exit()
	else:
		print("Make a valid choice. Yes or no!")

while player is False:
	print("=======================================")
	print("Computer Lives:", computer_lives)
	print("Player Lives:", player_lives)
	print("=======================================")
	print("Select Your Weapon!")
	player=input("chose rock, paper or scissors")

#start by doing some logic and condition checking
	print("computer: ", computer, "player", player)

#always check a breaking condiiton first
	if player== computer:
#we have a tie! the game ends here
		print("tie, no one wins! Try again")
	elif player == "quit":
		print("Go on and quit then, quitter.")
		exit()

	elif player == "rock":
		if computer == "paper":
			print("You Lose!", computer, "covers", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "paper":
		if computer == "scissors":
			print("You Lose!", computer, "slices", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("You won!", player, "slices", computer, "\n")
			computer_lives = computer_lives -1

	if player_lives is 0:
		winorlose("lose")
		# print("You Lost? How Shameful... Play Again?")
		# choice = input("Y / N")

		# if choice == "Y" or choice == "y":
		# #reset the game
		# 	player_lives = 5
		# 	computer_lives = 5
		# 	player = False
		# 	computer = choices[randint(0,2)]

		# elif choice == "N" or choice == "n":
		# 	print("You Decide to Leave... Come back Soon!")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or no!")

	if computer_lives is 0:
		winorlose("won")
		# print("You Won? Congratuations, Fate Smiles Upon You Today... Play Again?")
		# choice = input("Y / N")

		# if choice == "Y" or choice == "y":
		# #reset the game
		# 	player_lives = 5
		# 	computer_lives = 5
		# 	player = False
		# 	computer = choices[randint(0,2)]

		# elif choice == "N" or choice == "n":
		# 	print("You Decide to Leave... Come back Soon!")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or no!")


	else:
		player = False
		computer = choices[randint(0,2)]

	player = False
	computer=choices [randint(0,2)]
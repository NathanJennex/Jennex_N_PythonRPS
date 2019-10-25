from random import randint

#These are our choices
choices=["rock", "paper", "scissors"]

#let the ai make a choice
computer=choices[randint(0,2)]

#set up a game loop here so we dont have to keep restarting
player = False

while player is False:
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

	else:
		print("Not a tie. Now we can check other conditions")
		if player == "rock":
			print("check and see what the computer is, and win or lose")

	player = False
	computer=choices [randint(0,2)]
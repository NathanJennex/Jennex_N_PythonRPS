# #import the randomizer package to generate an ai choice
from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print("=======================================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("=======================================")
	print("Select Your Weapon!")
	player=input("choose rock, paper or scissors")
	compare.compareChoices(player)


	if gameVars.player_lives == 0:
		winlose.winorlose("lose")


	elif gameVars.computer_lives == 0:
		winlose.winorlose("won")


	else:
		player = False
		gameVars.computer = gameVars.choices[randint(0,2)]

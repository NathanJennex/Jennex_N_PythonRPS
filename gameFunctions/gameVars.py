from random import randint

# #These are our choices
choices=["rock", "paper", "scissors"]

#adding lives
player_lives = 5
computer_lives = 5

total_lives = 5

 #let the ai make a choice
computer=choices[randint(0,2)]

# #set up a game loop here so we dont have to keep restarting
player=False 
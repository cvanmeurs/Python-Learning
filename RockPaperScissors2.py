"""
Rock Paper Scissors 2

Our goal is to explore some options we have for breaking our initial
Rock Paper Scissors program into smaller chunks.

The game works like this:
- Initialize any game state we will need to keep track of.
- Enter the "main loop" of the game.
-   Greet the user.
-   If they have not set their name, ask for their name.
-   Enter the "rock paper scissors" loop
-     Play a round of rock, paper, scissors.
-       Get user selection
-       Decide a random CPU selection
-       Score the round
-       Tell the user the result.
-       Keep track of wins and losses.
-     Ask the user to play again.
-   When the player is done playing,
-     exit the "rock paper scissors" loop,
-     tell them the score, and
-     say goodbye.
"""

import random

gameActive = True
playerName = 0
playerSelection = 0
cpuSelection = 0
roundActive = True
answer = 0
numberOfWins = 0


while gameActive:
    while roundActive:  
        if playerName == 0:
            playerName = input("Hello!  Please enter your name:  ")
            print("Hello", playerName + "!") #the + eliminates the blank space between the variable value and the !
        
        if playerSelection == 0:
            playerSelection = input("Please choose rock, paper, or scissors:  ")
            print(playerName, "chose", playerSelection + ".")
#do some kind of animation or stall here
#       if cpuSelection == 0:
        cpuSelection = random.randint(1,4)

        if cpuSelection == 1:
            print("CPU chose rock.")
        elif cpuSelection == 2:
            print("CPU chose paper.")
        elif cpuSelection == 3:
            print("CPU chose scissors.")

        if playerSelection == "rock":
            if cpuSelection == 1:
                print("Draw!")
                roundActive = False
            elif cpuSelection == 2:
                print("You lost!")
                roundActive = False
            elif cpuSelection == 3:
                print("You won!")
                numberOfWins = numberOfWins + 1
                roundActive = False
        elif playerSelection == "paper":
            if cpuSelection == 1:
                print("You won!")
                numberOfWins = numberOfWins + 1
                roundActive = False
            elif cpuSelection == 2:
                print("Draw!")
                roundActive = False
            elif cpuSelection == 3:
                print("You lost!")
                roundActive = False
        elif playerSelection == "scissors":
            if cpuSelection == 1:
                print("You lost!")
                roundActive = False
            elif cpuSelection == 2:
                print("You won!")
                numberOfWins = numberOfWins + 1
                roundActive = False
            elif cpuSelection == 3:
                print("Draw!")
                roundActive = False
        

        if numberOfWins == 1:
            print("You have won 1 time!")
        elif numberOfWins >> 1:
            print("You have won", numberOfWins, "times!")

    answer = input("Do you want to play again? (y/n):  ")
    if answer == "y":
        playerSelection = 0
        cpuSelection = 0
        roundActive = True
    elif answer == "n":
        gameActive = False




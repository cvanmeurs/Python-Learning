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
roundActive = True
answer = 0
numberOfWins = 0

from enum import Enum
class Selection(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

validPlayerSelections = ["rock", "paper", "scissors"]

# TODO: I don't love this name. It's pretty awkward. Should we call "selections" "hands"?
stringToSelection = { "rock" : Selection.Rock,
                      "paper" : Selection.Paper,
                      "scissors" : Selection.Scissors }

def getPlayerSelection():
    print("Please choose rock, paper, or scissors.")
    playerSelectionIsValid = False
    while not playerSelectionIsValid:
        selection = input("Your selection:  ")
        playerSelectionIsValid = selection in validPlayerSelections
        if not playerSelectionIsValid:
            print(selection, "is not a valid selection. Please try again.")
    return stringToSelection[selection]

while gameActive:
    while roundActive:  
        print("Beginning of round")

        if playerName == 0:
            playerName = input("Hello!  Please enter your name:  ")
            print("Hello", playerName + "!") #the + eliminates the blank space between the variable value and the !
        
# TODO do some kind of animation or stall here

        playerSelection = getPlayerSelection()
        cpuSelection = Selection(random.randint(1,3))

        if cpuSelection == Selection.Rock:
            print("CPU chose rock.")
        elif cpuSelection == Selection.Paper:
            print("CPU chose paper.")
        elif cpuSelection == Selection.Scissors:
            print("CPU chose scissors.")

        if playerSelection == Selection.Rock:
            if cpuSelection == Selection.Rock:
                print("Draw!")
                roundActive = False
            elif cpuSelection == Selection.Paper:
                print("You lost!")
                roundActive = False
            elif cpuSelection == Selection.Scissors:
                print("You won!")
                numberOfWins = numberOfWins + 1
                roundActive = False
        elif playerSelection == Selection.Paper:
            if cpuSelection == Selection.Rock:
                print("You won!")
                numberOfWins = numberOfWins + 1
                roundActive = False
            elif cpuSelection == Selection.Paper:
                print("Draw!")
                roundActive = False
            elif cpuSelection == Selection.Scissors:
                print("You lost!")
                roundActive = False
        elif playerSelection == Selection.Scissors:
            if cpuSelection == Selection.Rock:
                print("You lost!")
                roundActive = False
            elif cpuSelection == Selection.Paper:
                print("You won!")
                numberOfWins = numberOfWins + 1
                roundActive = False
            elif cpuSelection == Selection.Scissors:
                print("Draw!")
                roundActive = False
        

        if numberOfWins == 1:
            print("You have won 1 time!")
        elif numberOfWins >> 1:
            print("You have won", numberOfWins, "times!")

    answer = input("Do you want to play again? (y/n):  ")
    if answer == "y":
        roundActive = True
    elif answer == "n":
        gameActive = False




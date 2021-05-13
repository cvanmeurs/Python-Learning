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

validPlayAgainAnswers = ["y", "n"]
def getPlayAgain():
    answerIsValid = False;
    while not answerIsValid:
        answer = input("Do you want to play again? (y/n):  ")
        answerIsValid = answer in validPlayAgainAnswers
        if not answerIsValid:
            print(answer, "is not a valid selection. Please choose y or n.")
    return answer



class RoundResult(Enum):
    Draw = 1
    Win = 2
    Loss = 3

def scoreRound(player, cpu):
    if player == cpu:
        return RoundResult.Draw

    if player == Selection.Rock:
        if cpu == Selection.Paper:
            return RoundResult.Loss
        else:
            return RoundResult.Win
    
    if player == Selection.Paper:
        if cpu == Selection.Scissors:
            return RoundResult.Loss
        else:
            return RoundResult.Win

    if player == Selection.Scissors:
        if cpu == Selection.Rock:
            return RoundResult.Loss
        else:
            return RoundResult.Win

def printRoundInfo(name, playerHand, cpuHand, roundResult, winCount):
    print(name, "chose", playerHand.name.lower() + ".")
    print("CPU chose", cpuHand.name.lower() + ".")
    if roundResult == RoundResult.Draw:
        print ("Draw!")
    elif roundResult == RoundResult.Win:
        print ("Win!")
    elif roundResult == RoundResult.Loss:
        print("Loss!")
    if winCount == 1:
        print("You have won 1 time!")
    elif winCount >> 1:
        print("You have won", winCount, "times!")

gameActive = True
numberOfWins = 0
playerName = input("Hello!  Please enter your name:  ")
print("Hello", playerName + "!") #the + eliminates the blank space between the variable value and the !

while gameActive:
    # TODO do some kind of animation or stall here
    playerSelection = getPlayerSelection()
    cpuSelection = Selection(random.randint(1,3))
    result = scoreRound(playerSelection, cpuSelection)
    if (result == RoundResult.Win):
        numberOfWins = numberOfWins + 1

    printRoundInfo(playerName, playerSelection, cpuSelection, result, numberOfWins)

    answer = getPlayAgain()
    if answer == "n":
        gameActive = False




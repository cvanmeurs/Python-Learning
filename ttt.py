#from random import *
import time
import random

"""Player enters name
player chooses X or O
show game board
determine who goes first
when it's the player's turn, select 0-8
convert string to int
Determine if space is blank
if it is, place X or O
if it's not, have them choose again
determine if there are 3 in a row
...

def getValidBoxSelection(initialValue):
    #TODO: Actually validate it
    intValue = int(initialValue)
    return intValue


while True:
    userInput = input("Enter something:  ")
    print("You entered", userInput)

    if userInput == "quit":
        quit()

    boxSelection = getValidBoxSelection(userInput)

    print(boxSelection)
"""


#  0 1 2
#  3 4 5
#  6 7 8

#I will use this later for the proper main game loop


def pause(seconds):
    time.sleep(seconds)

# get column number
def print_mod(a,b):
    print(a, "mod", b, "is", a%b)

def column(num):
    return num%3

# get row number
def print_div(a,b):
    print(a, "div", b, "is", a//b)

def row(num):
    return num//3


# print the values of each row and column
def print_row_and_column(num):
    print("The value of row", row(num), "and column", column(num), "is:", num) 

# call the function for numbers 0-8; add the values to an array





"""
while gameActive:
    while winCondition == False:
"""

def greetPlayer():
    print("Welcome to Tic-Tac-Toe!")
    #time.sleep(1) #1 second delay
    pause(1.5)
    playerName = input("Please enter your name: ")
    pause(.5)
    print("Hello", playerName + "!")
    nameEntered = True
    return playerName # this is what lets the variable be accessible outside of this function



def playerMakesSelection():
    playerSelection = input("Please select X or O: ")
    pause(.5)
    print(playerName, "chose", playerSelection.upper() + ".")
    return playerSelection

#assign CPU Selection

def cpuMakesSelection():
    if playerSelection.upper() == "X":
        cpuSelection = "O"
    elif playerSelection.upper() == "O":
        cpuSelection = "X"
    print("CPU will be", cpuSelection + ".")

    return cpuSelection




def index_of(row, column, width):
    # Return a number from 0 to 8
    """if column == 0:
        return (row * 3) + column
    elif column == 1:
        return (row * 3) + column
    elif column == 2:
        return (row * 3) + column"""
    return (row * width) + column

def printBox(width, values):
    #print("The width is: ", width)
    #print("")
    for row in range(width):

        for column in range(width):
            index = index_of(row, column, width)
            value = values[index]
            #print(f'{value:02} ', end="")
            print(value, end=" ")
        print("")

#show the player the selections they can make and draw the current game board
def showBoard(size):
    print()
    printBox(size, ["0", "1", "2", "3", "4", "5", "6", "7", "8"])
    print()
    #printBox(size, array)
    #print()

def showCurrent(size):
    printBox(size, array)
    print()

# player chooses space
def playerTurn():
    playerChoice = input("Please choose a space to place your X or O: ")
    pause(.5)
    print("You chose space #" + playerChoice + ".")
    # Check to see if that space is available
    if array[int(playerChoice)] == "-":
        # Add the player's X or O to the space they chose, as an integer.
        array[int(playerChoice)] = playerSelection
    else:
        print("Space occupied.  Please choose another.") # this is not returning to the top of the loop!!!!!
#    turns = turns + 1  # something is going wrong here.....................................
#    return playerChoice


    # CPU chooses random number from 0 to 8 
def cpuTurn():
    print("CPU will now make a choice.")
    cpuChoice = random.randint(0, 8)
    pause(2)
    # Check to see if CPUchoice is available
    while array[int(cpuChoice)] != "-":
        print("CPU chose an occupied space; choosing again...")
        pause(.5)
        cpuChoice = random.randint(0, 8)
    print("CPU chose space #" + str(cpuChoice) + ".") #have to convert cpuChoice to string
    pause(1)
    array[int(cpuChoice)] = cpuSelection
#    return cpuChoice

def isEven(number):
    return number%2 == 0


gameActive = True
winCondition = False
nameEntered = False
#playerName = "blank"
turns = 0
array = []
for x in range(9):
    #print_row_and_column(x)
    array.append("-")

def gameIsOver(array, turns):
    return turns >= 9


# --- BEGIN GAME ---

# TODO: Randomize who goes first.
#while gameActive:
if nameEntered == False:
    #greetPlayer() # This is NOT how you do it
    playerName = greetPlayer()

pause(1)
playerSelection = playerMakesSelection()
pause(1)
cpuSelection = cpuMakesSelection()
pause(1)

while !gameIsOver(array, turns):
    isPlayerTurn = isEven(turns)
    showBoard(3)
    showCurrent(3)
    if isPlayerTurn == True:
        playerTurn()
    else:
        cpuTurn()
    turns = turns + 1  # increment the number of turns taken
    pause(1)
    print()
showCurrent(3)
print("The game is over!")


# if no win condition and there's still room on the board
while winCondition == False:
    while turns < 9:
        isPlayerTurn = isEven(turns)
        showBoard(3)
        showCurrent(3)
        if isPlayerTurn == True:
            playerTurn()
            turns = turns + 1  # increment the number of turns taken
        else:
            cpuTurn()
            turns = turns + 1  # increment the number of turns taken


# NEED TO CHECK NUMBER OF TURNS AFTER EACH TURN
        pause(1)

        print()
    # add else statement
# win condition = function
    if turns >= 9:
        winCondition = True
        print("The game is over!")  # this isn't working


"""
array2 = [1, "cheese", 3.72]
print("The first array is a ", type(array))
print(array2)
array2[2] = "nachos"
print(array2)
print(array2[2])
print(index_of) """

"""#this prints the array and replaces the dash with an X at index position 5
array[5] = "X"
print()
printBox(3, array)

array[1] = "O"
print()
printBox(3, array)"""

# same as above, but this prints the array with the player selection (X or O) at the specified index
# array[chosenIndex] = playerSelection

"""" sequence of events

#) greet the player and ask them to enter their name; store it as a variable

1) show the player the game board with the index numbers
2) ask the player to choose an index number to place their X or O
3) make sure the space is a dash; if it's not, ask them to choose again
4) print the array with the updated choice
5) check win condition (how?)
6) CPU turn (random number selection?); slow this portion down a bit
7) (Generate random number between 0 and 8; check to see if that index is a dash; if not
do it again; if it is, then add the CPUselection to the array)
8) check win condition again (this should be a function)
9) go back to player turn (also should probably be a function, as well as the CPU turn; in fact the entire
game should probably be a loop of functions)
?) Should the player choose a number between 1 and 10 to see who goes first?  (random number gen; check to see
who is closest; if a tie, do another random number and check again)
"""
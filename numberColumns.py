
"""In a loop, reads user input
"""

while True:
    userInput = input("Enter something:  ")
    print("You entered", userInput)

    if userInput == "quit":
        quit()

        
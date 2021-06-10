
gameIsGoing = True
"""print(str.lower)
print("Foo".lower)
print("Foo".lower())"""

while gameIsGoing:
    name = input("Enter a name:   ")
    if name.lower() != "exit":
        print(name)
    if name.lower() == "exit":
#        exit()
        gameIsGoing = False
    print("End of Loop")


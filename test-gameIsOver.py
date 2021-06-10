def gameIsOver(board, turns):
    return True

def test(board, turns, expectedValue):
    isGameOver = gameIsOver(board, turns)
    print()
    printBox(board)
    if isGameOver == expectedValue:
        print("Success!", turns, expectedValue)
    else:
        print("Failure!", turns, expectedValue)

def index_of(row, column, width):
    return (row * width) + column

def printBox(values):
    for row in range(3):
        for column in range(3):
            index = index_of(row, column, 3)
            value = values[index]
            print(value, end=" ")
        print("")


test(["O", "O", "O", "X", "X", "-", "-", "-", "-"], 5, True)
test(["O", "-", "O", "X", "X", "-", "-", "-", "-"], 4, False)




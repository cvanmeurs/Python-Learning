def winInRow(row, board):
    column_0 = index_of(row, 0)
    column_1 = index_of(row, 1)
    column_2 = index_of(row, 2)
    isNotBlank = board[column_0] == O or board[column_0] == X
    isTheSameInAllColumns = (
        board[column_0] == board[column_1] and board[column_1] == board[column_2]
    )
    return isNotBlank and isTheSameInAllColumns


def winInColumn(column, board):
    return False


def winTopLeftToBottomRight(board):
    return False


def winBottomLeftToTopRight(board):
    return False


def outOfTurns(turns):
    return turns >= 9


def gameIsOver(board, turns):
    # There are 8 win conditions:
    #     Win in the nth row
    #     Win in the nth column
    #     Win in one of the two diagonals
    # And one "end game" non-win condition, a full board
    if winInRow(0, board):
        return True
    if winInRow(1, board):
        return True
    if winInRow(2, board):
        return True
    if winInColumn(0, board):
        return True
    if winInColumn(1, board):
        return True
    if winInColumn(2, board):
        return True
    if winTopLeftToBottomRight(board):
        return True
    if winBottomLeftToTopRight(board):
        return True
    if outOfTurns(turns):
        return True
    return False


def test(board, turns, expectedValue):
    isGameOver = gameIsOver(board, turns)
    if isGameOver != expectedValue:
        print()
        print("Test failed.")
        printBox(board)
        print("Expected isGameOver to be", expectedValue)
        print()


def index_of(row, column):
    return (row * 3) + column


def printBox(values):
    for row in range(3):
        for column in range(3):
            index = index_of(row, column)
            value = values[index]
            print(value, end=" ")
        print("")


O = "O"
X = "X"
B = "-"

# test(["O", "O", "O", "X", "X", "-", "-", "-", "-"], 5, True)
# test(["O", "-", "O", "X", "X", "-", "-", "-", "-"], 4, False)

# Win in the 0th row
test([O, O, O, X, X, B, B, B, B], 0, True)
# Win in the 1th row
test([O, O, B, X, X, X, B, B, B], 0, True)
# Win in the 2th row
test([O, O, B, B, B, B, X, X, X], 0, True)
# Win in the 0th column
test([O, X, B, O, X, B, O, B, B], 0, True)
# Win in the 1th column
test([O, X, B, O, X, B, B, X, B], 0, True)
# Win in the 2th column
test([O, B, X, O, B, X, B, B, X], 0, True)
# Win bottom left to top right
test([O, B, X, O, X, B, X, B, B], 0, True)
# Win top left to bottom right
test([X, B, O, O, X, B, B, B, X], 0, True)

# Nobody wins, but game is over
test([X, O, X, O, X, O, O, X, O], 9, True)

# Game is not over
test([B, B, B, B, B, B, B, B, B], 0, False)
# Game is not over
test([X, B, B, B, B, B, B, B, B], 0, False)
# Game is not over
test([X, B, B, B, O, B, B, B, B], 0, False)
# Game is not over
test([X, B, X, B, O, B, B, B, B], 0, False)
# Game is not over
test([X, O, X, B, O, B, B, B, B], 0, False)
# Game is not over
test([X, O, X, B, O, B, B, X, B], 0, False)

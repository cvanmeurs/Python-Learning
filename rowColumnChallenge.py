
    #Write the body of this function.


def index_of(row, column, width):
    # Return a number from 0 to 8
    """if column == 0:
        return (row * 3) + column
    elif column == 1:
        return (row * 3) + column
    elif column == 2:
        return (row * 3) + column"""
    return (row * width) + column

"""#column0
print(index_of(0, 0))
print(index_of(1, 0))
print(index_of(2, 0))

#column1
print(index_of(0, 1))
print(index_of(1, 1))
print(index_of(2, 1))

#column2
print(index_of(0, 2))
print(index_of(1, 2))
print(index_of(2, 2))"""

#width = 5



def printBox(width):
    print("The width is: ", width)
    print("")
    for row in range(width):

        for column in range(width):
            index = index_of(row, column, width)
    #        print("The value of row", row, "and column", column, "is", f'{index:02}')
            print(f'{index:02} ', end="")
        print("")


for size in range(1, 11):
    print("The size is: ", size)
    printBox(size)
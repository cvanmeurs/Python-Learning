from enum import Enum
class Selections(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

print("The 1th Selection is", Selections(1))
print("The 2nd Selection is", Selections(2))
print("The 3rd Selection is", Selections(3))

# advent day 2

from pprint import pprint

filename = "input_02.txt"

with open(filename) as f:
    content = f.readlines()

#print(content)


myDictionary = {}

for x, y in range(0, 999):
    myDictionary.update({str(x):int(y)})

print(myDictionary)
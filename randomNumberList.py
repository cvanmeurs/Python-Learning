import random


numberList = []
length = 0

if length < 5:
	randNum = random.randint(0, 100)
	numberList.append(randNum)
	length + 1
	print("Added to List:", randNum)
else:
	print("Done")

#print(numberList)


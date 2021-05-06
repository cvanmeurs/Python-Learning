import random

numberList = []

total = 0

while total < 100:
	randNum = random.randint(0, 10)
	numberList.append(randNum)
	total = total + randNum



print ("List of numbers:", numberList)
print ("Total is:", total)
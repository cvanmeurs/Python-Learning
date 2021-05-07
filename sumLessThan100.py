import random

numberList = []

total = 0

while total < 100:
	randNum = random.randint(0, 10)
		#if randNum = 
	numberList.append(randNum)
	print("Generated number is: ", randNum)
	total = total + randNum


#while total > 100:
#	numberList = numberList[:-1]



print ("List of numbers:", numberList)
print ("Total is:", total)
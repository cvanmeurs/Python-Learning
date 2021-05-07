import random

numberList = []
total = 0

while total < 100:
	randNum = random.randint(0, 10) #generate a random number between 0 and 10
	numberList.append(randNum) #add the random number to a list called randNum
	print("Generated number is: ", randNum)
	total = total + randNum #add the generated number to the total



if total > 100:
	numberList = numberList[:-1] #remove the last number if the total is greater than 100




print ("List of numbers:", numberList)
print ("Total is:", total)
# advent day 1

from pprint import pprint

filename = "advent21_day01-input.txt"

with open(filename) as f:
    content = f.readlines()


# store the text file as a list variable
mylist = []

for n in content:
	mylist.append(int(n))

# verify that it's working by accessing an index in the list
#print(mylist[1])

# Determine length of list
#print(len(mylist))  #<--- it's 2,000 long


# Here I'm figuring out the main logic...
"""
value1 = mylist[1]
value2 = mylist[2]

if value2 > value1:
	print("increased")
elif value1 >  value2:
	print("decreased")
"""



# Main Loop

for i in mylist:
	length = len(mylist)
	turn = 0
	answer = 0
	while turn <= length-2:

		currentValue = mylist[turn]
		nextValue = mylist[turn+1]
		#print(currentValue)
		#print(nextValue)
		if nextValue > currentValue:
			#print("Increased")
			answer = answer+1
		#elif nextValue < currentValue:
			#print("Decreased")
		turn += 1

print(answer)
	
#print(1)
#print(2)
#print(3)
#print(4)
#print(5)
#print(6)
#print(7)
#print(8)
#print(9)
#print(10)  # prints the numbers 1-10, each number on a new line

"""
# print the numbers from 1 to 10
number = 1

while number <= 10:
	print(number)
	number = number + 1 # increment the number; repeats until number is 11 and then stops

print(number) # displays 11; the number DID increment, but the loop stopped running at that point
"""

"""
# print the EVEN numbers from 1 to 10
number = 1

while number <= 10:
	if number % 2 == 0:  # is divisible by two (with no remainder; "mod 2")
		print(number)
	number = number + 1 # increment the number; repeats until number is 11 and then stops
"""

"""
# print the ODD numbers from 1 to 10
number = 1

while number <= 10:
	if number % 2 != 0:  # not divisible by 2
		print(number)
	number = number + 1 # increment the number; repeats until number is 11 and then stops
"""

# ask for a list of names until the list contains 3 names, then stop and print the list of names
my_list = []

while len(my_list) < 3:
	new_name = input("Please add a new name: ").strip().capitalize()
	my_list.append(new_name)

print("Sorry, the list is full!")
print(my_list)
"""

#range(1,11) # up to but not including 11

# [1,2,3,4,5,6,7,8,9,10]

for number in range(1,11):
	print(number)

# prints numbers from 1 to 10, as in the while example, but in only two lines of code

for letter in "abcd":
	print(letter)

# prints a, b, c, and d on a new line

for number in range(1,11,2): # step of 2; prints every other number (beginning with 1)
	print(number)

"""


"""
# determine the number of vowels and consonants in a given word

#word = "Hello"
word = input("Please enter a word: ") # ask the user for a word
vowels = 0
consonants = 0

for letter in word:
	if letter.lower() in "aeiou":
		vowels = vowels + 1
	elif letter == " ":
		pass  #if letter is a space, do nothing (pass!)  PASS!!!
	else:
		consonants = consonants + 1

print("The word is", word + ".")
print("There are {} vowels.".format(vowels))
print("There are {} consonants.".format(consonants))
"""

"""
# create a dictionary of male and female students (2 keys)
students = {
	"male": ["Tom", "Charlie", "Harry", "Frank"],
	"female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

# print the name of the student IF the letter "a" appears in the name
for key in students.keys():  #key becomes either male or female
	#print(key)  # prints male and female on their own line
	#print(students[key]) # prints two lists; male students on first line, and female on the second
	for name in students[key]:
		if "a" in name:
			print(name) 
"""

# List Comprehension

# create a list containing all the even numbers between 1 and 100 and print it
#even_numbers = [x for x in range(1,101) if x % 2 == 0]  # variable "x" loops through from 1 to 100, only kept if even
#print(even_numbers)
#odd_numbers = [y for y in range(1,101) if y % 2 != 0]
#print(odd_numbers)

# list comprehensions also work for other data types, including strings

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer) # the words are printed in upper case, then lower case, then the length for each is given; each 3 is its own list item within a list



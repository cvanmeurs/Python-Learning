"""
A = "part"
B = 1

# .format automatically converts whatever data type into a string
# you can put index numbers into the curly brackets to change the order that A, B etc are printed
print("{1} - {0}".format(A,B))

# if they are left blank it will assume the standard order A,B,etc
print("{} - {}".format(A,B))
"""


"""
# First, create a variable called start, and set it equal to "I am ".
# Remember the space after the word "am" !
start = ("I am ")

# Next, create a variable called age and set it equal to your age in years.
# This must be a number
age = int(43)

# Next, create a variable called end, and set it equal to " years old".
# Remember the space before the word "years"
end = " years old"

# Next, create a variable called output and use {} symbols and the format() function to stick the start, age and end variables
# together to make a string.
output = "{}{}{}".format(start,age,end)

# An example output string would be "I am 15 years old"


# Finally, print the output to the screen using the print() function.
print(output)
"""


"""
name = input("What is your last name? ").strip()

print(len(name))

print(name)
#strip() does NOT remove spaces from middle of last name; length of Van Meurs is 9 and counts the space!
"""


"""
# accessing the index number of a string
word = "supercalafragalisticexpealadocious"
output = word[2]
#print(output)
# prints the letter p

#output2 = word[start:end:step]  <-- specify beginning index, end index (next letter really), and the increments to step through
# start = index of first letter
# end = index of letter immediately following the one you want to stop at
# step = put a 2 here so it skips every other letter, so instead of "super" we'd get "spr"
# so to pull out the word "super" we need to...
output2 = word[0:5:1]

#print(output2)

# pull out the portion 'cali'
output3 = word[5:9:1]
#print(output3)

# the following prints the portion starting at where cala starts and ends where fraga begins, in increments of 1 (default)
print(word[word.index("cala"):word.index("fraga")])
"""



# Section 6
# =========


# Booleans

# if statements




# Section 7
# =========


# LISTS 

# lists are formed with angle brackets []
# Python lists can contain different variable types in the same list

#our_list = [1, 2, 3, "A", "B", "C"]
#print(our_list)

# lists can contain other lists
# nested lists can emulate tables

#our_table = [ [1,2,3], [4,5,6], [7,8,9]]

#print(our_table[0])  # prints the first index which is a list contatining 1,2,3
#print(our_table[1])  # prints the second index (4,5,6)
#print(our_table[2])  # prints the third

""" OUTPUT

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]  """

# To access a list inside a list

#print(our_table[0][1])  # from list element at index 0 (ie [1, 2, 3]), access index 1 (which is '2')

""" OUTPUT

2   """

# In this way, the first number [0] can be thought of as the row number, and the second [1] the column number when looking at
# the 3x3 grid of numbers above (starting in the upper left and counting down for rows, and across to the right for columns)



# in

#L = [1,5,2,6,2,9]
#print(2 in L) # checks to see if 2 is in the list L; returns True or False

""" OUTPUT

True """   # 2 is in the list so the return is True

#print(10 in L)

""" OUTPUT

False """  # 10 is not in the list so the return is False

#del L[0]  # del is used to remove a specific index when you don't know the value


# other ways to add to list

#A = [0, 8, 0, 9, 7]

#A = A + [8]  # adds 8 to the list; requires square brackets or it won't work.  Works like append

#print(A)  # results in [0, 8, 0, 9, 7, 8] being printed to the screen

# you can ONLY add lists to lists

#A = A + list("BCD") # adds each letter as its own element in the list
#print(A) # results in [0, 8, 0, 9, 7, 8, 'B', 'C', 'D'] printed to the screen; each letter is its own list entry/index

#A = A + [1, 2, 3] # adds the numbers 1, 2, and 3 as individual list entries
#print(A) # results in [0, 8, 0, 9, 7, 8, 'B', 'C', 'D', 1, 2, 3] printed to the screen

#A = A + list("456")  # not the correct way to add numbers; this adds them as string values not integers
#print(A)  # results in [0, 8, 0, 9, 7, 8, 'B', 'C', 'D', 1, 2, 3, '4', '5', '6']; the last 3 numbers are strings!

# to insert a number at a specific place
#A.insert(6,43)  # inserts 43 at index 6
#print(A) # results in [0, 8, 0, 9, 7, 8, 43, 'B', 'C', 'D', 1, 2, 3, '4', '5', '6'] printed to the screen

# Lists ARE mutable - you can add numbers to them without having to redefine them like you do with strings (A = A + list("string"))


# TUPLES

# tuples are immutable (like strings) and cannot be changed after they are defined. Useful for assignign permanent data.

#our_tuple = (1,2,3,"A","B","C") # works without parenthesis, but it's common practice to use them for tuples
#print(type(our_tuple))

#print(our_tuple[0:3]) # prints only the first 3 elements of the tuple, from index zero to 3 (but not including 3)


# DICTIONARIES  (key and value pairs)
"""
students = {}  # curly brackets for dictionaries

students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":22} # each 'key' is a string; each 'value' is an int
print(students)

print((students)["Dan"])  # will print the value associated with the Dan key
# results in printing 21 to the screen

students["Christian"] = 43  # appends another entry to the end of the dictionary
print(students)

#del students["Christian"] # removes the key 'Christian' and its value
#print(students)

students["Christian"] = 44 # updates value of existing key 'Christian'
print(students)

# so apparently you cannot have two keys with the same name; the second entry will overwrite the first

# dictionary values can be lists

# see students.py

"""


# Section 8 - Loops
# =========

# WHILE LOOPS

# while.py

# baby.py

# FOR LOOPS

# for.py

# LIST COMPREHENSION

# pig.py

# "pass" and "break"
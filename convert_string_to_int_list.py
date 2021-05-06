#!/usr/bin/env python

# Goal of this program is to:
# Convert the string "10 20 30 40"
# Into the array of integers [10, 20, 30, 40]

string = "10 20 30 40"
list_of_strings = string.split(" ")

list_of_numbers = []
for string in list_of_strings:
    list_of_numbers.append(int(string))

another_list_of_numbers = []
another_list_of_numbers.append(10)
another_list_of_numbers.append(20)
another_list_of_numbers.append(30)
another_list_of_numbers.append(40)

yet_another_list_of_numbers = []
yet_another_list_of_numbers.append(int("10"))
yet_another_list_of_numbers.append(int("20"))
yet_another_list_of_numbers.append(int("30"))
yet_another_list_of_numbers.append(int("40"))

print(list_of_strings)             # ['10', '20', '30', '40']
print(list_of_numbers)             # [10, 20, 30, 40]
print(another_list_of_numbers)     # [10, 20, 30, 40]
print(yet_another_list_of_numbers) # [10, 20, 30, 40]

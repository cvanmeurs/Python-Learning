#!/usr/bin/env python

# Goal of this program is to:
# Start with a lists/arrays of integers (e.g. [10, 20, 30, 40])
# Print the sum of all the numbers in the list/array

list_of_numbers = [10,20,30,40]

def compute_the_sum_of_numbers(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum = sum + number
    return sum

print("The sum of the numbers in this array",
      list_of_numbers,
      "is",
      compute_the_sum_of_numbers(list_of_numbers))


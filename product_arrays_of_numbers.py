#!/usr/bin/env python

# Goal of this program is to:
# Start with a lists/arrays of integers (e.g. [10, 20, 30, 40])
# Print the product of all the numbers in the list/array

def compute_the_product_of_numbers(list_of_numbers):
    product = 0
    for number in list_of_numbers:
        product = product * number
    return product

my_numbers = [10,20,30,40]
print("The product of the numbers in this array",
      my_numbers,
      "is",
      compute_the_product_of_numbers(my_numbers))


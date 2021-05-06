#!/usr/bin/env python

# Goal of this program is to:
# Start with lots of lists of integers (e.g. [10, 20, 30, 40])
# For each list of integers,
#   print the list of integers AND
#   print the sum of all the numbers in the list




def compute_the_sum_of_numbers(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum = sum + number
    return sum

def print_list_info(list_of_numbers):
    print("The sum of the numbers in this list", list_of_numbers, "is", compute_the_sum_of_numbers(list_of_numbers))


# list1 = [1,2,43,4]
# list2 = [0,0,0,0,0,0]
# list3 = [10102,21030,54045,4300202]
# list4 = [10102,21030,54045,4300202]
# list5 = [10,20,30,40]
# all_my_lists = [ list1, list2, list3, list4, list5 ]

all_my_lists = [[1,2,43,4],
                [0,0,0,0,0,0],
                [10102,21030,54045,4300202],
                [10102,21030,54045,4300202],
                [10,20,30,40]]

for l in all_my_lists:
    print_list_info(l)


# print("The sum of the numbers in this array",
#       list1,
#       "is",
#       compute_the_sum_of_numbers(list1))

# print("The sum of the numbers in this array",
#       list2,
#       "is",
#       compute_the_sum_of_numbers(list2))

# print("The sum of the numbers in this array",
#       list3,
#       "is",
#       compute_the_sum_of_numbers(list3))

# print("The sum of the numbers in this array",
#       list4,
#       "is",
#       compute_the_sum_of_numbers(list4))

# print("The sum of the numbers in this array",
#       list5,
#       "is",
#       compute_the_sum_of_numbers(list5))

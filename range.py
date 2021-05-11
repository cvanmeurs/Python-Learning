#!/usr/bin/env python

# Python's range function
 
print(list(range(10)))
print(list(range(1, 11)))
print(list(range(0, 30, 5)))
print(list(range(0, 10, 3)))
print(list(range(0, -10, -1)))
print(list(range(0)))
print(list(range(1, 0)))

# print(list(range(0, -10, 0))) # ValueError

print(range(10)[0])
print(range(10)[1])
print(range(10)[2])

# print(range(10)[10]) # IndexError: range object index out of range

def print_mod(a, b):
    print(a, "mod", b, "is : ", a%b )

for number in range(100):
    print_mod(number, 12)


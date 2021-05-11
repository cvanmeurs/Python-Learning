#!/usr/bin/env python
#
# Modular Arithmetic
# "What is the remainder after integer division?"
# a % b == the remainder of a divided by b
# % is called the modulus operator.
# 

def print_mod(a, b):
    print(a, "mod", b, "is : ", a%b )

print_mod(5, 12)
print_mod(17, 12)
print_mod(25, 12)
print_mod(2817891, 100)

def is_even(a):
    return a%2 == 0

def is_divisible_by(a, b):
    return a%b == 0

def print_is_divisible(a,b):
    print("Is", a, "divisible by", b, "?", is_divisible_by(a,b))

print_is_divisible(4,2) # true
print_is_divisible(5,2) # false

print_is_divisible(5, 12)
print_is_divisible(17, 12)
print_is_divisible(25, 12)
print_is_divisible(2817891, 100)
print_is_divisible(2817800, 100)

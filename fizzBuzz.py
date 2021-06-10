# Fizz Buzz!

# Print all the numbers between 1 and 100
# If the number is divisible by 3, print "Fizz"
# If the number is divisible by 5, print "Buzz"
# If the number is divisible by 3 AND 5, print "FizzBuzz"


for x in range(1, 101):
	if x%3 == 0 and x%5 == 0:
		print("FizzBuzz")
	elif x%3 == 0:
		print("Fizz")
	elif x%5 == 0:
		print("Buzz")
	else:
		print(x)


#    elif x%3 != 0 and x%5 != 0:
#       print(x)

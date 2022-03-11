# Outline:  
# 1) Ask the user their name.

name = input("What is your name?: ")

# 2) Ask the user their age.

age = input("How old are you?: ")

# 3) Ask the user where the live (city).

city = input("What city do you live in?: ")

# 4) Ask the user what they enjoy doing.

love = input("What do you love to do?: ")

#print("=" * 20)
#print(name)
#print(age)
#print(city)
#print(love)
#print("=" * 20)

# 5) Create output text.

#A = "part"
#B = 1
#"{} - {}".format(A,B)

string = "Your name is {} and you are {} years old.  You live in {} and you love {}."
output = string.format(name, age, city, love)



# 6) Print output text to screen.

print(output)
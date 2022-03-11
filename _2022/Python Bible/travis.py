# Travis the ridiculous security system

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

#print(len(known_users))  # prints the number of elements in the list ("length"), which is 8

while True:
	print("Hi! My name is Travis.") 
	name = input("What is your name?: ").strip().capitalize()  # you can use more than one method

	if name in known_users:  # checks whether entered name is in the list or not
		#print("Hello " + name +"!")   # this works, but it's not how the tutorial did it
		print("Hello {}!".format(name))  # .format(name) inserts the entered name into the curly brackets
		remove = input("Would you like to be removed from the system (y/n)?: ").lower() # .lower makes sure result is lower case

		if remove == "y":
			known_users.remove(name)
			#print(len(known_users))  # shows 7 whereas it started with 8, so the remove worked

		elif remove == "n":
			print("No problem. I didn't want you to leave anyway!")

	else:
		print("Hmmm.  I don't think I have met you yet {}".format(name))
		add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()

		if add_me == "y":
			known_users.append(name)  # append (add) name to list
			#print(len(known_users))  # shows 9, so 1 was added

		elif add_me == "n":
			print("No worries. See you around!")
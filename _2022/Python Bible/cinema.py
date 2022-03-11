films = {
	"Finding Dory": [3, 5], #age and number of available tickets
	"Bourne": [18, 5],
	"Tarzan": [15, 5],
	"Ghost Busters": [12, 5]

	}

while True:
	choice = input("What film do you want to watch?: ").strip().title() # convert to title case

	if choice in films:
		#pass # lets you fill this in later

		# check user age
		age = int(input("How old are you?: ").strip())
		if age >= films[choice][0]: # if user's age is greater than or equal to required age for film

			# check enough seats
			num_seats = films[choice][1]

			if num_seats > 0:
				print("Enjoy the film!")
				films[choice][1] = films[choice][1] - 1 # remove an available ticket
			else:
				print("There are no tickets left!")
		else:
			print("You are too young to see that film!")


	else:
		print("We don't have that film...")